import streamlit as st
from src.fs_calculator import FSCalculator


def main():
    st.title("FairShare Calculator")

    st.write("This calculator lets you split costs among friends when different friends are "
             "willing to pay different amounts for a shared cost."
             "For more details on how the calculator "
             "works please scroll to the bottom of the page. "
            , unsafe_allow_html = True)

    cost = st.number_input("Enter the total cost:", value=0.0, step=1.0)
    num_users = st.number_input("Enter the number of people splitting this cost:", value=1, max_value=50)
    avg_cost = cost/num_users
    st.write("Your average cost per person is: " + str(avg_cost))
    wtp_list = []
    for i in range(num_users):
        wtp = st.number_input("Enter the maximum amount that person number " + str(i+1) + " is happy to pay", value=avg_cost, step=1.0, key=i)
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
    calc_url_text = 'find the math here'

    st.write("<br>**How We Calculate Fair Costs:** <br><br>"
             "Here's how the calculator works. "
             "Each person enters information about how much they want to pay, and then "
             "we generate a suggested payment amount for each person. The people who are willing "
             "to pay more than the average cost subsidize people who want to pay below the average "
             "cost. First, enter the total cost and the number of people splitting it. You'll see "
             "the average cost displayed. Then, each person enters the maximum amount they would "
             "happily pay (what they feel is fair for them). That amount can be above or below the average "
             "cost. Finally, the calculator reallocates surplus. <br><br>"
             "Those paying above average won't be given a price higher than their listed price, but those paying "
             "below average may not achieve their listed price if there isn't enough surplus in the group. "             
             "For each person willing to pay above average, "
             "we take all those potential dollars and put them into the giver pot. That's our potential surplus. "
             "We also total up a deficit by adding up the total amount people want to pay below average. "
             "If your total surplus is above your total deficit you're golden.  <br><br>"
             "But how do we distribute? "
             "For each donor we look at the ratios of the amount they're willing to donate, and we "
             "distribute according to those ratios. For example, if one person is willing to pay 90 over the average "
             "and another is willing to pay 10 over average, then they will donate in a 9:1 ratio until they "
             "either run out of donor funds or cover the deficit. So if we have a total deficit of 20, then the "
             "first person will donate 18 and the second person will donate 2. So don't lowball OR highball your "
             "willingness to pay, or you'll shake those ratios around. "
             "What happens if the deficit isn't covered? Who receives what? We use the same logic we did on the "
             "donor side on the recipient side as well: we allocate funds according to the ratio of your delta "
             "to the average price. Since this tool is free as in open source, "
             "you can take a more detailed look at the math on github "
             "or just play around with the calculator until it makes intuitive sense. <br><br>"
             "If you're interested, you can "
             f'[{calc_url_text}]({calc_url})'
             " :)"
             ,  unsafe_allow_html=True)

    st.write("<br>**When Would You Use The FairShare Calculator?** <br><br>"
             "This app was originally developed for a group of friends who were half working 9-5 and half students. "
             "When we wanted to go on shared adventures together, the working half had higher budgets for shared "
             "expenses like housing. Folks in this group were happy to pay a little extra proportionally in order "
             "to make the adventure a little nicer for everyone, and the FairShare calculator was born as a way of "
             "facilitating that conversation. <br><br>"
             
             "More generally, anytime people in a group have trust and goodwill and want to make a shared purchase, "
             "but either have different spending constraints or are receiving different amounts of value from the "
             "shared purchase, FairShare might be useful. Trust and goodwill are key, because the calculator's idea "
             "of fairness is easy to manipulate. It really only works if everyone in the group wants everyone in the "
             "group to win."

             ,  unsafe_allow_html=True)

if __name__ == "__main__":
    main()
