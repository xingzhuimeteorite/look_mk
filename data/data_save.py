

class data():
    def __init__(self):
        self.total_count = self.get_count()

    def get_count(self):
        with open('data/data_count.txt','r') as d:
            c = d.read()
        if c == '':
            c=0
        self.total_count=int(c)
        return self.total_count
    
    def set_count(self,value):
        self.total_count = value
        with open('data/data_count.txt','w') as d:
            d.write(str(self.total_count))
    
    def add_count(self,value):
        self.total_count += value 
        self.set_count(self.total_count)

if __name__ == '__main__':
    cc = data()
    a = cc.get_count()
    print(a)


    
