# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 00:52:29 2022

@author: felix
"""
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ahk import AHK


class Manager(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, padding=10, **kwargs)
        ttk.Style().configure("TButton", font="TkFixedFont 12")
        self.pack(fill=BOTH, expand=YES)
        if "bootstyle" in kwargs:
            self.bootstyle = kwargs.pop("bootstyle")
        else:
            self.bootstyle = None
        # point to AHK executable
        self.ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\AutoHotkey.exe')
        self.create_shortcuts()
        
    def clicked(self):
        f = open("C:/Users/felix/OneDrive/Documents/Hotstring_Manager/hotstring_manager.ahk","w+")
        f.write("#SingleInstance Force \n#NoEnv \nSendMode Input\nSetWorkingDir %A_ScriptDir% \n")
        hslist = [self.hs1.get(), self.hs2.get(), self.hs3.get(), self.hs4.get(), 
                  self.hs5.get(), self.hs6.get(), self.hs7.get(), self.hs8.get(), self.hs9.get()]
        for index, item in enumerate(hslist):
            if item != '':
                key = str(index+1)
                strList = ["Numpad", key, "::\nSend ", str(item or ''), "\nreturn \n"] 
                insert = ''.join(strList)
                f.write(insert)
        f.close()
        self.ahk.run_script("C:/Users/felix/OneDrive/Documents/Hotstring_Manager/hotstring_manager.ahk", blocking=False)

    def clear(self):
        self.hs1.delete(0, END)
        self.hs2.delete(0, END)
        self.hs3.delete(0, END)
        self.hs4.delete(0, END)
        self.hs5.delete(0, END)
        self.hs6.delete(0, END)
        self.hs7.delete(0, END)
        self.hs8.delete(0, END)
        self.hs9.delete(0, END)
        open("C:/Users/felix/OneDrive/Documents/Hotstring_Manager/hotstring_manager.ahk", "w").close()

    def create_shortcuts(self):
        container = ttk.Frame(master=self, padding=2, bootstyle=self.bootstyle)
        container.pack(fill=BOTH, expand=YES)
        container.columnconfigure(2, weight=1)
        lbl1 = ttk.Label(container, text="Numpad 1").grid(column=1, row=1, sticky=W, pady=2)
        lbl2 = ttk.Label(container, text="Numpad 2").grid(column=1, row=2, sticky=W, pady=2)
        lbl3 = ttk.Label(container, text="Numpad 3").grid(column=1, row=3, sticky=W, pady=2)
        lbl4 = ttk.Label(container, text="Numpad 4").grid(column=1, row=4, sticky=W, pady=2)
        lbl5 = ttk.Label(container, text="Numpad 5").grid(column=1, row=5, sticky=W, pady=2)
        lbl6 = ttk.Label(container, text="Numpad 6").grid(column=1, row=6, sticky=W, pady=2)
        lbl7 = ttk.Label(container, text="Numpad 7").grid(column=1, row=7, sticky=W, pady=2)
        lbl8 = ttk.Label(container, text="Numpad 8").grid(column=1, row=8, sticky=W, pady=2)
        lbl9 = ttk.Label(container, text="Numpad 9").grid(column=1, row=9, sticky=W, pady=2)
        
        self.hs1 = ttk.StringVar()
        self.hs1 = ttk.Entry(container,width=40, textvariable = self.hs1)
        self.hs1.grid(column=2, row=1, padx=1, pady=1)
        self.hs2 = ttk.StringVar()
        self.hs2 = ttk.Entry(container,width=40, textvariable = self.hs2)
        self.hs2.grid(column=2, row=2, padx=1, pady=1)
        self.hs3 = ttk.StringVar()
        self.hs3 = ttk.Entry(container,width=40, textvariable = self.hs3)
        self.hs3.grid(column=2, row=3, padx=1, pady=1)
        self.hs4 = ttk.StringVar()
        self.hs4 = ttk.Entry(container,width=40, textvariable = self.hs4)
        self.hs4.grid(column=2, row=4, padx=1, pady=1)
        self.hs5 = ttk.StringVar()
        self.hs5 = ttk.Entry(container,width=40, textvariable = self.hs5)
        self.hs5.grid(column=2, row=5, padx=1, pady=1)
        self.hs6 = ttk.StringVar()
        self.hs6 = ttk.Entry(container,width=40, textvariable = self.hs6)
        self.hs6.grid(column=2, row=6, padx=1, pady=1)
        self.hs7 = ttk.StringVar()
        self.hs7 = ttk.Entry(container,width=40, textvariable = self.hs7)
        self.hs7.grid(column=2, row=7, padx=1, pady=1)
        self.hs8 = ttk.StringVar()
        self.hs8 = ttk.Entry(container,width=40, textvariable = self.hs8)
        self.hs8.grid(column=2, row=8, padx=1, pady=1)
        self.hs9 = ttk.StringVar()
        self.hs9 = ttk.Entry(container,width=40, textvariable = self.hs9)
        self.hs9.grid(column=2, row=9, padx=1, pady=1)

        btn = ttk.Button(container, text="Update Hotstrings", command=self.clicked)
        btn.grid(column=2, row=10, padx=10, pady=1)
        btn_clear = ttk.Button(container, text="Clear", command=self.clear)
        btn_clear.grid(column=1, row=10, padx=10, pady=1)


if __name__ == "__main__":

    app = ttk.Window(
        title="Hostring Manager",
        themename="solar",
        size=(400, 450)
    )
    Manager(app)
    app.mainloop()
    
    
"""    
    def create_shortcuts(self):
        container = ttk.Frame(master=self, padding=2, bootstyle=self.bootstyle)
        container.pack(fill=BOTH, expand=YES)
        shortcut_list = ["Numpad 1", "Numpad 2","Numpad 3","Numpad 4","Numpad 5",
                         "Numpad 6","Numpad 7","Numpad 8","Numpad 9"]
        container.columnconfigure(2, weight=1)
        for i, item in enumerate(shortcut_list):
            container.rowconfigure(i, weight=1)
            lbl = ttk.Label(container, text=item)
            lbl.grid(row=i, column=0, sticky=W, pady=2)
            hs = ttk.StringVar()
            hs = ttk.Entry(container,width=40, textvariable = hs)
            hs.grid(column=2, row=i , padx=1, pady=1)
        btn = ttk.Button(container, text="Update Hotstrings", command=self.clicked)
        btn.grid(column=2, row=10, padx=1, pady=1)
        btn_clear = ttk.Button(container, text="Clear", command=self.clear)
        btn_clear.grid(column=1, row=10, padx=1, pady=1)
"""
