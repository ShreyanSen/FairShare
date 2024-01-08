import streamlit as st
from src.fs_calculator import FSCalculator


def main():
    st.title("FairShare Calculator")

    st.write("**How This Works:** <br>"
             "Enter the total cost and the number of people splitting it below. Then for each person, "
             "enter the max amount they'd be willing to pay. This number can be above or below the average cost. "
             "If it's below, this person will be subsidized. If it's above, this person may pay more than average. " 
             "Scroll to the bottom of the page for more info on how fair costs are calculated. <br><br>"
             , unsafe_allow_html=True)

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
    st.write("Results Table:")
    st.write(calc_obj.results)

    #TODO: add features including better / interpetable results outputting and notice if you covered or not!
    # covered means everyone hit their wtp, gets a smiley face
    # not covered gets a sad face

    if calc_obj.coverage:
        st.write('Yay! Everyone met their number that they are willing to pay!')
    else:
        st.write('Uh oh! Not everyone met their number that they are willing to pay. Back to the drawing board.')

    st.write("<br>**How We Calculate Fair Costs:** <br>"
             "There's many possible ways to think about fairness when it comes to splitting costs. "
             "This tool basically assumes you're splitting costs with your friends, so you only put a max amount "
             "that you're really willing to lose, knowing it's going towards your friends, and if you're asking "
             "to receive you're doing it in good faith, putting a number that isn't below the amount you'd "
             "really be ok paying. You can also just experiment with the tool until you find numbers that really "
             "do feel right. The key is trust and communication! This tool is just an add on. <br> <br>"
             "The math behind the tool works like this. For each person willing to pay above average, "
             "we take all those potential dollars and put them into the giver pot. That's our potential surplus. "
             "We also total up a deficit by adding up the total amount people want to pay below average. "
             "If your total surplus is above your total deficit you're golden. But how do we distribute? "
             "Basically, for each donor we look at the ratios of the amount they're willing to donate, and we "
             "distribute according to those ratios. So if one person is willing to pay 90 over the average "
             "and another is willing to pay 10 over average, then they will donate in a 9:1 ratio until they "
             "either run out of donor funds or cover the deficit. So if we have a total deficit of 20, then the "
             "first person will donate 18 and the second person will donate 2. So don't lowball OR highball your "
             "willingness to pay, or you'll shake those ratios around. "
             "What happens if the deficit isn't covered? Who receives what? We use the same logic we did on the "
             "donor side on the recipient side as well: we allocate funds according to the ratio of your delta "
             "to the average price. Since this tool is free, you can take a more detailed look at the math on github "
             "or just play around with the calculator until it makes intuitive sense. And of course, these calculator "
             "values are just ways to get the conversation started. You can always just use these numbers as a "
             "starting point to find numbers that work for you and your friends! "
             ,  unsafe_allow_html=True)

if __name__ == "__main__":
    main()
