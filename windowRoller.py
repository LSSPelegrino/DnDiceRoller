import random
import tkinter as tk


def d20roll():
	rollLog.config(state=tk.NORMAL)
	roll = random.randint(1, 20)
	rollLog.insert(tk.INSERT, "You've rolled a {}\n".format(roll))
	if roll == 20:
		rollLog.insert(tk.INSERT, "NATURAL TWENTY!\n")
	elif roll == 1:
		rollLog.insert(tk.INSERT, "Oof! Critical failure!\n")
	rollLog.insert(tk.INSERT, "_" * 20 + "\n")
	rollLog.config(state=tk.DISABLED)
	rollLog.yview_scroll(1, tk.PAGES)


root = tk.Tk()
root.title("Dice Roller")

# Create roll log window
rollLog = tk.Text(
	root,
	state=tk.DISABLED,
	relief=tk.GROOVE,
	font="Helvetica"
)
rollLog.grid(
	padx=1,
	pady=1,
	row=0,
	column=0,
	sticky=tk.NW
)

# Create roll button
rollButton = tk.Button(
	root,
	text="Roll a d20",
	relief=tk.GROOVE,
	command=d20roll
)
rollButton.grid(
	padx=1,
	pady=1,
	row=1,
	column=0,
	sticky=tk.SW
)

root.mainloop()
