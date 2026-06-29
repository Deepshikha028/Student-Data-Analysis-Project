import pandas as pd

def analyze_data(df):

    print("\n========== DATA ANALYSIS ==========")

    # Module 4 : Data Filtering

    toppers = df[df["Marks"] >= 90]
    failed = df[df["Result"] == "Fail"]
    low_attendance = df[df["Attendance"] < 75]
    high_study = df[df["StudyHours"] > 8]

    # Save CSV Files
    toppers.to_csv("output/toppers.csv", index=False)
    failed.to_csv("output/failed_students.csv", index=False)

    # Module 5 : Analysis

    print("\nAverage Marks :", df["Marks"].mean())
    print("Highest Marks :", df["Marks"].max())
    print("Lowest Marks :", df["Marks"].min())

    print("\nAverage Attendance :", df["Attendance"].mean())
    print("Average Study Hours :", df["StudyHours"].mean())

    print("\nGrade Distribution")
    print(df["Grade"].value_counts())

    # Module 6 : Sorting

    print("\nTop 10 Students by Marks")
    print(df.sort_values(by="Marks", ascending=False).head(10))

    # Module 7 : Grouping

    print("\nAverage Marks by Grade")
    print(df.groupby("Grade")["Marks"].mean())

    print("\nStudents Count by Grade")
    print(df.groupby("Grade").size())

    # Module 8 : Statistical Analysis

    print("\nMean")
    print(df.mean(numeric_only=True))

    print("\nMedian")
    print(df.median(numeric_only=True))

    print("\nMode")
    print(df.mode())

    print("\nStandard Deviation")
    print(df.std(numeric_only=True))

    print("\nVariance")
    print(df.var(numeric_only=True))

    print("\nCorrelation")
    print(df.corr(numeric_only=True))