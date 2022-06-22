from turtle import Screen, Turtle

TILE_SIZE = 32
CURSOR_SIZE = 20

BLANK = 0
START = 1
END = 2
POL_POINT = 3
WALL = 4
IN_POL = 5
EXP_NODE = 6


class PenSquare(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(TILE_SIZE / CURSOR_SIZE)
        self.pencolor('black')
        self.penup()
        self.speed('fastest')


class PenClassic(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5 * TILE_SIZE / CURSOR_SIZE)
        self.pencolor('black')
        self.penup()
        self.hideturtle()
        self.speed('fastest')


def setup_maze(level, pen):
    ''' Conversion from the list to the map in turtle. '''

    maze_height, maze_width = len(level), len(level[0])

    for x in range(maze_height):
        for y in range(maze_width):
            # get the character at each x,y coordinate
            character = level[x][y]

            # check if it is a wall or a path
            if character == BLANK:
                pen.fillcolor('white')
            elif character == START:
                pen.fillcolor('green')
            elif character == END:
                pen.fillcolor('red')
            elif character == POL_POINT:
                pen.fillcolor('blue')
            elif character == WALL:
                pen.fillcolor('gray')
            elif character == IN_POL:
                pen.fillcolor('white')
            elif character == EXP_NODE:
                pen.fillcolor('cyan')

            # calculate the screen x, y coordinates
            screen_x = (y - maze_width) * TILE_SIZE + 300
            screen_y = (maze_height - x) * TILE_SIZE - 300

            pen.goto(screen_x, screen_y)
            pen.stamp()


def setup_path(level, paths, pen):
    maze_height, maze_width = len(level), len(level[0])

    for path in paths:
        x, y = path
        screen_x = (y - maze_width) * TILE_SIZE + 300
        screen_y = (maze_height - x) * TILE_SIZE - 300
        pen.goto(screen_x, screen_y)
        pen.stamp()
        
    pass


def draw(maze, paths, title):
    screen = Screen()
    screen.setup(1000, 1000)
    screen.title(title)

    pen_square = PenSquare()
    pen_classic = PenClassic()

    setup_maze(maze, pen_square)
    setup_path(maze, paths, pen_classic)

    screen.mainloop()

if __name__ == '__main__':
    maze = []
    paths = [(7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1)]

    with open("map.txt") as file:
        for line in file:
            maze.append(line.strip())
    
    draw(maze, paths)