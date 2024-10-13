# AI Automobility Class

This repository contains various projects and practice scripts related to AI, Python programming, and deep learning with a focus on automobility and neural networks. The repo also contains class notes from AI Automobility class. The repository is divided into several sections, each serving a different purpose for educational and practical programming exercises. This repo is under work in progress.

## Table of Contents

- [Environment](https://github.com/NuttyJamie/AI-Automobility-Class#environment)
- [Project Overview](https://github.com/NuttyJamie/AI-Automobility-Class#project-overview)
- [Directory Structure](https://github.com/NuttyJamie/AI-Automobility-Class#directory-structure)
- [Setup Instructions](https://github.com/NuttyJamie/AI-Automobility-Class#setup-instructions)
- [Usage](https://github.com/NuttyJamie/AI-Automobility-Class#usage)
- [License](https://github.com/NuttyJamie/AI-Automobility-Class#license)

## Environment
- Slaceware 15.0 linux
- Python 3.9.10

## Project Overview

This project includes exercises and examples focusing on:

- **MNIST Dataset**: Various scripts related to the MNIST dataset and neural networks, including regression models, perceptrons, and deep learning from scratch.
- **Python Practice**: General Python exercises such as code refactoring and utility scripts.
- **Calculators**: A simple calculator implementation with basic and engineering operations.

## Directory Structure

Here is a breakdown of the repository structure:

```bash
.
├── LICENSE                       # License file
├── MNIST                         # Contains MNIST related scripts and data files
│   ├── MNIST-myown.py            # Custom MNIST example
│   ├── MNIST_1node.py            # Single-node neural network example
│   ├── MNIST_Class.py            # MNIST class-based model
│   ├── MNIST_regression.py       # MNIST regression example
│   ├── NN.py                     # Neural network script
│   ├── Untitled.ipynb            # Jupyter notebook for experimentation
│   ├── basic-perceptron.py       # Perceptron example
│   ├── mnist_deeplearning-from-scatch.py  # Deep learning from scratch
│   ├── sample_weight.pkl         # Sample weights for the neural network
│   ├── t10k-images-idx3-ubyte    # Test images (MNIST)
│   ├── t10k-labels-idx1-ubyte    # Test labels (MNIST)
│   ├── train-images-idx3-ubyte   # Training images (MNIST)
│   └── train-labels-idx1-ubyte   # Training labels (MNIST)
├── Notes                         # Notes and documentation
│   └── README.md                 # Notes README file
├── Python-practice               # General Python practice and exercises
│   ├── Code-refactoring          # Examples of refactoring
│   │   ├── game_of_life.py       # Original Game of Life implementation
│   │   ├── game_of_life_refactored.py  # Refactored Game of Life
│   │   └── tests.py              # Unit tests for Game of Life
│   ├── README.md                 # Python practice README file
│   ├── calculator                # Simple calculator implementation
│   │   ├── LICENSE               # License for calculator project
│   │   ├── README.md             # README file for calculator project
│   │   ├── __init__.py           # Init file
│   │   ├── basic.py              # Basic calculator operations
│   │   ├── calculator_class.py   # Calculator class
│   │   ├── engineering.py        # Engineering operations
│   │   ├── test                  # Test scripts
│   │   │   └── test.py           # Unit tests for calculator
│   │   └── utils.py              # Utility functions
│   └── dictionary_reverse.py     # Reverse dictionary implementation
└── README.md                     # Main project README file
```

## Setup Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/AI-Automobility-Class.git
   cd AI-Automobility-Class
   ```

2. Install the necessary dependencies:

   - For the MNIST projects, make sure you have the required libraries such as NumPy and Matplotlib.

3. For the MNIST projects, ensure you have the required dataset files available in the `MNIST` folder.

## Usage

### MNIST Neural Network

To run the MNIST neural network example:

```bash
python MNIST/MNIST_Class.py #OR
python MNIST/MNIST-myown.py
```

### Calculator Project

You can use the calculator scripts in `Python-practice/calculator/` for basic and engineering calculations:

```bash
python Python-practice/calculator/basic.py
python Python-practice/calculator/engineering.py
```

### Code Refactoring (Game of Life)

To run the original or refactored versions of the Game of Life:

```bash
python Python-practice/Code-refactoring/game_of_life.py #OR
python Python-practice/Code-refactoring/game_of_life_refactored.py
```

## License

This repository is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.

---

Feel free to adjust any sections according to your project's specific needs. Let me know if you need further customization!
