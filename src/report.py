import pandas as pd

def generate_report(df):

    report = {
        "Total Students": [len(df)],
        "Passed Students": [len(df[df["Result"] == "Pass"])],
        "Failed Students": [len(df[df["Result"] == "Fail"])],
        "Highest Marks": [df["Marks"].max()],
        "Lowest Marks": [df["Marks"].min()],
        "Average Marks": [df["Marks"].mean()],
        "Average Attendance": [df["Attendance"].mean()],
        "Average Study Hours": [df["StudyHours"].mean()]
    }

    report_df = pd.DataFrame(report)

    report_df.to_csv("output/report.csv", index=False)

    print("\n===== REPORT GENERATED SUCCESSFULLY =====")