import tkinter as tk
import subprocess



def underline_label(parent, text):
    label = tk.Label(parent, text=text, font=("Helvetica", 12, "bold"))
    label.pack(side="left")
    canvas = tk.Canvas(parent, width=label.winfo_reqwidth(), height=2, bg="black", highlightthickness=0)
    canvas.create_line(0, 0, label.winfo_reqwidth(), 0, fill="black", width=2)
    canvas.pack(side="left", padx=(5, 0), pady=(10, 0))

# Function to handle button click event
def camera_details_clicked():
    # Placeholder for the action to be taken when the button is clicked
    print("Camera details button clicked")
    subprocess.Popen(['python', 'C:\\Users\\ADARSH\\Dropbox\\My PC (LAPTOP-PNFRB4FL)\\Desktop\\tk_project1\\camera.py'])
# Function to handle button click event
def draw_edit_zone_clicked():
    # Placeholder for the action to be taken when the button is clicked
    print("Draw edit zone button clicked")
    subprocess.Popen(['python', 'C:\\Users\\ADARSH\\Dropbox\\My PC (LAPTOP-PNFRB4FL)\\Desktop\\tk_project1\\zone.py'])

def save_clicked():
    # Placeholder for the action to be taken when the button is clicked
    print("Save button clicked")

# Function to handle button click event for "Start" button
def start_clicked():
    # Placeholder for the action to be taken when the button is clicked
    print("Start button clicked")

# Create the main window
root = tk.Tk()
root.title("KELTRON: SMART PELTRAC")

# Set the window size to 600x400
root.geometry("600x400")

# Create a frame for the title
title_frame = tk.Frame(root, bg="green")
title_frame.pack(side="top", fill="x")

# Create a label with the title text
title_label = tk.Label(title_frame, text="KELTRON: SMART PELTRAC", bg="green", fg="white", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Create a top frame
top_frame = tk.Frame(root)
top_frame.pack(expand=True, padx=20, pady=20)

# Add the "Camera details" button to the centered frame
camera_details_button = tk.Button(top_frame, text="Camera Details", bg="red",fg="white",command=camera_details_clicked, font=("Helvetica", 12, "bold"))
camera_details_button.pack()

# Create a top frame
top_frame = tk.Frame(root)
top_frame.pack(side="top", fill="x")

# Add the "Draw edit zone" button to the down frame
draw_edit_zone_button = tk.Button(top_frame, text="Draw Edit Zone", bg="red",fg="white", command=draw_edit_zone_clicked, font=("Helvetica", 12, "bold"))
draw_edit_zone_button.pack(pady=10)

# Create a center frame
center_frame = tk.Frame(root)
center_frame.pack(expand=True)

# Add the "Save" button to the center frame
save_button = tk.Button(center_frame, text="Save", command=save_clicked, font=("Helvetica", 12, "bold"))
save_button.pack(side="left", padx=10, pady=10)

# Add the "Start" button to the center frame
start_button = tk.Button(center_frame, text="Restart", command=start_clicked, font=("Helvetica", 12, "bold"))
start_button.pack(side="right", padx=10, pady=10)




# Run the Tkinter event loop
root.mainloop()