import tkinter as tk
from tkinter import Frame, messagebox, PhotoImage, Label, Button, Toplevel, Entry, Listbox, filedialog
import pickle
from pickle import *


class RecipeLinkedList:
    def __init__(self):
        self.Recipes = {}

    def AddRecipe(self, name, filepath):
        self.Recipes[name] = filepath

    def SearchRecipe(self, name):
        return self.Recipes.get(name)

    def DeleteRecipe(self, name):
        if name in self.Recipes:
            del self.Recipes[name]

    def PeekList(self):
        if len(self.Recipes) == 0:
            messagebox.showinfo("No Recipes", "No Recipes")
        else:
            return sorted(self.Recipes.keys())


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
        self.RecipeList = RecipeLinkedList()

    def AddRecipe(self):
        addWindow = Toplevel(self.master)
        addWindow.title("Add New Recipe")
        addWindow.geometry("400x300")

        addLabel = Label(addWindow, text="Enter Recipe Name")
        addLabel.pack()
        addEntry = Entry(addWindow)
        addEntry.pack()

        def openFileDialog():
            filepath = filedialog.askopenfilename()
            if self.RecipeList.AddRecipe(addEntry.get(), filepath):
                print("Recipe Added")
                messagebox.showinfo("success", "Recipe Added")
                addWindow.destroy()
            else:
                messagebox.showerror("Error", "No File Selected")

        button = Button(addWindow, text="select file", command=openFileDialog)
        button.pack()

    def SearchRecipe(self):
        addWindow = Toplevel(self.master)
        addWindow.title("Search For Recipe")
        addWindow.geometry("400x300")
        addLabel = Label(addWindow, text="Enter Recipe's Name")
        addLabel.pack()
        addEntry = Entry(addWindow)
        addEntry.pack()

    def ViewList(self):
        addWindow = Toplevel(self.master)
        addWindow.title("View sorted full list of recipes")
        addWindow.geometry("400x300")
        RecipeList = self.RecipeList.PeekList()

        if RecipeList:
            listbox = Listbox(addWindow)
            listbox.pack()
            for recipe in RecipeList:
                listbox.insert(recipe)
        else:
            label = Label(addWindow, text="No Recipes")


def main():
    root = tk.Tk()
    app = RecipeApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
