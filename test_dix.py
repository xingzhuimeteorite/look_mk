
# aa = {'aa':'ccccc'}

# print(aa.keys())
# print(aa.keys()) 

import re 

aa = 'aaaaacddddd'
#tail = 'dddd$' 
head = 'a'


while(1):
    try :
        begin = re.search(head,aa).end()
        print(begin)
        last_begin = 
        aa = aa[begin:]
    except :
        print()
print(begin)
# end = re.search(tail,aa).start()

# import re

# print(aa[begin:end])
# import time 
# print(time.strftime('%Y-%m-%d')) 
