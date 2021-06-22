import random
from random import randint
import time
gentype = '0123456789'
print("Welcome Carder.Join Our Telegram Channel C_A_N_C_E_R_0 ")
print("Welcome To Credit Card Generator")
print("This Script Created By DARK")
total = input("Quantity? ")
#Number To Generate
number = int(total)
file = (total + " Credit Cards.txt ")
file2 = 'Cards.txt'
mode = input("Chose Type \nMasterCard\nVisa\nAmex\nDiscover\n")
#MasterCard
if(mode == "MasterCard"):
    gentype = '0123456789'
    gentype2 = '5'
    for x in range(number):
        generate1 = random.choice(gentype2)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        generate16 = random.choice(gentype)
        space1 = "|"
        month = str(randint(1, 12))
        space2 = "|"
        year = str(randint(20,29))
        space3 = "|"
        generate17 = random.choice(gentype)
        generate18 = random.choice(gentype)
        generate19 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
          out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+generate11+generate12+generate13+generate14+generate15+generate16+space1+month+space2+year+space3+generate17+generate18+generate19+newline)
#Visa
if(mode == "Visa"):
    gentype = '0123456789'
    gentype3 = '4'
    for x in range(number):
        generate1 = random.choice(gentype3)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        generate16 = random.choice(gentype)
        space1 = "|"
        month = str(randint(1, 12))
        space2 = "|"
        year = str(randint(20,29))
        space3 = "|"
        generate17 = random.choice(gentype)
        generate18 = random.choice(gentype)
        generate19 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
          out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+generate11+generate12+generate13+generate14+generate15+generate16+space1+month+space2+year+space3+generate17+generate18+generate19+newline)
#Amex
if(mode == "Amex"):
    gentype = '0123456789'
    gentype4 = '3'
    for x in range(number):
        generate1 = random.choice(gentype4)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        generate16 = random.choice(gentype)
        space1 = "|"
        month = str(randint(1, 12))
        space2 = "|"
        year = str(randint(20,29))
        space3 = "|"
        generate17 = random.choice(gentype)
        generate18 = random.choice(gentype)
        generate19 = random.choice(gentype)
        generate20 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
          out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+generate11+generate12+generate13+generate14+generate15+generate16+space1+month+space2+year+space3+generate17+generate18+generate19+generate20+newline)
#Discover
if(mode == "Discover"):
    gentype = '0123456789'
    gentype6 = '6'
    for x in range(number):
        generate1 = random.choice(gentype6)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        generate16 = random.choice(gentype)
        space1 = "|"
        month = str(randint(1, 12))
        space2 = "|"
        year = str(randint(20,29))
        space3 = "|"
        generate17 = random.choice(gentype)
        generate18 = random.choice(gentype)
        generate19 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
          out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+generate11+generate12+generate13+generate14+generate15+generate16+space1+month+space2+year+space3+generate17+generate18+generate19+newline)
print ("Credit Cards Generated Sucessfully Thank u for using our Gen")
time.sleep(5)
