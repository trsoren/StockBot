import robin_stocks.robinhood as r
from getpass import getpass
from statistics import mean
import sched, time
import pandas as pd

#outputs longest streak of increase/decrease
#right before the point hist[i]. Note that
#a streak of 0 is impossible. Might very
#slightly favor positive streaks due to the =
def prev_streak(hist, i):
    max_strk = 0
    strk = 1

    while(hist[i-strk] >= hist[i-(strk+1)]):
        max_strk = strk
        strk = strk + 1
    if max_strk > 0:
        return max_strk

    while(hist[i-strk] <= hist[i-(strk+1)]):
        max_strk = strk
        strk = strk + 1
    return -1*max_strk


s = sched.scheduler(time.time, time.sleep)
password = getpass()
r.login("trsorensen@comcast.net", password, expiresIn = 86400) # change expiresIn

hist = r.crypto.get_crypto_historicals('BTC', interval='day', span='5year', bounds='24_7', info='close_price')
hist = [float(x) for x in hist]
streaks = []
gains = []
for i in range(10, len(hist)): #skip first 10 points so all points have plently of prior data
    strk = prev_streak(hist, i)
    if (strk == 0):
        exit()
    gain = ((hist[i] - hist[i-1]) / hist[i-1]) * 100
    streaks.append(strk)
    gains.append(round(gain, 2))

df = pd.DataFrame(list(zip(streaks, gains)), columns=['Streaks', 'Gains'])
df.to_csv('stonks_day_per_5years.csv', index=False)
    

# runs every 15 seconds
# def check_market(sc):
#     s.enter(15, 1, check_market, (sc,)) #first number is time to check (in seconds)
# s.enter(15, 1, check_market, (s,))
# s.run()
#has_bought_today = 0
