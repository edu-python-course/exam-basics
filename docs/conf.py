# Sphinx config

# this configuration should be used only for internal documentation checks
# the main documentation will be build within main project:
# https://github.com/edu-python-course/edu-python-course.github.io

import sys
from pathlib import Path

# setup paths
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "src" / "exam"))

# general project information
project = "Python Training Course - Exam - Basics"
version = "0.1.0"
authors = "Serhii Horodilov <sgorodil@gmail.com>"

# general configurations
extensions = ["sphinx.ext.autodoc"]
source_suffix = {".txt": "restructuredtext", ".rst": "restructuredtext"}
