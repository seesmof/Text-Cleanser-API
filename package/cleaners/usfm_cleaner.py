import re


class USFM_Constants:
    SINGLE_TAGS: list[str] = ["pmo", "m", "pi", "p", "b", "em"]
    LEVELED_TAGS: list[str] = ["q", "s"]
    NUMBERED_TAGS: list[str] = ["c", "v"]
    SURROUNDING_DELETE: list[str] = ["f", "x"]
    SURROUNDING_LEAVE: list[str] = ["nd", "wj"]


class USFM_Cleaner:
    def __init__(self, text: str = "") -> None:
        self.text: str = text

    def clean(self) -> str:
        """
        Remove all USFM tags from given text

        < text: str
            input text to remove USFM tags from

        > str
            output text with removed USFM tags
        """

        if not self.text:
            return ""

        for single in USFM_Constants.SINGLE_TAGS:
            single = r"\\" + single + r"\s*" if "\\" not in single else single
            self.text = re.sub(single, "", self.text)
        for level in USFM_Constants.LEVELED_TAGS:
            level = r"\\" + level + r"\d*\s*" if "\\" not in level else level
            self.text = re.sub(level, "", self.text)
        for number in USFM_Constants.NUMBERED_TAGS:
            number = r"\\" + number + r"\s*\d*" if "\\" not in number else number
            self.text = re.sub(number, "", self.text)
        for surrounding_delete in USFM_Constants.SURROUNDING_DELETE:
            surrounding_delete = (
                (
                    r"\\"
                    + surrounding_delete
                    + r"\s*(.*?)\\"
                    + surrounding_delete
                    + r"\*"
                )
                if "\\" not in surrounding_delete
                else surrounding_delete
            )
            self.text = re.sub(surrounding_delete, "", self.text)
        for surrounding_leave in USFM_Constants.SURROUNDING_LEAVE:
            surrounding_leave = (
                (r"\\" + surrounding_leave + r"\s*(.*?)\\" + surrounding_leave + r"\*")
                if "\\" not in surrounding_leave
                else surrounding_leave
            )
            self.text = re.sub(surrounding_leave, r"\1", self.text)

        return self.text
