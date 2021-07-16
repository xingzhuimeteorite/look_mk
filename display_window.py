
 
import tkinter as tk  # 使用Tkinter前需要先导入

# 显示器大小
# 窗口大小
screen_x = 1920
screen_y = 1080

window_x = 250
window_y = 50

total_count = 12
lable_txt  = 'total  : {}'.format(total_count) 

def display(data_class):
        
    
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()
    window.wm_attributes('-topmost',1)
    window.wm_attributes('-toolwindow',1)
    window.wm_attributes("-alpha", 0.5)        # 透明度(0.0~1.0)

    # 第2步，给窗口的可视化起名字
    window.title('My Window')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('{}x{}+{}+{}'.format(window_x,window_y,screen_x-window_x,0+50))  # 这里的乘是小x
    
    # 第4步，在图形界面上设定标签
    l = tk.Text(window, bg='white', font=('Arial', 30), width=20, height=5)
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
    
    # 第5步，放置标签
    l.pack()    # Label内容content区域放置位置，自动调节尺寸
    # 放置lable的方法有：1）l.pack(); 2)l.place();
    def refreshText():
        global lable_txt
        total_count =data_class.get_count()
        lable_txt  = 'total  : {}'.format(total_count) 
        l.delete(0.0,tk.END)
        l.insert(tk.INSERT,lable_txt)
        l.update()
        window.after(100,refreshText) 
    window.after(100,refreshText) 
    # 第6步，主窗口循环显示
    window.mainloop()
    # 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
    # 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。

if __name__ == '__main__':
    import data.data_save  as dd 
    aa = dd.data()
    display(aa)
    print('ss')