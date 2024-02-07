import streamlit as st
from src.fs_calculator import FSCalculator


def main():
    st.title("FairShare Calculator")

    st.write("**Using The FairShare Calculator:** <br><br>"
             "This calculator lets you split costs among friends when different friends are "
             "willing to pay different amounts for a shared cost. Based on the information "
             "provided, we generate a suggested payment amount such that people who are willing "
             "to pay more than the average cost subsidize people who want to pay below the average "
             "cost. Enter the total cost and the number of people splitting it. You'll see "
             "the average cost displayed. Each person enters the maximum amount they would "
             "happily pay (what they feel is fair for them). That amount can be above or below the average "
             "cost. The calculator allocates surplus from those willing to pay more to subsidize those "
             "who want to pay less. "
             "Those paying above average won't be given a price higher than their listed price, but those paying "
             "below average may not achieve their listed price if there isn't enough surplus in the group. "
             "These numbers are meant to be a starting point for a discussion on fair shares. "
             "Try playing around with them and seeing what the calculator suggests. "
             "Scroll to the bottom of the page for more info on how fair costs are calculated.  <br><br>"

             , unsafe_allow_html=True)

    cost = st.number_input("Enter the total cost:", value=0.0, step=1.0)
    num_users = st.number_input("Enter the number of people splitting this cost:", value=1, max_value=50)
    avg_cost = cost/num_users
    st.write("Your average cost per person is: " + str(avg_cost))
    wtp_list = []
    for i in range(num_users):
        wtp = st.number_input("Enter the maximum amount that person number " + str(i+1) + " is willing to pay", value=avg_cost, step=1.0, key=i)
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

    calc_url = 'https://github.com/ShreyanSen/FairShare/blob/main/src/fs_calculator.py'
    calc_url_text = 'find the math here '

    st.write("<br>**How We Calculate Fair Costs:** <br><br>"
             "There's many possible ways to think about fairness when it comes to splitting costs. "
             "This tool basically assumes you're splitting costs with your friends, so you only put a max amount "
             "that you're really willing to lose, knowing it's going towards your friends, and if you're asking "
             "to receive you're doing it in good faith, putting a number that isn't below the amount you'd "
             "really be ok paying. <br> <br>"
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
             "starting point to find numbers that work for you and your friends! <br><br>"
             "If you're interested, you can "
             f'[{calc_url_text}]({calc_url})'
             ,  unsafe_allow_html=True)

if __name__ == "__main__":
    main()
