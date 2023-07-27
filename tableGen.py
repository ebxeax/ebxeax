import os, time
def t(f):
    ti = os.path.getctime(f)
    til = time.localtime(ti)
    return time.strftime("%Y-%m-%d %H:%M:%S", til)

def t_c(f):
    ti = os.path.getatime(f)
    til = time.localtime(ti)
    return time.strftime("%Y-%m-%d %H:%M:%S", til)

dir = './md/'
name = os.listdir(dir)
print(">>>File : " + str(len(name)) + " files")
mdline = []
url = 'https://github.com/ebxeax/ebxeax/blob/master/md/'
for i in name:
    link = '[' + i.split('.md')[0] + '](' + url + i + ')'
    mdline.append("|" + t_c(dir + i) + "|" + t(dir + i) + "|" + link)

mdline.sort()
mdline.reverse()

title = """
|created date|lastest modified date|markdown links|
|-|-|-|
"""

rd0 = """# Welcome to my homepage

![ebxeax's GitHub stats](https://github-readme-stats.vercel.app/api?username=ebxeax&count_private=true&theme=dark)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs?username=ebxeax&layout=compact&count_private=true&theme=dark)

## Website [temp use waiting for finishing post sys]
- [https://ebxeax.github.io](https://ebxeax.github.io)
- [https://ebxeax.vercel.app](https://ebxeax.vercel.app)

## Markdown Table 

"""

rd = open('./README.md', '+w', encoding="utf-8")
rd.write(rd0)
rd.write(title)
for i in mdline:
    rd.write(i + '\n')
rd.close()
print(">>>Info : Success gen table")
