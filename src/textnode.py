class TextNode:
    def __init__(self, TEXT, text_type, URL=None):
        self.text = TEXT
        self.text_type = text_type
        self.url = URL
        
    def __eq__(self, textnode):
        if self.text == textnode.text and self.text_type == textnode.text_type and self.url == textnode.url:
            return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"