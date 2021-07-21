
import time 
class data():
    def __init__(self):
        self.total_count = self.get_count()

    def get_count(self):
        
        try:
            with open('data/{}_data_count.txt'.format(time.strftime('%Y-%m-%d')),'r') as d:
                c = d.read()
        except :
            with open('data/{}_data_count.txt'.format(time.strftime('%Y-%m-%d')),'a') as d:
                c=''
        if c == '':
            c=0
        self.total_count=int(c)
        return self.total_count
    
    def set_count(self,value):
        self.total_count = value
        with open('data/{}_data_count.txt'.format(time.strftime('%Y-%m-%d')),'w') as d:
            d.write(str(self.total_count))
    
    def add_count(self,value):
        self.total_count = self.get_count() + value 
        self.set_count(self.total_count)

if __name__ == '__main__':
    cc = data()
    a = cc.get_count()
    print(a)


    
