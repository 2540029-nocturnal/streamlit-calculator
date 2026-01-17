import streamlit as st


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


st.title("🧮 Simple Calculator Application")

num1 = st.number_input("Enter first number:", step=1.0, key="num1")
num2 = st.number_input("Enter second number:", step=1.0, key="num2")

operation = st.radio(
    "Choose an operation:",
    ("Addition", "Subtraction", "Multiplication", "Division"),
    key="operation"
)

if st.button("Calculate", key="calculate"):
    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)

    st.success(f"Result: {result}")
