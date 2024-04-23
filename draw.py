import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import cv2


def draw_square():
    # Draw a square on the Matplotlib plot
    ax.plot([100, 200, 200, 100, 100], [100, 100, 200, 200, 100], 'r-')
    canvas.draw()

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        photo = plt.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        video_label.config(image=photo)
        video_label.image = photo
        root.after(30, update_frame)

root = tk.Tk()
root.title("Video with Matplotlib Overlay")

# Create a label to display the video
video_label = tk.Label(root)
video_label.pack()

# Open the video capture
cap = cv2.VideoCapture('your_video_file.mp4')

# Create a Matplotlib figure and plot
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Call the update_frame function to start displaying the video
update_frame()

# Draw a square on the Matplotlib plot
draw_square()

root.mainloop()

# Release the video capture
cap.release()
