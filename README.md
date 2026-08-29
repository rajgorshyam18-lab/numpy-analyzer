# 🧮 NumPy Analyzer

## Python NumPy Data Analysis Toolkit

A Python-based NumPy Analyzer created to demonstrate the practical use of NumPy arrays, array manipulation, mathematical operations, searching, sorting, filtering, statistical analysis, modular programming, custom modules, and Python packages.

The application provides a simple menu-driven console interface for performing numerical and data-analysis operations using NumPy.

---

## 🎯 Project Objective

The main objective of this project is to understand and demonstrate:

- NumPy arrays
- 1D, 2D and 3D arrays
- Array indexing and slicing
- Array manipulation
- Mathematical operations
- Matrix operations
- Searching and sorting
- Filtering data
- Aggregating and statistical functions
- Custom Python modules
- Python package creation and usage
- Object-Oriented Programming
- Exception handling
- Menu-driven programming

---

## ✨ Features

### 🔢 1. Array Management

The Array Management section provides:

- Create 1D NumPy array
- Create 2D NumPy array
- Create 3D NumPy array
- Array indexing
- 1D slicing
- 2D slicing
- Combine arrays
- Split arrays

### 🧮 2. Mathematical Operations

The Mathematical Operations section provides:

- Addition
- Subtraction
- Multiplication
- Division
- Dot product
- Matrix multiplication

### 🔍 3. Search, Sort & Filter

The Search, Sort & Filter section provides:

- Search for a specific value
- Sort array in ascending order
- Sort array in descending order
- Filter values using conditions

Supported filter conditions:

- `>`
- `<`
- `>=`
- `<=`
- `==`
- `!=`

### 📊 4. Aggregating & Statistical Functions

The Statistics section provides:

- Sum
- Mean
- Median
- Standard deviation
- Variance
- Minimum
- Maximum
- Percentile
- Correlation coefficient
- Display all statistics

### 📐 5. Array Information

The application can display:

- Current array
- Number of dimensions
- Array shape

---

## 📂 Project Structure

 numpy-analyzer/
├── NumPy_Analyzer.py
├── README.md
└── analyzer/
    ├── __init__.py
    ├── array_operations.py
    ├── math_operations.py
    ├── search_sort_filter.py
    └── statistics.py 

---

## 📄 File Description

| File | Description |
|---|---|
| `NumPy_Analyzer.py` | Main program and menu-driven interface |
| `analyzer/__init__.py` | Initializes the custom Python package |
| `analyzer/array_operations.py` | Contains array creation, indexing, slicing, combining and splitting operations |
| `analyzer/math_operations.py` | Contains mathematical and matrix operations |
| `analyzer/search_sort_filter.py` | Contains searching, sorting and filtering operations |
| `analyzer/statistics.py` | Contains aggregation and statistical functions |
| `README.md` | Project documentation |
| `.gitignore` | Prevents unnecessary generated files from being uploaded |

---

## 🧩 Modules Used

| Module / Library | Purpose |
|---|---|
| `numpy` | Numerical computing and array operations |
| `analyzer.array_operations` | Custom array operations |
| `analyzer.math_operations` | Custom mathematical operations |
| `analyzer.search_sort_filter` | Custom searching, sorting and filtering |
| `analyzer.statistics` | Custom statistical operations |

---

## 🛠️ Technologies Used

- Python 3
- NumPy
- Object-Oriented Programming
- Python Modules
- Python Packages
- Exception Handling
- Console / Menu-Driven Programming

---

## 🧠 Concepts Demonstrated

### Python Concepts

- Variables
- Functions
- Classes
- Objects
- Constructors
- Class methods
- Static methods
- Conditional statements
- Loops
- User input
- Exception handling
- Modules
- Packages
- `__init__.py`
- `if __name__ == "__main__"`

### NumPy Concepts

- `np.array()`
- 1D arrays
- 2D arrays
- 3D arrays
- Array dimensions
- Array shape
- Indexing
- Slicing
- Mathematical operations
- Dot product
- Matrix multiplication
- Searching
- Sorting
- Filtering
- Aggregation
- Statistical functions

---

## 📦 Requirements

Before running the project, make sure Python 3 is installed.

Required:

- Python 3.x
- NumPy

No other external libraries are required.

---

## ⚙️ Installation

### Step 1: Check Python

Open Command Prompt or Terminal and run:

    python --version

### Step 2: Install NumPy

Run:

    pip install numpy

To verify the installation:

    python -c "import numpy; print(numpy.__version__)"

### Step 3: Open the Project

Open the `NumPy_Analyzer` folder in VS Code.

### Step 4: Open the Terminal

Make sure the terminal is inside the project folder:

    NumPy_Analyzer

---

## ▶️ How to Run

Run the main Python file:

    python NumPy_Analyzer.py

On Windows, you can also use:

    py NumPy_Analyzer.py

---

## 📋 Main Menu

When the program starts, it displays:

    =======================================================
                  NUMPY ANALYZER
    =======================================================

    1. Array Management
    2. Mathematical Operations
    3. Search, Sort & Filter
    4. Aggregating & Statistical Functions
    5. Display Current Array
    6. Exit

    Enter your choice:

Enter the number of the required operation and follow the instructions shown by the program.

---

## 🔢 Array Management

### Create 1D Array

    --- Array Creation ---

    1. Create 1D Array
    2. Create 2D Array
    3. Create 3D Array
    4. Back

    Enter your choice: 1

    Enter elements separated by spaces:
    10 20 30 40 50

    Created 1D Array:
    [10. 20. 30. 40. 50.]

### Create 2D Array

Example:

    Enter number of rows:
    2

    Enter number of columns:
    2

    Enter 4 elements separated by spaces:
    1 2 3 4

    Created 2D Array:
    [[1. 2.]
     [3. 4.]]

### Create 3D Array

Example shape:

    2 2 2

The application accepts the required number of values and creates the array with the specified dimensions.

---

## ✂️ Indexing & Slicing

### Indexing

For:

    [10. 20. 30. 40. 50.]

Enter:

    2

Output:

    Selected element: 30.0

### 1D Slicing

Example:

    Enter start index:
    1

    Enter end index:
    4

Output:

    Sliced Array:
    [20. 30. 40.]

### 2D Slicing

The application allows selecting a range of rows and columns from a 2D array.

---

## 🔗 Combine & Split Arrays

### Combine Arrays

Two arrays can be entered and combined into a single array.

### Split Current Array

The current array can be divided into a specified number of sections.

---

## 🧮 Mathematical Operations

### Addition

    Enter values for Array 1:
    10 20 30 40 50

    Enter values for Array 2:
    1 2 3 4 5

    Result:
    [11. 22. 33. 44. 55.]

### Subtraction

    Enter values for Array 1:
    10 20 30 40 50

    Enter values for Array 2:
    1 2 3 4 5

    Result:
    [ 9. 18. 27. 36. 45.]

### Multiplication

    Enter values for Array 1:
    10 20 30 40 50

    Enter values for Array 2:
    1 2 3 4 5

    Result:
    [ 10.  40.  90. 160. 250.]

### Division

    Enter values for Array 1:
    10 20 30 40 50

    Enter values for Array 2:
    1 2 3 4 5

    Result:
    [10. 10. 10. 10. 10.]

### Dot Product

    Enter values for Array 1:
    1 2 3

    Enter values for Array 2:
    4 5 6

    Result:
    32

### Matrix Multiplication

Example:

    Enter rows of first matrix:
    2

    Enter columns of first matrix:
    2

    Enter rows of second matrix:
    2

    Enter columns of second matrix:
    2

    Enter 4 values for first matrix:
    1 2 3 4

    Enter 4 values for second matrix:
    5 6 7 8

Result:

    [[19. 22.]
     [43. 50.]]

---

## 🔍 Search, Sort & Filter

### Search Value

For the current array:

    [10. 20. 30. 40. 50.]

Search:

    Enter value to search:
    30

Output:

    Value found at index: (array([2]),)

### Sort Ascending

    Ascending order:
    [10. 20. 30. 40. 50.]

### Sort Descending

    Descending order:
    [50. 40. 30. 20. 10.]

### Filter Values

Example:

    Enter condition (>, <, >=, <=, ==, !=):
    >

    Enter value:
    25

Output:

    Filtered values:
    [30. 40. 50.]

---

## 📊 Statistical Operations

For the array:

    [10. 20. 30. 40. 50.]

Example results:

    Sum:
    150.0

    Mean:
    30.0

    Median:
    30.0

    Minimum:
    10.0

    Maximum:
    50.0

### Standard Deviation

The application calculates the standard deviation of the current array using NumPy statistical functions.

### Variance

The application calculates the variance of the current array.

### Percentile

Example:

    Enter percentile (0-100):
    50

Output:

    50.0th Percentile:
    30.0

### Correlation Coefficient

Example:

    Enter values for first dataset:
    1 2 3 4 5

    Enter values for second dataset:
    2 4 6 8 10

Output:

    Correlation Coefficient:
    1.0

### Display All Statistics

The application can display all supported statistical results for the current array at once.

---

## 🖥️ Current Array Information

The application provides an option to display the current array along with its:

- Number of dimensions
- Shape

Example:

    Current Array:
    [10. 20. 30. 40. 50.]

    Dimensions: 1
    Shape: (5,)

---

## 🛡️ Error Handling

The application includes input validation and exception handling for common errors such as:

- Invalid menu choices
- Invalid numeric input
- Incorrect number of array elements
- Invalid array dimensions
- Invalid percentile values
- Division by zero
- Incompatible matrix dimensions
- Invalid slicing input

This helps make the application more reliable and user-friendly.

---

## 🏗️ Application Architecture

The application follows a modular and object-oriented structure:

    NumPy Analyzer
           │
           ▼
    NumPy_Analyzer.py
           │
           ├── ArrayOperations
           │
           ├── MathOperations
           │
           ├── SearchSortFilter
           │
           └── Statistics

Each class is responsible for a specific group of operations, which makes the project easier to understand, maintain and extend.

---

## 🔄 Program Flow

    Start
      │
      ▼
    Create DataAnalytics Object
      │
      ▼
    Display Main Menu
      │
      ├── Array Management
      │      ├── Create Array
      │      ├── Indexing & Slicing
      │      └── Combine & Split
      │
      ├── Mathematical Operations
      │      ├── Addition
      │      ├── Subtraction
      │      ├── Multiplication
      │      ├── Division
      │      ├── Dot Product
      │      └── Matrix Multiplication
      │
      ├── Search, Sort & Filter
      │
      ├── Aggregating & Statistical Functions
      │
      ├── Display Current Array
      │
      └── Exit
             │
             ▼
            End

---

## 📚 Learning Outcome

This project provides practical experience with:

**Python → NumPy → Arrays → Modules → Packages → OOP → Data Analysis → Statistics**

The project demonstrates how a Python application can be divided into smaller reusable components while keeping the main program organized and easy to maintain.

---

## 🌍 Real-World Use Cases

The concepts demonstrated in this project can be useful for:

- Numerical data processing
- Basic data analysis
- Mathematical calculations
- Array manipulation
- Statistical calculations
- Data filtering
- Data sorting
- Scientific computing fundamentals
- Educational NumPy applications

---

## 🚀 Future Improvements

Possible future enhancements include:

- CSV file import and export
- Pandas integration
- Matplotlib data visualization
- Graphical User Interface
- Advanced statistical functions
- Multiple-condition filtering
- Saving analysis results to files
- Data visualization dashboards
- Interactive data analysis

---

## 🧹 Git & GitHub

Generated Python cache files should not be uploaded to GitHub.

Recommended `.gitignore`:

    __pycache__/
    *.pyc

This keeps the repository clean and professional.

---

## 🧪 Testing Status

The application has been tested successfully through the console interface.

Verified operations include:

- 1D array creation
- 2D array creation
- 3D array creation
- Array indexing
- 1D slicing
- 2D slicing
- Array combining
- Array splitting
- Addition
- Subtraction
- Multiplication
- Division
- Dot product
- Matrix multiplication
- Searching
- Ascending sorting
- Descending sorting
- Filtering
- Sum
- Mean
- Median
- Standard deviation
- Variance
- Minimum
- Maximum
- Percentile
- Correlation coefficient
- Current array display
- Program exit

Verified example results:

    Addition:
    [11. 22. 33. 44. 55.]

    Dot Product:
    32

    Matrix Multiplication:
    [[19. 22.]
     [43. 50.]]

---

## 📌 Project Information

| Item | Details |
|---|---|
| Project Name | NumPy Analyzer |
| Project Type | NumPy Data Analysis Toolkit |
| Programming Language | Python 3 |
| Main Library | NumPy |
| Interface | Console / Menu-Driven |
| Architecture | Modular & Object-Oriented |
| Package | `analyzer` |
| External Dependency | NumPy |
| Status | Completed and Tested |

---

## 👨‍💻 Author

**Shyam Gor**

Created for educational purposes to demonstrate:

- NumPy
- Modular programming
- Python packages
- Object-Oriented Programming
- Array operations
- Mathematical operations
- Search, sort and filter
- Statistical analysis

---

## 📄 License

This project is created for educational purposes as part of a Python and NumPy programming project.

You are free to study and modify the code for learning and academic purposes.
