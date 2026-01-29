import config
from core.gpa_models import gpa4_models
from core.gpa_models import gpa5_models



# Calculate the gpa in calculation strategy in the configuration.
def get_gpa_dic(model:str, system:int):
    gpa_dic = {}

    if config.CALCULATION_STRATEGY == "total":
        total_gpa = get_total_gpa_by_total(model, system)
        gpa_dic["total"] = total_gpa

    elif config.CALCULATION_STRATEGY == "terms":
        terms_list = get_terms_list()

        for t in terms_list:
            term_gpa = get_total_gpa_by_term(t, model, system)
            gpa_dic[t] = term_gpa
        
        total_gpa = get_total_gpa_by_total(model, system)
        gpa_dic["total"] = total_gpa
        
    return gpa_dic




# Get the sorted terms list.
def get_terms_list():
    terms_list = []
    for r in config.CURRENT_OBJECT_LIST:
        if r.term in terms_list:
            continue
        else:
            terms_list.append(r.term)
   
    terms_list.sort()
    return terms_list




# Get all the record objects in a term.
def get_term_object_list(term:str):
    term_object_list = []
    for obj in config.CURRENT_OBJECT_LIST:
        if obj.term == term:
            term_object_list.append(obj)
    return term_object_list





# Use the specified model and objects list to calculate the total gpa(4).
def get_total_gpa_by_total(model:str, system:int):
    gpa_list = get_gpa_list(config.CURRENT_OBJECT_LIST, model, system)

    total_grade_points = 0
    for i in range(0, len(config.CURRENT_OBJECT_LIST)):
        total_grade_points += config.CURRENT_OBJECT_LIST[i].credit * gpa_list[i]
    
    total_credits = sum(r.credit for r in config.CURRENT_OBJECT_LIST)
    
    result = total_grade_points / total_credits
    return result





# Get the GPA list by specified model.
def get_gpa_list(object_list:list, model:str, system:int):
    gpa_list = []

    if system == 4:
        if model == "PKU Model":
            for r in object_list:
                subject_gpa = gpa4_models.get_gpa_pku(r.grade)
                gpa_list.append(subject_gpa)
        
        elif model == "WES Model (None_Official)":
            for r in object_list:
                subject_gpa = gpa4_models.get_gpa_wes(r.grade)
                gpa_list.append(subject_gpa)

        elif model == "Standard 4.0":
            for r in object_list:    
                subject_gpa = gpa4_models.get_gpa_standard_4(r.grade)
                gpa_list.append(subject_gpa)
            
    
    elif system == 5:
        if model == "Standard Linear Model":
            for r in object_list:
                subject_gpa = gpa5_models.get_gpa_linear(r.grade)
                gpa_list.append(subject_gpa)

        if model == "Step Mapping Model":
            for r in object_list:
                subject_gpa = gpa5_models.get_gpa_mapping(r.grade)
                gpa_list.append(subject_gpa)

    return gpa_list  






# Get the total gpa this term.
def get_total_gpa_by_term(term:str, model:str, system:int):
    term_object_list = get_term_object_list(term)

    gpa_list = get_gpa_list(term_object_list, model, system)

    total_grade_points = 0
    for i in range(0, len(term_object_list)):
        total_grade_points += term_object_list[i].credit * gpa_list[i]
    
    total_credits = sum(r.credit for r in term_object_list)

    result = total_grade_points / total_credits
    return result


