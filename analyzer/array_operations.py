import numpy as np


class ArrayOperations:
    """
    Handles NumPy array creation, indexing, slicing,
    combining, and splitting operations.
    """

    def __init__(self):
        self.array = None

    def create_1d_array(self, elements):
        """Create a 1D NumPy array."""
        self.array = np.array(elements)
        return self.array

    def create_2d_array(self, rows, cols, elements):
        """Create a 2D NumPy array."""
        self.array = np.array(elements).reshape(rows, cols)
        return self.array

    def create_3d_array(self, elements, shape):
        """Create a 3D NumPy array."""
        self.array = np.array(elements).reshape(shape)
        return self.array

    def get_element(self, index):
        """Get an element from the array."""
        return self.array[index]

    def get_row(self, row_index):
        """Get a specific row from a 2D array."""
        return self.array[row_index]

    def get_column(self, column_index):
        """Get a specific column from a 2D array."""
        return self.array[:, column_index]

    def slice_array(self, start, end):
        """Return a slice of the array."""
        return self.array[start:end]

    def slice_2d_array(self, row_start, row_end, col_start, col_end):
        """Return a slice from a 2D array."""
        return self.array[row_start:row_end, col_start:col_end]

    def combine_arrays(self, array1, array2, axis=0):
        """Combine two arrays using NumPy concatenate."""
        return np.concatenate((array1, array2), axis=axis)

    def split_array(self, array, sections, axis=0):
        """Split an array into smaller arrays."""
        return np.array_split(array, sections, axis=axis)

    @staticmethod
    def display_array(array):
        """Display a NumPy array."""
        print("\nArray:")
        print(array)