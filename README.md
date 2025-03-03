# Turtle Artist

Turtle Artist is a simple Python program that allows you to control a turtle using commands in Russian. It is inspired by the "Кумир" programming environment and is designed to help users learn basic programming concepts in a fun and interactive way.

## Features

- **Russian Commands**: Use commands like `вперед(n)`, `вправо(n)`, `влево(n)`, `поднять хвост`, and `опустить хвост` to control the turtle.
- **Algorithm Structure**: Programs must start with `алг` and `нач`, and end with `кон`. Loops (`нц` and `кц`) are also supported.
- **Grid and Coordinates**: The drawing area includes a grid with gray lines and brown X/Y axes for better visualization.
- **Zoom and Pan**: Use the mouse to pan around the canvas and a slider to zoom in and out.
- **Error Handling**: Errors are displayed in red, making it easy to debug your programs.

## How to Use

1. **Write Your Program**: Enter your commands in the left text box. Example:
алг
нач
опустить хвост
нц 4 раз
вперед(10)
вправо(90)
кц
кон

Copy

2. **Run the Program**: Click the "Выполнить" button to execute your commands. The turtle will draw on the right canvas.

3. **Pan and Zoom**:
- **Pan**: Click and drag with the left mouse button to move around the canvas.
- **Zoom**: Use the slider at the bottom to adjust the zoom level (10% to 200%).

4. **Reset**: Each time you click "Выполнить", the turtle resets to the starting position and clears the canvas.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python)
- `turtle` (usually included with Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/turtle-artist.git
Navigate to the project directory:

bash
Copy
cd turtle-artist
Run the program:

bash
Copy
python main.py
Example Programs
Square
Copy
алг
нач
  опустить хвост
  нц 4 раз
    вперед(10)
    вправо(90)
  кц
кон
Spiral
Copy
алг
нач
  опустить хвост
  нц 10 раз
    вперед(50)
    вправо(36)
  кц
кон
Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
