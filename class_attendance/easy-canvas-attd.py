import pandas as pd
import os
from collections import Counter
from names_and_emails_hash import full_name_hash,email_hash

keys=full_name_hash.keys()
vals=full_name_hash.values()
absentees = []
attd_sheets = sorted(os.listdir("data"))

def find_missing_emails(first_name):
    for key in keys:
        if first_name in key:
            return full_name_hash[key]
        else:
            continue

def update_present_emails(full_name,email,present):     
    if pd.notnull(email):
        present.append(email)
    else:
        partial_name = full_name.split(",")[0]
        missing_email = find_missing_emails(partial_name)
        if missing_email:
            present.append(missing_email)
def print_names_emails_and_absence(absentees_freq):
    for mail in absentees_freq:
        print(f"{mail:<30}",f"{email_hash[mail]:<20}",f"{'--->':<5}",f"{absentees_freq[mail]:<3}")
    print("Total:",len(absentees_freq))


def read_columns_from_morning_and_afternoon():
    emails_present = []
    absentees = []
   
    try:
        for sheet in attd_sheets:          
            file_path = "data/" + sheet      
            df = pd.read_csv(file_path)         
            for ind in range(len(df)):
                try:
                    full_name = ",".join(str(df.iloc[ind][0]).strip().split()).lower()
                    email = df.iloc[ind][1]
                    
                    update_present_emails(full_name,email,emails_present)
                except:
                    continue                    
            absentees_per_session = set(vals) - set(emails_present)                    
            emails_present = []
            absentees += list(absentees_per_session) 
        absent_freq = Counter(absentees)
        print_names_emails_and_absence(absent_freq)

 
    except Exception as e:
        print(f"Error reading column from Excel file: {e}")
        return None
    
def main():
    read_columns_from_morning_and_afternoon()


if __name__== "__main__":
    main()
         
 
