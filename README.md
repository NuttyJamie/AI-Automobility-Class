# Python Practice Projects

This repository is a work in progress. It contains various Python practice projects to help sharpen your coding skills. Below is a brief overview of the projects included.

## Environment 
- Slaceware 15.0 linux
- Python 3.9.10

## Tree

'''bash
75 ~/Projects/Python-practice $ tree
.
├── Code-refactoring
│   ├── game_of_life.py
│   ├── game_of_life_refactored.py
│   └── tests.py
├── LICENSE
├── README.md
├── calculator
│   ├── LICENSE
│   ├── README.md
│   ├── __init__.py
│   ├── basic.py
│   ├── calculator_class.py
│   ├── engineering.py
│   ├── tags
│   ├── test
│   │   └── test.py
│   └── utils.py
└── dictionary_reverse.py
'''
---

## 1. Calculator

A simple Python calculator that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division and engnieering operations such as trigonometric functions.

[View the code here](link-to-your-calculator-code)-->

---

## 2. Game of Life

### About the Game of Life

The **Game of Life** is a cellular automaton devised by the mathematician John Conway. It simulates how cells live, die, or multiply based on simple rules:

- A live cell with fewer than two live neighbors dies (underpopulation).
- A live cell with two or three live neighbors lives on to the next generation (survival).
- A live cell with more than three live neighbors dies (overpopulation).
- A dead cell with exactly three live neighbors becomes a live cell (reproduction).

### My Python Implementation

This project is my Python implementation of Conway's Game of Life. It randomly initializes a board and follows the rules to simulate cellular evolution.

[View the code here](./Code-refactoring/game_of_life_refactored.py)

---

## How to Run the Projects

1. Clone this repository:
    ```bash
    git clone https://github.com/NuttyJamie/Python-practice.git
    ```
2. Navigate to the project folder:
    ```bash
    cd Python-practice
    ```
3. Run the Python scripts for each project:
    ```bash
    python Code-refactoring/game_of_life.py
    python Code-refactoring/game_of_life_refactored.py
    ```
    ```bash
	python calculator/basic.py
	python calculator/engnieering.py
    ```

Feel free to explore, contribute, or suggest improvements to these projects!

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
