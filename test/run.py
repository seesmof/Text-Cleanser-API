""" 
TODO
add json formatting
"""

import os

from package.cleaner import Cleaner
from package.file_handler import File_Handler

current_dir: str = os.path.dirname(os.path.abspath(__file__))
target_file: str = os.path.join(current_dir, "data.md")

text: str = File_Handler.read_file(target_file)
cleaner = Cleaner(text)
text = cleaner.clean()

File_Handler.write_file(target_file, text) if text else None
