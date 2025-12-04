#NOTE:  FilePointer.tell()-->Gives Present Index of file pointer
#Note: FilePointer.seek(Index)-->Will re-set the File Pointer to the Index in File

"""Guido Van Rossum
is the Author of Python
Developed in Nether lands
Python is an oop lang
and  also object oriented programming Lang
and It is used in Many Apps Devlopment
KVR is the Faculty for Python"""

with open("D:\\Python\\Notes\\KVR Notes-01\\FILES\\notes\\python.info","r") as fp:
    print("Initially, Pos of fp =", fp.tell())  # Initially, Pos of fp= 0
    filedata = fp.read(5)
    print("File Data=", filedata)  # File Data= Guido
    filedata = fp.read(5)
    print("File Data=", filedata)  #
    print("Now, Pos of fp=", fp.tell())  #
    filedata = fp.read(6)
    print("File Data=", filedata)  #
    print("Now, Pos of fp=", fp.tell())