import pandas as pd

raw_data = pd.read_excel('.../raw_data.xlsx')

user_class = list(raw_data['购买课程'])
str_class = []
for i in user_class:
    a = i.strip().split(';')
    a = list(set(a))
    str_class.append(a)
    
df_class = pd.DataFrame(str_class)
df_class.to_excel('.../df_class.xlsx')
