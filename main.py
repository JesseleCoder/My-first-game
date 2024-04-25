import tkinter as tk
import random
from random import randint as int
from tkinter.font import names
from tkinter import Message, Text, messagebox
import time

messagebox.showinfo(message="Hello I am Jesse.Q this is my game its hard but i hope you will like it")
messagebox.showinfo(message="tip-attacking lowers the enemys armor if a enemy has no armor you can land a critical hit")
messagebox.showwarning
global Health
global Health_mon
global Name
global Damge
global Armor

Player_health_Max = 75
Player_health = 50

#AI_Powers
def AI_Power_1():
  if int(1,5) == 5:
    global Player_health
    AI_Power_attack = int(10,25)
    Player_health = Player_health - AI_Power_attack
    AI_Power_attack_msg = "AI Uses a power attack and Throws a big rock at you for "+str(AI_Power_attack) + " damage"
    messagebox.showinfo(message=AI_Power_attack_msg)
  else:
    messagebox.showinfo(message="The AI tryed a Power attack but failed!")
  




#AI Defs

def AI_Power():
  global AI_POWER
  if AI_POWER == 1:
    AI_Power_1()

def AI():
 global Player_health, AI_damge, AI_health
 AI_Turn = int(1, 4)
 if AI_Turn == 1:
   AI_Damge_Get = int(1, AI_Damge)
   AI_Damge_msg = "The AI did " +str(AI_Damge_Get) + " Damge"
   Player_health = Player_health - AI_Damge_Get
   messagebox.showinfo(message=AI_Damge_msg)
 elif AI_Turn == 2:
    global AI_Health_mon
    AI_regen = int(1, 10)
    AI_regen_msg = "The AI has regenerated " + str(AI_regen) + " Health"
    AI_Health_mon = AI_Health_mon + AI_regen
    messagebox.showinfo(message=AI_regen_msg)
 elif AI_Turn == 3:
    AI_Power()

#player Defs

def Player_attack():
  global AI_Health_mon, Health, Damge, AI_Armor
  print("DEBUG_ATTACK")
  Player_Damge = int(1, 8) / AI_Armor
  AI_Health_mon = AI_Health_mon - Player_Damge / AI_Armor
  Attack_Get = "you did " + str(Player_Damge) + " Damge"
  messagebox.showinfo(message=Attack_Get)
  if AI_Armor >1:
    AI_Armor = AI_Armor - 1
    AI()
  else:
    Crit=int(1,5)
    if Crit == 5:
      AI_Health_mon = AI_Health_mon - 25
      messagebox.showinfo(message="CRITICAL HIT +25 DAMAGE")
      AI()
    else:
      AI()

def Player_heal():
  global Player_health
  Player_regen = int(1,5)
  Player_health = Player_health + Player_regen
  Player_health_msg = "You have regenerated " + str(Player_regen) + " Health"
  messagebox.showinfo(message=Player_health_msg)
  AI()

def Player_Check():
  global Health, AI_Health_mon

  Check = "Health: " + str(Player_health) + " AI Health: " + str(AI_Health_mon) + "AI POWER-" + str(AI_POWER)
  messagebox.showinfo(message=Check)


#window-1
root = tk.Tk()
label = root.title('Name')
Button1 = tk.Button(root, text="Attack", command=Player_attack)
Button2 = tk.Button(root, text="Heal", command=Player_heal)
Button3 = tk.Button(root, text="Check", command=Player_Check)

#window-2
Button1.pack()
Button2.pack()
Button3.pack()

#Monsters
mon = int(1, 1)
print(mon)

#Mon List
if mon == 1:
  AI_Health_mon = int(10,100)
  AI_Max_health = AI_Health_mon +25
  AI_Damge = int(1,15)
  AI_Armor = int(1,10)
  AI_POWER = int(0,1)
  #BOSS MOB (UNFINISHED)
elif mon == 2:
  AI_Max_health = 15
  AI_Health_mon = 10
  AI_Damge = 1
  AI_Armor = 0
  AI_POWER = 0
elif mon == 2:
  AI_Max_health = 15
  AI_Health_mon = 5
  AI_Damge = 1
  AI_Armor = 2
  AI_POWER = 0
#Loops

messagebox.showinfo(message="Your goal is to defeat the AI")

def do_something():
  global Player_health, AI_Health_mon , AI_Max_health , Player_health, Player_health_Max
  # Code to execute while mainloop is running
  if AI_Health_mon <= 1:
    messagebox.showinfo(message="You Win Close and reopen to replay")


  if Player_health < 1:
    messagebox.showinfo(message="GAME OVER")
    messagebox.showinfo(message="TIP Your Damge is divide by Armor")



  if AI_Max_health < AI_Health_mon:
    AI_Health_mon = AI_Max_health
    print("Health Maxed out")


  if Player_health_Max < Player_health:
    Player_health = Player_health_Max
    print("Player Health Maxed out")
root = tk.Tk()


def periodic_execution():
  do_something()
  root.after(1000, periodic_execution)


periodic_execution()

root.mainloop()
