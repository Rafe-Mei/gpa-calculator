import config


CALCULATION_STRATEGY_OPTIONS = '''1. Total: Calculate all terms data into one row.
2. Terms: Calculate each term's and the total data into different rows.'''



# Set calculation strategy in the configuration.
def set_calculation_strategy():
    config.CURRENT_STATUS = "[Strategy]"

    print(f"{config.CURRENT_STATUS} Calculation Strategy:")
    print(CALCULATION_STRATEGY_OPTIONS)

    user_input = input(f"{config.CURRENT_STATUS} conmmand: ")
    if user_input == "1":
        config.CALCULATION_STRATEGY = "total"
        print(f"{config.CURRENT_STATUS} Calculation strategy changed successfully! Startegy: [{config.CALCULATION_STRATEGY}]")

    elif user_input == "2":
        config.CALCULATION_STRATEGY = "terms"
        print(f"{config.CURRENT_STATUS} Calculation strategy changed successfully! Startegy: [{config.CALCULATION_STRATEGY}]")

    else:
        print("[Error] Invalid calculation strategy command!")

    config.CURRENT_STATUS = "[Calculation]"