import numpy as np


class SearchSortFilter:
    """
    Handles searching, sorting, and filtering operations
    on NumPy arrays.
    """

    def search_value(self, array, value):
        """Find the indexes where the given value exists."""
        return np.where(array == value)

    def sort_array(self, array, ascending=True):
        """Sort an array in ascending or descending order."""
        sorted_array = np.sort(array)

        if ascending:
            return sorted_array

        return sorted_array[::-1]

    def filter_values(self, array, condition, value):
        """
        Filter array values using a condition.

        Supported conditions:
        >, <, >=, <=, ==, !=
        """

        if condition == ">":
            return array[array > value]

        elif condition == "<":
            return array[array < value]

        elif condition == ">=":
            return array[array >= value]

        elif condition == "<=":
            return array[array <= value]

        elif condition == "==":
            return array[array == value]

        elif condition == "!=":
            return array[array != value]

        else:
            raise ValueError(
                "Invalid condition. Use >, <, >=, <=, ==, or !="
            )

    @staticmethod
    def display_result(result):
        """Display the result."""
        print("\nResult:")
        print(result)