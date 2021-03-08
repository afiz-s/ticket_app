month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']


def from_list_to_year_month_dict(data):
    year_month = {}
    for sale in data:
        month = month_list[sale[1]-1]
        if sale[0] in year_month.keys():
            year_month[sale[0]][month] = sale[2]
        else:
            year_month[sale[0]] = {}
            year_month[sale[0]][month] = sale[2]
    return year_month