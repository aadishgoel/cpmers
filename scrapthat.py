from bs4 import BeautifulSoup 
from datetime import datetime as dt
import requests
import re
import urllib.request

print(""" codeforces """)

data=[]
limit=5

site = 'http://codeforces.com'
tab = '/submissions/'
#users = ['tourist', 'mmaxio', 'Petr', 'Slamur', 'uwi', 'I_love_Tanya_Romanova', 'AlexDmitriev', 'RomaWhite', 'akashd', 'anta', 'Um_nik', 'W4yneb0t', 'FatalEagle', 'Radewoosh', 'rajat1603', 'Sumeet.Varma']
users = ['pulkitkapoor15', 'amand26', 'Qvod', 'vinay29', 'kuldeepsharma1312', 'ayushjainpnp', 'pulkit.kapoor', 'zlover', 'dbhrockzz']
#users = ['zlover','dbhrockzz','pulkit.kapoor','vinay29']
#users = ['zlover']
for user in users:
    try:    
        scrap = requests.get(site+tab+user)
        soup = BeautifulSoup(scrap.text,'html.parser')

        for tr in soup.find('table',{'class':'status-frame-datatable'}).findAll('tr')[1:limit+1]:
            date = tr.find('td',{'class':'status-small'}).string.strip()
            lang = tr.find('td',class_=None).string.strip()
            status = ' '.join(tr.find('td',{'class':'status-cell'}).stripped_strings)
            ques = tr.find('td',{'data-problemid':re.compile("^\d*$") }).a.string.strip()    
            qlink = tr.find('td',{'data-problemid':re.compile("^\d*$") }).a['href']
            link = tr.find('td',{'class':'id-cell'}).a['href']
            data.append({'user':user,'ques':ques,'status':status,'date':date,'lang':lang,'qlink':qlink,'link':link})
    except:
        print('Something Fishy with '+user)
        continue
def cfDateSorter(record):
        date = record['date']
        date, time = date.split()
        year, month, date = date.split('-')
        second, minute, hour = time.split(':')
        return year,month,date,hour,minute,second
    
data.sort(key=cfDateSorter ,reverse=True)

for box in data:
    print(box['date'].split()[0],site+box['qlink'],box['user'],box['status'])
    
""" codeforces """

print(""" codechef """) 

data = []
limit = 10
site = 'https://www.codechef.com'
url = 'https://www.codechef.com/submissions?sort_by=All&sorting_order=asc&language=All&status=All&year=2017&handle=__user__&pcode=&ccode=&Submit=GO'
#users = ['rajat1603', 'gennady.korotkevich', 'anushi', 'uwi', 'mmaxio', 'anushi5']
users = ['pulkit_hr', 'dbhrockzz1', 'zlover', 'mittal_tanisha', 'vinay2991997', 'navkrishna21']

for user in users:
    try:
        scrap = requests.get(url.replace('__user__',user))
        soup = BeautifulSoup(scrap.text, 'html.parser')
        
        for tr in soup.find('table',{'class':'dataTable'}).tbody.findAll('tr')[:limit]:
            date = tr.find('td',{'width':130}).string
            temp = tr.findAll('td',{'width':110})
            ques = temp[0].string
            qlink = temp[0].a['href']
            contest = temp[1].string
            clink = temp[1].a['href']
            lang = tr.find('td',{'width':109}).string
            temp = tr.find('td',{'width':75}).a.attrs
            link = temp['href'] if 'href' in temp else None
            temp = tr.find('td',{'width':71}).span
            status=''.join(temp.stripped_strings) if temp['title']=='' else temp['title']
            data.append({'user':user,'date':date,'ques':ques,'qlink':qlink,'contest':contest,'clink':clink,'lang':lang,'link':link,'status':status})
    except:
        print('Something Fishy with '+user)
        continue

def ccDateSorter(record):
    time, ampm, date=record['date'].split()
    if date =='ago':
        now=dt.now()
        return now.year,now.month,now.day,now.hour-int(time),now.minute   
    date, month, year = map(int,date.split('/'))
    hour, minute = map(int,time.split(':'))
    if ampm=='PM' and hour<12:
        hour+=12
    return year,month,date,hour,minute

data.sort(key=ccDateSorter, reverse=True)

    
for row in data:
        print(row['date'],row['ques'],row['user'])


























""" codechef """
