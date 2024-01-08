import streamlit as st
from src.fs_calculator import FSCalculator

def main():


    st.title("Simple Calculator")

    # Get user inputs
    #number1 = st.number_input("Enter the first number:", value=0.0)
    #number2 = st.number_input("Enter the second number:", value=0.0)
    #number3 = st.number_input("Enter the third number:", value=0.0)


    cost = st.number_input("Enter the total cost:", value=0.0)
    key_index = 0

    st.session_state.numbers_list = [st.number_input("Enter a number:", value=0.0, key=key_index)]

    if st.button("Add new row"):
        key_index += 1
        st.session_state.numbers_list.append(st.number_input("Enter a number:", value=0.0, key=key_index))

    # Create a list of numbers
    #numbers = [number1, number2, number3]
    #import pdb; pdb.set_trace()
    # Perform the calculation
    calc_obj = FSCalculator(cost, st.session_state.numbers_list)

    # Display the result
    st.write("Result:")
    st.write(calc_obj.rebalanced_pay)

    # TODO: this code doesn't work. The whole adding new buttons dynamically isn't working. Try asking for num of rows needed and then set them?
    # Then user id is implicitly set without asking for names which is a benefit! Since the row corresponds to the user
if __name__ == "__main__":
    main()
