import pandas as pd
file_path = "./AWSclasslist.xlsx"   
df = pd.read_excel(file_path,sheet_name='Nobel-Feb')  
 
# print(df,'hi')   
emails_hash={}   
for ind,row in df.iterrows():
    try:   
         
        # full_name = row["name-21"]
        # email = row['email address']
        emails_hash[row['email address']]=row['name-21']
        
    except:
        continue
print(emails_hash)       
        
        