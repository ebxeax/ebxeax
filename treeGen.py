import os
dir = './md/'
mds = os.listdir(dir)
mds.sort()
lis = []
url = 'https://github.com/ebxeax/ebxeax/blob/master/md/'
for i in mds:
    st = '- [' + i.split('.md')[0] + '](' + url + i + ')'
    lis.append(st)
lis.sort()

rd0 = """# Welcome to my homepage

![ebxeax's GitHub stats](https://github-readme-stats.vercel.app/api?username=ebxeax&count_private=true&theme=dark)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs?username=ebxeax&layout=compact&count_private=true&theme=dark)

## Website [temp use waiting for finishing post sys]
- [https://ebxeax.github.io](https://ebxeax.github.io)
- [https://ebxeax.vercel.app](https://ebxeax.vercel.app)

## Markdown Tree 

"""

rd = open('./README.md', '+w')
rd.write(rd0)
for i in lis:
    rd.write(i + '\n')
rd.close()