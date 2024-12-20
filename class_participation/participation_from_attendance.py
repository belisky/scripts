import csv
import os
from names_hash import names_list

os.chdir('class_participation')
 
# Function to read the first column of a CSV file
def read_first_column(csv_file):
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        first_column = ['-'.join(row[0].lower().split()) for row in reader if row]  # Read first column for non-empty rows
    return first_column

# Example usage
csv_file = vtt_file = 'data/'+os.listdir("data")[0]  # Replace with your CSV file path
first_column = read_first_column(csv_file)
present_speakers=set()

for speaker in sorted(first_column):
    # print(f"{speaker}: {duration:.2f} seconds")
    for ind,repeated_names in enumerate(names_list):
        
        if len(set(repeated_names.split('-')))<5 and len(set(repeated_names.split('-'))-set(speaker.split('-')))<2:
            # print(speaker,names_list[ind])
            present_speakers.add(names_list[ind])
        if len(set(speaker.split('-')))>4 and len(set(repeated_names.split('-'))-set(speaker.split('-')))<3:
            # print(speaker,names_list[ind])
            present_speakers.add(names_list[ind])
        
print("present",len(present_speakers))
# present_speakers=set('paul-botchwey,gaius-junior-erzoah,emmanuel-tandoh,precious-annor-mante,amankwah-andy-prempeh,emily-wepiah-wobi,esegbe-able-katapu,hanisha-abdul-majid,edward-attram-menya,moses-kwarteng,sibdou-ibrahim-issifu,henrietta-nutifafa-kessie,eugget-nyarko-wireko,alex-karikari,jeffery-darko,sylvia-famieh-quines,enyonam-beatson-affram,charles-cornah,david-kwabena-arhin,anku-jude,kwamena-essiful-ansah,isaac-junior-nyemekye,nobel-fiawornu,ann-dwamena,eric-affum,clifford-kingsley-baidoo,edwin-adu-boateng,samuel-agyarko,richelle-asmah,moses-tetteh,aaron-atter,noah-boye,karen-hanson,bright-sefah,victor-okyere,joseph-osei-yaw-nyarko,kingsley-anim,mensah-sitti,evans-obu,albert-kofi-kwansah-ansah,ivy-botchway,eunice-kessewaa,bernard-kirk-adjarnor-katamanso,emmanuel-kissi-addo,salihu-shaban,emmanuel-selase-tormeti,emmanuel-gyan-ansah'.split(','))
print(present_speakers)
    # if speaker not in present_speakers:
    #     error_names.add(speaker)
all_except=set(names_list)-present_speakers
print("\n\nall except",len(all_except))
for names in sorted(all_except):
    print(names)

# Print the values in the first column
 
