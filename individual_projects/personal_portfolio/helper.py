# import needed libraries
import tkinter as tk
from tkinter import ttk
import subprocess
import sys

# setup class startpage, which is the main page of the app
class StartPage(tk.Frame):

    # initialize the start page
    def __init__(self, parent):
        super().__init__(parent)

        # variables to track selected project and running process
        self.selected_project = None
        self.process = None

        # create UI elements
        # title label
        title = ttk.Label(self,
            text="Programming Portfolio",
            font=("Verdana", 30))
        # paragraph with welcome message and instructions
        paragraph = ttk.Label(self,
            text="Welcome! Select a project, then click Run.",
            font=("Verdana", 12),
            wraplength=600)

        # section title for projects
        my_projects = ttk.Label(self,
            text="My Projects",
            font=("Verdana", 20))


        # buttons for each project with lambda functions to select the project and display info
        project_one = ttk.Button(self,
            text="Project 1: Fractal Pattern Generator",
            command=lambda: self.select_project(
                "fractal",
                "Fractal Pattern Generator",
                "Generates fractal patterns using recursion.\n\n• Learned Turtle graphics\n• Learned recursion\n\n• Overcame recursion confusion"))

        # project two button with lambda function to select project and display info
        project_two = ttk.Button(self,
            text="Project 2: Password Generator",
            command=lambda: self.select_project(
                "password",
                "Password Generator",
                "Creates secure random passwords.\n\n• Learned random library\n• Learned string manipulation\n\n• Overcame input validation issues"))

        # project three button with lambda function to select project and display info
        project_three = ttk.Button(self,
            text="Project 3: Morse Code Translator",
            command=lambda: self.select_project(
                "morse",
                "Morse Code Translator",
                "Converts text to Morse code and back.\n\n• Learned dictionaries\n• Learned encoding systems\n\n• Overcame list mapping logic"))

        # project four button with lambda function to select project and display info
        project_four = ttk.Button(self,
            text="Project 4: Financial Calculator",
            command=lambda: self.select_project(
                "word",
                "Financial Calculator",
                "Performs financial calculations.\n\n• Learned functions\n• Learned input validation\n\n• Overcame percentage calculations"))


        # label to display selected project information, initially prompting user to select a project
        self.project_info_paragraph = ttk.Label(self,
            text="Click a project to view details.",
            font=("Verdana", 12),
            wraplength=600)

        # button to run the selected project, which calls the run_project function
        run_button = ttk.Button(self,
            text="Run Selected Project",
            command=self.run_project)

        # button to exit the program, which calls the exit_program function
        exit_button = ttk.Button(self,
            text="Exit",
            command=self.exit_program)


        # pack all the UI elements with appropriate padding and fill options
        title.pack(pady=(40, 20), padx=20)
        paragraph.pack(pady=(10, 20), padx=20)
        my_projects.pack(pady=(40, 20), fill="x", padx=20)

        project_one.pack(pady=10, fill="x", ipady=10, padx=20)
        project_two.pack(pady=10, fill="x", ipady=10, padx=20)
        project_three.pack(pady=10, fill="x", ipady=10, padx=20)
        project_four.pack(pady=10, fill="x", ipady=10, padx=20)

        self.project_info_paragraph.pack(pady=(40, 20), fill="x", padx=20)

        run_button.pack(pady=20, fill="x", ipady=20, padx=20)
        exit_button.pack(pady=(20, 40), padx=20, anchor="sw")
    
    # methods
    # method to select a project, which updates the selected_project variable and displays project information in the project_info_paragraph label
    def select_project(self, project_name, display_name, description):
        self.selected_project = project_name
        self.project_info_paragraph['text'] = (f"Project Name:\n{display_name}\n\nProject Description:\n{description}")

    # method to run the selected project, which checks which project is selected and runs the corresponding main.py file using subprocess.Popen. If a project is already running, it terminates the process before starting a new one. If no project is selected, it prompts the user to select a project first.
    def run_project(self):
        if self.process is not None:
            self.process.terminate()
            self.process = None

        # couldn't figure out another way to import the files
        if self.selected_project == "fractal":
            self.process = subprocess.Popen(["python", "individual_projects/fractal_pattern_generator/main.py"])

        elif self.selected_project == "password":
            self.process = subprocess.Popen(["python", "individual_projects/password_generator.py"])

        elif self.selected_project == "morse":
            self.process = subprocess.Popen(["python", "individual_projects/morse_code_translator.py"])

        elif self.selected_project == "word":
            self.process = subprocess.Popen(["python", "individual_projects/financial_calculator.py"])

        else:
            self.project_info_paragraph['text'] = "Please select a project first!"

    # method to exit the program, which destroys the main window and exits the program using sys.exit()
    def exit_program(self):
        self.winfo_toplevel().destroy()
        sys.exit()