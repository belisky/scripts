import pandas as pd
file_path = "AWSclasslist.xlsx"   
df = pd.read_excel(file_path,sheet_name='Nobel-Feb')  
 
# print(df)      
for ind,row in df.iterrows():
    try:   
         
        full_name = row["name-21"]
        email = row['email address']
        print(full_name,email)
        
    except:
        continue
        
        
        