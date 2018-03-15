import pyautogui as pg
import webbrowser

videos = [", https://www.youtube.com/watch?v=qZHycHI3F1Q, https://www.youtube.com/watch?v=Fj8G9dGuNkU"]

Music = ["https://www.spotify.com/us/premium/?utm_source=us-en_brand_contextual_text&utm_medium=paidsearch&utm_campaign=alwayson_ucanz_us_performancemarketing_core_brand+contextual+text+exact+us-en+google&gclid=CLGztIPjudkCFYmvswod6GUBvg&gclsrc=ds,"]

answer = pg.prompt(
"""

which would you rather do?
a)watch videos
b)listen to music

"""

    )

if answer == "a":
    for i in videos:
        Webbrowser.open(i)

elif answer == "b":
    for i in music:
        webbrowser.open(i)
