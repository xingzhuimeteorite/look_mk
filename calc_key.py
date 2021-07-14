import re 



def read_file(key_file,position,offset,split_separtor):
    '''
    入參:   
        key_file:文件流
        position:文件指針位置
        offset:阅读长度
        split_separtor:文本流分隔符
    返回:
        txt:本次读到的文本内容
        seek_after_position:文件指针位置
        flag:文件结束：0 文件未结束：1


    '''
    key_file.seek(position,0) 
    current_position = key_file.tell()
    # print('当前指针位置',current_position)
    txt = key_file.read(offset) 
    read_after_position =  key_file.tell()
    # print('阅读后指针位置',read_after_position)
    if (read_after_position-current_position<offset):
        return txt,read_after_position,0
    last_separtor = re.search(split_separtor,txt[::-1]).end() 
    seek_after_position= key_file.tell()-last_separtor+1
    key_file.seek(seek_after_position,0) 
    # print('偏移后指针的位置',seek_after_position)
    return  txt[:-last_separtor],seek_after_position,1

def test_read_file():
    file_name = '2021-07-14.txt'
    with  open('record/{}'.format(file_name),'r') as key_file:
        buffer=50
        begin_positon= 0
        flag = 1 
        while(flag):
            txt,next_position,flag = read_file(key_file,begin_positon,buffer,';')
            print(txt)
            begin_positon = next_position 

def calc_key_count(txt_dic,txt,split_separtor):
    for i in re.split(split_separtor,txt):
        if i in txt_dic.keys():
            txt_dic[i]+=1
        else :
           txt_dic[i]=1 
    
    return txt_dic

def test_calc():
    aa = {'ctrl':3}
    cc = calc_key_count(aa,'ctrl;alt;s',';')
    print(cc)


def order_key(txt_dic):
    return sorted(txt_dic.items(),  key=lambda d: d[1], reverse=True)

def test_main():
    file_name = 'main2.txt'
    result = {}
    with  open('record/{}'.format(file_name),'r') as key_file:
        buffer=50
        begin_positon= 0
        flag = 1 
        while(flag):
            txt,next_position,flag = read_file(key_file,begin_positon,buffer,';')
            result = calc_key_count(result,txt,';')
            begin_positon = next_position 
    
    cc = order_key(result)
    cnt = 0 
    for key,values in cc :
        print('%-20s%-20s'%(key,values))
        cnt += values
    print('total:',cnt) 

if __name__ == '__main__':

    # test_read_file()
    # test_calc()
    test_main()