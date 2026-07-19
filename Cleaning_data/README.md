# Data Cleaning with Python (Pandas)

## Project Overview

This project demonstrates data cleaning techniques using **Python**, **Pandas**, and **NumPy**. Two datasets, **sales.csv** and **students.csv**, were cleaned by handling missing values, correcting invalid data, removing duplicates, and exporting the cleaned datasets.

## Technologies Used

- Python 3
- Pandas
- NumPy

---

## Project Structure

```
Cleaning_data/
│── README.md
│── sales.csv
│── students.csv
│── sales_cleaning.py
│── students_cleaning.py
│── sales_data_cleaned.csv
└── student_data_cleaned.csv
```

---

# Sales Dataset Cleaning

### Cleaning Steps

- Loaded the dataset using Pandas.
- Checked for invalid values.
- Replaced:
  - Negative values in **Quantity** with `NaN`.
  - Negative values in **UnitPrice** with `NaN`.
  - Invalid month names with `NaN`.
- Filled missing values:
  - **Month** → `"Unknown"`
  - **Product** → `"Unknown"`
  - **Quantity** → Mean value
  - **UnitPrice** → Median value
- Recalculated the **TotalSales** column using:

```
TotalSales = Quantity × UnitPrice
```

- Saved the cleaned dataset as:

```
sales_data_cleaned.csv
```

---

# Student Dataset Cleaning

### Cleaning Steps

- Converted the **Physics** column to numeric values.
- Converted invalid values to `NaN`.
- Checked for invalid values:
  - Age less than 0 or greater than 100
  - StudyHours less than 0 or greater than 24
  - Attendance less than 0 or greater than 100
  - Math scores outside the range of 0–100
- Replaced invalid values with `NaN`.
- Filled missing values:
  - **Name** → `"Unknown"`
  - **Gender** → `"No Gender"`
  - **Department** → `"Chemistry"`
  - **Age** → Mean value
  - **StudyHours** → Median value
  - **Attendance** → Mean value
  - **Math** → Median value
  - **Physics** → Median value
  - **Programming** → Median value
- Calculated the **Average** score using:

```
Average = (Math + Physics + Programming) / 3
```

- Standardized gender values:
  - `"Male"` → `"M"`
  - `"X"` → `"No Gender"`
- Removed duplicate records.
- Saved the cleaned dataset as:

```
student_data_cleaned.csv
```

---

# Learning Objectives

This project demonstrates how to:

- Read CSV files using Pandas.
- Detect missing values.
- Detect invalid data.
- Replace invalid values with `NaN`.
- Fill missing values using the mean, median, or text values.
- Standardize categorical data.
- Remove duplicate records.
- Create calculated columns.
- Export cleaned datasets as CSV files.

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

The cleaned datasets will be generated automatically in the project folder.

---

# Output Files

- `sales_data_cleaned.csv`
- `student_data_cleaned.csv`

---

# Author

**Farzana Hakimi**

Computer Science Student

Asian University for Women