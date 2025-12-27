import tensorflow as tf
import matplotlib.pyplot as plt

(x_train, y_train), _ = tf.keras.datasets.fashion_mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_train = x_train[:1000]  # small sample
y_train = y_train[:1000]

model = tf.keras.Sequential([
    tf.keras.layers.Reshape((28,28,1)),
    tf.keras.layers.Conv2D(16, 3, activation='relu'),
    tf.keras.layers.GlobalAvgPool2D(),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))
model.fit(x_train, y_train, epochs=1, verbose=0)

print("👕 Week 6: Fashion CNN — Trained on CPU in seconds!")