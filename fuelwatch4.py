from feedparser import parse #if you want top import certain functions from libraries.  Also available to type 'parse' instead of feedparser.parse
from requests import get
from pprint import pprint #instead of the below line 14 
from time import sleep
from json import dumps
rtod = get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=6&Suburb=Balcatta&Surrounds=yes&Day=today') #gets data and saves to r.text
rtom = get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=6&Suburb=Balcatta&Surrounds=yes&Day=tomorrow') #gets data and saves to r.text
tod = parse(rtod.text) #parses raw data to tagged format
tom = parse(rtom.text) #parses raw data to tagged format
klist = []
klistSorted = []

i = 0
while i < len(tod['entries']): 
	klist.append({'price':tod['entries'][i]['price'],'brand':tod['entries'][i]['brand'],'location': tod['entries'][i]['location'], 'day':'today'})
	klist.append({'price':tom['entries'][i]['price'],'brand':tom['entries'][i]['brand'],'location': tom['entries'][i]['location'], 'day':'tomorrow'})
	i+=1

def mysort(klist):
	return klist['price']

klistSorted = sorted(klist, key=mysort)
"""
i = 0
while i < len(tod['entries']):
	klist.append(tod['entries'][i]['price'])
	klist.append(tod['entries'][i]['brand'])
	klist.append(tod['entries'][i]['location'])
	i+=1

print('Fuel prices for today:')
"""
print(klistSorted)
#pprint(klist,indent =2, width = 100)
print(dumps(klistSorted, indent=2))

len(klistSorted)
newlist=[]
i=0
while i < len(klistSorted):
	newlist.append(klistSorted[i]['price'])
	newlist.append(klistSorted[i]['brand'])
	newlist.append(klistSorted[i]['location'])
	newlist.append(klistSorted[i]['day'])
	i+=1
i=0
file = open('something2.html', 'w')
file.write(<table>)
    file.write('''<tbody>
        <tr>
            <td>'Price'</td>
            <td>'Brand'</td>
            <td>'Suburb'</td>
            <td>'Day'</td>
        </tr>
  		<tr>
  			<td>{}</td>
  			<td>{}</td>
  			<td>{}</td>
  			<td>{}</td>
  		</tr>
  		</tbody>
    </table>'''.format(newlist[0],newlist[1],newlist[2],newlist[3])
file.close()    

sleep(60)