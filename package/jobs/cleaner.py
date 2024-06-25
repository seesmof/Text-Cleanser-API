from package.cleaners.html_cleaner import HTML_Cleaner
from package.cleaners.usfm_cleaner import USFM_Cleaner
from package.cleaners.space_cleaner import Space_Cleaner
from package.tools.logger import Logger
from package.tools.file_handler import File_Handler


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

    def load_from_file(self, file_path: str) -> None:
        """
        Load text from a file

        < file_path: str
            path of the file to read
        """

        self.text = File_Handler.read_file(file_path)

    def save_to_file(self, file_path: str) -> None:
        """
        Save text to a file

        < file_path: str
            path of the file to write to
        """

        File_Handler.write_file(file_path, self.text)

        file_name: str = file_path.split("\\")[-1]
        Logger.show_success(f"Text saved to {file_name}")
