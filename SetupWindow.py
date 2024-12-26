from tkinter import *

class SetupWindow:
    def __init__(self):
        self.active = True
        root = self.root = Tk()
        root.geometry("400x300")
        root.title("Multiplayer setup")
        root.resizable(False, False)

        # Static text
        Label(root, text="Host/Server port:", font=("Arial", 14)).place(y=30, x=200, anchor=CENTER)

        # Single-line text field to enter server's port
        portField = self.portField = Entry(root, font=("Arial", 12), justify=CENTER)
        portField.place(x=200, y=60, anchor=CENTER)
        portField.insert(END, "13579 - Auto")
        portField.config(state=DISABLED)

        # Static text
        Label(root, text="Displayed name:", font=("Arial", 14)).place(y=110, x=200, anchor=CENTER)

        # Single-line text field to enter player's preferred name
        nameField = self.nameField = Entry(root, font=("Arial", 12), justify=CENTER)
        nameField.place(x=200, y=140, anchor=CENTER)


        # Static text
        Label(root, text="This name will be visible to your opponent\n and will be recorded to match history",
              font=("Arial", 10)).place(y=175, x=200, anchor=CENTER)

        # A button to submit data
        submitButton = self.submitButton = (Button(root, text="Play online", font=("Arial", 14), command=lambda: self.Submit()))
        submitButton.place(x=200, y=240, anchor=CENTER)

    def Submit(self):
        self.root.quit()