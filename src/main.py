from copy import copy_files
from generate import generate_pages_recursive
import os

copy_files("./static", "./public")
generate_pages_recursive("content", "template.html", "public")
