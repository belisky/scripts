from datetime import datetime,timedelta
import os
from names_hash import names_hash,repeated_names_list,names_list


def parse_vtt(vtt_file):
    speakers = {}
    with open(vtt_file, 'r') as file:
        lines = file.readlines()
        speaker = None
        start_time = None
        end_time = None
        for line in lines:
             
            if line.strip().isdigit():
                start_time, end_time = lines[lines.index(line) + 1].strip().split(' --> ')
                start_time = datetime.strptime( start_time, "%H:%M:%S.%f")
                end_time = datetime.strptime( end_time, "%H:%M:%S.%f")
                speaker = lines[lines.index(line) + 2].strip().split(':')[0] if ':' in lines[lines.index(line) + 2].strip() else None
                try:
                    speaker='-'.join(speaker.lower().split())
                except:
                    continue
                if not speaker or speaker.isdigit(): 
                    continue
                else: 
                    if speaker not in speakers:     
                        speakers[speaker] = 0
                    speakers[speaker] += timedelta.total_seconds(end_time-start_time)
    return speakers

def main():
    vtt_file = 'data/'+os.listdir("data")[0] # Replace with your VTT file path
    present_speakers=set()
    error_names=set()
    class_list=set(names_hash.keys())
    speakers_duration = parse_vtt(vtt_file)
    # print(speakers_duration)
    # print(len(speakers_duration))
    for speaker, duration in sorted(speakers_duration.items()):
        print(f"{speaker}: {duration:.2f} seconds")
        for ind,repeated_names in enumerate(names_hash.keys()):
            
            if len(set(repeated_names.split('-')))<5 and (len(set(repeated_names.split('-'))-set(speaker.split('-')))<2):
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
    all_except=class_list-present_speakers
    print("\n\nall except",len(all_except))
    for names in sorted(all_except):
        print(names)
    # print(len(list(present_speakers)))
    # print(list(error_names))
    # print(len(list(error_names)))


    os.remove(vtt_file)
if __name__ == "__main__":
    os.chdir('class_participation')
    os.system('clear')
    
    main()