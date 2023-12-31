# System dependencies (Ubuntu): xclip
import re
from PyPDF2 import PdfReader
import pyperclip3 as pc
import glob
import os
import time
import info #Personal info file

def pdfToTxt(pdfFileName):
    reader = PdfReader(pdfFileName)
    firstPage = reader.pages[0]
    return firstPage.extract_text()

def findRecentFile(file_type):
    fileList = glob.glob("./*" + file_type)
    if len(fileList) <= 0:
        print("-!-Most recent file not found-!-")
        return
    else:
        newestFile = max(fileList, key=os.path.getctime)
        return newestFile[2:]
    

def fileCount(file_type):
    fileList = glob.glob("./*" + file_type)
    # newestFile = max(fileList, key=os.path.getctime)
    return len(fileList)

def confirmChanges():
    try:
        new_content = ""
        with open(findRecentFile(".tex")) as file:
            for line in file:
                new_content += line
        file.close()

        regex = fr"({info.name})"
        if search_result:=len(re.findall(regex, new_content)) == 3:    # should be 3 results for each occurence of my name
            print("---changes confirmed---")
        else:
            print("---failed to confirm changes, ", int(search_result), " occurences found---")
    except:
        print("-!-Failed to fill out your info-!-")

def waitForTexFile(name, idNum):
    t_end = time.time() + 60 * 5    # Time will run for 5 minutes
    initial_file_count = len(glob.glob("./*.tex"))
    while time.time() < t_end:
        if (current_file_count:=fileCount(".tex")) != initial_file_count:      # Cool way to save a value being checked in the if statement.   varName := captureVariable ;  https://stackoverflow.com/questions/1550134/how-to-assign-a-variable-in-an-if-condition-and-then-return-it
            file = findRecentFile(".tex")
            time.sleep(1)                               # Sleeping here seems to fix reliability when downloading from Canvas.
            sysCmd = "bash autoCompleteInfo '%s' '%s' '%s' " % (str(file), name, idNum)
            try:
                os.system(sysCmd)
                print("---file '" + str(file) + "' changed where applicable---")
                print("current: " + str(current_file_count) + ", previous: " + str(initial_file_count))
                return
            except:
                print("-!-Error trying to make changes to '" + str(file) + "'-!-\n")
                return

def getCode(extraction_file):
    try:
        content = pdfToTxt(extraction_file)
        regex = r'(?:Quiz Code \(enter in Canvas to get access to the LaTeX template\)[ .]*)([A-Z]\w+)'
        try:
            return re.search(regex, content).group(1)
        except:
            print("-!-Failed to locate quiz code-!-")
    except:
        print("-!-Failed to read/open PDF-!-")

def copyToClipboard(code, extraction_file):
    try:
        pc.copy(code)
        print('Copied:' + code + ' to clipboard from ' + extraction_file)
    except:
        print("-!-Code failed to copy to clipboard-!-")
        print("Code: " + code + "\n")