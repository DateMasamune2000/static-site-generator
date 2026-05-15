import unittest

from textnode import TextNode, TextType
from parse import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
	def test_plain(self):
		plain = TextNode(text_type=TextType.PLAIN, text="hello, world")

		nodes_bold = split_nodes_delimiter([plain], "**", TextType.BOLD)
		self.assertEqual(nodes_bold, [TextNode("hello, world", TextType.PLAIN)])

		nodes_bold = split_nodes_delimiter([plain], "_", TextType.ITALIC)
		self.assertEqual(nodes_bold, [TextNode("hello, world", TextType.PLAIN)])

		nodes_bold = split_nodes_delimiter([plain], "`", TextType.CODE)
		self.assertEqual(nodes_bold, [TextNode("hello, world", TextType.PLAIN)])

	def test_bold(self):
		bold = TextNode(text_type=TextType.PLAIN, text="hello, **world**!")

		nodes_bold = split_nodes_delimiter([bold], "**", TextType.BOLD)
		self.assertEqual(nodes_bold, [
			TextNode("hello, ", TextType.PLAIN),
			TextNode("world", TextType.BOLD),
			TextNode("!", TextType.PLAIN)
		])

		nodes_italic = split_nodes_delimiter([bold], "_", TextType.ITALIC)
		self.assertEqual(nodes_italic, [
			TextNode("hello, **world**!", TextType.PLAIN)
		])

		nodes_code = split_nodes_delimiter([bold], "`", TextType.CODE)
		self.assertEqual(nodes_code, [
			TextNode("hello, **world**!", TextType.PLAIN)
		])

	def test_italic(self):
		italic = TextNode(text_type=TextType.PLAIN, text="hello, _world_!")

		nodes_italic = split_nodes_delimiter([italic], "_", TextType.ITALIC)
		self.assertEqual(nodes_italic, [
			TextNode("hello, ", TextType.PLAIN),
			TextNode("world", TextType.ITALIC),
			TextNode("!", TextType.PLAIN)
		])

		nodes_bold = split_nodes_delimiter([italic], "**", TextType.BOLD)
		self.assertEqual(nodes_bold, [
			TextNode("hello, _world_!", TextType.PLAIN)
		])

		nodes_code = split_nodes_delimiter([italic], "`", TextType.CODE)
		self.assertEqual(nodes_code, [
			TextNode("hello, _world_!", TextType.PLAIN)
		])

	def test_code(self):
		code = TextNode(text_type=TextType.PLAIN, text="hello, `world`!")

		nodes_code = split_nodes_delimiter([code], "`", TextType.CODE)
		self.assertEqual(nodes_code, [
			TextNode("hello, ", TextType.PLAIN),
			TextNode("world", TextType.CODE),
			TextNode("!", TextType.PLAIN)
		])

		nodes_bold = split_nodes_delimiter([code], "**", TextType.BOLD)
		self.assertEqual(nodes_bold, [
			TextNode("hello, `world`!", TextType.PLAIN)
		])

		nodes_italic = split_nodes_delimiter([code], "_", TextType.ITALIC)
		self.assertEqual(nodes_italic, [
			TextNode("hello, `world`!", TextType.PLAIN)
		])
