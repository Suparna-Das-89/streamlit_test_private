import streamlit as st
st.title("Hello, Suparna! Today is a nice day." )
st.write("Welcome to this demo of Streamlit.")
name = st.text_input("Enter your name:", "")
button = st.button("Submit")
if button:
    st.write("Hello," , name)

import pandas as pd
df = pd.DataFrame({
    "date": pd.date_range("2023-01-01", periods=10),
    "value": range(10)
})
st.dataframe(df)
st.line_chart(df.set_index("date"))
st.bar_chart(df.set_index("date"))
st.area_chart(df.set_index("date"))
st.write("This is a simple Streamlit app that demonstrates basic functionality.")

#link to a website
st.markdown("[Visit Streamlit Documentation](https://docs.streamlit.io/)")
image = st.camera_input("Take a picture", key="camera_input")
st.image(image, caption="Captured Image", use_container_width=True)