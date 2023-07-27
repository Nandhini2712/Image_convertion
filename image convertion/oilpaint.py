import cv2
import os

def Image(img,frame_name):
    outputfolder="content\output\oilpaintoutput"      
    cv2.imshow(frame_name,img)
    cv2.imwrite(os.path.join(outputfolder,frame_name+'.jpg'),img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

inputfolder = 'content\sourceimg\oilpaintsource' 
imgin=input("Enter the image name:")
path=inputfolder+imgin
# print(path)
img = cv2.imread(path)
res = cv2.xphoto.oilPainting(img, 3, 3)
Image(img,"original_"+imgin[1:-4])
Image(res,"oilpaint_"+imgin[1:-4])
# cv2.imshow("original", img)
# cv2.imshow("oilpaint", res)
# cv2.imwrite(os.path.join(outputfolder,"original_"+imgin),img)
# cv2.imwrite(os.path.join(outputfolder,"oilpaint_"+imgin),res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

