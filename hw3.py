
import psycopg2
import sys

with open('password.txt') as f:
    lines = [line.rstrip() for line in f]
username = lines[0]
pg_password = lines[1]
f.close()
conn = psycopg2.connect(database="COSC3380",
                        user=username, password=pg_password)
cursor = conn.cursor()

inString = sys.argv[1]
#instring = trans.txt
input_= inString.split("=")
input_name=input_[1]
fp = open(input_name, 'r')
line = fp.readline()

dt=[]
while line:
    line=fp.readline()

    tup=line.split(",")

    if tup[-1].find("\n") != -1:
        tup[-1] = tup[-1].strip("\r\n)")
    dt.append(tup)

dt.pop()
class Info():
    def __init__(self, name, id):
        self.passenger_name=name
        self.passenger_id=id

class Node():
    def __init__(self,data,next=None,previous=None):
        self.data=data
        self.next=next
        self.previous=previous
class Queue:
    def __init__(self):
        self.top = Node(None)
        self.last=self.top
    def add(self,item):
        self.last.next=item #adjust the link of the last item
        self.last=item #point this item to the last
    def remove(self):
        topItem=self.top
        self.top=topItem.next #arrange the link of top
        return topItem #return top
queue=Queue()
dt=[['8559460462', '1001'], ['7339561341', '1005'],['fgfg', '1fdg5'],['fgf61341', 'ooooo']]

b=Node(Info(dt[0][0],dt[0][1]))


for i, record in enumerate(dt):
    item=Node(Info(record[0],record[1]))
    queue.add(item)
