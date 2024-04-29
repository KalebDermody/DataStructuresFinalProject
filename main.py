import tkinter as tk
from tkinter import filedialog, messagebox


def button_click():
    print("Button Clicked!")


class RecipeApplication():
    def __init__(self, master):
        self.master = master
        self.master.title("Recipie Book")
        self.master.geometry("720x300")
        self.recipes = {}
        self.gui()

    def gui(self):
        self.addButton = tk.Button(self.master, text="add recipe", command=self.add_recipe)
        self.addButton.pack()

        self.SearchButton = tk.Button(self.master, text="add recipe", command=self.add_recipe)
        self.SearchButton.pack()

        self.ViewButton = tk.Button(self.master, text="add recipe", command=self.add_recipe)
        self.ViewButton.pack()

    def add_recipe(self):
        addWindow = tk.Toplevel(self.master)
        addWindow.title("Add New Recipe")
        addWindow.geometry("400x300")




def main():
    root = tk.Tk()
    app = RecipeApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
