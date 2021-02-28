class DemDaemon:
  def __init__(self, total_cost, total_frenz, payment_vec):
    self.total_cost = total_cost
    self.total_frenz = total_frenz
    self.avg_cost = self.total_cost / self.total_frenz
    self.htp = payment_vec
    self.htp_delta = self.get_delta_pay()
    self.rebalanced_pay = self.rebalance_costs()

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

