import pandas as pd

def load_data():
    df = pd.read_csv("data/student_dataset_v2.csv")

    print("\n===== DATA LOADED SUCCESSFULLY =====")

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nLast 5 Rows:")
    print(df.tail())

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nData Types:")
    print(df.dtypes)

    print("\nInformation:")
    print(df.info())

    return df