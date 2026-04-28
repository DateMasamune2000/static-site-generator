from textnode import TextType, TextNode

a = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
print(a)