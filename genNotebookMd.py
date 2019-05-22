#!/usr/bin/python

import os
import urllib.parse

# traverse root directory, and list directories as dirs and files as files
targetDir = os.path.join(os.getcwd(), "assets/notes")
for root, dirs, files in os.walk(targetDir):
    path = root.split(os.sep)
    relPathLen = len(os.path.relpath(targetDir, root).split("/"))
    print(relPathLen * '#' + " " + os.path.basename(root))
    print("")
    #print((len(path) - 1) * '#', os.path.basename(root))
    for file in files:
        if not file.startswith("."):
            rawFilePath = os.path.join(os.path.relpath(root, os.getcwd()), file)
            #print("parent file: " + os.path.abspath(os.path.join(rawFilePath, "..")))
            parentDir = os.path.dirname(rawFilePath).split("/")[-1]
            urlEncFilePath = urllib.parse.quote(rawFilePath)
            # print("- [" + file + "]" + "(" + "/" + rawFilePath.replace(" ", "%20") + ")")
            print("- [" + file + "]" + "(" + "/" + urlEncFilePath + ")")
    print("")
