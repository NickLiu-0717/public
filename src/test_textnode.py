import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is not a text node", "bold")
        self.assertNotEqual(node, node2)
    
    def test_URL(self):
        node = TextNode("This is a text node", "bold", None)
        self.assertIsInstance(node, TextNode)
    
    def test_diff_type(self):
        TYPE = ["bold", "Italic", "Blockquote"]
        for type in TYPE:
            self.assertIsInstance(TextNode("This is a text node", type), TextNode)


if __name__ == "__main__":
    unittest.main()