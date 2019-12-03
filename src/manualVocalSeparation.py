# TODO: Pull up the video and gather timestamp feedback by userinput and use that to match the lyrics with the images
import os
import keyboard
import time


def playback(path, lyrics):
    #os.system("xdg-open {}".format(path))
    timestamps = []
    i = 0
    t0 = None
    t1 = None
    x = 0

    while 1:
        try:
            if keyboard.is_pressed("s"):
                print("Started")
                t0 = time.time()
                print(lyrics[0])
                break
            if keyboard.is_pressed("d"):
                t1 = time.time()
                timestamps.append(t1-t0)
                x += 1
                if x == len(lyrics[i]):
                    i += 1
                    print(lyrics[i])
                    x = 0
                break
        except Exception:
            print("Goodbye")
            break



