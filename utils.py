# Print missing and unique values in tabular format
from tabulate import tabulate
def tab_data(df):
    headers = ['Column', 'Null Count', 'Unique Count']
    meta_list = []
    cols = [i for i in df.columns]
    for col in cols:
        temp = []
        temp.append(col)
        temp.append(df[col].isna().sum())
        temp.append(df[col].nunique())
        meta_list.append(temp)
    print(tabulate(meta_list, headers, tablefmt='rst'))