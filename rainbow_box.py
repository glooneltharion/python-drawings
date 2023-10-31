import tkinter as tk


# Define the main window
class RainbowBox:
    def __init__(self, master):
        self.master = master
        self.WIDTH = 315
        self.HEIGHT = 315
        self.canvas = tk.Canvas(self.master, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()
        self.draw_image()

    def draw_image(self):
        # Create a square drawing function that takes 3 parameters (the square size, the fill color and the graphics)
        # and draws a square of that size and color to the center of the canvas. Create a loop that fills the canvas
        # with rainbow colored squares (red, orange, yellow, green, blue, indigo, violet).

        box = 300
        colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (127, 0, 255)]

        for i in range(7):
            new_color = colors[i]
            self.draw_box(box - 50 * i, new_color)

    def draw_box(self, box, color):
        x0 = (self.WIDTH / 2) - (box / 2)
        y0 = (self.HEIGHT / 2) - (box / 2)
        x1 = x0 + box
        y1 = y0 + box
        r, g, b = color
        color_string = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_string)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Drawing")

    app = RainbowBox(root)

    root.mainloop()

    root.mainloop()
