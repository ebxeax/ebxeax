import os
from movefile import *
from getImages import *
from movefile import *

__version__ = '2.0'

def moveImages(md = 'md'):
    fileslist = getFilelist('./' + md)
    img = []
    for file in fileslist:
        print(f'>>>>>>load: {file}')
        with open(file, encoding='utf-8') as f:
            mdContent = f.read()
        picslist = getPicslist(mdContent)
        img.append(picslist)
        print(f'>>>>>>find pic: {len(picslist)}')
        rf = open(file, 'r')
        omd = rf.read()
        rf.close()
        for pic in picslist:
            src = pic
            cdn = 'https://cdn.jsdelivr.net/gh/bookcooker/img@' + __version__ + '/'
            des = cdn + pic.replace('../images/', file.replace('./md/', '').replace('.md', '') + '/')
            # print('>>>>>>cast new: ' + src, '-->', des)
            omd.replace(src, des)
        wf = open(file, 'w+')
        wf.write(omd)
        wf.close()
        
        print('>>>>>>finish.')
if __name__ == "__main__":
    moveImages()