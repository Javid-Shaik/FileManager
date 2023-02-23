import re,os,time,shutil, PyPDF2
from fpdf import FPDF
from tqdm import tqdm

def data():
	lines=[]
	while True:
		line=input(">>")
		if line:
			lines.append(line)
		else:
			break
	text="\n".join(lines)+"\n"
	return text

def files_list():
	print("\n\t\tList of files in the current folder")
	folder=os.listdir(".")
	folder.sort()
	n = len(folder)
	if n==0:
		print("folder is empty!")
	else:
		i=0
		for file in folder:
			i+=1
			print(str(i)+".",file)
	return folder

def make_changes(fn):
	path=os.getcwd()
	print("Current path : ",path)
	print("Current file name : ",os.path.basename(fn))
	dir =input("Enter the path preceeding with cd : ").lower()
	if dir[0]=="c":
		if dir[3]!=".":
			os.chdir("".join(dir[3:]))
		else :
			p="".join(path[:path.rfind("/")])
			print(p)
			os.chdir(p)
	elif dir[0]=="m":
		os.makedirs("".join(dir[5:]))
	else:
		return None

def insert(fn):
	f1=open(fn,"w+")
	print("Enter the text you want to insert")
	x=data()
	f1.write(x)
	f1.close()
	return None

def display(fn):
	f1=open(fn,"r")
	lines=f1.readlines()
	if len(lines)==0:
		print("The file is empty!\n")
	else:
		l_num=0
		for line in lines:
			l_num+=1
			print(str(l_num)+". "+line.replace("\n",""))
	f1.close()
	return None

def update(fn,lnum,ch_):
	f1=open(fn,"r+")
	lines=f1.readlines()
	f1.seek(0)
	if len(lines)!=0:
		print("Enter updating data")
		dataa=data()
		ln=-1
		for line in lines:
			ln+=1
			if lnum==ln+1:
				if ch_.lower()=="update":
					del lines[ln]
				lines.insert(ln,dataa)
				break
		text="".join(lines)
		f1.write(text)
		f1.close()
	else:
		print("File is Empty!\n")

def Delete(fn,*ln):
	f1=open(fn,"r+")
	lines=f1.readlines()
	f1.close()
	f1=open(fn,"w+")
	lnum=0
	del_lines={}
	for i in lines:
		lnum+=1
		if lnum not in ln:
			f1.write(i)
		else:
			del_lines.update({lnum:i})
	f1.close()
	return del_lines

def undone(fn, del_lines):
	f1=open(fn,"r+")
	lines=f1.readlines()
	for ln in range(max(del_lines.keys())):
		ln+=1
		for key in del_lines.keys():
			if ln==key:
				lines.insert(key-1,del_lines[key])
	f1.seek(0)
	f1.writelines(lines)
	f1.close()

def Search(fn):
	count = lc = tc = 0
	ln =[]
	word = input("Enter the word you want to search : ").strip()
	f1 = open(fn,'r')
	lines = f1.readlines()
	for line in lines:
		lc+=1
		x = re.search(word, line.casefold())
		if x :
			count+=1
			ln.append(lc)
	print("The lines in which the word %s appears is : " %word,ln)
	print("The word %s appears %d times" %(word, count))
	if len(ln) ==0:
		return
	ch = input("If you want to read the lines of the word you have searched enter (y/n) : ")
	if ch=='n':
		f1.close()
		return
	#lnum = list(map(int,input("Enter the line nums seperated with comma (,) you want to read : ").split(",")))
	for line in lines:
		tc+=1
		if tc in ln:
			print(tc,".  ",line,sep="")
	f1.close()
	return tc

def apend(fn):
	f1=open(fn,"a")
	txt=data()
	f1.write(txt)
	f1.close()

def file_info(fn):
	folder = os.listdir(".")
	if fn not in folder:
		print("There is no file with %s name " %fn)
		return
	f1=open(fn,"r")
	lines=f1.readlines()
	print("Lines :",len(lines))
	wc=cc=0
	for i in lines:
		y=i.strip('\n')
		y=re.sub("[^\w]" ,"",y)
		cc+=len(y)
		i=i.split()
		x=len(i)
		wc+=x
	print("words =",wc)
	print("characters =",cc)

def fun(fname,pdfname):
	pdf= FPDF('P',"mm",'A4')
	pdf.add_page() 
	pdf.set_font("Times","B" ,size = 15)
	pdf.set_margins(15,15,15)
	pdf.set_text_color(0,0,255)
	f = open(fname, "r")
	for x in f:
		for y in x:
			if ord(y)>256:
				x=x.replace(y,"")
		w=pdf.get_string_width(x)
		pdf.multi_cell(175,10,txt = x,border=0,fill=0,align = 'L') 
	pdf.output(pdfname+".pdf")
	print("Your pdf is ready check the folder")

def desire(fn):
	f1 = open(fn,"r+")
	lines= f1.readlines()
	wish = "yes"
	if len(lines) ==0:
		print("Sorry the file is Empty")
		return None
	low , high = map(int,input("Enter the range seperated with (,) : ").split(","))
	while True:
		if wish !="yes":
			return None
		if low>len(lines):
		    return None
		if low and high:
			ln=0
			for line in lines :
				ln+=1
				if ln >= int(low) and ln<=high:
					time.sleep(1.25)
					print(str(ln)+".  "+line)
		wish = input("Do you wish to continue (yes/no) : ").lower()
		low = high
		high +=10

def merge_files(fileNames):
    new = input("Enter the new file name : ")
    mix = open(new,'w+')
    for fn in fileNames:
        file = open(fn,'r+')
        lines=file.readlines()
        mix.writelines(lines)
        file.close()
    mix.close()
    return mix

def copyFile(fn):
	cfn = input("Enter the file name you want to make the copy : ")
	shutil.copyfile(fn,cfn)
	return cfn

def DeleteFiles(fileNames,folder):
	for del_fn in fileNames:
		if del_fn not in folder:
			print("File _",del_fn,"_ does not Exists!")
			continue
		print("File _",del_fn,"_ has been Deleted!")
		dch = input("If you want to Undo the Deletion Enter (Y/N) : ").lower()
		if dch == 'y':
			print("File _",del_fn,"_ has been Recovered")
		else :
			os.remove(del_fn)
			folder.remove(del_fn)
	return folder

def extractText(folder):
	pdf = input("Enter PDF File name : ")
	#txt = input("Enter the text file name to store : ")
	pdf_file = open(pdf+".pdf", "rb")
	pdf_reader = PyPDF2.PdfReader(pdf_file)
	n = len(pdf_reader.pages)
	text = ""
	for page in tqdm(range(n)):
		text += pdf_reader.pages[page].extract_text()
	text_file = open(pdf+".txt", "w")
	text_file.write(text)
	text_file.close()
	pdf_file.close()
	folder.append(pdf+".txt")
	print("Text Extracted Successfully!\nFile has been created. Check in the folder by entering 11")

def help1():
	"""Handling with files
	Give the file name as below example.
	file_name.extension\n
	_________________
	--> 1. Insert
	---------------
	This method can be used to create a new file.\n
	If the file is already exists it will erase the data in the file.\n
	To give the input text refer the below example.\n
	To stop giving the input text just press enter key without text\n
	---------------
	input example     
	________ 
	abc <enter key> 
	efg <enter key>
	| <enter key>    
	---------------
	output example  
	________ 
	abc
	efg
	---------------\n
	NOTE : Give the input text as in the above example.
	Whenever you are giving the input text.\n
	_________________
	--> 2 Line manipulation [update/add]
	To update a specific line enter (update) or to add enter (add)
	Then enter the line number you want to manipulate.\n
	After that enter data like in above example.\n
	_________________
	--> 3 Display
	To display the file content enter -> (3)\n
	_________________
	--> 4 Delete Line(s)
	To delete one line enter that line number.\n
	To delete multiple lines.
	Enter the line number(s) seperated with comma (,) to delete.
	If you want to undo the deletion enter (Y/N).\n
	_________________
	--> 5 Delete File(s)
	To delete file(s) enter the file name(s) seperated with space.\n
	_________________
	--> 6 Append 
	To add the text at the end of the file enter (6).\n
	_________________
	--> 7 Help & Information
	To get help and information enter (7).\n
	_________________
	--> 8 Open or Create another file
	To open or create an another file enter (8).\n
	_________________
	--> 9 PDF CREATION
	To convert the text file into pdf enter (9).\n
	_________________
	--> 0 EXIT 
	To exit from the program enter (0).\n
	_________________
	--> 11 List of files
	To know the list of files in current folder enter (11).\n
	_________________
	--> 12 Make Changes
	To change the current directory or to create a folder enter (12).\n
	To change the directory enter the path preceeding with cd Ex: cd /changing/path
	To create a directory enter the directory preceeding with mkdir Ex : mkdir /directory
	_________________
	--> 13 Word Search
	To search a word in the present text file enter 13 and then enter the word.
	_________________
	--> 14 Readlines
	This function allows you to read the lines in a certain range.
	_________________
	--> 15 Rename File
	To rename file this function can be used.
	_________________
	--> 16 Merge Files
	This function will create a new text file by appending the text from the multiple files.
	_________________
	--> 17 Copy Files
	To copy the contents form a file to another file this function can be used.
	_________________
	--> 18 Extract Pdf
	This function will extract the text from the pdf and creats a text file.
	_________________
	"""
	return None

def menu():
	print("""\t\t\tMenu\n>> 1.Insert  2.(Update/Add) 3.Display  4.Delete lines
	\n\n>> 5.Delete File(s)  6.Append  7.Help  8.Another File
	\n\n>> 9.Create Pdf  10.Menu  11.List of Files
	\n\n>> 12.Changes Directory  13.Word_Search  14.Readlines
	\n\n>> 15.Rename File  16.Merge Files  17.Copy Files 
	\n\n>> 18.Extract Pdf  0.Exit\n""")

def main():
	menu()
	global fn
	fn=input("Enter file name : ")
	folder = os.listdir(".")
	if len(fn)<1:
	    print("You must provide a valid file name")
	    return
	while True :
		ch = int(input("Enter your choice : "))
		if ch ==10:
			menu()
		if ch==1:
			insert(fn)
			folder.append(fn)
		elif ch==2:
			if fn in folder:
				f1 = open(fn,'r')
				lines = len(f1.readlines())
				print("To update a line enter (update)\nTo add a line before a specific line enter (add)")
				ch_=input("Enter your choice (update/add) : ").lower()
				if ch_ not in ('add','update'):
					raise ValueError
				ln=int(input(f"Enter the line number to {ch_} : "))
				if ln>lines:
					print("Line number exceeded!")
				else:
					update(fn,ln,ch_)
			else :
				print("No such file or directory!")
		elif ch==3:
			try :
				display(fn)
			except Exception as e:
				print(e,"File Not Found!")
				continue
		elif ch==4:
			if fn not in folder:
				print("No such File or Directory!")
				continue
			ln=tuple(map(int,input("Enter line number(s) seperated with comma to delete : ").split(",")))
			del_lines=Delete(fn,*ln)
			undo=input("If you want undo the deletion enter (Y/N) : ")
			if undo.lower()=="y":
				undone(fn,del_lines)
		elif ch==5:
			fileNames = map(str,input("Enter file name(s) seperated with space: ").split())
			folder = DeleteFiles(fileNames,folder)
		elif ch==7:
			print(help1.__doc__)
			try:
				file_info(fn)
			except Exception as e:
				print(e)
				continue
		elif ch==6:
			print("Enter the data to append")
			apend(fn)
		elif ch==9:
			pdfname=input("Enter the pdf name you want to create : ")
			fun(fn,pdfname)
		elif ch==8:
			cfn=input("Enter the new file name : ")
			if len(cfn[len(cfn)-4:])!=4:
				fn=cfn
			else:
				fn=cfn
		elif ch==0:
			print("You are out of the program")
			break
		elif ch==11:
			files_list()
		elif ch==13:
			Search(fn)
		elif ch==12:
			try :
				make_changes(fn)
			except Exception as e:
				print(e)
				continue
		elif ch==14:
			desire(fn)
		elif ch==15:
			print("Current File Name is : ",os.path.basename(fn))
			new_fn = input("New file Name : ")
			if new_fn==fn:
			    print("Renamed successfully")
			    continue
			if new_fn in folder:
			    print("The file",new_fn,"is already exists.\nDot you still want to Rename?")
			    rch = input("Enter (Y/N) : ").lower()
			    if rch=="n":
			        continue
			os.rename(fn,new_fn)
			print("Renamed sucessfully")
			folder.remove(fn)
			fn = new_fn
			folder.append(fn)
		elif ch==16:
		    fileNames= input("Enter file names seperated with space : ").split()
		    merge_files(fileNames)
		    print("Files merged sucessfully! Check in the folder")
		elif ch==17:
			cfn = copyFile(fn)
			print("Copied content into",cfn,"successfully!")
		elif ch==18:
			extractText(folder)
	return ch

try:
	if __name__ =='__main__':
		files_list()
		print("\n    Please first provide the file name you want to handle")
		print("\n\tTo get help and information. Enter 7\n")
		main()
except FileNotFoundError as e:
	print(e,"\nFile not found!")
except ValueError as e:
	print("Please enter valid input")
except :
	print("Error occurred!")
