#This class handles zipfiles 
import zipfile

class extractZip():
    #This mehtod unzips a zip compressed file
    #Takes the path as first input and filename as second input
    #Uses zipfile libary
    @staticmethod
    def unzipfile(path, filename):
        with zipfile.ZipFile(path + filemname + ".zip", "r") as z:
            z.extractall(".")

unzipfile("../BallmerPeak/Dataset/Data/", "data")
