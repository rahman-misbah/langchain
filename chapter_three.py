import streamlit as st

st.title("Report Submission")

col1, col2 = st.columns(2)

with col1:
    st.header("IEEE Format")
    st.image("https://ieee.eecs.umich.edu/images/ieee-logo.png", width=200)

with col2:
    st.header("AMU Format")
    st.image("https://digital.amu.ac.in/assets/img/LOGO2.png", width=200)


st.sidebar.header("Student Info")
name = st.sidebar.text_input("Student Name")
course = st.sidebar.selectbox("Course", ["B.Sc", "M.Sc", "MCA"])

if name and course:
    with st.expander("Student Info"):
        st.write(f"Student Name: {name}")
        st.write(f"Student Course: {course}")

st.markdown("## Markdown block")
