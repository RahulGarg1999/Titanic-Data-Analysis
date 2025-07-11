# Titanic-Data-Analysis
Titanic Data Analysis Project
This repository contains a Python script for analyzing the Titanic dataset using pandas, matplotlib, seaborn. It includes data loading, cleaning, visualization, and basic preprocessing steps.


📌 Features

✅ Load Titanic data from CSV

✅ Explore data shape, columns, data types

✅ Descriptive statistics and info

✅ Survival analysis with pie charts and bar plots

✅ Gender and class-based visualizations

✅ Age distribution histograms

✅ Data cleaning (missing values, encoding)

✅ Matplotlib and Seaborn plots


🗂️ Project Structure:
.
├── analysis_script.py      # Main Python script
├── Titanic.csv             # Dataset (you'll need to add this)
└── README.md               # This file


⚙️ Requirements

Python 3.x

pandas

matplotlib

seaborn

numpy

Install them using:

pip install pandas matplotlib seaborn numpy


🚀 How to Run

1️⃣ Place your Titanic.csv file in the same folder as the script.

2️⃣ Run the script:

python analysis_script.py


📊 Analysis Steps in Script

Load CSV file using pandas.

Display first and last 10 rows.

Show data shape and column names.

Display data types.

Summary statistics with .describe() and .info().

Count and visualize survival with pie charts.

Analyze female passengers by class with pie charts.

Study survival of females under age 30.

Study survival of males over age 40.

Age distribution with histogram (20 bins).

Age distribution by survival status.

Class and gender-based survival analysis with bar plots.

Passenger class counts in bar plots.

Survival by class with seaborn countplots.

Combined subplots for gender/class survival and class counts.

Survival among 3rd class males and 1st class females.

Crosstab for class vs gender.

Label encoding for Sex and Embarked columns.

Handling missing Age values.

Dropping unwanted columns for final dataset.


📈 Example Visuals

Pie chart of survived vs not-survived passengers

Bar chart of passengers per class

Histograms of age distribution

Countplots for survival by class and gender


✅ Notes

Make sure your Titanic CSV file has the required columns (like Survived, Pclass, Sex, Age, etc.).

You can adapt the script for other CSV file paths or formats.
