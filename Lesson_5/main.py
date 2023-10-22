import numpy as np
import pandas as pd


if __name__ == "__main__":

    data = pd.read_csv("titanic_with_labels.csv", sep=' ')

    pd.options.mode.chained_assignment = None
    # pd.options.display.max_rows = None

    data_sp1 = data[(data['sex'] != 'Не указан') & (data['sex'] != '-')]

    data_sp1['sex'] = data_sp1['sex'].map(lambda x:1 if (x == 'Ж' or x == 'ж') else 0)

    max_val_row = data['row_number'].max()
    data_sp1['row_number'] = data_sp1['row_number'].fillna(max_val_row)

    mean_data = data_sp1['liters_drunk'].map(lambda x:0 if (x >= 10 or x < 0) else x).mean()
    data_sp1['liters_drunk'] = data_sp1['liters_drunk'].map(lambda x:mean_data if (x >= 10 or x < 0) else x)

    data_sp1.insert(loc= 5 , column='age_child', value=0) 
    data_sp1.insert(loc= 5 , column='age_adult', value=0) 
    data_sp1.insert(loc= 5 , column='age_old', value=0) 

    data_sp1['age_child'] = data_sp1['age'].map(lambda x:x if (x<18) else 'none')
    data_sp1['age_adult'] = data_sp1['age'].map(lambda x:x if (x>=18 and x<=50) else 'none')
    data_sp1['age_old'] = data_sp1['age'].map(lambda x:x if (x>50) else 'none')

    data_sp1 = data_sp1.drop(columns='age', axis=1)

    data_sp1['drink'] = data_sp1['drink'].map(lambda x:'0' if (str(x).find('beer') == (-1)) else '1')


    print(data_sp1)
    # print(max_val_row)