#Finding of day using date
print("The date format should be date-month-year ex (12-02-2022)")
mcd={1:0, 2:3, 3:3, 4:6, 5:1, 6:4, 7:6, 8:2, 9:5, 10:0, 11:3, 12:5}
def ycd(year):
	if year<1600:
		yc=0
	elif year>=1600 and year<1700:
		yc=6
	elif year>=1700 and year<1800:
		yc=4
	elif year>=1800 and year<1900:
		yc=2
	elif year>=1900 and year<2000:
		yc=0
	elif year>=2000 and year<2100:
		yc=6
	elif year>=2100 and year<2200:
		yc=4
	return yc
def leap_years(gap,year):
	leaps=[]
	for i in range(gap,year+1):
		if i%400==0 and i%100==0:
			leaps.append(i)
		elif i%4==0 and i%100!=0:
			leaps.append(i)
			lc=len(leaps)
	return (leaps,lc)
try:
	date=input("Enter date : ").split("-")
	if len(date)<3 :
		print("Incorrect Format!\nPlease enter the correct format")
		exit(0)
	nayc=int(date[2][2:])
	year=int(date[2])
	dt=int(date[0])
	mt=int(date[1])
	gap=year-nayc
	leap=leap_years(gap,year)
	lc=leap[1]
	feb_28=bool(year not in leap[0] and mt==2 and dt>28)
	month_31=bool(mt in [1,3,5,7,8,12] and dt>31)
	month_30=bool(mt in [4,6,9,11] and dt>30)
	leap_feb_29=bool(mt==2 and dt>29 or year<1500)
	if feb_28 or month_31 or month_30 or mt>12 or year>2200 or leap_feb_29:
		raise ValueError("Enter the correct date")
except ValueError as e:
	print("The date is not in the restricted range\n",e,sep="")
	exit(0)
x=ycd(year)
mc=0
for j in mcd:
    if int(mt)==j:
        mc=mcd[j]
        break
day=(int(dt)+mc+x+nayc+lc)%7
if year in leap[0] and mt in (2,1):
	if day==0:
		day=2
	day=day-1
if year<2000:
	if day>5:
		day=0
	else:
		day+=1
if year>2100:
	day+=1
sday={1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thrusday',6:'Friday',0:'Saturday'}
for i in sday:
	if i==day:
		print("The day is ->",sday[i])
		break
