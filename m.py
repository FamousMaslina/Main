import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Bidirectional
from keras.layers import LSTM
# Load the Bitcoin price data
df = pd.read_csv('bitcoin_prices.csv')
prices = df['Close'].values

# Split the data into training and testing sets
train_prices = prices[:int(len(prices) * 0.8)]
test_prices = prices[int(len(prices) * 0.8):]

# Normalize the data
train_prices = (train_prices - np.mean(train_prices)) / np.std(train_prices)
test_prices = (test_prices - np.mean(test_prices)) / np.std(test_prices)

# Create the LSTM model
model = Sequential()
# Use a Bidirectional layer instead of an LSTM layer
model.add(Bidirectional(LSTM(128, input_shape=(train_prices.shape[1],))))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')

# Train the model
model.fit(train_prices, train_prices, epochs=100)

# Make predictions on the test set
predictions = model.predict(test_prices)

# Evaluate the model
mse = np.mean((predictions - test_prices)**2)
print('MSE:', mse)
