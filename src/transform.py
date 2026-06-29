def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def transform_data(df):

    print("\n===== DATA TRANSFORMATION =====")

    # Grade Column
    df["Grade"] = df["Marks"].apply(calculate_grade)

    # Result Column
    df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

    # Performance Score
    df["PerformanceScore"] = (
        df["Marks"] * 0.6 +
        df["Attendance"] * 0.2 +
        df["StudyHours"] * 2
    )

    print("Transformation Completed Successfully!")

    return df