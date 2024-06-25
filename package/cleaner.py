from package.logger import Logger
from package.usfm_cleaner import USFM_Cleaner
from package.html_cleaner import HTML_Cleaner
from package.space_cleaner import Space_Cleaner


class Cleaner:
    def __init__(self, text: str = "") -> None:
        self.text: str = text

    def clean(self) -> str:
        """
        Remove all tags and extra spaces from given text

        < text: str
            input text to remove tags from

        > str
            output text with removed tags
        """

        if not self.text:
            Logger.show_error("No text to clean")
            return ""

        cleaner = USFM_Cleaner(self.text)
        self.text = cleaner.clean()

        cleaner = HTML_Cleaner(self.text)
        self.text = cleaner.clean()

        cleaner = Space_Cleaner(self.text)
        self.text = cleaner.clean()

        return self.text
