import display_window as dw 
import keyboard 
import record_key
from multiprocessing import  Process
import data.data_save as dd
 
def display_file_count(file_c):
    dw.display(file_c)


def write_file_count(file_c):
    def printcall(e):
        file_c.add_count(1)
    keyboard.on_press(printcall)
    keyboard.wait()




if  __name__ == '__main__':
    print('敲击-running...')
    file = dd.data() 
    p1 = Process(target=display_file_count,args=(file,)) #实例化进程对象

    p3 = Process(target=write_file_count,args=(file,)) #实例化进程对象
    p1.start()

    p3.start() 
    p1.join()

    p3.join()  
    print('敲击，ending...')


















    