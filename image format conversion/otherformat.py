import os
import cv2

def convert(k,p,a):
    source = os.listdir(k)
    dirs = p
    if not os.path.exists(dirs):
        os.makedirs(dirs)

    jpg = []
    for i in source:
        if not i.endswith(a):
            jpg.append(i)
    kl  = []
    for i in jpg:
        if i.endswith('.ppm'):
            kl.append(i)

    for i in jpg:
        if i.endswith('.png'):
            kl.append(i)

    for i in jpg:
        if i.endswith('.jpg'):
            kl.append(i)

    for i in jpg:
        if i.endswith('.JPEG'):
            kl.append(i)
    
    n=0
    for i in kl:
        img = cv2.imread(i)
        img_name = os.path.splitext(i)[0]
        
        cv2.imwrite(os.path.join(dirs,(img_name+str(n)+a)), img)
        n+=1  



source = input('specify the folder')
destination = input('specify the path to copy files')
a = input('to which format u want to convert')
convert(source,destination,a)
