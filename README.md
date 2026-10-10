
# Library Management System | Data Analytics Dashboard

A Python-based Library Management System that analyzes library borrowing transactions using Pandas, NumPy, Matplotlib, and Seaborn.

## Features

- Load library transaction data from CSV files.
- Identify missing values in the dataset.
- Fill missing numerical values using the mean.
- Fill missing categorical values using the mode.
- Calculate mean, median, maximum, standard deviation, variance, and sum.
- Group transactions by book genre.
- Calculate total and average borrowing duration.
- Generate library transaction summary reports.
- Visualize borrowing trends using charts.
- Implement Object-Oriented Programming (OOP).

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- CSV Dataset

## Project Structure

```text
Library-Management-System/
│
├── library_dashborad.py
├── library_transactions(1).csv
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Library-Management-System
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

Alternatively, install using the requirements file:

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python library_dashborad.py
```

## Main Menu

```text
============== Library Management System ===============

1. Load Dataset
2. Clearing Dataset
3. Calculate Statistics
4. Filter Transactions
5. Generate Report
6. Create Chart
7. Exit
```

## Data Analysis

### Data Cleaning
- Check missing values.
- Fill numerical missing values using column means.
- Fill categorical missing values using column modes.

### Statistical Analysis
- Mean borrowing duration.
- Median borrowing duration.
- Maximum borrowing duration.
- Standard deviation.
- Variance.
- Total borrowing duration.

### Transaction Analysis
- Count books by genre.
- Calculate total borrowing days by genre.
- Calculate average borrowing days by genre.

## Data Visualization

The application provides the following chart options:

1. Bar Chart — Top five most borrowed books.
2. Line Chart — Monthly borrowing trends.
3. Pie Chart — Borrowing distribution by genre.
4. Heatmap — Intended for borrowing activity analysis.

Note: The current heatmap implementation requires correction before it will work successfully.

## Learning Objectives

- Understand Python OOP concepts.
- Perform data cleaning using Pandas.
- Calculate statistical measures using NumPy.
- Group and aggregate transaction data.
- Generate reports from CSV datasets.
- Visualize data using Matplotlib and Seaborn.

## Future Enhancements

- Add, update, and delete books.
- Manage library members.
- Track book availability and due dates.
- Export reports to CSV, Excel, or PDF.
- Add an interactive dashboard using Streamlit.
- Store transaction records in a database.

## Author

**Shrey Anghan**

GitHub: [anghanshrey](https://github.com/anghanshrey)

## License

This project is created for educational and learning purposes.

---

⭐ If you find this project useful, consider giving the repository a star.
