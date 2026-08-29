# 🧮 NumPy Analyzer

## Python-Based Numerical Data Analysis Toolkit

A clean, modular and menu-driven Python application built using NumPy for performing array management, mathematical operations, searching, sorting, filtering and statistical analysis.

---

## 🎯 Project Objective

The main objective of this project is to demonstrate the practical use of NumPy and modular programming concepts through a structured command-line application.

The project demonstrates:

- NumPy arrays and array manipulation
- 1D, 2D and 3D arrays
- Indexing and slicing
- Combining and splitting arrays
- Mathematical operations
- Matrix multiplication
- Searching, sorting and filtering
- Aggregation and statistical functions
- Python modules and packages
- Object-Oriented Programming
- Exception handling
- Menu-driven programming

---

## ✨ Features

### 🔢 Array Management

- Create 1D arrays
- Create 2D arrays
- Create 3D arrays
- Indexing
- 1D slicing
- 2D slicing
- Combine arrays
- Split arrays

### 🧮 Mathematical Operations

- Addition
- Subtraction
- Multiplication
- Division
- Dot Product
- Matrix Multiplication

### 🔍 Search, Sort & Filter

- Search for a value
- Sort in ascending order
- Sort in descending order
- Filter values using conditions

Supported conditions:

`>` `<` `>=` `<=` `==` `!=`

### 📊 Statistical Operations

- Sum
- Mean
- Median
- Standard Deviation
- Variance
- Minimum
- Maximum
- Percentile
- Correlation Coefficient
- Display All Statistics

### 📐 Array Information

- Display current array
- Display number of dimensions
- Display array shape

---

## 📂 Project Structure

numpy-analyzer/
│
├── NumPy_Analyzer.py
├── README.md
│
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
| `NumPy_Analyzer.py` | Main application and menu-driven interface |
| `README.md` | Project documentation |
| `analyzer/__init__.py` | Initializes the custom Python package |
| `analyzer/array_operations.py` | Handles array creation, indexing, slicing, combining and splitting |
| `analyzer/math_operations.py` | Handles mathematical and matrix operations |
| `analyzer/search_sort_filter.py` | Handles searching, sorting and filtering |
| `analyzer/statistics.py` | Handles aggregation and statistical calculations |

---

## 📦 Modules Used

| Module | Purpose |
|---|---|
| `numpy` | Numerical computing and array operations |
| `analyzer.array_operations` | Array creation and manipulation |
| `analyzer.math_operations` | Mathematical calculations |
| `analyzer.search_sort_filter` | Searching, sorting and filtering |
| `analyzer.statistics` | Statistical and aggregation operations |

---

## 🛠️ Technologies Used

- Python 3
- NumPy
- Object-Oriented Programming
- Modular Programming
- Python Packages
- Exception Handling
- Console / Menu-Driven Interface

---

## 🧠 Concepts Demonstrated

### Python Concepts

- Classes and Objects
- Constructors
- Instance Methods
- Class Methods
- Static Methods
- Functions
- Conditional Statements
- Loops
- User Input
- Exception Handling
- Modules
- Packages
- `__init__.py`
- `if __name__ == "__main__"`

### NumPy Concepts

- `np.array()`
- Array dimensions
- Array shape
- 1D arrays
- 2D arrays
- 3D arrays
- Indexing
- Slicing
- Array manipulation
- Element-wise operations
- Dot Product
- Matrix Multiplication
- Searching
- Sorting
- Filtering
- Aggregation
- Statistical calculations

---

## ⚙️ Requirements

- Python 3.x
- NumPy

Install NumPy with:

`pip install numpy`

No other external libraries are required.

---

## 🚀 How to Run

### 1. Clone the Repository

`git clone https://github.com/rajgorshyam18-lab/numpy-analyzer.git`

### 2. Open the Project Folder

`cd numpy-analyzer`

### 3. Install NumPy

`pip install numpy`

### 4. Run the Application

`python NumPy_Analyzer.py`

On Windows:

`py NumPy_Analyzer.py`

---

## 🖥️ Main Menu

The application provides the following options:

1. Array Management
2. Mathematical Operations
3. Search, Sort & Filter
4. Aggregating & Statistical Functions
5. Display Current Array
6. Exit

Select the required option and follow the instructions displayed in the terminal.

---

## 🔢 Array Management

The Array Management section provides:

- 1D array creation
- 2D array creation
- 3D array creation
- Indexing
- 1D slicing
- 2D slicing
- Array combination
- Array splitting

---

## 🧮 Mathematical Operations

The Mathematical Operations section provides:

- Addition
- Subtraction
- Multiplication
- Division
- Dot Product
- Matrix Multiplication

Example matrix multiplication result:

[[19. 22.]
 [43. 50.]]

---

## 🔍 Search, Sort & Filter

The Search, Sort & Filter section provides:

- Value searching
- Ascending sorting
- Descending sorting
- Conditional filtering

Example search result:

Value found at index: (array([2]),)

---

## 📊 Statistical Analysis

The Statistics section provides:

- Sum
- Mean
- Median
- Standard Deviation
- Variance
- Minimum
- Maximum
- Percentile
- Correlation Coefficient
- Display All Statistics

These operations demonstrate practical NumPy-based data analysis.

---

## 🛡️ Error Handling

The application handles common input errors such as:

- Invalid menu choices
- Invalid numeric input
- Incorrect number of array elements
- Invalid dimensions
- Invalid percentile values
- Division by zero
- Incompatible matrix dimensions
- Invalid slicing input
- Mismatched dataset sizes

---

## 🏗️ Application Architecture

The project follows a modular and object-oriented structure.

The main `DataAnalytics` class connects the different operation modules:

- `ArrayOperations`
- `MathOperations`
- `SearchSortFilter`
- `Statistics`

This separation keeps the code organized, reusable and easier to maintain.

---

## 🧪 Testing

The following major features were tested through the console interface:

- 1D array creation
- 2D array creation
- 3D array creation
- Indexing
- 1D slicing
- 2D slicing
- Combining arrays
- Splitting arrays
- Addition
- Subtraction
- Multiplication
- Division
- Dot Product
- Matrix Multiplication
- Searching
- Ascending Sorting
- Descending Sorting
- Filtering
- Sum
- Mean
- Median
- Standard Deviation
- Variance
- Minimum
- Maximum
- Percentile
- Correlation Coefficient
- Current Array Display
- Program Exit

---

## 📸 Screenshots

Screenshots demonstrating the application interface and output are included in the repository.

They showcase:

- Main menu
- Array operations
- Mathematical operations
- Matrix multiplication
- Search, sort and filter
- Statistical operations

---

## 🌍 Real-World Applications

The concepts demonstrated in this project can be applied to:

- Numerical data processing
- Basic data analysis
- Scientific computing
- Mathematical calculations
- Statistical analysis
- Data filtering
- Data sorting
- Array-based data processing
- Educational data analysis

---

## 🚀 Future Improvements

Possible future enhancements include:

- CSV import and export
- Pandas integration
- Matplotlib visualization
- Graphical User Interface
- Advanced statistical functions
- Multiple-condition filtering
- Saving analysis results
- Data visualization
- Interactive data analysis

---

## 📚 Learning Outcome

This project provides practical experience with:

Python → NumPy → Arrays → Modules → Packages → OOP → Data Analysis → Statistics

It demonstrates how a Python application can be divided into reusable modules while keeping the main program organized, readable and maintainable.

---

## 📋 Project Information

| Item | Details |
|---|---|
| Project Name | NumPy Analyzer |
| Project Type | Numerical Data Analysis Toolkit |
| Programming Language | Python 3 |
| Main Library | NumPy |
| Interface | Console / Menu-Driven |
| Architecture | Modular & Object-Oriented |
| Package | `analyzer` |
| External Dependency | NumPy |
| Status | Completed |

---

## 👨‍💻 Author

**Shyam Gor**

Created for educational purposes to demonstrate NumPy, modular programming, packages, object-oriented programming and basic data analysis.

---

## 📄 License

This project is created for educational and academic purposes.
