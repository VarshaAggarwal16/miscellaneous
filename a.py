import os
import fnmatch

dir_path = r'D:\code\pythonvarsha'
count = len(fnmatch.filter(os.listdir(dir_path), "*.txt"))
print('File Count:', count)

for i in range(count+1, count+10+1):
    file_name=str(i)+"test.txt"
    file=open(file_name, 'w')
    print("files created")