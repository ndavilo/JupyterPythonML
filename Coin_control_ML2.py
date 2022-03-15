import joblib
from sklearn.tree import DecisionTreeClassifier

# Example: Coin_control2(30000, 1)


def Coin_control2(BTCvalue, Index):
    try:
        BTCvalue = float(BTCvalue)
        Index = int(Index)

        model = joblib.load('BTC_decision.joblib')
        decision = model.predict([[BTCvalue, Index]])

        return decision
    except:
        return 'Input Error'
