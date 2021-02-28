import itertools
from itertools import product
import functools
import numpy as np
import pandas as pd


class Anonymize:
  """
  Generate anonymous usernames from a set of input emails and send them to people
  """

  def __init__(self, email_list):
    self.email_list = email_list
    self.gen_usernames()
    self.email_usernames_out()

  def gen_usernames(self):
    colors = ['red', 'blue', 'green', 'orange', 'pink', 'purple', 'yellow', 'black', 'white']
    emotions = ['happy', 'eager', 'quirky', 'hangry', 'chill', 'lofi', 'redundant', 'nontoxic']
    animals = ['beaver', 'lion', 'kitty', 'guanaco', 'antelope', 'gator', 'crow', 'snek', 'playtpus', 'pikachu']

    def combine_str(x): return functools.reduce(lambda a, b: a + '_' + b, x)

    usertuples = list(product(emotions, colors, animals))
    usernames = list(map(combine_str, usertuples))
    selected_usernames = np.random.choice(y, len(self.email_list), False)

    self.username_dict = dict(zip(self.email_list, selected_usernames))

  def email_usernames_out(self):
    return


class DemSpirit:
  def __init__(self, total_cost, total_frenz, payment_dict):
    self.total_cost = total_cost
    self.total_frenz = total_frenz
    self.avg_cost = self.total_cost / self.total_frenz
    self.htp = payment_dict
    self.htp_delta = self.get_delta_pay()
    self.rebalanced_pay = self.rebalance_costs()

  def get_delta_pay(self):
    delta_pay = [pay - self.avg_cost for pay in self.htp.values()]
    return delta_pay

  def rebalance_costs(self):
    delta_pay_df = pd.DataFrame(list(zip(self.htp.keys(),[self.avg_cost]*len(self.htp),self.htp.values(), self.htp_delta)), columns=['username','avg_cost','happy_to_pay','delta_pay'])
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

if __name__=="__main__":
  TOTAL_COST = 1000
  TOTAL_FRENZ = 10

  HAPPY_TO_PAY = {'A': 100, 'B': 150, 'C': 10, 'D': 20}

  Socialism = DemSpirit(TOTAL_COST, TOTAL_FRENZ, HAPPY_TO_PAY)
  Socialism.rebalanced_pay
