import tkinter as tk
import random
  from tkinter import mainloop, messagebox
  import random
  from random import randint as int
  import time 
  from time import sleep as wait

  AI_Health_Main = 24
  Dying = True
  #AI BRAIN
  AI_Health_HIGH = 75
  AI_Health_Low = 25


  while True:
    time.sleep(0.005)
    print(AI_Health_Main)

    if AI_Health_Main > AI_Health_HIGH:
     Dying = False
    if AI_Health_Main < AI_Health_Low:
     Dying = True


    if  Dying == True:
      AI_Health_Main = AI_Health_Main + 1


    if  Dying == False:
      AI_Health_Main = AI_Health_Main - 1
