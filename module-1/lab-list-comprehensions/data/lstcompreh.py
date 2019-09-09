# import os
# import pandas as pd

# file_list = [f for f in os.listdir('/Users/anielkaaslan/Documents/data-labs/module-1/lab-list-comprehensions/data') if f.endswith('.csv')]
# data_sets = [pd.read_csv(os.path.join('/Users/anielkaaslan/Documents/data-labs/module-1/lab-list-comprehensions/data', f)) for f in file_list]
# data = pd.concat(data_sets, axis=0)


# data = pd.read_csv('vehicles.csv')

# selected_columns = [col for col in data._get_numeric_data() if data[col].mean() > 15]
# print(selected_columns)
import math
def area_of_circle(r):
    """Function that defines an area of a circle"""
    a = r**2 * math.pi
    return a

print area_of_circle(4.5)



