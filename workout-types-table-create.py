#import pandas
import pandas as pd

#create dictionary that will become workout types table
work_out_types = {"Type_ID": ["01", "02", "03", "04", "05"], "Type_Name":['Arms', 'Chest','Back','Legs','Shoulders']}

#pass dictionary into df
work_out_types = pd.DataFrame(work_out_types)

#write the df into a csv file 
work_out_types.to_csv(r'Z:\Users\WKerby\\My Computer\Documents\Python\workout-types-table.csv', index = False)