from tabulate import tabulate

def display_data(cursor,data):
    field_names = [i[0] for i in cursor.description]
    #fancy_grid, textile, 
    print(tabulate(data, headers=field_names,tablefmt='fancy_grid'))
    # for x in data:
    #     print (x)