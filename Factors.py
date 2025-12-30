#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 17:05:47 2025

@author: bill
"""

import tkinter as tk

w = tk.Tk()
w.title("Prime Factors")
w.resizable(False, False)

w.option_add("*font", "Arial 16")

numStr = tk.StringVar()

x = 0
count = 0

xlist = []
dlist = []

def getFacts(n):
    outLbl2["state"] = tk.NORMAL
    outLbl2.delete("1.0", tk.END)
    
    dlist = []
    v1 = n
    for i in range(2, n):
        if (n % i) == 0 and v1 > i:
            v1 = n // i
            dlist.append((i, v1))
            
    if len(dlist) > 0:
        for k in dlist:
            outLbl2.insert(tk.END, f"{k[0]} x {k[1]}\n")

    outLbl2["state"] = tk.DISABLED
        
def getPrimes(ev = None):
    global count, x
    
    xlist = []
    
    x = int(numStr.get())
    if isinstance(x, int):
        
        testv = x
    
        for i in range(2, x):
            if (testv % i) == 0:
                while (testv % i) == 0:
                    count += 1
                    testv = testv // i
                xlist.append((i, count))
                count = 0
        
        if len(xlist) < 1:
            outLbl1["text"] = "prime"
            
            outLbl2["state"] = tk.NORMAL
            outLbl2.delete("1.0", tk.END)
            outLbl2["state"] = tk.DISABLED
            
        else:
            ost = ""
            
            for j in xlist:
                ost += f"{j[0]}({j[1]})\n"
                
            outLbl1["text"] = ost
            
            getFacts(x)
            
inEnt = tk.Entry(w, textvariable=numStr, width=10, justify=tk.RIGHT)
inEnt.grid(row=0, column=0)

calcBtn = tk.Button(w, text="Calculate", command=getPrimes)
calcBtn.grid(row=0, column=1)
w.bind("<Return>", getPrimes)
w.bind("<KP_Enter>", getPrimes)

l1 = tk.Label(w, text="Primes (exponent)", bd=2, relief=tk.SUNKEN)
l1.grid(row=1, column=0, sticky=tk.EW)

l2 = tk.Label(w, text="Factors", bd=2, relief=tk.SUNKEN)
l2.grid(row=1, column=1, sticky=tk.EW)

outLbl1 = tk.Label(w, bd=2, relief=tk.SUNKEN, background="white",
                   anchor=tk.N, justify=tk.LEFT)
outLbl1.grid(row=2, column=0, sticky=tk.NSEW)

fr = tk.Frame(w)
fr.grid(row=2, column=1)

sb = tk.Scrollbar(fr)
sb.pack(side=tk.RIGHT, fill=tk.BOTH)

outLbl2 = tk.Text(fr, width=20, height=20, state=tk.DISABLED, yscrollcommand=sb.set)
outLbl2.pack() #grid(row=2, column=1, sticky=tk.N)

sb.config(command=outLbl2.yview)

w.mainloop()
