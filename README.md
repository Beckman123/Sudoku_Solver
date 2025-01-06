# Sudoku Solver

This project provides a solution for solving Sudoku puzzles using both a manual solver and an AI-based solver. It also includes functionality to read Sudoku puzzles from images using Optical Character Recognition (OCR).

## Requirements

- Python 3.x
- TensorFlow
- NumPy
- OpenCV
- Tesseract OCR
- Pandas
- Scikit-learn

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/sudoku-solver.git
   cd sudoku-solver
   ```

2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR:

   - On macOS:
     ```sh
     brew install tesseract
     ```
   - On Ubuntu:
     ```sh
     sudo apt-get install tesseract-ocr
     ```

4. Download the pre-trained AI model and place it in the project directory:
   ```sh
   wget https://example.com/sudoku_solver_model.h5
   ```

## Usage

### Preprocess Data

1. Preprocess the Sudoku dataset:
   ```sh
   python import_process_data.py
   ```

### Train AI Model

1. Train the AI model:
   ```sh
   python train_model.py
   ```

### Solve Sudoku Puzzle

1. Solve a Sudoku puzzle from an image:
   ```sh
   python solve_from_image.py path/to/sudoku_image.png
   ```

### Example

1. Example input puzzle:
   ```plaintext
   100489006730000040000001295007120600500703008006095700914600000020000037800512004
   ```
2. Example output:

   ```plaintext
   Input puzzle:
   1 0 0 4 8 9 0 0 6
   7 3 0 0 0 0 0 4 0
   0 0 0 0 0 1 2 9 5
   0 0 7 1 2 0 6 0 0
   5 0 0 7 0 3 0 0 8
   0 0 6 0 9 5 7 0 0
   9 1 4 6 0 0 0 0 0
   0 2 0 0 0 0 0 3 7
   8 0 0 5 1 2 0 0 4

   Solved puzzle using AI model:
   1 5 2 4 8 9 3 7 6
   7 3 9 2 5 6 8 4 1
   4 4 8 3 7 1 2 9 5
   3 9 7 1 2 8 6 5 9
   5 9 1 7 6 3 4 2 8
   2 8 6 8 9 5 7 2 3
   9 1 4 6 7 7 8 2 2
   6 2 5 9 4 4 5 3 7
   8 7 3 5 1 2 9 6 4

   Solved puzzle manually:
   1 5 2 4 8 9 3 7 6
   7 3 9 2 5 6 8 4 1
   4 6 8 3 7 1 2 9 5
   3 8 7 1 2 4 6 5 9
   5 9 1 7 6 3 4 2 8
   2 4 6 8 9 5 7 1 3
   9 1 4 6 3 7 5 8 2
   6 2 5 9 4 8 1 3 7
   8 7 3 5 1 2 9 6 4
   ```
