import os
# to rename extensions
MEDIA_PATH = os.getcwd()
extension = {'test'}
count = 0
for root, dirs, files in os.walk(MEDIA_PATH):
    for i in files:
        a = (i[-3::])  # replace -3 with -4 incase of html
        if(a == 'txt'):
            count += 1
            dst = i[0:3]+'.txt'  # replace txt with something
            os.rename(root+'/'+i, root+'/'+dst)
            extension.add(a)


print(count)
print(extension)

# use this for removing srt files
# find . -name \*.srt -type f -delete

# FOR FOLDERS

for root, dirs, files in os.walk(MEDIA_PATH):
    for dir in dirs:
        a = (dir[0:2])  # replace -3 with -4 incase of html
        print(a)
        os.rename(root+'/'+dir, root+'/'+a)


# FINAL RENAMING SOLN
# no need to use for dir in dirs:
top = ''
for root, dirs, files in os.walk(MEDIA_PATH):
    for i in files:
        filename, file_extension = os.path.splitext(root+'/'+i)
        for j in i:
            if j == '.':
                break
            top += j
        if len(top) == 1:
            top = (str(top).zfill(2))
        answer = top+file_extension
        os.rename(root+'/'+i, root+'/'+answer)
        top = ''
