import tkinter as tk


def draw_star(star_color, bg_color):
    root = tk.Tk()

    canvas = tk.Canvas(root, width=400, height=420, bg=bg_color)
    canvas.pack()

    points = [200, 20, 80, 396, 380, 156, 20, 156, 320, 396]
    canvas.create_polygon(points, outline=star_color, fill=star_color)

    root.mainloop()


draw_star('#b280ff', 'black')
