import numpy as np
import pandas as pd


class Model:

    def place_bets(self, opps, summary, inc):
        N = len(opps)
        min_bet = summary.iloc[0].to_dict()['Min_bet']
        bets = np.zeros((N, 2))
        bets[np.arange(N), np.random.choice([0, 1], N)] = min_bet
        return pd.DataFrame(data=bets, columns=['BetH', 'BetA'], index=opps.index)
