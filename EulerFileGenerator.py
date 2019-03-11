import os
from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    idx = 0
    ii = 0
    numBottom = ""
    numTop = ""
    topDirName = ""
    ifLastDelTopDir = ""
    while(True):
        try:
            if (idx % 20 == 0):
                numBottom = str(ii * 20 + 1)
                numTop = str(((ii + 1) * 20))
                topDirName = "Projects " + numBottom + " - " + numTop
                if not os.path.exists(topDirName):
                    os.makedirs(topDirName)
                ifLastDelTopDir = topDirName
                ii = ii + 1
            fulldirName = topDirName + '/' + 'P' + str(idx + 1) + '_'
            fullPath = fulldirName + '/' + 'P' + str(idx + 1) + '.py'
            if os.path.exists(fullPath):
                print(fullPath + " Skipped. Already Exists.")
                idx += 1
                continue
            r = requests.get("https://projecteuler.net/problem=" + (str(idx + 1)))
            soup = BeautifulSoup(r.text, 'html.parser')
            paragraph = soup.find(class_='problem_content')
            addString = str(paragraph.text)
            if not os.path.exists(fulldirName):
                os.makedirs(fulldirName)
            if not os.path.exists(fullPath):
                writeFile = open(fullPath, 'w')
                writeFile.write('"""\n')
                writeFile.write(addString)
                writeFile.write('"""\n')
                writeFile.close()
            print(fullPath + " Successfully Generated.")
            idx += 1
        except:
            if len(os.listdir(ifLastDelTopDir)) == 0:
                os.rmdir(ifLastDelTopDir)
            print("Done")
            break
        
