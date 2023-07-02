from canvas import Canvas
import shapes

# Ask user for canvas width, height and color
canvas_width = int(input("Please enter a number for canvas width: "))
canvas_height = int(input("Please enter a number for canvas height: "))
canvas_color = input("Please enter a color (black or white): ").lower()

if canvas_color == "black":
    canvas_color = (0, 0, 0)
elif canvas_color == "white":
    canvas_color = (255, 255, 255)

# Create canvas object from the Canvas class
canvas = Canvas(width=canvas_width, height=canvas_height, color=canvas_color)

figure_choice = input("What you want to draw. Choose 'square' or 'rectangle'"
                      "to draw or 'quit' to exit the program: ").lower()

while figure_choice != "quit":
    if figure_choice == "square":
        # Ask user for parameters and create square object in case if statement is True

        square_x = int(input("Please enter x (a number) for square drawing staring point: "))
        square_y = int(input("Please enter y (a number) for square drawing staring point: "))
        square_side = int(input("Please enter side (a number) for square drawing: "))
        square_red = int(input("How much red: "))
        square_green = int(input("How much green: "))
        square_blue = int(input("How much blue: "))

        # Create square object
        square = shapes.Square(x=square_x, y=square_y, side=square_side, color=(square_red, square_green, square_blue))

        # Add new figure to the canvas
        square.draw(canvas)

    elif figure_choice == "rectangle":

        # Ask user for parameters and create square object in case if statement is True
        rectangle_x = int(input("Please enter x (a number) for rectangle drawing staring point: "))
        rectangle_y = int(input("Please enter y (a number) for rectangle drawing staring point: "))
        rectangle_width = int(input("Please enter with (a number) for rectangle drawing: "))
        rectangle_height = int(input("Please enter height (a number) for rectangle drawing: "))
        rectangle_red = int(input("How much red: "))
        rectangle_green = int(input("How much green: "))
        rectangle_blue = int(input("How much blue: "))

        # Create rectangle object
        rectangle = shapes.Rectangle(x=rectangle_x, y=rectangle_y, width=rectangle_width, height=rectangle_height,
                                     color=(rectangle_red, rectangle_green, rectangle_blue))
        # rectangle.draw(canvas)
        rectangle.draw(canvas)

    canvas.make("files/canvas.png")

    figure_choice = input("What you want to draw. Choose 'square' or 'rectangle'"
                          "to draw or 'quit' to exit the program: ").lower()
