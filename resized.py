from itertools import count
import cv2 
import glob 
import os 
 
inputFolder = 'media' 
os.mkdir('media/ResizedFolder') 

img = "C:/Users/Yagmur/OneDrive/Masaüstü\Pedestrian-Detection-Project\media"

 
i = 0 
for img in glob.glob(inputFolder + "/*.png"): 
    image = cv2.imread(img) 
    imgResized = cv2.resize(image, (200, 200)) 
    cv2.imwrite("media/ResizedFolder/image%i.png" %i , imgResized) 