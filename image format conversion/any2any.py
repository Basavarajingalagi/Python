import os
import cv2

def convert(k,p,a,x,y):
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
        img = cv2.resize(img,(x,y))
        cv2.imwrite(os.path.join(dirs,(img_name+str(n)+a)), img)
        n+=1  


def copypng(source,destination,a,x,y):
    source = os.listdir(source)
    dirs = destination
    if not os.path.exists(dirs):
        os.makedirs(dirs)

    png = []
    for i in source:
        if i.endswith(a):
            png.append(i) 
    n=0
    for i in png:
        img = cv2.imread(i)
        img_name = os.path.splitext(i)[0]
        img = cv2.resize(img,(x,y))
        cv2.imwrite(os.path.join(dirs,(img_name+str(n)+a)), img)
        n+=1
        

def length(a):
    jz = []
    for i in os.listdir(source):
        if i.endswith(a):
            jz.append(i)
    b = len(jz)
    return b

source = input('specify the folder')
destination = input('specify the path to copy files')
a = input('to which format u want to convert')
x = int(input('specify x dimension'))
y = int(input('specify y dimension'))
b = length(a)
print('there exist {} files of format {}'.format(b,a))
ask = input("do you want to copy same format existing files also\n if yes press Y else N\n")
if ask.upper() == 'Y':
      copypng(source,destination,a,x,y)
      convert(source,destination,a,x,y)
      
elif ask.upper() == 'N':
      convert(source,destination,a,x,y)

else:
      print('input either Y or N')
