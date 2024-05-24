import argparse
import markdown
import os
from glob import glob
from pathlib import Path


OUTPUT_FOLDER = "site"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate HTML from Markdown")
    parser.add_argument(
        "--files", nargs="*", help="List of Markdown files to process", default=[]
    )
    args = parser.parse_args()
    return args


def generate_html_files(markdown_files: list[str]):
    try:
        os.mkdir(OUTPUT_FOLDER)
    except FileExistsError:
        pass

    md = markdown.Markdown(extensions=["fenced_code", "codehilite"])

    for filepath in markdown_files:
        file = filepath.split("/")[-1]
        filename, _ = file.split(".")
        print(f"Converting {file} to html")

        output_filename = Path(OUTPUT_FOLDER) / f"{filename}.html"
        print(f"Output: {output_filename}")

        with open(filepath) as f:
            html = md.convert(f.read())

        with open(output_filename, "w") as f:
            f.write('<link rel="stylesheet" href="styles.css"/>')
            f.write(html)

        md.reset()


def main():
    args = parse_args()
    print(f"{args=}")

    if args.files:
        markdown_files = args.files
    else:
        markdown_files = glob("**/*.md", recursive=True)

    generate_html_files(markdown_files)


if __name__ == "__main__":
    main()
