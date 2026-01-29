import config

HEADERS = ("Term","Arithmetic Mean","Weighted Average")


# Calculate all the average scores and print them as a table.
def display_avg():
    avg_dic = get_avg_dic()

    print(f"\n{HEADERS[0]:<8} {HEADERS[1]:<18} {HEADERS[2]:<18}")
    for key in avg_dic.keys():
        print(f"{key:<8} {avg_dic[key][0]:<18.2f} {avg_dic[key][1]:<18.2f}") 






# Calculate the average scores by calculation strategy in the configuration.
def get_avg_dic():
    avg_dic = {}

    if config.CALCULATION_STRATEGY == "total":
        arith_avg = get_arithmetic_mean_by_total()
        weighted_avg = get_weighted_average_by_total()
        avg_dic["total"] = (arith_avg, weighted_avg)

    elif config.CALCULATION_STRATEGY == "terms":
        terms_list = get_terms_list()

        for t in terms_list:
            arith_avg = get_arithmetic_mean_by_term(t)
            weighted_avg = get_weighted_average_by_term(t)
            avg_dic[t] = (arith_avg, weighted_avg)
        
        total_arith_avg = get_arithmetic_mean_by_total()
        total_weighted_avg = get_weighted_average_by_total()
        avg_dic["total"] = (total_arith_avg, total_weighted_avg)
        

    return avg_dic



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







# Caculate the total arithmetic mean.
def get_arithmetic_mean_by_total():
    subject_amount = len(config.CURRENT_OBJECT_LIST)

    total_score = sum(r.grade for r in config.CURRENT_OBJECT_LIST)

    result = total_score / subject_amount
    return result



# Calculate the total weighted average score.
def get_weighted_average_by_total():
    weighted_points = sum( (r.credit * r.grade) for r in config.CURRENT_OBJECT_LIST)
    
    total_credits = sum(r.credit for r in config.CURRENT_OBJECT_LIST)
    
    result = weighted_points / total_credits
    return result







# Calculate the specified term's arithmetic mean.
def get_arithmetic_mean_by_term(term:str):
    subject_amount = 0
    total_score = 0

    for r in config.CURRENT_OBJECT_LIST:
        if r.term == term:
            subject_amount += 1
            total_score += r.grade

    result = total_score / subject_amount
    return result




# Calculate the specified term's weighted average score.
def get_weighted_average_by_term(term:str):
    weighted_points = 0
    total_credits = 0

    for r in config.CURRENT_OBJECT_LIST:
        if r.term == term:
            weighted_points += r.credit * r.grade
            total_credits += r.credit
    
    result = weighted_points / total_credits
    return result