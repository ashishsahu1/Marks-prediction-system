import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  

import pickle
url = "http://bit.ly/w-data"
s_data = pd.read_csv(url)
print("Data imported successfully")

X = s_data.iloc[:, :-1].values  
y = s_data.iloc[:, 1].values  


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  

regressor.fit(X, y) 
print("Training complete.")

pickle.dump(regressor,open('model.pkl','wb'))

model=pickle.load(open('model.pkl','rb'))
print("Pickle creation sucessfull")