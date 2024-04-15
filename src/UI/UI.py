import tkinter as tk
from Agents import *
import yaml
from os import environ
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
class UI:
    """
    parent class for all UI classes
    """
    def __init__(self, root: tk.Tk):
        self.root = root

    def run(self):
        self.root.mainloop()

class MenuUI(UI):
    """
    class for the main menu
    """
    def __init__(self, root: tk.Tk):
        super().__init__(root)
        root.title("Main Menu")

        if not root:
            raise Exception("No root provided")
        
        with open("src/UI/UIConfigs.yaml") as UI_CONFIGS:
            self.configs = yaml.load(UI_CONFIGS, Loader=yaml.FullLoader)["MENU_WINDOW_CONFIGS"]

        print(self.configs)

        root.geometry(self.configs["GEOMETRY"])
        root.resizable(self.configs["RESIZABLE"], self.configs["RESIZABLE"])

        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_buttons()

    def create_labels(self):
        pass

    def create_buttons(self):
        tk.Button(self.root, text="Chat", command=self.chat).pack()

    def chat(self):
        print(environ.get("GPT_API_KEY"))
        agent = SQLmanager.SQLmanager(llm = "GPT", APIKEY = environ.get("GPT_API_KEY"), mode = "SQL")
        text = tk.Text(self.root)
        message = agent.getResponse("Hello")
        text.pack()
        text.insert(self.root.END, message)



class ChatUI(UI):
    """
    class for the chat UI
    """
    def __init__(self, root: tk.Tk):
        super().__init__(root)

    def create_widgets(self):
        self.create_labels()
        self.create_textboxes()
        self.create_entries()

    def create_labels(self):
        pass

    def create_textboxes(self):
        pass

    def create_entries(self):
        pass

class ConfigsUI(UI):
    """
    class for the configuration UI
    """
    def __init__(self, root: tk.Tk):
        super().__init__(root)

    def create_widgets(self):
        self.create_labels()
        self.create_entries()
        self.create_buttons()

    def create_labels(self):
        pass

    def create_entries(self):
        pass

    def create_buttons(self):
        pass