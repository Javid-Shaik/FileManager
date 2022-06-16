import re,os
from fpdf import FPDF
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
	if len(folder)==0:
		print("folder is empty!")
	else:
		i=0
		for file in folder:
			i+=1
			print(str(i)+".",file)
	return folder
def make_changes(fn):
	path=os.getcwd()
	print(path[0:19])
	print("Current path : ",path)
	print("Current file name : ",os.path.basename(fn))
	print("To change the directroy enter (C)\nTo make a folder enter (M)")
	ch_1=input("Enter your choice : ").lower()
	if ch_1=="c":
		dir=input("Enter the changing path : ")
		os.chdir(path[0:19]+dir)
	elif ch_1=="m":
		folder=input("Enter folder name : ")
		os.makedirs(folder)
	else:
		return None
def insert(fn):
	f1=open(fn,"w+")
	print("Enter the text you want to insert")
	x=data()
	f1.write(x)
	f1.close()
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
		return
		f1.close()
	#lnum = map(int,input("Enter the line nums seperated with comma (,) you want to read : ").split(","))
	for line in lines:
		tc+=1
		if tc in ln:
			print(tc,".  ",line,sep="")
	f1.close()
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
	pdf.set_font("Times","B" ,size = 17)
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
def help1():
	"""Handling with files
	Give the file name as below example.
	file_name.extension\n
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
	--> 2 Line manipulation [update/add]
	------------------------------------
	To update a specific line enter (update) or to add enter (add)
	Then enter the line number you want to manipulate.\n
	After that enter data like in above example.\n
	--> 3 Display
	-------------
	To display the file content enter -> (3)\n
	--> 4 Delete Line(s)
	-------------------
	To delete one line enter that line number.\n
	To delete multiple lines.
	Enter the line number(s) seperated with comma (,) to delete.
	If you want to undo the deletion enter (Y/N).\n
	--> 5 Delete File
	---------------
	To delete a file enter the file name.\n
	-->6 Append 
	-------------
	To add the text at the end of the file enter (6).\n
	--> 7 Help & Information
	-------------------------
	To get help and information enter (7).\n
	--> 8 Open or Create another file
	--------------    --------------
	To open or create an another file enter (8).\n
	--> 9 PDF CREATION
	--------------------
	To convert the text file into pdf enter (9).\n
	--> 0 EXIT 
	------------
	To exit from the program enter (0).\n
	--> 11 List of files
	----------------
	To know the list of files in current folder enter (11).\n
	--> 12 Make Changes
	----------------
	To change the current directory or to create a folder enter (12).\n
	"""
	return None
def menu():
	print("\t\t\tMenu\n>> 1.Insert  2.(Update/Add) 3.Display  4.Delete lines\n\n>> 5.Delete File  6.Append  7.Help  8.Another File\n\n>> 9.Create Pdf 10.Menu 11.List of Files \n\n>>12.Make Changes 13.Word_Search 0.Exit\n")
def main():
	menu()
	fn=input("Enter file name : ")
	folder = os.listdir(".")
	if len(fn[len(fn)-4:])!=4:
		fn=fn+".txt"
	else:
		fn=fn
	if len(fn)<1:
		print("Enter valid file name!")
		return None
	while True :
		ch=int(input("Enter your choice : "))
		if fn not in folder and ch!=1 and ch!=8:
			print("There is no file with %s name.\nPlease enter valid filename..." %fn)
			break
		folder.append(fn)
		if ch ==10:
			menu()
		if ch==1:
			insert(fn)
		elif ch==2:
			print("To update a line enter (update)\nTo add a line before a specific line enter (add)")
			ch_=input("Enter your choice (update/add) : ").lower()
			if ch_ not in ('add','update'):
				raise ValueError
			ln=int(input(f"Enter the line number to {ch_} : "))
			update(fn,ln,ch_)
		elif ch==3:
			display(fn)
		elif ch==4:
			ln=tuple(map(int,input("Enter line number(s) seperated with comma to delete : ").split(",")))
			del_lines=Delete(fn,*ln)
			undo=input("If you want undo the deletion enter (Y/N) : ")
			if undo.lower()=="y":
				undone(fn,del_lines)
		elif ch==5:
			fn1=input("Enter the file name you want to delete : ")
			os.remove(fn1)
			print("File is delted !")
		elif ch==7:
			print(help1.__doc__)
			file_info(fn)
		elif ch==6:
			print("Enter the data to append")
			apend(fn)
		elif ch==9:
			pdfname=input("Enter the pdf name you want to create : ")
			fun(fn,pdfname)
		elif ch==8:
			cfn=input("Enter the new file name : ")
			if len(cfn[len(cfn)-4:])!=4:
				fn=cfn+".txt"
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
			make_changes(fn)
try:
	if __name__ =='__main__':
		files_list()
		print("Please first provide the file name you want to handle")
		print("To get help and information. Enter 7\n")
		main()
except FileNotFoundError as e:
	print(e,"\nFile not found!")
except ValueError as e:
	print("Please enter valid input")
except :
	print("Error occurred!")
