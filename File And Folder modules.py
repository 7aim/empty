import os 

#print(os.getcwd()) #shows file's path

#print(os.listdir()) #shows the contents of the current file
#print(os.listdir(r"C:\Users")) #shows the contents of the any file

#os.chdir(r"C:\Users") #change current listdir argument
#print(os.listdir())

#os.mkdir(r"C:\Users\aim7l\OneDrive\Masaüstü\aim17\Folder1") #create folder in argumentpath
#os.rmdir(r"C:\Users\aim7l\OneDrive\Masaüstü\aim17\Folder1") #delete folder in argumentpath
#os.rename("Folder1","Folder2") #renames the folder/file? name

os.O_RDONLY #read only
os.O_WRONLY #write only
os.O_RDWR #read and write
os.O_CREAT #create file

#file1 = os.open("File1",os.O_RDWR|os.O_CREAT)

#os.write(file1,"Selam,Aim".encode())
#os.lseek(file1, 0, os.SEEK_SET) #changes the cursor's position 

#stats = os.stat(file1) #shows stats
#text_size = stats.st_size #shows text size in stats

#print(os.read(file1,text_size).decode())

#os.close(file1)

#os.remove("File1")