import os, re

directory=[]
urls=[]
#This makes a list of the directories we are going to explore
folders =str(os.getcwd()+'/mission/')

#test_phrase_one='https://drive.google.com/open?id=1tWJBFrSQL06qTZgkohs4t_a5Cu84AheLo'


#test_phrase_two='https://docs.google.com/document/d/Q-DcxM17nJm_El0aGsNnY7FajaogRviwja/edit'

pattern=r'https://[-?/_=.\w]+'


def search(file,pattern=r'https://[-?/_=.\w]+'):
    f=open(file,'r')
    text=f.read()
    if re.search(pattern, text):
        return re.search(pattern,text)
    else:
        return ""

for folder, subfolders, files in os.walk(folders):
    for f in files:
        full_path=folder+'/'+f
        findings=search(full_path)
        urls.append(findings)

print(urls)

##print("test_phrase_two is ", re.search(pattern,test_phrase_two))

#creates a list of the file contents that may contain the desired information
#for folder, subfolders, files in os.walk(folders):
#        for f in files:
#            a=open(f,'rb')
#            urls+=a.read()
#            a.close()

#print(urls)
