from core import gpa_calculation
import config


GPA4_MODELS = '''1. PKU Model
2. WES Model (Non-Official)
3. Standard 4.0'''

def gpa_4_menu():
    config.CURRENT_STATUS = "[GPA 4]"
    print(f"{config.CURRENT_STATUS} Select a calculation model:")
    print(GPA4_MODELS)
    
    user_input = input(f"{config.CURRENT_STATUS} command: ")
    if user_input == "1":
        display_gpa("PKU Model", 4)
    elif user_input == "2":
        display_gpa("WES Model (None_Official)", 4)
    elif user_input == "3":
        display_gpa("Standard 4.0", 4)
    else:
        print("[Error] Invalid command!")
    
    config.CURRENT_STATUS = "[Calculation]"



GPA5_MODELS = '''1. Standard Linear Model
2. Step Mapping Model'''

def gpa_5_menu():
    config.CURRENT_STATUS = "[GPA 5]"
    print(f"{config.CURRENT_STATUS} Select a calculation model:")
    print(GPA5_MODELS)
    
    user_input = input(f"{config.CURRENT_STATUS} command: ")
    if user_input == "1":
        display_gpa("Standard Linear Model", 5)
    elif user_input == "2":
        display_gpa("Step Mapping Model", 5)    
    else:
        print("[Error] Invalid command!")
    
    config.CURRENT_STATUS = "[Calculation]"  





# Calculate all the gpa data and print them as a table.
def display_gpa(model:str, system:int):
    headers = ["Term", f"GPA({system}) [{model}]"]
    gpa_dic = gpa_calculation.get_gpa_dic(model, system)

    print(f"\n{headers[0]:<8} {headers[1]:<16}")
    for key in gpa_dic.keys():
        print(f"{key:<8} {gpa_dic[key]:<16.2f}") 






