import csv

data_dic={}
mon_list=['January','Febuary','March','April', 'May', 'June' ,'July', 'August', 'September' ,'October','November','December']
cr = csv.reader(open("2013_Source.csv","r"))

wtr= csv.writer(open("C:/Users/AjaySivaSantoshReddy/Desktop/result.csv","wb"))
#wtr.writerow(['a','b'])
    

for r in cr:
    val=''
    s=str(r[2])
    mon=''
    if(s[0:2]=='01'):
        mon='January'
    if(s[0:2]=='02'):
        mon='Febuary'
    if(s[0:2]=='03'):
        mon='March'
    if(s[0:2]=='04'):
        mon='April'
    if(s[0:2]=='05'):
        mon='May'
    if(s[0:2]=='06'):
        mon='June'
    if(s[0:2]=='07'):
        mon='July'
    if(s[0:2]=='08'):
        mon='August'
    if(s[0:2]=='09'):
        mon='September'
    if(s[0:2]=='10'):
        mon='October'
    if(s[0:2]=='11'):
        mon='November'
    if(s[0:2]=='12'):
        mon='December'
    val=str(mon+","+r[4]+","+r[5]+","+r[7]+","+r[8]+","+r[23])
    if (r[4]!="" and r[5] != "" and r[5] != " Queens and Brooklyn" and r[7] != "" and r[8] != "" and r[23] != ""):
        if mon in data_dic.keys():
            data_dic[mon].append(val)
        else:
            data_dic[mon]=[val]
    
print("Insert Successful")

wtr.writerow(["Month", "Department", "Complaint Type" ,"Location Type","Zipcode" ,"Borough"])
for month in mon_list:
    global r2
    r2=1000
    i = 0
    while i < r2:
        val1=data_dic[month][i]
        i=i+1
        val2=val1.split(',')
        if(" Queens and Brooklyn" in val2):
            r2=r2+1
            continue
        wtr.writerow(val2)