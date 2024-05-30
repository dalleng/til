import re
import argparse
from dataclasses import dataclass
import shutil
import markdown
import os
from glob import glob
from pathlib import Path
from pygments.formatters import HtmlFormatter


ROOT_DIR = Path().parent
INPUT_FOLDER = ROOT_DIR / "site-gen"
OUTPUT_FOLDER = ROOT_DIR / "site"
SYNTAX_HIGHLIGHTING_CSS = "highlighting.css"
BASE_HTML_TEMPLATE = "base_template.html"
BASE_CSS_STYLES = "base_styles.css"
INDEX_TEMPLATE = "index_template.html"


@dataclass(order=True)
class TILNote:
    filename: str
    source: str
    category: str
    created_at: str

    def __init__(self, source: str):
        self.source = source
        self.category, filename_with_ext = source.split("/")
        self.filename, _ = filename_with_ext.split(".")
        m = re.match(r"\d{4}-\d{2}-\d{2}", self.filename)
        if m is None:
            raise ValueError("Filename should begin with date in format YYYY-MM-DD")
        self.created_at = m.group()

    @property
    def title(self) -> str | None:
        with open(self.source, "r") as file:
            for line in file:
                # regex for lines starting with one or more '#', which would be files
                if match := re.match(r"^\#+\s*(.*)", line.strip()):
                    return match.group(1).strip()
        return None

    @property
    def url(self) -> str:
        return str(OUTPUT_FOLDER / f"{self.filename}.html")

    def to_html(self, markdown_instance: markdown.Markdown | None = None) -> str:
        md = markdown_instance or markdown.Markdown()

        with open(self.source, "r") as f:
            html = md.convert(f.read())

        return html


@dataclass
class Template:
    content: str

    @classmethod
    def from_file(cls, source: Path | str):
        with open(source) as f:
            content = f.read()
        return cls(content)

    def render(self, data: dict) -> str:
        return self.content.format(**data)

    def write_to_file(self, destination: Path | str, data: dict):
        with open(destination, "w") as fout:
            fout.write(self.render(data))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate HTML from Markdown")
    parser.add_argument(
        "--files", nargs="*", help="List of Markdown files to process", default=[]
    )
    args = parser.parse_args()
    return args


def generate_html_files(markdown_files: list[str]):
    # Generate html files for each markdown file
    tils = []
    md = markdown.Markdown(extensions=["fenced_code", "codehilite"])
    template = Template.from_file(INPUT_FOLDER / BASE_HTML_TEMPLATE)

    for filepath in markdown_files:
        til = TILNote(filepath)
        tils.append(til)
        html = til.to_html(md)

        output_filename = OUTPUT_FOLDER / f"{til.filename}.html"
        print(f"Output: {output_filename}")

        head_content = f'<link rel="stylesheet" href="{SYNTAX_HIGHLIGHTING_CSS}" />'
        template.write_to_file(
            output_filename, dict(head_content=head_content, body_content=html)
        )
        md.reset()


def generate_index(markdown_files: list[str]):
    # Generate index.html
    tils = [TILNote(mf) for mf in markdown_files]
    tils.sort(reverse=True)
    list_template = Template("<ul>{list_content}</ul>")
    list_item_template = Template(
        '<li><span class="tag">{category}</span> <a href="{url}">{title}</a> - <small>{created_at}</small></li>'
    )
    list_content = "\n".join(
        [
            list_item_template.render(
                dict(
                    url=til.url,
                    title=til.title,
                    created_at=til.created_at,
                    category=til.category,
                )
            )
            for til in tils
        ]
    )
    main_content = list_template.render(dict(list_content=list_content))
    body_content = Template.from_file(INPUT_FOLDER / INDEX_TEMPLATE).render(
        data=dict(main_content=main_content)
    )

    # copy 'base_styles.css' from ./site-gen to ./site
    shutil.copy(INPUT_FOLDER / BASE_CSS_STYLES, OUTPUT_FOLDER)
    head_content = f'<link rel="stylesheet" href="site/{BASE_CSS_STYLES}" />'

    Template.from_file(INPUT_FOLDER / BASE_HTML_TEMPLATE).write_to_file(
        ROOT_DIR / "index.html",
        dict(head_content=head_content, body_content=body_content),
    )


def generate_css(style_name: str, filename: Path):
    formatter = HtmlFormatter(style=style_name)
    with open(filename, "w") as f:
        f.write(formatter.get_style_defs(".codehilite"))


def main():
    args = parse_args()
    print(f"{args=}")

    try:
        output_filepath = str(OUTPUT_FOLDER)
        print(f"Creating output folder: {output_filepath}")
        os.mkdir(output_filepath)
    except FileExistsError:
        print("Output folder alredy exists")
        pass

    generate_css("default", OUTPUT_FOLDER / SYNTAX_HIGHLIGHTING_CSS)
    all_markdown_files = glob("**/*.md", recursive=True)

    if args.files:
        markdown_files = args.files
    else:
        markdown_files = all_markdown_files

    generate_html_files(markdown_files)
    generate_index(all_markdown_files)


if __name__ == "__main__":
    main()
