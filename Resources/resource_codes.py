import pandas as pd 
import numpy as np 
import os
from Resources.utilities import *


def scenario_method():
    df = pd.read_excel("Data/Employee.xlsx", sheet_name="Sheet")    
    department_df = df.groupby(['Department']).size().reset_index(name='Count')
    print(department_df)
    write_in_csv(department_df, 'Departments')
    