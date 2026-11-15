import streamlit as st

st.title("Report Maker")
st.subheader("Make your report!")

uml_diagrams = st.checkbox("Add UML Diagrams")

if uml_diagrams:
    st.write("UML diagrams added!")

if st.button("Make Report"):
    st.success("Report creation started!")

report_type = st.radio("Select Report Format: ", ["IEEE", "AMU", "Nothing Specific"])
st.write(f"Selection is {report_type}")

technical_depth = st.slider("Technical Depth", 1, 10, 6)
st.write(f"Selected depth level is {technical_depth}")

page_len = st.number_input("How many pages?", 1, 10, 2, 2)

author_name = st.text_input("Enter author name")
if author_name:
    st.success(f"Report is being written by {author_name}!")

submission_date = st.date_input("Submission Date")
st.write(f"Due date is {submission_date}")
