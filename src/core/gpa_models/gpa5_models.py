
# Standard Linear Model
def get_gpa_linear(grade:float):
    raw_gpa = (grade - 50) / 10
    gpa = max(0, raw_gpa)
    return gpa




# Table Mapping Model
def get_gpa_mapping(grade:float):
    if grade < 60:
        return 0.0
    elif grade < 70:
        return 2.0
    elif grade < 80:
        return 3.0
    elif grade < 90:
        return 4.0
    else: 
        return 5.0