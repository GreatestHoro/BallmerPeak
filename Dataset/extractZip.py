#This class handles zipfiles 
import zipfile

class extractZip():
    #This mehtod unzips a zip compressed file
    #Takes the path as first input and filename as second input
    #Uses zipfile libary
    @staticmethod
    def unzipfile(path, filename):
        with zipfile.ZipFile(path + filename + ".zip", "r") as z:
            z.extractall(path)

extractZip.unzipfile("../BallmerPeak/Dataset/Data/", "data")
