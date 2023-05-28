import markdown
import os
import sys
from treeGen import *
from time import sleep
exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
html = """
<HTML lang="zh-cn">
<HEAD>
<TITLE>ebxeax</TITLE>
<LINK REL="stylesheet" TYPE="text/css" HREF="../css/lua.css">
<link rel="Shortcut Icon" href="../images/favicon.ico" type="image/x-icon" />
<META HTTP-EQUIV="content-type" CONTENT="text/html; charset=utf-8">
<STYLE TYPE="text/css">
blockquote, .display {
	border: solid #a0a0a0 2px ;
	border-radius: 8px ;
	padding: 1em ;
	margin: 0px ;
}

.display {
	word-spacing: 0.25em ;
}

dl.display dd {
	padding-bottom: 0.2em ;
}

tt, kbd, code {
	font-size: 12pt ;
}
</STYLE>
</HEAD>

<BODY>

<H1>
<A HREF="http://www.github.com/ebxeax"><IMG SRC="../images/favicon.ico" width="100" height="100" ALT="ebxeax"></A>
Homepage
</H1>


<DIV CLASS="menubar">
	<A HREF="#about">about</A>
	&middot;
	<A HREF="#tutorial">tutorial</A>
	&middot;
	<A HREF="#test">test</A>
	&middot;
	<A HREF="tree.html">tree</A>
</DIV>
%s
</BODY>
</HTML>    
"""

def md2html(mdstr):
    ret = markdown.markdown(mdstr,extensions=exts)
    return html % ret

def get_from_argv():
    if len(sys.argv) < 3:
        print('usage: md2html.py [source_filename] [target_file]')
        sys.exit()
    infile = open(sys.argv[1],'r')
    md = infile.read()
    infile.close()
    if os.path.exists(sys.argv[2]):
        os.remove(sys.argv[2])
    outfile = open(sys.argv[2],'a')
    outfile.write(md2html(md))
    outfile.close()
    print('convert %s to %s success!'%(sys.argv[1],sys.argv[2]))

def removeCache(filepath):
    delist = os.listdir(filepath)
    for f in delist:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(">>>>>clean html := " + file_path)

if __name__ == '__main__':

    root = './md/'
    des = './html/'
    removeCache(des)
    sleep(2)
    mdir = os.listdir(path = root)
    ll = []
    for i in mdir:
        if i.split(sep = '.')[1] == 'md':
            ll.append(i)
    for i in ll:
        oldfile = root + i
        newfile = des + i.split('.')[0] + '.html'
        print(">>>>>gen md2html := " + newfile)
        infile = open(oldfile, 'r')
        md = infile.read()
        infile.close()
        outfile = open(newfile ,'w')
        outfile.write(md2html(md))
        outfile.close()
    hdir = os.listdir(path = des)
    hdir.reverse()
    treeGen(hdir)
