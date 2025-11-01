import streamlit as st

# Set app title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator App")
st.write("Perform basic arithmetic operations easily using Streamlit.")

# Input numbers
num1 = st.number_input("Enter first number:", format="%.5f")
num2 = st.number_input("Enter second number:", format="%.5f")

# Operation selection
operation = st.selectbox(
    "Select operation:",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Perform calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"✅ Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"✅ Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"✅ Result: {num1} × {num2} = {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"✅ Result: {num1} ÷ {num2} = {result}")
        else:
            st.error("❌ Division by zero is not allowed.")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit")
