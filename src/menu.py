import config

from utils import csv_handler
from utils import printer

from core import strategy
from core import avg_calculation
from core import gpa



HELP = '''\\q   Quit the program.
\\l   Load specified csv file in the data folder.
\\c   Enter the calculate mode.'''


def main_menu():
  
    while True:
        if config.CURRENT_STATUS is None:
            config.CURRENT_STATUS = "[Main Menu]"

        printer.print_divider()
        user_input = input(f"{config.CURRENT_STATUS} command: ")

        if user_input == "\\q":
            break

        elif user_input == "\\help":
            print(HELP)

        elif user_input == "\\l":
            csv_handler.load_csv()

        elif user_input == "\\c":
            try:
                csv_handler.csv_load_checker()
            except RuntimeError as e:
                print("[Error]", e)
                continue
            calculate_menu()

        else:
            print("[Error] Invalid command! You can input \\help to get help.")





CAL_MODE_OPTIONS = '''\\q   Quit calculate mode.
\\s   Select the calculate method (by terms/total).
1. Average score (arithmetic & weighted)
2. GPA (4)
3. GPA (5)'''



def calculate_menu():
    printer.print_divider()
    config.CURRENT_STATUS = "[Calculation]"
    print(f"{config.CURRENT_STATUS} Command List:")
    print(CAL_MODE_OPTIONS)

    while True:
        printer.print_divider()
        user_input = input(f"{config.CURRENT_STATUS} command: ")

        if user_input == "\\q":
            config.CURRENT_STATUS = f"[{config.CURRENT_CSV_FILE_NAME}]"
            break

        elif user_input == "\\help":
            print(f"{config.CURRENT_STATUS} Command List:")
            print(CAL_MODE_OPTIONS)
        
        elif user_input == "\\s":
            strategy.set_calculation_strategy()

        # Calculate the weighted and arithmetic average scores.
        elif user_input == "1":
            avg_calculation.display_avg()

        elif user_input == "2":
            gpa.gpa_4_menu()

        elif user_input == "3":
            gpa.gpa_5_menu()

        else:
            print("[Error] Invalid command! You can input \\help to get help.")



