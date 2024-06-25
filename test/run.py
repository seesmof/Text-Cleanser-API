""" 
TODO
add json formatting
"""

import os

from package.cleaner import Cleaner
from package.file_handler import File_Handler

current_dir: str = os.path.dirname(os.path.abspath(__file__))
target_file: str = os.path.join(current_dir, "data.md")

cleaner: Cleaner = Cleaner()
cleaner.load_from_file(target_file)
cleaner.clean()
cleaner.save_to_file(target_file)

print(cleaner.text)
