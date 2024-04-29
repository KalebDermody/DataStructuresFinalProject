import tkinter as tk
from tkinter import Frame, messagebox, PhotoImage, Label, Button, Toplevel


class RecipeLinkedList:
    def __init__(self):
        self.Recipes = []

    def AddRecipe(self, name, filepath):
        self.Recipes[name] = filepath

    def SearchRecipe(self, name):
        return self.Recipes[name]

    def DeleteRecipe(self, name):
        if name in self.Recipes:
            self.Recipes.remove(name)

    def PeekList(self):
        if len(self.Recipes) == 0:
            messagebox.showinfo("No Recipes", "No Recipes")
        else:
            return sorted(self.Recipes)


class RecipeApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Recipie Book")
        self.master.geometry("620x680")
        self.bg = PhotoImage(file="gusteaus.png")
        # Show image using label
        label1 = Label(master, image=self.bg)
        label1.place(x=0, y=0)
        label2 = Label(master, text="Welcome")
        label2.pack(pady=50)
        # Create Frame
        frame1 = Frame(master)
        frame1.pack(pady=20)
        # Add buttons
        self.AddButton = Button(self.master, text="add recipe", command=self.AddRecipe)
        self.AddButton.pack(pady=20)
        self.SearchButton = Button(self.master, text="Search", command=self.SearchRecipe)
        self.SearchButton.pack(pady=20)
        self.ViewButton = Button(self.master, text="View List", command=self.ViewList)
        self.ViewButton.pack(pady=20)
        self.exit_button = Button(master, text="Exit", command=master.destroy)
        self.exit_button.pack(pady=20)

    def AddRecipe(self):
        addWindow = Toplevel(self.master)
        addWindow.title("Add New Recipe")
        addWindow.geometry("400x300")

    def SearchRecipe(self):
        addWindow = Toplevel(self.master)
        addWindow.title("Search For Recipe")
        addWindow.geometry("400x300")

    def ViewList(self):
        addWindow = Toplevel(self.master)
        addWindow.title("View sorted full list of recipes")
        addWindow.geometry("400x300")


def main():
    root = tk.Tk()
    app = RecipeApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
