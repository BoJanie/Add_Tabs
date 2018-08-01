import os

#Put your file name as the text variable
text = 'AddTabsToThisFile.txt'
newText = 'TabsAddded.txt'

with open(text, 'r+') as f:
    old = f.readlines()
    newLines = '\t'.join(old)
with open(newText, 'w+') as f:
#Future edit: Automatically make filename same as before, with append
#with open(os.text.basename + '_TabsAdded.txt','w+') as f:
    f.write('\t')
    f.writelines(newLines)
    f.close()
    
