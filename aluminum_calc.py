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
    can_low = weight / 14.5
    can_high = weight / 13.5
    acan_low = 118 / 14.5
    acan_high = 118 / 13.5
    st.write(f"There should be between {round(can_low, 2)} and {round(can_high, 2)} aluminum cans in the cube")
    st.write(f"Actually, there should be between {round(acan_low, 2)} and {round(acan_high, 2)} aluminum cans in the cube")
    st.write(f"The weight should be around {round(weight, 2)}")
config()
main()
