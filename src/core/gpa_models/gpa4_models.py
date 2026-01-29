
# PKU Model
def get_gpa_pku(grade:float):
    if grade < 60:
        return 0.0
    elif grade <= 63:
        return 1.0
    elif grade <= 67:
        return 1.5
    elif grade <= 71:
        return 2.0
    elif grade <= 74:
        return 2.3
    elif grade <= 77:
        return 2.7
    elif grade <= 81:
        return 3.0
    elif grade <= 84:
        return 3.3
    elif grade <= 89:
        return 3.7
    else:
        return 4.0




# WES Model (Non-Official)
def get_gpa_wes(grade:float):
    if grade < 60:
        return 0.0
    elif grade < 75:
        return 2.0
    elif grade < 85:
        return 3.0
    else: 
        return 4.0
    




# Standard 4.0 Model
def get_gpa_standard_4(grade:float):
    if grade < 60:
        return 0.0
    elif grade < 70:
        return 1.0
    elif grade < 80:
        return 2.0
    elif grade < 90:
        return 3.0
    else: 
        return 4.0