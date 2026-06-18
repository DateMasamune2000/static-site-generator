from copy import copy_files
from generate import generate_pages_recursive
import os
import sys

basepath = sys.argv[1]

copy_files("./static", "./docs")
generate_pages_recursive(basepath, "content", "template.html", "docs")
