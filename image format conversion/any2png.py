import os
import cv2

def copy2png(source,destination):
    a = os.listdir(source)
    dirs = destination
    if not os.path.exists(dirs):
        os.makedirs(dirs)

    jpg = []
    for i in a:
        if i.endswith('.jpg'):
            jpg.append(i)

    for i in a:
        if i.endswith('.ppm'):
            jpg.append(i)

    for i in a:
        if i.endswith('.JPEG'):
            jpg.append(i)
    
    n=0
    for i in jpg:
        img = cv2.imread(i)
        img_name = os.path.splitext(i)[0]
        
        cv2.imwrite(os.path.join(dirs,(img_name+str(n)+'.png')), img)
        n+=1    

def copypng(source,destination):
    a = os.listdir(source)
    dirs = destination
    if not os.path.exists(dirs):
        os.makedirs(dirs)

    png = []
    for i in a:
        if i.endswith('.png'):
            png.append(i) 
    n=0
    for i in png:
        img = cv2.imread(i)
        img_name = os.path.splitext(i)[0]
        
        cv2.imwrite(os.path.join(dirs,(img_name+str(n)+'.png')), img)
        n+=1    
    
source = input('enter the path of folder containing images')
destination = input('enter the path to which u want to copy ong files')
ask = input("do you want to copy png files also if yes press Y else N")
if ask.upper() == 'Y':
      copypng(source,destination)
      copy2png(source,destination)
      
elif ask.upper() == 'N':
      copy2png(source,destination)

else:
      print('input either Y or N')
