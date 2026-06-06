import unittest

from parse import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_single_line(self):
        md = "# hello, world"
        self.assertEqual(extract_title(md), "hello, world")

        md = "dankmemes"
        with self.assertRaises(Exception):
            title = extract_title(md)

    def test_multiple_lines(self):
        md = """# title
this is one line of content
this is another line of content
"""
        self.assertEqual(extract_title(md), "title")

        md = """this is one line of content
this is another line of content
"""
        with self.assertRaises(Exception):
            title = extract_title(md)
        
        md = """  
# title
This is one line of content
This is another line of content
"""
        self.assertEqual(extract_title(md), "title")

if __name__ == '__main__':
    unittest.main()
