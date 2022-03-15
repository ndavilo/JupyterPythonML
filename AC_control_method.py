import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def AC_control(temp, weather):
    try:
        temp = float(temp)
        weather = int(weather)
        if int(weather) == 0 or 1:
            df2 = pd.read_csv('AC_action.csv')
            X = df2.drop(columns=['action'])
            y = df2['action']

            model = DecisionTreeClassifier()
            model.fit(X.values, y)
            decision = model.predict([[temp, weather]])

            return decision
    except:
        return 'Input Error'
    
# Example: AC_control(30, 1)
