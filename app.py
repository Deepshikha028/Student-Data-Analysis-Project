import streamlit as st
from src.load_data import load_data
from src.clean_data import clean_data
from src.transform import transform_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.title("📊 Student Data Analysis Dashboard")

# Load data
df = load_data()
df = clean_data(df)
df = transform_data(df)

# Show dataset
st.subheader("Dataset Preview")
st.dataframe(df)

# Basic stats
st.subheader("Basic Statistics")
st.write(df.describe())

# Top students
st.subheader("Top 10 Students")
st.write(df.sort_values("Marks", ascending=False).head(10))
st.sidebar.header("Filters")

min_marks = st.sidebar.slider("Minimum Marks", 0, 100, 50)
min_attendance = st.sidebar.slider("Minimum Attendance", 0, 100, 60)

df = df[(df["Marks"] >= min_marks) & (df["Attendance"] >= min_attendance)]

st.subheader("Filtered Data")
st.dataframe(df)
st.subheader("📊 Study Hours vs Marks")

st.scatter_chart(df[["StudyHours", "Marks"]])
st.subheader("🏆 Top 10 Students")

top10 = df.sort_values("Marks", ascending=False).head(10)
st.bar_chart(top10.set_index("Name")["Marks"])

st.subheader("📊 Attendance vs Marks")

st.scatter_chart(df[["Attendance", "Marks"]])
df = df.dropna()

# ================= ML MODEL =================

st.subheader("🤖 ML Prediction - Marks Prediction")

# Features and target
X = df[["StudyHours", "Attendance"]]
y = df["Marks"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
score = model.score(X_test, y_test)
st.write("Model Accuracy:", round(score, 2))

st.subheader("🎯 Predict Marks")

study = st.number_input("Enter Study Hours", 0.0, 10.0, 5.0)
attendance = st.number_input("Enter Attendance", 0, 100, 75)

if st.button("Predict Marks"):
    prediction = model.predict(np.array([[study, attendance]]))
    st.success(f"Predicted Marks: {prediction[0]:.2f}")
    import streamlit as st
from src.load_data import load_data
from src.clean_data import clean_data
from src.transform import transform_data

st.title("📊 Student Data Analysis Dashboard")

df = load_data()
df = clean_data(df)
df = transform_data(df)

st.dataframe(df)