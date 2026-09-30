# Source - https://stackoverflow.com/a/54923798
# Posted by Pavel Vorobyov
# Retrieved 2026-09-30, License - CC BY-SA 4.0

from io import StringIO

from markdown import Markdown


def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


# patching Markdown
Markdown.output_formats["plain"] = unmark_element  # pyright: ignore[reportArgumentType]
__md = Markdown(output_format="plain")  # pyright: ignore[reportArgumentType]
__md.stripTopLevelTags = False


def unmark(text):
    return __md.convert(text)
