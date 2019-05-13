from myParentclass import *

class save_point(interactive_object):
    def __init__(self, width, height, x=0, y=0):
        interactive_object.__init__(self, width, height, x, y)

    def interact(self, player):
        # save game
        return

class drawing_piece(interactive_object):
    def __init__(self, width, height, x=0, y=0):
        interactive_object.__init__(self, width, height, x, y)

    def interact(self, player):
        # save game
        return

class gate(interactive_object):
    def __init__(self, width, height, x=0, y=0):
        interactive_object.__init__(self, width, height, x, y)

    def interact(self, player):
        # get to next level
        return

class stair(interactive_object):
    def __init__(self, width, height, x=0, y=0):
        interactive_object.__init__(self, width, height, x, y)
