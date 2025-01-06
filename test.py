import numpy as np
import tensorflow as tf
from manual_solver import solve_puzzle

# Load the saved model
model = tf.keras.models.load_model("sudoku_solver_model.h5")

# Function to preprocess the input puzzle
def preprocess_puzzle(puzzle):
    x = np.array([int(i) for i in puzzle]).reshape((9, 9, 1))
    x = x / 9
    x -= 0.5
    return np.array([x])

# Function to post-process the prediction
def postprocess_prediction(prediction):
    prediction = prediction.reshape((81, 9))
    solved_puzzle = np.argmax(prediction, axis=1) + 1
    return solved_puzzle.reshape((9, 9))

# Function to print the puzzle in a readable format
def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(num) for num in row))

# Example input puzzle
input_puzzle = "100489006730000040000001295007120600500703008006095700914600000020000037800512004"

# Preprocess the input puzzle
preprocessed_puzzle = preprocess_puzzle(input_puzzle)

# Make a prediction using the AI model
prediction = model.predict(preprocessed_puzzle)

# Post-process the prediction
solved_puzzle_ai = postprocess_prediction(prediction)

# Solve the puzzle manually
solved_puzzle_manual = solve_puzzle(input_puzzle)

# Print the input puzzle
print("Input puzzle:")
input_puzzle_grid = np.array([int(i) for i in input_puzzle]).reshape((9, 9))
print_puzzle(input_puzzle_grid)

# Print the solved puzzle using AI model
print("\nSolved puzzle using AI model:")
print_puzzle(solved_puzzle_ai)

# Print the solved puzzle manually
print("\nSolved puzzle manually:")
print_puzzle(solved_puzzle_manual)