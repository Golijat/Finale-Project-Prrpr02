"""
Block is used as a template to create other blocks
that can be used for many things.
"""
class Block:
    """
    Template for other blocks
    """
    def __init__(self, bg_color, size, span):
        self.bg_color = bg_color
        self.size = size
        self.span = span

class TopBlock(Block):
    """
    Used to put a line at the top of the main gui.
    """
    def __init__(self, bg_color, size, span):
        super().__init__(bg_color, size, span)
