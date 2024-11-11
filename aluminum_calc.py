import streamlit as st

def config():
    st.set_page_config(page_title="Alluminum Calculator",
                    layout="wide")
    st.subheader("Welcome to Harrison's Aluminum Calculator")
    st.write("Record the dimmensions of the alluminum cube in centimeters:")

def main():
    width = st.number_input("What is the width of the cube?")
    length = st.number_input("What is the length of the cube?")
    height = st.number_input("What is the height of the cube?")

    cube = width * length * height
    weight = 2.7 * cube
    cans_low = weight / 13.5
    cans_high = weight / 14.5
    can_total = round(((cans_low + cans_high) / 2), 2)
    st.write(f"There should be roughly {can_total} aluminum cans in the cube")
config()
main()