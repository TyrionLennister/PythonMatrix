"""This class is used to make some Matrix calculations
"""

class Matrix():
    """Matrix class
    """

    rows = 0
    cols = 0

    def __init__(self, rows, cols):
        """Init the class Matrix

        Arguments:
            rows {int} -- Set the row size of the matrix
            cols {int} -- Set the col size of the matrix
        """

        if isinstance(rows, int) and isinstance(cols, int):
            self.rows = rows
            self.cols = cols
        else:
            raise TypeError()
