#This class handles zipfiles 
import zipfile

#This method unzips a file
def unzipfile():
    Dataset = "data"
    with zipfile.ZipFile("../BallmerPeak/Dataset/Data/"+Dataset+".zip","r") as z:
        z.extractall(".")

unzipfile()
