import tkinter as tk
from tkinter import filedialog, messagebox


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
        self.master.geometry("720x300")
        self.gui()

    def gui(self):
        self.AddButton = tk.Button(self.master, text="add recipe", command=self.AddRecipe)
        self.AddButton.pack()

        self.SearchButton = tk.Button(self.master, text="Search", command=self.SearchRecipe)
        self.SearchButton.pack()

        self.ViewButton = tk.Button(self.master, text="View List", command=self.ViewList)
        self.ViewButton.pack()

    def AddRecipe(self):
        addWindow = tk.Toplevel(self.master)
        addWindow.title("Add New Recipe")
        addWindow.geometry("400x300")

    def SearchRecipe(self):
        addWindow = tk.Toplevel(self.master)
        addWindow.title("Search For Recipe")
        addWindow.geometry("400x300")

    def ViewList(self):
        addWindow = tk.Toplevel(self.master)
        addWindow.title("View sorted full list of recipes")
        addWindow.geometry("400x300")


def main():
    root = tk.Tk()
    app = RecipeApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
