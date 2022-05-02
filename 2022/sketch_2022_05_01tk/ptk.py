import tkinter as tk
import __main__

def size(w, h):
    global tk_window, tk_canvas
    __main__.width = w
    __main__.height = h
    tk_window = tk.Tk()
    tk_canvas = tk.Canvas(tk_window, bg="lightgray", height=w, width=h)

def poly(*args, **kwargs):
    """Expects a tuple of coordinate-tuples, plus the usual attribute kwargs"""
    return tk_canvas.create_polygon(*args, **kwargs)

def rect(x, y, w, h, *args, **kwargs):
    return tk_canvas.create_rectangle(x, y, x + w, y + h, *args, **kwargs)
#arc = tk_canvas.create_arc(coord, start=0, extent=150, fill="red")

def line(xa, ya, xb, yb, *args, **kwargs):
    return tk_canvas.create_line(xa, ya, xb, yb, *args, **kwargs)

def background(*args):
    if len(args) == 1:
        args = args * 3
    tk_canvas.config(bg=color(*args))

def color(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def line_grid(ox, oy, w, h, d,  *args, **kwargs):
    lines = []
    for x in range(ox, ox + w + 1, d):
        lines.append(tk_canvas.create_line(x, oy, x, oy + h, *args, **kwargs))
    for y in range(oy, oy + h + 1, d):
        lines.append(tk_canvas.create_line(ox, y, ox + w, y, *args, **kwargs))
    return lines

def ptk_run():
    tk_canvas.pack()
    tk_window.mainloop()
