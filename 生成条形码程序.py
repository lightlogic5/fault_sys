import logging
import sys
from pystrich.code128 import Code128Encoder
from PIL import Image
from io import StringIO,BytesIO
import re
PUBLIC_SIZE=24
typename=input('请输入款式')
size=input("请输入型号")
color=input("请输入颜色对照码")
typesize='%s%s%s'%(typename,size,color)
with open('number.txt','r+') as f:
    data=f.read()
    if typesize in data:
        number=re.search(r'%s(\w+)'%typesize,data).group(1)
        NUMBER=int(number)+PUBLIC_SIZE
        data=re.sub(r'%s(\w+)'%typesize,'%s%d'%(typesize,NUMBER),data)
        f.write(data)
    else:
        print('+++')
        data+='%s%d\n'%(typesize,PUBLIC_SIZE)
        number='0'
        NUMBER=int(number)+PUBLIC_SIZE
with open('number.txt','w+') as f:
    f.write(data)
img_list=[]
for i in range(int(number),NUMBER):
    i=str(i).zfill(6)
    encoder = Code128Encoder("%s%s"%(typesize,i))
    img_list.append(BytesIO(encoder.get_imagedata()))
toImage = Image.new('RGBA',(1550,2000))
for i in range(PUBLIC_SIZE):
    fromImge = Image.open(img_list[i])
    loc = ((int(i/8) * 520), (i % 8) * 200)
    toImage.paste(fromImge, loc)
toImage.save('merged.png',quality =100)