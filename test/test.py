"""
pip install dist/text_cleaner-0.1-py3-none-any.whl --force-reinstall
"""

from text_cleaner import Cleaner

cleaner = Cleaner("Hello,    World!")
cleaner.clean()

print(cleaner.text)
