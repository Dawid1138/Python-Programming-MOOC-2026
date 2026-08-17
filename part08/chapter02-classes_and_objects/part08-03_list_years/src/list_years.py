from datetime import date

def list_years(years):
    year_lst = []
    for date in years:
        year_lst.append(date.year)
    return sorted(year_lst)