def is_date_format_correct(date:str)->bool:
    """
    This function takes in a date in string format
    and returns true if the date matches the format
    YYYY-MM-DD and false if it doesn't
    """
    #your code here#

    if date[4] and date[7] == "-":
        return True
    else:
        return False

print(is_date_format_correct("20221129"))