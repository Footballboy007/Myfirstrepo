import pyautogui as pg
import time

points = 0

#Question 1

answer = pg.prompt(
"""
Which La Liga soccer team do you like the most?

a)Barcelona
b)Real Madrid
c)Athletico Madrid 
"""

    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

#Question 2

answer = pg.prompt(
"""
Which British Premier League soccer team do you like the most?

a)Arsenal
b)Chelsea
c)Manchester City 
"""

    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

