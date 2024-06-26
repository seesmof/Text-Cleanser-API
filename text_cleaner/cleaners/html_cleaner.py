import io
from html.parser import HTMLParser


class HTML_Processor(HTMLParser):
    def __init__(self) -> None:
        self.reset()
        self.strict: bool = False
        self.convert_charrefs: bool = True
        self.text: str = io.StringIO()

    def handle_data(self, data: str) -> None:
        self.text.write(data)

    def get_data(self) -> str:
        return self.text.getvalue()


class HTML_Cleaner(HTMLParser):
    def __init__(self, text: str = "") -> None:
        self.text: str = text

    def clean(self) -> str:
        """
        Remove HTML tags from given text

        < text: str
            input text to remove HTML tags from

        > str
            output text with removed HTML tags
        """

        if not self.text:
            ("No text to clean")
            return ""

        cleaner: HTML_Processor = HTML_Processor()
        cleaner.feed(self.text)
        return cleaner.get_data()
