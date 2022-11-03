import os
from Function import *

def FirstMenu(playlist_tracks):
    while(True):
        print("##################################################################################################")
        print("####################################  W E L C O M E   ############################################")
        printSongs(playlist_tracks)
        print("-------------------------------Select Your Song (Only Name)---------------------------------------")
        try:
            song = input("")
            return (checkSong(song, playlist_tracks))
        except:
            print("Value entered incorrectly")
            os.system('cls')
            return False

def SecondMenu(songSelected):
    while(True):
        print("##################################################################################################")
        print(f"#Song Selected-----> {songSelected.name}- {songSelected.artist}")
        print("###OPTIONS###")
        print("1.Filter By Group")
        print("2.Filter By Seems")
        print("3.Filter By Ranking")
        print("--------------------------------------Select Your Option ------------------------------------------")
        try:
            option=int(input(""))
            return option
        except:
            print("Option Incorrectly")

