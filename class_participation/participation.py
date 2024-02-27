from datetime import datetime,timedelta

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
                if not speaker or speaker.isdigit(): 
                    continue
                else: 
                    if speaker not in speakers:     
                        speakers[speaker] = 0
                    speakers[speaker] += timedelta.total_seconds(end_time-start_time)
    return speakers

def main():
    vtt_file = "trans.vtt"  # Replace with your VTT file path
    speakers_duration = parse_vtt(vtt_file)
    for speaker, duration in speakers_duration.items():
        print(f"{speaker}: {duration:.2f} seconds")

if __name__ == "__main__":
    main()