import streamlit as st
from src.fs_calculator import FSCalculator

def main():


    st.title("FairShare Calculator")
    cost = st.number_input("Enter the total cost:", value=0.0, step=1.0)
    num_users = st.number_input("Enter the number of people splitting this cost:", value=1, max_value=50)

    st.write("Your average cost per person is: " + str(cost/num_users))
    wtp_list = []
    for i in range(num_users):
        wtp = st.number_input("Enter the maximum amount that person number " + str(i+1) + " is willing to pay", value=0.0, step=1.0, key=i)
        wtp_list.append(wtp)

    # Perform the calculation
    calc_obj = FSCalculator(cost, wtp_list)

    # Display the result
    st.write("Result:")
    st.write(calc_obj.rebalanced_pay)

    #TODO: add features including better / interpetable results outputting and notice if you covered or not!
    # covered means everyone hit their wtp, gets a smiley face
    # not covered gets a sad face


if __name__ == "__main__":
    main()
