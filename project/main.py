__author__ = 'root'

import time
import subprocess
import sys
import os
import glob
import shutil

from time import sleep


def shutdown ():
    print("")
    print ("\nThe system is now shutting down")
    for x in range(5, -1, -1):
       do_task()
       sys.stdout.write('\r')
       sys.stdout.write(formatTime(x))
    if (formatTime(x)) == "00:00":
        print("\nProcess Completed!")
        #subprocess.call(["gnome-screensaver-command", "--lock"])

def formatTime(x):
    minutes, seconds_rem = divmod(x, 60)
# use string formatting with C type % specifiers
# %02d means integer field of 2 left padded with zero if needed
    return "%02d:%02d" % (minutes, seconds_rem)

def do_task():
    time.sleep(1)

def process_load():
    for i in range (21):
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
        sys.stdout.flush()
        sleep(0.25)

def del_file():
    for name in glob.glob('/root/Classified'):
        print ("\nClassified Files Found: " + name)
        print ("Deleting Classified Information!")
        process_load()
        do_task()
        shutil.rmtree(name)

def file_list():
    for name in glob.glob('/root/Classified'):
        print ("Securing Files...")
        do_task()
        process_load()
        print("\nFiles Found:" + name)
        print("Files Secured!")





def main():

    access= str(input("Enter your access code:"))

    if access != 'guru12':
        print ("Access Denied!")
        del_file()
        print("")
        print ("\nInitiating Shutdown Protocol")
        do_task()
        process_load()

        shutdown()

    else:
        print ("Access Granted!")
        file_list()


if __name__ == "__main__":
    main()

