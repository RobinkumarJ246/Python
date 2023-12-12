import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt


input_data = [1, 2, 3, 4, 5]
output_data = [10, 20, 30, 40, 50]

model = keras.Sequential([
    keras.layers.Dense(1,input_shape=[1])])


model.compile(optimizer='adam', loss='mean_squared_error')


model.fit(input_data, output_data, epochs=100)

new_input = [7]
prediction = model.predict(new_input)

print(prediction)
plt.plot(input_data,output_data)
plt.show()