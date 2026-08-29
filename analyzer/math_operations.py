import numpy as np


class MathOperations:
    """
    Handles mathematical operations on NumPy arrays.
    """

    def addition(self, array1, array2):
        """Perform element-wise addition."""
        return np.add(array1, array2)

    def subtraction(self, array1, array2):
        """Perform element-wise subtraction."""
        return np.subtract(array1, array2)

    def multiplication(self, array1, array2):
        """Perform element-wise multiplication."""
        return np.multiply(array1, array2)

    def division(self, array1, array2):
        """Perform element-wise division."""
        return np.divide(array1, array2)

    def dot_product(self, array1, array2):
        """Calculate the dot product of two arrays."""
        return np.dot(array1, array2)

    def matrix_multiplication(self, array1, array2):
        """Perform matrix multiplication on 2D arrays."""
        return np.matmul(array1, array2)

    @staticmethod
    def display_result(result):
        """Display the mathematical result."""
        print("\nResult:")
        print(result)