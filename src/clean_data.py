import pandas as pd

def clean_data(df):

    print("\n===== DATA CLEANING =====")

    # Missing Values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Fill missing Marks with Mean
    df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

    # Duplicate Records
    print("\nDuplicate Rows:", df.duplicated().sum())

    # Remove Duplicates
    df = df.drop_duplicates()

    # Attendance Validation (0-100)
    df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)]

    # Study Hours Validation
    df = df[df["StudyHours"] >= 0]

    # Save Cleaned Data
    df.to_csv("output/cleaned_data.csv", index=False)

    print("\nData Cleaning Completed Successfully!")

    return df