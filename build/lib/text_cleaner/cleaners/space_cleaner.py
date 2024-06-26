class Space_Cleaner:
    def __init__(self, text: str = "") -> None:
        self.text: str = text

    def clean(self) -> str:
        """
        Remove all leading and trailing and extra spaces from given text

        < text: str
            input text to remove spaces from

        > str
            output text with removed spaces
        """

        if not self.text:
            return ""

        clean_text: str = " ".join(self.text.split())
        lines: list[str] = [
            line.strip() for line in clean_text.splitlines() if line.strip()
        ]
        clean_text = "\n".join(lines).strip()
        return clean_text
