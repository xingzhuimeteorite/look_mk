import keyboard  
import time
# keyboard.press_and_release('shift+s, space') 
import keyboard

# def print_pressed_keys(e):

#   print(keyboard._pressed_events)
#   print(keyboard._pressed_events)
#   print(type(keyboard._pressed_events))
#   print(str(e))
#   line = ', '.join(str(code) for code in keyboard._pressed_events)
#   print(line)
 
# keyboard.on_press(print_pressed_keys)
# keyboard.wait('Ctrl')ggggggggggggggdffddddd


def listen(event):
    print(type(event))
    if event.event_type == "down" :
        print(event.name) 

keyboard.hook(listen)
keyboard.wait() 