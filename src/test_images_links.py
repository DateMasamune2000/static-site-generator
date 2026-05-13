import unittest

from convert import extract_markdown_images, extract_markdown_links

class TestImagesLinks(unittest.TestCase):
	def test_images(self):
		text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
		self.assertEqual(
			extract_markdown_images(text),
			[
				("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
				("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
			]
		)

		text = "This is text with a"
		self.assertEqual(extract_markdown_images(text), [])

	def test_links(self):
		text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
		self.assertEqual(
			extract_markdown_links(text),
			[
				("to boot dev", "https://www.boot.dev"),
				("to youtube", "https://www.youtube.com/@bootdotdev")
			]
		)

		text = "This is text with a"
		self.assertEqual(extract_markdown_links(text), [])

	def test_images_are_not_links(self):
		text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
		self.assertEqual(extract_markdown_links(text), [])


