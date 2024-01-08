class FSCalculator:
  """
  This class lets you split costs between your friends according to people's willingness to pay, 
  particularly for friend groups where some friends would like to pay under the average cost 
  while other friends are happy to pay over the average cost. Based on the "happy to pay" number
  the class redistributes from those willing to pay more, to those willing to pay less, according to the
  relative magnitudes of those listed quantities.
  
  If k friends buy something that costs X, each friend's default share is X/k
  However, we ask everyone to list a cost they would be happy to pay. 
  If they're a friend in need, then their cost c <= X/k
  If they're a friend in surplus, then their cost c >= X/k
  If they're a friend happy to pay at cost, they can also list c == X/k
  
  The delta for each friend is X/k - c, and can be positive or negative
  
  Based solely on that happy to pay number c, we redistribute any total surplus from the friends paying over to the friends paying under.
  If there isn't enough surplus to completely cover, we distribute the surplus proportional to each friend's listed need (the delta
  between c and X/k).
  
  If there is enough surplus to completely cover, each friend paying surplus will pay an identical fraction of the gap between their c and X/k
  
  This means friends in surplus should not list numbers higher than they're really willing to pay, because their money will get ate disproportionately
  compared to other surplus friends (the rate on their delta is fixed). 
  
  Likewise, if a friend in need lists a really low number, and the total surplus doesn't cover total need,
  they'll get more dollars back than their other friends in need, because each friend gets a fixed fraction of their delta paid back.
  
  Based on this adjustment, no friend in surplus will pay more than their happy to pay number.
  
  
  """
  def __init__(self, total_cost, payment_vec):
    """
    total_cost: decimal listing the total cost of the shared expense
    payment_vec: a list listing one number per friend, their happiness to pay number which can be at cost, above cost, or below cost
    
    """
    self.total_cost = total_cost
    self.htp = payment_vec
    self.total_frenz = len(payment_vec)
    self.avg_cost = self.total_cost / self.total_frenz
    self.htp_delta = self.get_delta_pay()
    self.rebalanced_pay = self.rebalance_costs() 
    
    # check self.rebalanced_pay to see what each person owes based on their original happy to pay number
    # please ask each person to remember their happy to pay number so they can look up their adjusted cost
    # if multiple people have the same happy to pay number, that's ok because they'll have the same adjusted cost as well

  def get_delta_pay(self):
    delta_pay = [pay - self.avg_cost for pay in self.htp]
    return delta_pay

  def rebalance_costs(self):
    delta_pay_df = pd.DataFrame(list(zip([self.avg_cost]*len(self.htp),self.htp, self.htp_delta)), columns=['avg_cost','happy_to_pay','delta_pay'])
    total_surplus = sum(delta_pay_df.loc[delta_pay_df.delta_pay > 0, 'delta_pay'])
    total_need = -1*sum(delta_pay_df.loc[delta_pay_df.delta_pay < 0, 'delta_pay'])

    delta_pay_df['rebalanced_delta'] = delta_pay_df['delta_pay']

    if total_surplus > total_need:
      delta_pay_df.loc[delta_pay_df.delta_pay > 0,'rebalanced_delta'] = delta_pay_df.loc[delta_pay_df.delta_pay > 0,'delta_pay']*(total_need / total_surplus) 
    elif total_surplus < total_need:
      delta_pay_df.loc[delta_pay_df.delta_pay < 0,'rebalanced_delta'] = delta_pay_df.loc[delta_pay_df.delta_pay < 0,'delta_pay']*(total_surplus / total_need) 

    delta_pay_df['adjusted_cost'] = delta_pay_df['avg_cost'] + delta_pay_df['rebalanced_delta']
    return delta_pay_df


    surplus_share = self.delta_pay / total_need
    surplus_share 

