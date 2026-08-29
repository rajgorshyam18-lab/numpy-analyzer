import numpy as np


class Statistics:
    """
    Handles statistical and aggregating operations
    on NumPy arrays.
    """

    def total(self, array):
        """Calculate the sum of all elements."""
        return np.sum(array)

    def mean(self, array):
        """Calculate the mean of the array."""
        return np.mean(array)

    def median(self, array):
        """Calculate the median of the array."""
        return np.median(array)

    def standard_deviation(self, array):
        """Calculate the standard deviation."""
        return np.std(array)

    def variance(self, array):
        """Calculate the variance."""
        return np.var(array)

    def minimum(self, array):
        """Find the minimum value."""
        return np.min(array)

    def maximum(self, array):
        """Find the maximum value."""
        return np.max(array)

    def percentile(self, array, value):
        """Calculate the requested percentile."""
        return np.percentile(array, value)

    def correlation(self, array1, array2):
        """Calculate the correlation coefficient."""
        return np.corrcoef(array1, array2)[0, 1]

    @staticmethod
    def display_statistics(array):
        """Display common statistical values."""
        print("\nStatistics")
        print("-" * 30)
        print("Sum:", np.sum(array))
        print("Mean:", np.mean(array))
        print("Median:", np.median(array))
        print("Standard Deviation:", np.std(array))
        print("Variance:", np.var(array))
        print("Minimum:", np.min(array))
        print("Maximum:", np.max(array))