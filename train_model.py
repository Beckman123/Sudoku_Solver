import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
import pickle

# Load the processed dataset
with open("processed_sudoku.pkl", 'rb') as f:
    X_train, X_val, X_test, y_train, y_val, y_test = pickle.load(f)

# Define the CNN model
def build_sudoku_cnn():
    model = models.Sequential()
    model.add(layers.Input(shape=(9, 9, 1)))
    model.add(layers.Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Conv2D(128, kernel_size=(1, 1), activation='relu', padding='same'))
    model.add(layers.Flatten())
    model.add(layers.Dense(81 * 9))
    model.add(layers.Reshape((-1, 9)))
    model.add(layers.Activation('softmax'))
    return model

model = build_sudoku_cnn()

# Compile the model with accuracy as a metric
adam = optimizers.Adam(learning_rate=0.001)
model.compile(loss='sparse_categorical_crossentropy', optimizer=adam, metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, batch_size=32, epochs=30, validation_data=(X_val, y_val))

# Save the model
model.save("sudoku_solver_model.h5")

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Test accuracy: {test_acc}')
print(f'Test loss: {test_loss}')