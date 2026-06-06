from parse import extract_title
from convert import markdown_to_html_node

import os

def generate_pages_recursive(from_path, template_path, dest_path):
    print(f"Generating HTML in {dest_path} for all Markdown sources in {from_path}")

    for fname in os.listdir(from_path):
        srcname = f"{from_path}/{fname}"
        dstname = f"{dest_path}/{fname}"
        if os.path.isdir(srcname):
            if not os.path.isdir(dstname):
                os.mkdir(dstname)
            generate_pages_recursive(srcname, template_path, dstname)
        else:
            name, _ = fname.split(".")
            generate_path(f"{from_path}/{name}.md", template_path, f"{dest_path}/{name}.html")

def generate_path(from_path, template_path, dest_path):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")
	
	contents_from = ""
	with open(from_path, "r") as markdown_from:
		contents_from = markdown_from.read()
		
	contents_template = ""
	with open(template_path, "r") as html_template:
		contents_template = html_template.read()

	contents_from_html = markdown_to_html_node(contents_from).to_html()
	page_title = extract_title(contents_from)
	
	contents_template = contents_template.replace("{{ Title }}", page_title)
	contents_template = contents_template.replace("{{ Content }}", contents_from_html)
	
	with open(dest_path, "w") as dest:
		dest.write(''.join([contents_from_html, contents_template]))
