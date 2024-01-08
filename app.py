import streamlit as st
from src.fs_calculator import FSCalculator

def main():


    st.title("Simple Calculator")

    # Get user inputs
    number1 = st.number_input("Enter the first number:", value=0.0)
    number2 = st.number_input("Enter the second number:", value=0.0)
    number3 = st.number_input("Enter the third number:", value=0.0)
    cost = st.number_input("Enter the total cost:", value=0.0)


    # Create a list of numbers
    numbers = [number1, number2, number3]

    # Perform the calculation
    calc_obj = FSCalculator(cost, numbers)

    # Display the result
    st.write("Result:")
    st.write(calc_obj.rebalanced_pay)

if __name__ == "__main__":
    main()
