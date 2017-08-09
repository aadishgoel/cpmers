from bs4 import BeautifulSoup 
#from datetime import datetime as dt
import requests
#import re
import urllib.request

"""  ^ codechef """  

site = 'https://www.codechef.com'
tab = '/contests'

ccpresent = []
ccfuture = []

scrap = requests.get(site+tab)
soup = BeautifulSoup(scrap.text,'html.parser')

ptable, ftable, trash = soup.findAll('table',{'class':'dataTable'})

def cccollect(raw,result):
    try:
        for tr in raw.tbody.findAll('tr'):
            temp = tr.findAll('td')
            code = temp[0].string
            link = '/'+code
            name = temp[1].a.string
            dstart = ' '.join(temp[2].stripped_strings)
            dend = ' '.join(temp[3].stripped_strings)
            dstart_in_no = temp[2]['data-starttime']
            dend_in_no = temp[3]['data-endtime']
            result.append({'code':code,'link':link,'name':name,'dstart':dstart,'dend':dend,'dstart_in_no':dstart_in_no,'dend_in_no':dend_in_no})
    except Exception as e:
        print(e)
        pass

cccollect(ptable,ccpresent)
cccollect(ftable,ccfuture)

print('*****    Codechef    ******') 
print('Live:')
for row in ccpresent:
    print(row['dstart'],row['name'])
print('Upcoming:')
for row in ccfuture:
    print(row['dstart'],row['name'])
    



"""  codechef $  """


"""  ^ codeforces """

site = 'http://codeforces.com'
tab = '/contests'

scrap = requests.get(site+tab)
soup = BeautifulSoup(scrap.text,'html.parser')

cfcontests=[]

for tr in soup.find('div',{'class':'datatable'}).table.findAll('tr')[1:]:
    temp = tr.findAll('td')
    name = temp[0].string.strip()
    date = ' '.join(temp[2].a.stripped_strings)
    tlink = temp[2].a['href']
    length = temp[3].string.strip()
    stime = ' '.join(temp[4].stripped_strings)
    rtime = ' '.join(temp[5].stripped_strings)
    cfcontests.append({'name':name, 'date':date, 'tlink':tlink, 'length':length, 'stime':stime, 'rtime':rtime })


print('  Codeforces ***** ')
for row in cfcontests:
    print(row['name'],row['rtime'],row['stime'])


"""  codeforces $ """

""" ^ atcoder """

site = 'https://atcoder.jp'
tab = '/contest'

atpresent = []
atfuture = []
#print(site+tab)
#scrap = requests.get(site+tab)
#soup = BeautifulSoup(scrap.text,'html.parser')

scrap  = urllib.request.urlopen(site+tab)
soup = BeautifulSoup(scrap.read(),'html.parser')

tables = soup.find_all('div',{'class':'table-responsive'})
ptable, ftable = tables[0].table,tables[1].table

def atcollect(raw,result):
    try:
        for tr in raw.tbody.findAll('tr',recursive=False):
            temp = tr.findAll('td')
            tlink = temp[0].a['href']
            date = temp[0].a.string
            name = temp[1].a.string
            link = temp[1].a['href']
            length = temp[2].string                              # Can be ∞ for infinitely long
            result.append({'tlink':tlink,'date':date,'name':name,'link':link,'length':length})
    except Exception as e:
        print(e)
        pass

atcollect(ptable,atpresent)
atcollect(ftable,atfuture)

print('******   Atcoder   ******* ')
print('Live: ')
for row in atpresent:
    print(row['date'],row['name'])
print('Upcoming: ')
for row in atfuture:
    print(row['date'],row['name'])


""" atcoder $ """

