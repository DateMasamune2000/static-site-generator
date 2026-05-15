import unittest

from textnode import TextNode, TextType
from parse import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
	def test_plain(self):
		text = "hello, world"
		self.assertEqual(text_to_textnodes(text), [
			TextNode("hello, world", TextType.PLAIN)
		])

	def test_one(self):
		text = "hello, **world**!"
		self.assertEqual(text_to_textnodes(text), [
			TextNode("hello, ", TextType.PLAIN),
			TextNode("world", TextType.BOLD),
			TextNode("!", TextType.PLAIN)
		])

		text = "hello, **world**"
		self.assertEqual(text_to_textnodes(text), [
			TextNode("hello, ", TextType.PLAIN),
			TextNode("world", TextType.BOLD),
		])

		text = "**world**!"
		self.assertEqual(text_to_textnodes(text), [
			TextNode("world", TextType.BOLD),
			TextNode("!", TextType.PLAIN)
		])

	def test_multiple_same(self):
		text = "_hello_, _world_!"
		self.assertEqual(text_to_textnodes(text), [
			TextNode("hello", TextType.ITALIC),
			TextNode(", ", TextType.PLAIN),
			TextNode("world", TextType.ITALIC),
			TextNode("!", TextType.PLAIN),
		])

	def test_multiple_different(self):
		text = "**hello**, _world_`!`"
		self.assertEqual(text_to_textnodes(text), [
			TextNode("hello", TextType.BOLD),
			TextNode(", ", TextType.PLAIN),
			TextNode("world", TextType.ITALIC),
			TextNode("!", TextType.CODE),
		])

		text = "huh? **why** are you _running_?"
		self.assertEqual(text_to_textnodes(text), [
			TextNode("huh? ", TextType.PLAIN),
			TextNode("why", TextType.BOLD),
			TextNode(" are you ", TextType.PLAIN),
			TextNode("running", TextType.ITALIC),
			TextNode("?", TextType.PLAIN),
		])
