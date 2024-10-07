#!/usr/bin/env python3

from gpiozero import MotionSensor
import sys
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

file_gentleman = "/home/pi/Videos/gentleman.mp4"
duration_gentleman = 74
file_daughter = "/home/pi/Videos/daughter.mp4"
duration_daughter = 59
file_gentleman1 = "/home/pi/Videos/gentleman1.mp4"
duration_gentleman1 = 29
file_daughter1 = "/home/pi/Videos/daughter1.mp4"
duration_daughter1 = 22
file_gentleman2 = "/home/pi/Videos/gentleman2.mp4"
duration_gentleman2 = 48
file_daughter2 = "/home/pi/Videos/daughter2.mp4"
duration_daughter2 = 38

slength = "1920"
swidth = "1080"

print("Starting up....")
tgr = 0

try:
    # Start up the video player
    VIDEO_PATH = Path(file_gentleman)
    player = OMXPlayer(
        VIDEO_PATH,
        args=["--no-osd", "--loop", "--win", "0 0 {0} {1}".format(slength, swidth)],
    )

    # Start up the motion sensor
    pir = MotionSensor(4)
    sleep(2)
    print("Ready to trigger")

    while True:
        player.pause()
        if pir.motion_detected:
            print("trigger count {}".format(tgr))
            player.play()


            if tgr % 6 == 0:
                sleep(duration_daughter2)
                player.stdin.write(b'p')  # Send 'p' key to pause the video
                player.stdin.flush()

                player.load(file_gentleman)
            elif tgr % 6 == 1:
                sleep(duration_gentleman)
                player.stdin.write(b'p')  # Send 'p' key to pause the video
                player.stdin.flush()

                player.load(file_daughter)
            elif tgr % 6 == 2:
                sleep(duration_daughter)
                player.stdin.write(b'p')  # Send 'p' key to pause the video
                player.stdin.flush()

                player.load(file_gentleman1)
            elif tgr % 6 == 3:
                sleep(duration_gentleman1)
                player.stdin.write(b'p')  # Send 'p' key to pause the video
                player.stdin.flush()

                player.load(file_daughter1)
            elif tgr % 6 == 4:
                sleep(duration_daughter1)
                player.stdin.write(b'p')  # Send 'p' key to pause the video
                player.stdin.flush()

                player.load(file_gentleman2)
            elif tgr % 6 == 5:
                sleep(duration_gentleman2)
                player.stdin.write(b'p')  # Send 'p' key to pause the video
                player.stdin.flush()

                player.load(file_daughter2)
            else:
                pass
            tgr = tgr + 1
        else:
            pass

        player.set_position(0.0)


except KeyboardInterrupt:
    player.quit()
    sleep(3)
    sys.exit()
