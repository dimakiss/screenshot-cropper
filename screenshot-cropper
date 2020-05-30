from pynput.mouse import Listener
from PIL import Image
import PIL.ImageGrab,os,glob
import tkinter as tk
from pyautogui import press
points=[]

def on_click(x, y, button, pressed):
    if pressed:
        print ('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        points.append([x,y])
        if points.__len__()==2:
            listener.stop()



master=""
text_box=""
def callback(self):
    global master,Name_of_new_file
    print(1)
    Name_of_new_file=str(text_box.get("1.0","end-2c"))
    print(Name_of_new_file)
    tk.Tk.quit(master)
def get_new_name():
    global master,text_box
    master = tk.Tk()
    text_box=tk.Text(master,height="1")
    text_box.grid(sticky=tk.NSEW)
    master.bind('<Return>', callback)
    master.mainloop()


image = 'tempfile.png' #name
press("printscreen")
im = PIL.ImageGrab.grabclipboard()
im.save(image,'PNG')

with Listener( on_click=on_click) as listener:
    listener.join()

p1=points[0]
p2=points[1]
p1_x=p1[0]
p1_y=p1[1]
p2_x=p2[0]
p2_y=p2[1]
im = Image.open(image)
Name_of_new_file="new.png"
get_new_name()
if ".png" not in Name_of_new_file:
    Name_of_new_file+=".png"
if glob.glob(Name_of_new_file).__len__()!=0:
    print("choose different name")
    get_new_name()
    if ".png" not in Name_of_new_file:
        Name_of_new_file += ".png"
else:
    im_crop = im.crop((p1_x, p1_y, p2_x, p2_y),)
    im_crop.save(Name_of_new_file, quality=100,subsampling=0)





