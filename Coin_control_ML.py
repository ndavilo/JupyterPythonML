import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def Coin_control(BTCvalue, Index):
    try:
        BTCvalue = float(BTCvalue)
        Index = int(Index)
        if int(Index) == 0 or 1 or -1:
            df = pd.read_csv('BTC-USD.csv')
            X = df.drop(columns=['Advice'])
            y = df['Advice']

            model = DecisionTreeClassifier()
            model.fit(X.values, y)
            decision = model.predict([[BTCvalue, Index]])

            return decision
    except:
        return 'Input Error'
    
# Example: Coin_control(30, 1)
