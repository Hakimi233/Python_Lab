# Data Cleaning with Python (Pandas)

## Project Overview
This project demonstrates how to clean real-world datasets using **Python**, **Pandas**, and **NumPy**. Two datasets were cleaned by identifying missing values, invalid values, duplicates, and inconsistent data, then exporting the cleaned datasets as new CSV files.

## Technologies Used
- Python 3
- Pandas
- NumPy

## Project Structure

```
Data_Cleaning/
│── Cleaning_data/
│   ├── sales.csv
│   └── students.csv
│
│── sales_cleaning.py
│── students_cleaning.py
│
│── Sales_data_Cleaning.csv
│── Student_data_cleaned.csv
│
└── README.md
```

---

# Dataset 1: Sales Data Cleaning

### Cleaning Tasks Performed

- Loaded the dataset using Pandas.
- Checked for invalid values.
- Replaced:
  - Negative Quantity values with NaN.
  - Negative UnitPrice values with NaN.
  - Invalid Month names with NaN.
- Filled missing values:
  - Month → "Unknown"
  - Product → "Unknown"
  - Quantity → Mean value
  - UnitPrice → Median value
- Recalculated the **TotalSales** column:

```
TotalSales = Quantity × UnitPrice
```

- Exported the cleaned dataset as:

```
Sales_data_Cleaning.csv
```

---

# Dataset 2: Student Data Cleaning

### Cleaning Tasks Performed

- Converted the **Physics** column to numeric values.
- Converted invalid values to NaN.
- Checked for invalid data:
  - Age less than 0 or greater than 100
  - StudyHours less than 0 or greater than 24
  - Attendance less than 0 or greater than 100
  - Math marks outside 0–100
- Replaced invalid values with NaN.
- Filled missing values:
  - Name → "Unknown"
  - Gender → "No Gender"
  - Department → "Chemistry"
  - Age → Mean
  - StudyHours → Median
  - Attendance → Mean
  - Math → Median
  - Physics → Median
  - Programming → Median
- Calculated the Average score:

```
Average = (Math + Physics + Programming) / 3
```

- Standardized Gender values:
  - Male → M
  - X → No Gender
- Removed duplicate records.
- Exported the cleaned dataset as:

```
Student_data_cleaned.csv
```

---

# Learning Objectives

This project demonstrates how to:

- Read CSV files using Pandas.
- Detect missing values.
- Detect invalid values.
- Replace invalid values with NaN.
- Fill missing values using mean, median, or text values.
- Standardize categorical data.
- Remove duplicate records.
- Create new calculated columns.
- Export cleaned datasets.

---

# How to Run

Install the required libraries:

```bash
pip install pandas numpy
```

Run the scripts:

```bash
python sales_cleaning.py
```

```bash
python students_cleaning.py
```

The cleaned CSV files will be generated automatically.

---

# Output Files

- `Sales_data_Cleaning.csv`
- `Student_data_cleaned.csv`

---

# Author

**Farzana Hakimi**

Computer Science Student

Asian University for Women