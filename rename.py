import os

path = "C:\\Users\\...."   #path of folder containing images
a = []
os.chdir(path)
a =os.listdir()
i = 0

for x in range(len(a)):
    num  = str(i)
    num = num.zfill(4)
    os.rename(a[x],'Sample'+num+'.jpg')
    i = i+1
