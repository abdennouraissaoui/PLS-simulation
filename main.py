import pandas as pd
import streamlit as st

expected_prize_per_ticket = 0.0167694112359
st.subheader("Settings:")
num_clients = st.slider("Number of clients", min_value=1, max_value=10000, step=100, value=5000)
avg_ticket_price = st.slider("Average ticket price ($)", min_value=1, max_value=200, step=5, value=35)
avg_acct_size = st.slider("Average account size ($)", min_value=500, max_value=10000, step=100, value=6000)
net_apy = st.text_input("Net APY % (APY earned - paid out)", 1)
total_deposits = avg_acct_size * num_clients
num_tickets = total_deposits / avg_ticket_price

weekly_rev = ((1+float(net_apy)/100)**(1/52)-1)*total_deposits
weekly_prize = expected_prize_per_ticket * num_tickets

st.subheader("Results:")

st.write(f"Expected Weekly APY Spread: {'${:,.2f}'. format(weekly_rev)}")
st.write(f"Expected Weekly Prizes: {'${:,.2f}'. format(weekly_prize)}")
st.write(f"Expected Weekly Cash Netflow: **{'${:,.2f}'. format(weekly_rev - weekly_prize).replace('$-', '-$')}**")

st.subheader(f"Assumptions:")
odds = {'Prize': {0: ' $0.10 ',
  1: ' $0.15 ',
  2: ' $0.75 ',
  3: ' $10.00 ',
  4: ' $2.50 ',
  5: ' $10,000.00 ',
  6: ' $10,000,000.00 ',
  7: ' $0.15 ',
  8: ' $7.00 ',
  9: ' $3,000.00 ',
  10: ' $40,000.00 '},
 'Probablility': {0: '0.91%',
  1: '0.55%',
  2: '0.12%',
  3: '0.01%',
  4: '0.00%',
  5: '0.00%',
  6: '0.00%',
  7: '0.63%',
  8: '0.02%',
  9: '0.00%',
  10: '0.00%'},
 'Expected payout/ticket/week': {0: ' $0.000909 ',
  1: ' $0.000829 ',
  2: ' $0.000865 ',
  3: ' $0.001009 ',
  4: ' $0.000009 ',
  5: ' $0.000465 ',
  6: ' $0.001211 ',
  7: ' $0.000938 ',
  8: ' $0.001589 ',
  9: ' $0.008647 ',
  10: ' $0.000300 '}}

st.write(pd.DataFrame.from_dict(odds))
st.write(f"Total: ${expected_prize_per_ticket}")