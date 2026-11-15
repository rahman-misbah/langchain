import streamlit as st

st.title("Deuz's Playground")
st.subheader("I really should be doing my report tbh")
st.text("But alas, streamlit it is")
st.write("A message for me?")
message = st.selectbox(
    "Message: ", ["Do report", "Well done", "Tumse naa hoga", "YOLO!"]
)
st.write(f"You chose {message}, really?")

st.success("Congrats on leaving a message!")
