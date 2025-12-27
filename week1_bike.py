import numpy as np
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

X, y = make_regression(n_samples=1000, n_features=10, noise=50, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor().fit(X_train, y_train)
pred = model.predict(X_test)

print("🚲 Week 1: Bike Rental Predictor")
print(f"MAE: {mean_absolute_error(y_test, pred):.0f} rentals")