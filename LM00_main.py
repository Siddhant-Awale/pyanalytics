   #Topic: Linear Regression Stock Market Prediction 
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Stock_Market = {'Year': [2017,2017,2017, 2017,2017,2017,2017,2017, 2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016, 2016,2016,2016], 'Month': [12, 11,10,9,8,7,6, 5,4,3, 2,1,12,11, 10,9,8,7,6,5,4,3,2,1], 'Interest_Rate': [2.75,2.5,2.5,2.5,2.5, 2.5,2.5,2.25,2.25, 2.25,2,2,2,1.75,1.75, 1.75,1.75, 1.75,1.75,1.75,1.75,1.75,1.75,1.75], 'Unemployment_Rate': [5.3,5.3, 5.3,5.3,5.4,5.6,5.5, 5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1, 5.9,6.2,6.2, 6.1],'Stock_Index_Price':[1464,1394,1357,1293,1256,1254,1234,1195, 1159,1167,1130,1075,1047,965, 943,958,971,949,884,866,876,822,704,719]   }  #dictionary format
type(Stock_Market)

df = pd.DataFrame(Stock_Market, columns=['Year','Month','Interest_Rate', 'Unemployment_Rate', 'Stock_Index_Price' ]) 
df.head(n=5)
print (df)
df.shape
#check that a linear relationship exists between the:
#Stock_Index_Price (dependent variable) and Interest_Rate (independent variable)
#Stock_Index_Price (dependent variable) and Unemployment_Rate (independent variable)

#run these lines together
%matplotlib inline
plt.scatter(df['Interest_Rate'], df['Stock_Index_Price'], color='red')
plt.title('Stock Index Price Vs Interest Rate', fontsize=14)
plt.xlabel('Interest Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.show()
# linear relationship exists between the Stock_Index_Price and the Interest_Rate. Specifically, when interest rates go up, the stock index price also goes up:
    
plt.scatter(df['Unemployment_Rate'], df['Stock_Index_Price'], color='green')
plt.title('Stock Index Price Vs Unemployment Rate', fontsize=14)
plt.xlabel('Unemployment Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.show() ;   

#linear relationship also exists between the Stock_Index_Price and the Unemployment_Rate – when the unemployment rates go up, the stock index price goes down (here we still have a linear relationship, but with a negative slope):

#Multiple Linear Regression
from sklearn import linear_model #1st method
import statsmodels.api as sm  #2nd method
    
X = df[['Interest_Rate','Unemployment_Rate']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example. Alternatively, you may add additional variables within the brackets
Y = df['Stock_Index_Price']
X 
Y
# with sklearn : from sklearn import linear_model
regr = linear_model.LinearRegression() #empty model
regr.fit(X, Y)
regr.score(X, Y)  #R2 
print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)
#Stock_Index_Price = (Intercept) + (Interest_Rate coef)*X1 + (Unemployment_Rate coef)*X2
#Stock_Index_Price = (1798.4040) + (345.5401)*X1 + (-250.1466)*X2

# prediction with sklearn
New_Interest_Rate = 2.75
New_Unemployment_Rate = 5.3
print ('Predicted Stock Index Price: \n', regr.predict([[New_Interest_Rate ,New_Unemployment_Rate]]))
#Interest Rate = 2.75 (i.e., X1= 2.75)
#Unemployment Rate = 5.3 (i.e., X2= 5.3)
Stock_Index_Price = (1798.4040) + (345.5401)*(2.75) + (-250.1466)*(5.3) #1422.86
Stock_Index_Price

# with statsmodels
import statsmodels.api as sm  #2nd method
X = sm.add_constant(X) # adding a constant
X.head() 
model = sm.OLS(Y, X).fit()  #create model
predictions = model.predict(X) 
predictions 
print_model = model.summary()
print(print_model)
#coefficients captured in this table match with the coefficients generated by sklearn.
print('R2 ', round(regr.score(X, Y),3) , 'Intercept: \n', np.round(regr.intercept_,3),  ' Coefficients', np.round(regr.coef_,3))
#we got consistent results by applying both sklearn and statsmodels.
#ref
#https://datatofish.com/multiple-linear-regression-python/
#end here