import cv2 
import glob 
import os 
 
inputFolder = 'media' 
os.mkdir('ResizedFolder') 
 
i = 0 
for img in glob.glob(inputFolder + "/*.jpeg"): 
    image = cv2.imread(img) 
    imgResized = cv2.resize(image, (80, 80)) 
    cv2.imwrite("ResizedFolder/image%i.jpeg" %i , imgResized) 
 

