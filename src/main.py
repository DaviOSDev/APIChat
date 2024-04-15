import os
from dotenv import find_dotenv
import tkinter as tk
from UI.UI import MenuUI

def checkRequirements():
    """
    install the requirements from the requirements.txt file
    """
    os.system("pip install -r configs/requirements.txt")

def createDotenv() -> bool:
    """
    check if the .env file exists, if not create one
    return True if the file exists, False if it was created
    """
    if not find_dotenv():
        os.system("type nul > .env")
        return False
    
    return True

if __name__ == '__main__':
    checkRequirements()
    createDotenv()
    root = tk.Tk()
    MenuUI(root).run()
