class Cube(object):
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args

    def __init__(self, side=0):
        self._side = side

    def get_Side(self):
        """Return the side of the Cube"""
        return self._side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = abs(new_side)
