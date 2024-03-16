import streamlit as st

st.title('Weather App')

city = st.text_input("Search City...")
type = st.selectbox
if st.button("Search"):
    if type == "Current Weather":
        st.page_link("pages/cuaca.py")
    else:
        st.page_link("pages/predcuaca.py")