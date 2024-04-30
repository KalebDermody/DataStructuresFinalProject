import tkinter as tk
from tkinter import Frame, messagebox, PhotoImage, Label, Button, Toplevel, Entry, Listbox, filedialog


# Linked List Data structure class
class RecipeLinkedList:
    def __init__(self):
        self.Recipes = {}

    # Add Recipe Method
    def AddRecipe(self, name, filepath):
        self.Recipes[name] = filepath

    # Search Recipe Method
    def SearchRecipe(self, name):
        return self.Recipes.get(name)

    # Delete recipe method
    def DeleteRecipe(self, name):
        if name in self.Recipes:
            del self.Recipes[name]

    # Peek List Method
    def PeekList(self):
        if len(self.Recipes) == 0:
            messagebox.showinfo("No Recipes", "No Recipes")
        else:
            # Sorts The List Before Displaying
            return sorted(self.Recipes.keys())


# Gui Application
class RecipeApplication:

    # Build Main GUI Window
    def __init__(self, master):
        self.master = master
        self.master.title("Recipe Book")
        self.master.geometry("620x680")
        self.bg = PhotoImage(file="gusteaus.png")
        # Show image using label
        label1 = Label(master, image=self.bg)
        label1.place(x=0, y=0)
        label2 = Label(master, text="Kaleb's Recipes")
        label2.pack(pady=50)
        # Create Frame
        frame1 = Frame(master)
        frame1.pack(pady=20)
        # Add buttons
        self.AddButton = Button(self.master, text="Add Recipe", command=self.AddRecipe)
        self.AddButton.pack(pady=20)
        self.SearchButton = Button(self.master, text="Search", command=self.SearchRecipe)
        self.SearchButton.pack(pady=20)
        self.ViewButton = Button(self.master, text="View List", command=self.ViewList)
        self.ViewButton.pack(pady=20)
        self.exit_button = Button(master, text="Exit", command=master.destroy)
        self.exit_button.pack(pady=20)
        self.RecipeList = RecipeLinkedList()

    # Add Recipe Window
    def AddRecipe(self):
        AddWindow = Toplevel(self.master)
        AddWindow.title("Add New Recipe")
        AddWindow.geometry("400x300")

        AddText = Label(AddWindow, text="Enter Recipe Name")
        AddText.pack()
        addEntry = Entry(AddWindow)
        addEntry.pack()

        # Open And Read File Provided By User
        def openFileDialog():
            filepath = filedialog.askopenfilename()
            if filepath:
                with open(filepath, "r") as f:
                    recipe = f.read()
                    self.RecipeList.AddRecipe(addEntry.get(), recipe)
                    print("Recipe Added")
                    messagebox.showinfo("Success", "Recipe Added")
                    AddWindow.destroy()
            else:
                messagebox.showerror("Error", "No File Selected")

        button = Button(AddWindow, text="Select File", command=openFileDialog)
        button.pack()

    # Search Recipe Window
    def SearchRecipe(self):
        SearchWindow = Toplevel(self.master)
        SearchWindow.title("Search For Recipe")
        SearchWindow.geometry("400x300")
        SearchText = Label(SearchWindow, text="Enter Recipe's Name")
        SearchText.pack()
        SearchEntry = Entry(SearchWindow)
        SearchEntry.pack()

        # Search Button Method
        def SearchButton():
            recipeName = self.RecipeList.SearchRecipe(SearchEntry.get())
            if recipeName:
                messagebox.showinfo("Recipe Found", recipeName)
            else:
                messagebox.showinfo("ERROR", "Recipe Not Found")

        SearchButton = Button(SearchWindow, text="Search Recipe", command=SearchButton)
        SearchButton.pack()

    # View List Window
    def ViewList(self):
        ViewWindow = Toplevel(self.master)
        ViewWindow.title("View sorted full list of recipes")
        ViewWindow.geometry("400x300")
        RecipeList = self.RecipeList.PeekList()

        # Delete Button Method That Utilizes The Delete Method In The Linked List
        def DeleteButton():
            SelectedRecipe = listbox.curselection()
            if SelectedRecipe:
                SelectedItem = RecipeList[SelectedRecipe[0]]
                self.RecipeList.DeleteRecipe(SelectedItem)
                listbox.delete(*SelectedRecipe)
            else:
                messagebox.showinfo("ERROR", "No Recipe Selected")
        if RecipeList:
            listbox = Listbox(ViewWindow)
            listbox.pack(fill=tk.BOTH, expand=True)
            for recipe in RecipeList:
                listbox.insert(tk.END, recipe)
            DeleteButton = Button(ViewWindow, text="Delete", command=DeleteButton)
            DeleteButton.pack()
        else:
            label = Label(ViewWindow, text="No Recipes")
            label.pack()


# Main Method To Run The GUI
def main():
    root = tk.Tk()
    app = RecipeApplication(root)
    root.mainloop()


# Driver Method
if __name__ == "__main__":
    main()
