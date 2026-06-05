import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_absolute_error, accuracy_score , r2_score
import matplotlib.pyplot as plt


x = [
    [1],[2],[3],[4],[5]
]
y = [5,7,8,9,10]

x_train , x_test , y_train , y_test = train_test_split(x,y , test_size=0.2 , random_state=42)

model = LinearRegression()

model.fit(x_train , y_train)

pred = model.predict(x_test)

mae = mean_absolute_error(y_test , model.predict(x_test))
score = r2_score(y_test , pred)

print(f"Predection = {pred}")
print(f"Mean Error = {mae}")
print(f"R2 Score = {score}")


