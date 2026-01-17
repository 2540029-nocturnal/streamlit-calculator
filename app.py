import streamlit as st

# -------------------------------
# Functions for arithmetic logic
# -------------------------------
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🧮 Simple Calculator Application")

# Input fields
num1 = st.number_input("Enter first number:", step=1.0)
num2 = st.number_input("Enter second number:", step=1.0)

# Operation selection
operation = st.radio(
    "Choose an operation:",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Compute result
if st.button("Calculate"):
    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)

    st.success(f"Result: {result}")
