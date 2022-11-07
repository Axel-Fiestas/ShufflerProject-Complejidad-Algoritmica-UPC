import csv
from Classes.classes import *

#Track Name = row[1]
#Artist Name= row[3]
#Popularity= row[15]
#Genres Artist=row[18]

playlist_tracks=[]

def getSongs():
    with open("DataSet/liked2.csv", encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                #print(row[1],row[3],row[15],row[29])
                line_count += 1
            else:
                #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                s=Song(row[1],row[3],row[15],row[18].split(","),round(int(float(row[29]))))
                playlist_tracks.append(s)
                line_count += 1
        print(f'Processed {line_count} lines.')

    return playlist_tracks
