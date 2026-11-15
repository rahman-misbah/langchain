# Calculate age by subtracting input year from current year
import streamlit as st
import datetime

st.title("Age Calculator")
st.header("Just the year for now xD")

dob = st.date_input("Enter your DOB", min_value=datetime.date(1900, 1, 1))
submit = st.button("Submit")

if submit:
    current_year = datetime.date.today().year
    age = current_year - dob.year
    st.success(f"You're {age} years old")
