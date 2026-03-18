from tkinter import *

class Scoreboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Football Scoreboard")
        
        # Set to fullscreen and black background
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="black")

        self.home_score = 0
        self.away_score = 0

        # UI Layout: Two columns for Home and Away
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Home Side
        self.home_label = Label(root, text="HOME", font=("Helvetica", 60, "bold"), fg="#aaaaaa", bg="black")
        self.home_label.place(relx=0.25, rely=0.2, anchor="center")
        
        self.home_display = Label(root, text=str(self.home_score), font=("Consolas", 400, "bold"), fg="white", bg="black")
        self.home_display.grid(row=0, column=0)

        # Away Side
        self.away_label = Label(root, text="AWAY", font=("Helvetica", 60, "bold"), fg="#aaaaaa", bg="black")
        self.away_label.place(relx=0.75, rely=0.2, anchor="center")

        self.away_display = Label(root, text=str(self.away_score), font=("Consolas", 400, "bold"), fg="white", bg="black")
        self.away_display.grid(row=0, column=1)

        # Instructions Footer
        self.info = Label(root, text="Space: Home +1  |  Enter: Away +1  |  Esc: Quit  |  R: Reset", 
                             font=("Helvetica", 20), fg="#444444", bg="black")
        self.info.place(relx=0.5, rely=0.95, anchor="center")

        # Controls
        self.root.bind("<space>", self.add_home)
        self.root.bind("<Return>", self.add_away)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.bind("r", self.reset_scores)
        self.root.bind("R", self.reset_scores)

    def add_home(self, event):
        self.home_score += 1
        self.home_display.config(text=str(self.home_score))

    def add_away(self, event):
        self.away_score += 1
        self.away_display.config(text=str(self.away_score))
        
    def reset_scores(self, event):
        self.home_score = 0
        self.away_score = 0
        self.home_display.config(text="0")
        self.away_display.config(text="0")

if __name__ == "__main__":
    root = Tk()
    app = Scoreboard(root)
    root.mainloop()