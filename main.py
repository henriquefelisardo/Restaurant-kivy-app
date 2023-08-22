

'''from os import environ

density = 2
dpi = 395 
width = 432
height = 960
environ['KIVY_METRICS_FONTSCALE'] = '1'
environ['KIVY_METRICS_DENSITY'] = str(density)
environ['KIVY_DPI'] = str(dpi)'''

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.utils import platform
from kivy.config import Config
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.core.clipboard import Clipboard
from kivy.metrics import dp
import time
from datetime import date
from datetime import datetime


class Mainscreen (Screen):
    #hora = (self.manager.get_screen('menu').ids.hora.text)
    pass

class MyScreenManager(ScreenManager):
    pass

sm = ScreenManager()
sm.add_widget(Mainscreen(name='menu'))


class MainApp(MDApp):
    #Window.size = (480,854) #full hd
    Window.size = (1080,1920) #poco x5 pro
    '''Window.size = (dp(width), dp(height))'''
    def build(self): 
        self.theme_cls.primary_palette = 'Red'      
        self.theme_cls.theme_style = 'Dark'

        a = open('kivvy log total.txt', 'w')
        print('',end = '', file=a)
        a = open('kivvy log.txt', 'w')
        print('',end = '', file=a)

        kvfile = Builder.load_file('main.kv') 
        return kvfile
    

    def display_data(self,pedido):

        list = (('Feijoada Pequena',40),('Feijoada Média',50),
('Feijoada Grande',60),('Baião Pequeno',30),
('Baião Médio',35),('Baião Grande',40),
('Parmediana fr Pequena',16),('Parmediana fr Média',18),
('Parmediana fr Grande',20),('Filé Pequeno',16),
('Filé Médio',18),('Filé Grande',20),('Bife semc Pequeno',16),
('Bife semc Médio',18),('Bife semc Grande',20),('Bife ac Pequeno',16),
('Bife ac Médio',18),('Bife ac Grande',20),('Iscas filé Pequeno',16),
('Iscas filé Médio',18),('Iscas filé Grande',20),('Iscas carne Pequeno',16),
('Iscas carne Médio',18),('Iscas carne Grande',20),('Carne deP Pequeno',16),
('Carne deP Médio',18),('Carne deP Grande',20),('Porç Arroz',6),
('Mistura Ext',13.00),('Por Torresmo',8.00),('Coca 2L',14.00),('Coca 1L',10.00),
('Coca 600ml',8.00),('Coca Lata',5.50),('Guaraná antártica 1.5L',9.00),
('Ovo Extra',1.50),)
        
        print(f'{list[pedido][0]}: {list[pedido][1]:.2f}')
        a = open('kivvy log.txt', 'a')
        print(f'{list[pedido][0]}: {list[pedido][1]:.2f}', file=a)
        def_valor(list[pedido][1])

    def display_data16(self):
        a = open('kivvy log.txt', 'w')
        print('',end = '', file=a)
        a = open('kivvy log note.txt', 'w')
        print('',end = '', file=a)
        a = open('kivvy log total.txt', 'w')
        print('',end = '', file=a)


    def display_data17(self):
        
        #print(self.root.ids.menu.ids.hora.text)

        copyText = ''
        username = self.root.ids.username.text.title()
        hora = self.root.ids.hora.text
        
        a = open('kivvy log note.txt', 'w')
        print('',end = '', file=a)
        a = open('kivvy for.txt', 'w')
        print('',end = '', file=a)
        a = open('kivvy log total.txt', 'r')
        read = a.readline()
        
        if read != '':
            a = open('kivvy log total.txt', 'r')
            for line in a.readlines():
                sum = 0
                line = line.split(',')
            for x in range (0,len(line)-1):
                sum += float(line[x])    
            print(f'\n\
Total: {sum:.2f}')
        a = open('kivvy log.txt', 'r')
        read_log = a.read()

        a = open('kivvy log note.txt', 'a')
        print(f'{username} para {hora}\n', file=a)
        a = open('kivvy log note.txt', 'a')
        print(read_log, file=a)
        
        a = open('kivvy log total.txt', 'r')
        read_total = a.readline()
        if read_total != '':
            a = open('kivvy log note.txt', 'a')
            print(f'Total: {sum:.2f}', file=a)
        
        a = open('kivvy log.txt', 'w')
        print('',end = '', file=a)
        a = open('kivvy log total.txt', 'w')
        print('',end = '', file=a)
        
        f = open('kivvy for.txt', 'a')
        print(f'ok, pode ser pra {hora}\n', file=f)
        with open("kivvy for.txt") as f:
            copyText = f.read()
        #pyperclip.copy(copyText)
        Clipboard.copy(copyText)
        
        time.sleep(0.5) 

        with open('kivvy log note.txt') as r:
            copyText = r.read()
        #pyperclip.copy(copyText)
        Clipboard.copy(copyText)

        data1 = date.today()
        data = (f'{data1.day}/{data1.month}/{data1.year}')
        
        self.root.ids.username.text = ''


    def botao_hora(self):  
        hoje_autogen = datetime.now()
        hora_h = int(hoje_autogen.strftime("%H"))
        hora_m = int(hoje_autogen.strftime("%M"))
        
        hora_m = str(hora_m)
        if int(hora_m)<10:
            hora_m = f'0{hora_m}'
        if int(hora_h)<10:
            hora_h = f'0{hora_h}'
        if int(hora_m)<10:
            hora_m = f'0{hora_m}'
        hora_m = [hora_m[0],hora_m[1]]
        if 3<=int(str(hora_m[1]))<=7:
            hora_m[1] = '5'
        elif 0<=int(str(hora_m[1]))<=2 or 8<=int(str(hora_m[1]))<=9:
            if int(hora_m[1])>5 and int(hora_m[0])<5:
                hora_m[0] = f'{int(hora_m[0])+1}'
                hora_m[1] = '0'
                if int(hora_h)<23:
                    hora_h += 1
            elif int(hora_m[1])<5:
                hora_m[1] = '0'    
        h1 = hora_m
        hora_m = ''
        for x in range (0,2):hora_m += h1[x]
        hora_now = f'{hora_h}:{hora_m}'
        self.root.ids.hora.text = hora_now
        print(hora_now)
        print(self.root.ids.hora.text)
        #self.manager.ids.hora.text = 'tua mae e minea'

    def hora_ativa(self):    
        for x in range (0,1):
            hoje_autogen = datetime.now()
            hora_h = int(hoje_autogen.strftime("%H"))
            hora_m = int(hoje_autogen.strftime("%M"))
            hora_now = f'{hora_h}:{hora_m}'
            self.root.ids.hora.text = hora_now 
            

        
    def botao_h_somada(self):  
        hoje_autogen = datetime.now()
        hora_h = int(hoje_autogen.strftime("%H"))
        hora_m = int(hoje_autogen.strftime("%M"))
        minutagem_def = int(self.root.ids.hora_sum.text)
        hora_m = hora_m + minutagem_def
        
        if 120>int(hora_m) >= 60:
            hora_m = int(hora_m)-60
            hora_h += 1
        elif 180>int(hora_m) >= 120:
            hora_m = int(hora_m)-120
            hora_h += 2
        elif int(hora_m) >= 180:
            hora_m = int(hora_m)-180
            hora_h += 3
        if 120>int(hora_m) >= 60:
            hora_m = int(hora_m)-60
            hora_h += 1

        if int(hora_m)<10:
            hora_m = f'0{hora_m}'
        if int(hora_h)<10:
            hora_h = f'0{hora_h}'
        if int(hora_m)<10:
            hora_m = f'0{hora_m}'
        
        hora_m = str(hora_m)
        hora_m = [hora_m[0],hora_m[1]]
        if 3<=int(str(hora_m[1]))<=7:
            hora_m[1] = '5'
        elif 0<=int(str(hora_m[1]))<=2 or 7<=int(str(hora_m[1]))<=9:
            if int(hora_m[1])>5 and int(hora_m[0])<5:
                hora_m[0] = f'{int(hora_m[0])+1}'
                hora_m[1] = '0'
                if int(hora_h)<23:
                    hora_h += 1
            elif int(hora_m[1])<5:
                hora_m[1] = '0'    
        h1 = hora_m
        hora_m = ''
        for x in range (0,2):hora_m += h1[x]

        hora_ped = f'{hora_h}:{hora_m}'
        self.root.ids.hora.text = hora_ped
        print(self.root.ids.hora.text)


def def_valor(val):
    a = open('kivvy log total.txt', 'a')
    print(f'{val},',end = '', file=a)


MainApp().run()
