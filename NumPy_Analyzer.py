import numpy as np

from analyzer.array_operations import ArrayOperations
from analyzer.math_operations import MathOperations
from analyzer.search_sort_filter import SearchSortFilter
from analyzer.statistics import Statistics


class DataAnalytics:
    """Main class for the NumPy Analyzer application."""

    def __init__(self):
        self.array_operations = ArrayOperations()
        self.math_operations = MathOperations()
        self.search_sort_filter = SearchSortFilter()
        self.statistics = Statistics()
        self._current_array = None

    @classmethod
    def create_analyzer(cls):
        """Create and return a DataAnalytics object."""
        return cls()

    @staticmethod
    def display_title():
        """Display application title."""
        print("\n" + "=" * 55)
        print("              NUMPY ANALYZER")
        print("=" * 55)

    def create_array_menu(self):
        """Create 1D, 2D or 3D NumPy arrays."""
        print("\n--- Array Creation ---")
        print("1. Create 1D Array")
        print("2. Create 2D Array")
        print("3. Create 3D Array")
        print("4. Back")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                elements = list(map(float, input(
                    "Enter elements separated by spaces: "
                ).split()))

                self._current_array = (
                    self.array_operations.create_1d_array(elements)
                )

                print("\nCreated 1D Array:")
                print(self._current_array)

            elif choice == "2":
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))

                elements = list(map(float, input(
                    f"Enter {rows * cols} elements separated by spaces: "
                ).split()))

                if len(elements) != rows * cols:
                    print("Error: Number of elements does not match the shape.")
                    return

                self._current_array = (
                    self.array_operations.create_2d_array(
                        rows, cols, elements
                    )
                )

                print("\nCreated 2D Array:")
                print(self._current_array)

            elif choice == "3":
                dimensions = input(
                    "Enter 3D shape (e.g. 2 2 2): "
                ).split()

                if len(dimensions) != 3:
                    print("Please enter exactly three dimensions.")
                    return

                shape = tuple(map(int, dimensions))
                total_elements = np.prod(shape)

                elements = list(map(float, input(
                    f"Enter {total_elements} elements separated by spaces: "
                ).split()))

                if len(elements) != total_elements:
                    print("Error: Number of elements does not match the shape.")
                    return

                self._current_array = (
                    self.array_operations.create_3d_array(
                        elements, shape
                    )
                )

                print("\nCreated 3D Array:")
                print(self._current_array)

            elif choice == "4":
                return

            else:
                print("Invalid choice.")

        except ValueError as error:
            print("Invalid input:", error)

    def indexing_slicing_menu(self):
        """Perform indexing and slicing operations."""
        if self._current_array is None:
            print("\nPlease create an array first.")
            return

        print("\n--- Indexing & Slicing ---")
        print("1. Indexing")
        print("2. 1D Slicing")
        print("3. 2D Slicing")
        print("4. Back")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                if self._current_array.ndim == 1:
                    index = int(input("Enter index: "))
                    result = self.array_operations.get_element(index)

                elif self._current_array.ndim == 2:
                    row = int(input("Enter row index: "))
                    col = int(input("Enter column index: "))
                    result = self._current_array[row, col]

                else:
                    index = int(input("Enter first dimension index: "))
                    result = self._current_array[index]

                print("Selected element:", result)

            elif choice == "2":
                if self._current_array.ndim != 1:
                    print("1D slicing is available for a 1D array.")
                    return

                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))

                result = self.array_operations.slice_array(start, end)
                print("Sliced Array:", result)

            elif choice == "3":
                if self._current_array.ndim != 2:
                    print("2D slicing is available for a 2D array.")
                    return

                row_start = int(input("Row start: "))
                row_end = int(input("Row end: "))
                col_start = int(input("Column start: "))
                col_end = int(input("Column end: "))

                result = self.array_operations.slice_2d_array(
                    row_start,
                    row_end,
                    col_start,
                    col_end
                )

                print("Sliced Array:")
                print(result)

            elif choice == "4":
                return

            else:
                print("Invalid choice.")

        except (ValueError, IndexError) as error:
            print("Invalid input:", error)

    def combine_split_menu(self):
        """Combine or split arrays."""
        print("\n--- Combine & Split Arrays ---")
        print("1. Combine Arrays")
        print("2. Split Current Array")
        print("3. Back")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                first = list(map(float, input(
                    "Enter first array elements: "
                ).split()))

                second = list(map(float, input(
                    "Enter second array elements: "
                ).split()))

                array1 = np.array(first)
                array2 = np.array(second)

                if array1.ndim != array2.ndim:
                    print("Arrays must have the same dimensions.")
                    return

                result = self.array_operations.combine_arrays(
                    array1, array2
                )

                print("Combined Array:")
                print(result)

            elif choice == "2":
                if self._current_array is None:
                    print("Please create an array first.")
                    return

                sections = int(input("Enter number of sections: "))

                result = self.array_operations.split_array(
                    self._current_array,
                    sections
                )

                print("\nSplit Arrays:")
                for index, part in enumerate(result, start=1):
                    print(f"Part {index}:")
                    print(part)

            elif choice == "3":
                return

            else:
                print("Invalid choice.")

        except ValueError as error:
            print("Invalid input:", error)

    def mathematical_operations_menu(self):
        """Perform mathematical operations on arrays."""
        print("\n--- Mathematical Operations ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")
        print("7. Back")

        choice = input("Enter your choice: ")

        if choice == "7":
            return

        try:
            if choice in {"1", "2", "3", "4", "5", "6"}:
                print("\nEnter values for Array 1:")
                array1 = np.array(
                    list(map(float, input().split()))
                )

                print("Enter values for Array 2:")
                array2 = np.array(
                    list(map(float, input().split()))
                )

                if choice == "1":
                    result = self.math_operations.addition(
                        array1, array2
                    )

                elif choice == "2":
                    result = self.math_operations.subtraction(
                        array1, array2
                    )

                elif choice == "3":
                    result = self.math_operations.multiplication(
                        array1, array2
                    )

                elif choice == "4":
                    if np.any(array2 == 0):
                        print("Division by zero is not allowed.")
                        return

                    result = self.math_operations.division(
                        array1, array2
                    )

                elif choice == "5":
                    result = self.math_operations.dot_product(
                        array1, array2
                    )

                elif choice == "6":
                    try:
                        rows1 = int(input(
                            "Enter rows of first matrix: "
                        ))
                        cols1 = int(input(
                            "Enter columns of first matrix: "
                        ))
                        rows2 = int(input(
                            "Enter rows of second matrix: "
                        ))
                        cols2 = int(input(
                            "Enter columns of second matrix: "
                        ))

                        if cols1 != rows2:
                            print(
                                "Matrix multiplication requires "
                                "columns of first matrix = rows of second."
                            )
                            return

                        values1 = list(map(float, input(
                            f"Enter {rows1 * cols1} values for first matrix: "
                        ).split()))

                        values2 = list(map(float, input(
                            f"Enter {rows2 * cols2} values for second matrix: "
                        ).split()))

                        matrix1 = np.array(values1).reshape(
                            rows1, cols1
                        )
                        matrix2 = np.array(values2).reshape(
                            rows2, cols2
                        )

                        result = self.math_operations.matrix_multiplication(
                            matrix1, matrix2
                        )

                    except ValueError as error:
                        print("Invalid matrix input:", error)
                        return

                else:
                    print("Invalid choice.")
                    return

                self.math_operations.display_result(result)

            else:
                print("Invalid choice.")

        except ValueError as error:
            print("Invalid input:", error)

    def search_sort_filter_menu(self):
        """Perform search, sort and filter operations."""
        if self._current_array is None:
            print("\nPlease create an array first.")
            return

        print("\n--- Search, Sort & Filter ---")
        print("1. Search Value")
        print("2. Sort Ascending")
        print("3. Sort Descending")
        print("4. Filter Values")
        print("5. Back")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                value = float(input("Enter value to search: "))
                result = self.search_sort_filter.search_value(
                    self._current_array,
                    value
                )

                if len(result[0]) == 0:
                    print("Value not found.")

                else:
                    print("Value found at index:", result)

            elif choice == "2":
                result = self.search_sort_filter.sort_array(
                    self._current_array,
                    ascending=True
                )

                print("Ascending order:")
                print(result)

            elif choice == "3":
                result = self.search_sort_filter.sort_array(
                    self._current_array,
                    ascending=False
                )

                print("Descending order:")
                print(result)

            elif choice == "4":
                condition = input(
                    "Enter condition (>, <, >=, <=, ==, !=): "
                )
                value = float(input("Enter value: "))

                result = self.search_sort_filter.filter_values(
                    self._current_array,
                    condition,
                    value
                )

                print("Filtered values:")
                print(result)

            elif choice == "5":
                return

            else:
                print("Invalid choice.")

        except (ValueError, TypeError) as error:
            print("Invalid input:", error)

    def statistics_menu(self):
        """Display aggregating and statistical functions."""
        if self._current_array is None:
            print("\nPlease create an array first.")
            return

        print("\n--- Statistics ---")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")
        print("9. Correlation Coefficient")
        print("10. Display All Statistics")
        print("11. Back")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                print("Sum:", self.statistics.total(self._current_array))

            elif choice == "2":
                print("Mean:", self.statistics.mean(self._current_array))

            elif choice == "3":
                print(
                    "Median:",
                    self.statistics.median(self._current_array)
                )

            elif choice == "4":
                print(
                    "Standard Deviation:",
                    self.statistics.standard_deviation(
                        self._current_array
                    )
                )

            elif choice == "5":
                print(
                    "Variance:",
                    self.statistics.variance(self._current_array)
                )

            elif choice == "6":
                print(
                    "Minimum:",
                    self.statistics.minimum(self._current_array)
                )

            elif choice == "7":
                print(
                    "Maximum:",
                    self.statistics.maximum(self._current_array)
                )

            elif choice == "8":
                percentile_value = float(
                    input("Enter percentile (0-100): ")
                )

                if not 0 <= percentile_value <= 100:
                    print("Percentile must be between 0 and 100.")
                    return

                result = self.statistics.percentile(
                    self._current_array,
                    percentile_value
                )

                print(
                    f"{percentile_value}th Percentile:",
                    result
                )

            elif choice == "9":
                print(
                    "Enter values for first dataset:"
                )
                array1 = np.array(
                    list(map(float, input().split()))
                )

                print(
                    "Enter values for second dataset:"
                )
                array2 = np.array(
                    list(map(float, input().split()))
                )

                if array1.size != array2.size:
                    print("Both datasets must contain the same number of values.")
                    return

                result = self.statistics.correlation(
                    array1,
                    array2
                )

                print("Correlation Coefficient:", result)

            elif choice == "10":
                self.statistics.display_statistics(
                    self._current_array
                )

            elif choice == "11":
                return

            else:
                print("Invalid choice.")

        except (ValueError, TypeError) as error:
            print("Invalid input:", error)

    def run(self):
        """Run the main menu."""
        while True:
            self.display_title()

            print("\n1. Array Management")
            print("2. Mathematical Operations")
            print("3. Search, Sort & Filter")
            print("4. Aggregating & Statistical Functions")
            print("5. Display Current Array")
            print("6. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                while True:
                    print("\n--- Array Management ---")
                    print("1. Create Array")
                    print("2. Indexing & Slicing")
                    print("3. Combine & Split")
                    print("4. Back")

                    sub_choice = input("Enter your choice: ")

                    if sub_choice == "1":
                        self.create_array_menu()

                    elif sub_choice == "2":
                        self.indexing_slicing_menu()

                    elif sub_choice == "3":
                        self.combine_split_menu()

                    elif sub_choice == "4":
                        break

                    else:
                        print("Invalid choice.")

            elif choice == "2":
                self.mathematical_operations_menu()

            elif choice == "3":
                self.search_sort_filter_menu()

            elif choice == "4":
                self.statistics_menu()

            elif choice == "5":
                if self._current_array is None:
                    print("\nNo array has been created yet.")
                else:
                    print("\nCurrent Array:")
                    print(self._current_array)
                    print("Dimensions:", self._current_array.ndim)
                    print("Shape:", self._current_array.shape)

            elif choice == "6":
                print("\nThank you for using NumPy Analyzer!")
                break

            else:
                print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    analyzer = DataAnalytics.create_analyzer()
    analyzer.run()