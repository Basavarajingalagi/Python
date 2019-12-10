import os
import cv2

def convert(informat,k,p,a):
    source = os.listdir(k)
    dirs = p
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    kl = []
    k = []
    if informat == '':
        #kl = []
        for i in source:
            if i.endswith('.ppm'):
                k.append(i)

        for i in source:
            if i.endswith('.png'):
                k.append(i)

        for i in source:
            if i.endswith('.jpg'):
                k.append(i)

        for i in source:
            if i.endswith('.JPEG'):
                k.append(i)
    
        n=0
        for i in k:
            img = cv2.imread(i)
            img_name = os.path.splitext(i)[0]
            
            cv2.imwrite(os.path.join(dirs,(img_name+str(n)+a)), img)
            n+=1  
        
    else:             
       # k  = []
        for i in source:
            if  i.endswith(informat):
                kl.append(i)
                
        n=0
        for i in kl:
            img = cv2.imread(i)
            img_name = os.path.splitext(i)[0]
            
            cv2.imwrite(os.path.join(dirs,(img_name+str(n)+a)), img)
            n+=1  



informat = input('give the input format')
source = input('specify the src folder')
destination = input('specify the path to copy files')
a = input('to which format u want to convert')
convert(informat,source,destination,a)
