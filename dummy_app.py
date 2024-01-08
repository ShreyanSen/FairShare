import streamlit as st

def multiply_by_two(numbers):
    return [2 * num for num in numbers]

def main():
    st.title("Dynamic Calculator")

    # Initialize the session state
    if 'numbers_list' not in st.session_state:
        st.session_state.numbers_list = []

    # Display the existing rows
    for i, row in enumerate(st.session_state.numbers_list):
        st.write(f"Row {i + 1}: {row}")

    # Allow the user to add new rows
    if st.button("Add new row"):
        num_inputs = st.number_input("Number of inputs:", min_value=1, value=3)
        new_row = [st.number_input(f"Number {j + 1}:", value=0.0) for j in range(num_inputs)]
        st.session_state.numbers_list.append(new_row)

    # Perform the calculation for each row
    results = [multiply_by_two(row) for row in st.session_state.numbers_list]

    # Display the results for each row
    for i, result in enumerate(results):
        st.write(f"Result for Row {i + 1}: {result}")

if __name__ == "__main__":
    main()
