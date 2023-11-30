import tkinter as tk

class DragonCurveApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Dragon Curve Fractal")
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack()

        self.order = 0
        self.points = [(250, 375), (650, 375)]

        self.canvas.bind("<Button-1>", self.draw_next_iteration)
        self.draw_dragon_curve()

    def draw_dragon_curve(self):
        self.canvas.delete("all")
        self.canvas.create_line(self.points, width=2, tags="dragon_curve")

    def generate_next_iteration(self):
        new_points = [self.points[0]]

        for i in range(len(self.points) - 1):
            if i%2 != 0:
                x1, y1 = self.points[i]
                x2, y2 = self.points[i + 1]
                new_x = (x1 + x2) / 2 - (y2 - y1) / 2
                new_y = (y1 + y2) / 2 + (x2 - x1) / 2
                new_points.append((new_x, new_y))
                new_points.append(self.points[i + 1])
            else:
                x1, y1 = self.points[i]
                x2, y2 = self.points[i + 1]
                new_x = (x1 + x2) / 2 + (y2 - y1) / 2
                new_y = (y1 + y2) / 2 - (x2 - x1) / 2
                new_points.append((new_x, new_y))
                new_points.append(self.points[i + 1])

        self.points = new_points

    def draw_next_iteration(self, event):
        self.generate_next_iteration()
        self.draw_dragon_curve()
        self.order += 1
        self.master.title(f"Dragon Curve Fractal - Order: {self.order}")


def main():
    root = tk.Tk()
    app = DragonCurveApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
