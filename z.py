import os
import fnmatch

def existingFileCount(path, pattern):
    count = len(fnmatch.filter(os.listdir(dir_path), pattern))
    print('File Count:', count)
    return count

def createFiles(counter):
    for i in range(counter+1, counter+10+1):
        file_name=str(i)+"test.txt"
        file=open(file_name, 'w')
    print("files created")

if __name__ == "__main__":
    dir_path = r'D:\code\pythonvarsha'
    pat = "*.txt"
    count = existingFileCount(dir_path, pat)
    createFiles(count)