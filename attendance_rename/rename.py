import os
from datetime import date,timedelta,datetime
import pandas as pd
 


def rename(folder):

    # date_start=input("Enter start date in yyyy-mm-dd format: ")
    # date_end=input("Enter end date in yyyy-mm-dd format: ")
    # date_exceptions=list(input("Enter dates to be excluded in the file renaming: "))
    # day_increment=timedelta(hours=24, minutes=0)


    for ind,file in enumerate(folder): 
        df = pd.read_csv("attd/"+file)        
         
        date_item,duration,time_of_day = df.iloc[0][4].strip().split()
        new_date=datetime.strptime('-'.join(date_item.split('-')[::-1]),"%Y-%m-%d")
        print(new_date,date_item,duration,time_of_day)
        
               
        prefix= "Morning_" if time_of_day=="AM" else "Afternoon_"
        prefix+=str(new_date).split()[0]
        
        os.rename("./attd/"+file,"./renamed/"+prefix+".csv")
        # if date_exceptions and ind==date_exceptions[0]:
        #     date_exceptions.pop(0)
        #     continue
        # else: 

        #     if "Afternoon" in prefix:
        #         new_date+=day_increment
        #         # print(new_date)
        #     else:
        #         continue
         
    print(ind+1,"files renamed successfully!!!")

    
 
def main():
    attendance_folder = sorted(os.listdir("attd"))
    print(attendance_folder)
    rename(attendance_folder)
   


if __name__== "__main__":
    os.chdir('attendance_rename')
    main()
         
 
