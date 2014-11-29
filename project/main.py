__author__ = 'GuruShiva'

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
        #subprocess.call(["shutdown", "-h", "now"])


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

 name = glob.glob('/root/Classified')
 print ("Checking for Classified Files...")
 process_load()

 if not name:
     print ("\nClassified files not found.")
     print ("Halting Shutdown Procedure!")
     sys.exit("\nSystem is secured!")

 else:


     for name in glob.glob('/root/Classified'):
        print ("\nClassified Files Found @: " + name)
        print ("Deleting Classified Information!")
        process_load()
        do_task()
        shutil.rmtree(name)

def file_list():
    name = glob.glob('/root/Classified')
    print ("Checking for Classified Files...")
    process_load()

    if not name:
         print ("\nClassified Files not found ")
         sys.exit("\nSystem is secured!")




    else:
        for name in glob.glob('/root/Classified'):
          print ("\nClassified Files Found @: " + name)
          print ("\nSecuring Classified Files...")
          process_load()
          print ("\nSystem is secured!")





def main():

    access= str(input("Enter your access code:"))

    if access != '12345':
        print ("Access Denied!")
        print("System Breached!")
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

