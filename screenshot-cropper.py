from pynput.mouse import Listener
from PIL import Image
import PIL.ImageGrab,os
from tkinter.filedialog import asksaveasfile
from tkinter import *
from pyautogui import press
#from pynput import *
import keyboard

class App():

    remmember_path = ""
    image = 'tempfile.png'  # name
    points = []
    signal_key = "print_screen"  # default key
    default_dir_flag=True

    def __init__(self, *args, **kwargs):
        while True:  # making a loop
            try:
                #ctrl+prtscn
                if keyboard.is_pressed('ctrl') and keyboard.is_pressed(self.signal_key):
                    return
                elif keyboard.is_pressed(self.signal_key):
                    print('You Pressed A Key! ', self.signal_key)
                    self.image_save()
                else:
                    pass
            except:
                pass
    
    # saves screen shot under 'tempfile.png'
    def take_screen_shot(self):
        press("printscreen")
        im = PIL.ImageGrab.grabclipboard()
        im.save(self.image, 'PNG')
        im.close()

    # saves cropped 'tempfile.png' and delete the original 
    def image_save(self):
        self.take_screen_shot()
        im_crop = self.imag_crop()
        root = Tk()
        root.withdraw()
        if self.default_dir_flag:
            f = asksaveasfile(parent=root, mode='w', defaultextension=".png",initialdir=os.getcwd())  #
            self.default_dir_flag = False
        else:
            f = asksaveasfile(parent=root, mode='w', defaultextension=".png")
        try:
            Name_new_file = f.name
            im_crop.save(Name_new_file, quality=100, subsampling=0)
        except:
            pass
        os.remove(self.image)
        root.destroy()
    
    # crop the screenshot
    def imag_crop(self):
        self.listen_to_mouse_clicks()
        im = PIL.Image.open(self.image)
        if self.points == []:
            return im
        else:
            p1 = self.points[0]
            p2 = self.points[1]
            p1_x = p1[0]
            p1_y = p1[1]
            p2_x = p2[0]
            p2_y = p2[1]
            self.points.clear()

        return im.crop((p1_x, p1_y, p2_x, p2_y))
    
    # when mouse click
    def on_click_mouse(self,x, y, button, pressed):
        global listener
        if pressed:
            print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
            if button.name == 'right':
                self.points.clear()
                listener.stop()
                return
            self.points.append([x, y])
            if self.points.__len__() == 2:
                listener.stop()

    # listen to mouse click and save the 2 clicks for cropping
    def listen_to_mouse_clicks(self):
        global listener
        with Listener(on_click=self.on_click_mouse) as listener:
            listener.join()
    
    # when key pressed
    def on_press(self,key):
        try:
            # print(key.name) #pring the key name
            self.signal_key = str(key.name)
            self.listener.stop()
        except:
            print("Bad key try again")

    # change the key to listen for screen capture 
    def change_signal_key(self):
        with Listener(
                on_press=self.on_press) as self.listener:
            self.listener.join()


if __name__ == '__main__':
    App()
