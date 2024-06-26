class File_Handler:
    @staticmethod
    def read_file(file_path: str) -> str:
        """
        Reads a file and returns its content

        < file_path: str
            path of the file to read

        > str
            content of the file
        """

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def write_file(file_path: str, text: str) -> None:
        """
        Writes text to a file

        < file_path: str
            path of the file to write to
        < text: str
            content to write to the file
        """

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)
