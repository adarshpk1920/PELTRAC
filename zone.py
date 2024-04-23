import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import matplotlib.pyplot as plt
import subprocess
def view_clicked():
    print("View button clicked")
    file_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
    if file_path:
        global cap
        cap = cv2.VideoCapture(file_path)
    

def draw_clicked():
    print("Draw button clicked")
    subprocess.Popen(['python', 'C:\\Users\\ADARSH\\Dropbox\\My PC (LAPTOP-PNFRB4FL)\\Desktop\\tk_project1\\draw.py'])


def back_clicked():
    print("Back button clicked")

# Create the main window
root = tk.Tk()
root.title("Button Placement Example")

# Creating the header label
header_label = tk.Label(root, text="Zone", font=('Helvetica', 18, 'bold'), bg="#f0f0f0")
header_label.pack(pady=40)

# Set the window size to 600x400
root.geometry("600x400")

# Create a center frame
center_frame = tk.Frame(root)
center_frame.pack(expand=True)

# Create buttons with green color
view_button = tk.Button(center_frame, text="View", bg="green", command=view_clicked,fg="white", font=('Helvetica', 12, 'bold'), relief='raised')
view_button.pack(side="top",padx=60)
draw_button = tk.Button(center_frame, text="Draw", bg="green", command=draw_clicked,fg="white", font=('Helvetica', 12, 'bold'), relief='raised')
draw_button.pack(side="top",padx=60)
back_button = tk.Button(root, text="Back", bg="blue", command=back_clicked,fg="white", font=('Helvetica', 12, 'bold'), relief='raised')
back_button.pack(pady=10)

# Place buttons using pack and anchor
view_button.pack(side=tk.LEFT)
draw_button.pack(side=tk.RIGHT)
back_button.pack(side=tk.BOTTOM)

# Set the window size to 600x400
root.geometry("400x200")

root.mainloop()
