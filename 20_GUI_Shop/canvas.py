from tkinter import Tk, Canvas


def create_root():
    root = Tk()

    root.title("GUI Shop")
    root.geometry("800x700")
    root.resizable(False, False)

    return root


def create_frame():
    frame = Canvas(root, width=800, height=700)
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()