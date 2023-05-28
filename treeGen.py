import os

mds = os.listdir('./md')
mds.sort()
#print(len(mds))
#print(mds[1:9])

lis = []
for i in mds:
    st = '[' + i.split('.md')[0] + ']' + '(https://github.com/ebxeax/ebxeax/md/' + i + ')'
    lis.append(st)
lis.sort()

tree = open('./tree.md', '+w')
tree.writelines(lis)
tree.close()