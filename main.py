# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 10:58:45 2020

@author: iaedo
"""
import configparser
from datetime import datetime
import os
import pandas as pd
import sys
from time import sleep
from tkinter import *



CONFIG_FILE = './config.txt'
CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_FILE)



def timerRead(CONFIG):
    IO = os.path.normpath(CONFIG['FILE']['io'])
    SHEET_NAME = CONFIG['FILE']['sheet_name']
    HEADER = int(CONFIG['FILE']['header'])
    DELAY = int(CONFIG['TIMER']['delay'])
    try:
        df_past = pd.read_excel(IO, SHEET_NAME, HEADER)
        #print('reading...')
        time_past = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    except:
        create_warning('¡Archivo no encontrado! Revisar config.txt')
        sys.exit()
    df_past = df_past.fillna(0)
    sleep(DELAY)
    df_current = pd.read_excel(IO, SHEET_NAME, HEADER)
    df_current = df_current.fillna(0)
    time_current = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    return (time_past, df_past), (time_current, df_current)


def create_table(*args):
    dif_past, dif_curr, time_past, time_current, file_name = args
    # take the data 
    dif_total = pd.concat([dif_past,dif_curr])
    dif_total = dif_total.reset_index()
    dif_total = dif_total.rename(columns={'index':'Fila'})
    dif_total = dif_total.loc[:, dif_total.columns != 'mask']
    # create root window 
    root = Tk()     
    root.title('Diferencia en %s entre %s y %s' % (file_name, time_past, time_current))
    # populate column names
    for j, col_name in enumerate(dif_total.columns):
        e = Entry(root, width=10, fg='black', 
                  font=('Arial',11,'bold'))       
        e.grid(row=0, column=j) 
        e.insert(END, col_name)        
    # populate rows
    for i, row in dif_total.iterrows():
        for j, item in enumerate(row.tolist()):
            e = Entry(root, width=10, fg='blue', 
                      font=('Arial',11))       
            e.grid(row=i+1, column=j) 
            e.insert(END, item)        
    # init window mainloop
    root.mainloop() 


def create_warning(*args):
    text_warning = args
    root = Tk()
    T = Text(root, height=10, width=30)
    T.pack()
    T.insert(END, text_warning)
    root.mainloop()


def compExcel(df_past, df_current):
    df_comp = df_current.eq(df_past)
    df_past['mask'] = ''
    df_current['mask'] = ''
    for i in range(len(df_comp)):
        #print(df_comp.loc[i].all())
        df_past['mask'].loc[i] = df_comp.loc[i].all().copy()
        df_current['mask'].loc[i] = df_comp.loc[i].all().copy()
    return df_past[df_past['mask']==False], df_current[df_current['mask']==False]



# MAIN
while True:
    (time_past, df_past), (time_current, df_current) = timerRead(CONFIG)
    dif_past, dif_curr = compExcel(df_past, df_current)
    if not dif_past.equals(dif_curr):
        create_table(dif_past, dif_curr, time_past, time_current, CONFIG['FILE']['io'])
