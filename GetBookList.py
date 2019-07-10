#!/usr/bin/env python3


import os
import sys


def GetBookList():
    directorys = {}
    with open("BookList.txt", "w") as fileObject:
        for eachFileAndDir in os.listdir(os.getcwd()):
            if os.path.isdir(eachFileAndDir) and (not eachFileAndDir.startswith(".")):
                directorys[eachFileAndDir] = []
                for eachPDF in os.listdir(os.getcwd()+"/"+eachFileAndDir):
                    directorys[eachFileAndDir].append("* [" + eachPDF + "](https://github.com/ColorHistory/Book/blob/master/" + eachFileAndDir + "/" + eachPDF + ")")

    for key, value in directorys.items():
        print(key+"\n")
        for eachfile in value:
            print(eachfile)

    
GetBookList()
