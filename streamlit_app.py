import streamlit as st

# Set the title of the app
st.title("Simple Streamlit App")

# Create an input widget
name = st.text_input("Enter your name")

# Create a button and define what happens when it is clicked
if st.button("Greet"):
    if name:
        st.write(f"Hello, {name}! Welcome to Streamlit.")
    else:
        st.write("Please enter your name.")

# Add a simple slider
number = st.slider("Select a number", 1, 100)
st.write(f"You selected: {number}")
