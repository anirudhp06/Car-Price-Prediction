import streamlit as st

# Define a function to get or create session state
def get_session_state():
    return st.session_state

# Define the first form
def first_form():
    st.header("First Form")
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:",min_value=1,value=999999,step=1)
    if not name=="" and age==999999:
        return name, age

# Define the second form
def second_form(name, age):
    st.header("Second Form")
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    # Add additional form elements here

# Main code
st.title("Multi-Form Streamlit App")

state = get_session_state()

if 'name' and 'age' not in state:
    state.name, state.age = first_form()

if st.button("Submit First Form"):
    # Process first form data
    # Add any processing code here

    # Display the second form
    second_form(state.name, state.age)