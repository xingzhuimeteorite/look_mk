
import re 
import time 

class record_key:

    def __init__(self,key_event:dict):
        self.single_key_dict = key_event
        self.single_key_dict_code = list(key_event.keys())[0]
        self.single_key_dict_value = key_event[self.single_key_dict_code]
        
    def get_key_event_name(self):
        return str(self.single_key_dict_value)
    def get_key_name(self):
        full_name = self.get_key_event_name()
        name_head = r'^KeyboardEvent\('
        name_end =r' down\)' 
        name_begin_position = re.search(name_head,full_name).end()
        name_end_position = re.search(name_end,full_name).start()
        return full_name[name_begin_position:name_end_position]
    
    def write_txt(self):
        with open('record/{}.txt'.format(time.strftime('%Y-%m-%d')),'a') as fp:
            fp.write(self.get_key_name())
            fp.write(';')

    
if __name__ == '__main__':
    import keyboard 
    def printcall(e):
        a = record_key(keyboard._pressed_events)
        a.write_txt()
    keyboard.on_press(printcall)
    keyboard.wait() 
    