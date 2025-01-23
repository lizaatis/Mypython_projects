#example file working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
#print the name of os
 #print(os.name)

 #Check for item existence and type
 #print("Item exists: " + str(path.exists("textfile.txt")))
 #print("Item is a file: " + str(path.isfile("textfile.txt")))
 #print("Item is a direectory: " + str(path.isdir("textfile.txt")))

 #Work with file paths
 print("Item path: " + str(path.realpath("textfile.txt")))
 print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))
