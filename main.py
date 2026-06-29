from src.load_data import load_data
from src.clean_data import clean_data
from src.transform import transform_data
from src.analyze import analyze_data
from src.report import generate_report

df = load_data()
df = clean_data(df)
df = transform_data(df)
analyze_data(df)
generate_report(df)

print("PROJECT COMPLETED SUCCESSFULLY")