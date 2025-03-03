# Kumir Turtle

Kumir Turtle is a Python-based implementation of the "Кумир" programming environment, designed to help users learn programming concepts using a turtle graphics interface. The program supports Russian commands and provides a user-friendly interface for drawing and learning.

## Features

- **Russian Commands**: Use commands like `вперед(n)`, `вправо(n)`, `влево(n)`, `поднять хвост`, and `опустить хвост` to control the turtle.
- **Algorithm Structure**: Programs must start with `алг` and `нач`, and end with `кон`. Loops (`нц` and `кц`) are also supported.
- **Grid and Coordinates**: The drawing area includes a grid with gray lines and brown X/Y axes for better visualization.
- **Zoom and Pan**: Use the mouse to pan around the canvas and a slider to zoom in and out.
- **Error Handling**: Errors are displayed in red, making it easy to debug your programs.
- **Clipboard Support**: Use `Ctrl+V` to paste text into the command input area.

## How to Use

1. **Write Your Program**: Enter your commands in the left text box. Example:
```
алг
нач
опустить хвост
нц 4 раз
вперед(10)
вправо(90)
кц
кон
```
3. **Run the Program**: Click the "Выполнить" button to execute your commands. The turtle will draw on the right canvas.

4. **Pan and Zoom**:
- **Pan**: Click and drag with the left mouse button to move around the canvas.
- **Zoom**: Use the slider at the bottom to adjust the zoom level (10% to 200%).

4. **Reset**: Each time you click "Выполнить", the turtle resets to the starting position and clears the canvas.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python)
- `turtle` (usually included with Python)

## Installation

1. Clone the repository:
```
git clone https://github.com/TheVolt2/kumir.git
```
2. Navigate to the project directory:
cd kumir
3. Run the program:
python main.py
Example Programs
Square
```
алг
нач
  опустить хвост
  нц 4 раз
    вперед(10)
    вправо(90)
  кц
кон
```
Spiral
```
алг
нач
  опустить хвост
  нц 10 раз
    вперед(50)
    вправо(36)
  кц
кон
```
# Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request
