from tkinter import Label, Tk
import time


class DigitalClock:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title('Clock')   # Set the window title
        self.root.geometry('640x400')  # Set the window size

        # Define font, background color, and border width for the clock label
        self.text_font = ('Arial', 70, 'bold')
        self.background = '#fb7e14'
        self.border_width = 145

        # Create a label widget to display the time
        self.label = Label(self.root, font=self.text_font, bg=self.background, bd=self.border_width)
        self.label.grid(row=0, column=1)  # Place the label on the grid layout

        # Start updating the clock
        self.update_clock()

    def update_clock(self):
        # Get the current time in HH:MM:SS format
        time_live = time.strftime('%H:%M:%S')

        # Update the label with the current time
        self.label.config(text=time_live)

        # Schedule the update_clock function to be called every 100 milliseconds
        self.label.after(100, self.update_clock)


# Only run the application if the script is executed directly
if __name__ == '__main__':
    root = Tk()   # Create the main application window
    clock = DigitalClock(root)   # Instantiate the DigitalClock class
    root.mainloop()  # Start the Tkinter event loop
