# Cartoon Sketch using Bilateral Filter and  Median Blur
#Import the necessary packages
import cv2
import matplotlib.pyplot as plt
import matplotlib
import os


def Image(img,frame_name):
    output_folder = 'content\output\cartoonoutput'        
    cv2.imshow(frame_name,img)
    cv2.imwrite(os.path.join(output_folder,frame_name+'.jpg'),img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# TODO - To lighten the image and apply blur and detect sharp edges


#Function to print Image
try:
    inputfolder="content\sourceimg\cartoonsource"
    fname=input("Enter image name :")
    path=inputfolder+fname
    # path='content\\sourceimg\\pencilsource\\Dhanush_at_VIP_2_Success_Meet.jpg' 
    img=cv2.imread(path)
    height,width, channels = img.shape
    #print(height,width)
    fname=fname[1:-4]
except AttributeError as AE:
    print('----------Check Validity of Image path--------------')
    exit() 
except AssertionError as Asserr:
    print('--------Check Path----')
    exit()
except Exception as e:
    print(e)
    print('-----------Please check your Image Path-------------')
    exit()

name = list(path.split('.'))[0] # Name of the image

#Verify image 
Image(img,'Original Image '+fname)

col_img = cv2.bilateralFilter(img,5,255,255)
Image(col_img,"Bilateral Filter "+fname)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Image(gray,'Grayscaled Image '+fname)
gray = cv2.medianBlur(gray,3)
Image(gray,'Grayscale '+fname)
edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,5)
Image(edges,'Getting edges '+fname)
cartoon = cv2.bitwise_and(col_img,col_img,mask=edges)
Image(cartoon,'Cartoon '+fname)
filename = name + '_cartoon.png'
# cv2.imwrite(filename,cartoon)

