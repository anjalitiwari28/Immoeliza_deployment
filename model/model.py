import pandas as pd

from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error



df = pd.read_csv('data_cleaned.csv', sep = ',')

df.replace({'property-type':{'APARTMENT' : 1, 'HOUSE' : 2}}, inplace = True)


X = df.loc[:, ["area","property-type","rooms-number"]].to_numpy()
y = df["Price"].to_numpy().reshape(-1 , 1)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()

regressor.fit(X_train,y_train)

# predict the target on train and test data 
predict_train = regressor.predict(X_train)
predict_test = regressor.predict(X_test)


# Root Mean Squared Error on train and test date
print('RMSE on train data: ', mean_squared_error(y_train, predict_train)**(0.5))
print('RMSE on test data: ',  mean_squared_error(y_test, predict_test)**(0.5))




# pickle your model  

import pickle

# Save the model 
pickle.dump(regressor, open('model.pkl', 'wb'))

