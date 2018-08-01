import os

#Put your file name as the text variable
text = 'AddTabsToThisFile.txt'

with open(text, 'r+') as f:
    old = f.readlines()
    newLines = '\t'.join(old)

with open(os.path.splitext(text)[0]+ '_TabsAdded.txt','w+') as f:
    f.write('\t')
    f.writelines(newLines)
    f.close()
    
