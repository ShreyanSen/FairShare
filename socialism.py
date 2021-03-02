import itertools
from itertools import product
import functools
import numpy as np
import pandas as pd
import smtplib, ssl


class AnonSpirit:
  """
  Generate anonymous usernames from a set of input emails and send them to people

  """

  def __init__(self, email_list, total_cost, output_fp='/content/gdrive/MyDrive/happiness_to_pay.csv'):
    """
    Pass a list of emails and the total cost. We'll send each friend on the list
    a unique username and generate a csv with username and happiness to pay, to
    be filled out as inputs to the DemSpirit.
    Each friend must have an email. Total frenz = len(email_list).
    """
    self.email_list = email_list
    self.avg_cost = total_cost / len(email_list)
    self.output_fp = output_fp
    self.gen_usernames()
    self.email_usernames_out()
    self.usernames_to_csv()

  def gen_usernames(self):
    colors = ['red', 'blue', 'green', 'orange', 'pink', 'purple', 'yellow', 'black', 'white']
    emotions = ['happy', 'eager', 'quirky', 'hangry', 'chill', 'lofi', 'redundant', 'nontoxic', 'sporty', 'spicy']
    animals = ['beaver', 'lion', 'kitty', 'guanaco', 'antelope', 'gator', 'crow', 'snek', 'playtpus', 'pikachu']

    def combine_str(x): return functools.reduce(lambda a, b: a + '_' + b, x)

    usertuples = list(product(emotions, colors, animals))
    usernames = list(map(combine_str, usertuples))
    selected_usernames = np.random.choice(usernames, len(self.email_list), False)

    self.username_dict = dict(zip(self.email_list, selected_usernames))

  def email_usernames_out(self):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "institute4thotleadership@gmail.com"  # Enter your address
    # receiver_email = "your@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")

    SUBJECT = "Sparkle Bronies Unite"
    TEXT = "Get the mystery link from your friend, find your socialish username, and enter your Happiness to Pay. Your socialish username is... "
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      for receiver_email in self.username_dict:
        server.sendmail(sender_email, receiver_email, message + self.username_dict[receiver_email])

  def usernames_to_csv(self):
    tracking_df = pd.DataFrame(self.username_dict.values(), columns=['socialish_username'])
    tracking_df['happy_to_pay'] = self.avg_cost
    tracking_df.to_csv(self.output_fp, index=False)


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
