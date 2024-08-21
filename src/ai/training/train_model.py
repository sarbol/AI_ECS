import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load and preprocess data
data = pd.read_csv('environment_data.csv')
X = data[['temperature', 'humidity', 'air_quality']]
y = data[['optimal_temp', 'optimal_lighting']]

# Train the model
model = RandomForestRegressor()
model.fit(X, y)

# Save the trained model
with open('../models/model_v1.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
