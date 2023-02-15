import time
from datetime import date
from inky.auto import auto  #imports that auto class from the inky.auto library
from PIL import Image, ImageFont, ImageDraw  #imports three classes needed from the Python Image Library (PIL)
from font_fredoka_one import FredokaOne #import the desired font

target_date = date(2022, 7, 9)

today = date.today()

days_left = abs(target_date - today) #returns the absolute value

inky_display = auto()  #creates an instance of the class called inky_display
inky_display.set_border(inky_display.WHITE) #sets the border color (the thin line at the edge of the display) color to black
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))  #creates a new image that is the width and height of the Inky pHAT display
draw = ImageDraw.Draw(img)  #creates a drawing canvas to which text and graphics can be drawn

if target_date > today:
    message = str(days_left.days) #converts the number of days (without hours) into a string
    font = ImageFont.truetype(FredokaOne,100) #set the font size
else:
    message = "EASY" #this is what will be displayed when the countdown is complete
    font = ImageFont.truetype(FredokaOne,75) #set the font size

print (message,"DAYS")

#use the width and height constants we created above to center our message:
w, h = font.getsize(message)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - ((h / 2) + 10)

draw.text((x, y), message, inky_display.RED, font)  #sets the color of the text
inky_display.set_image(img)  #sets the image
inky_display.show()  #calls the function to refresh the Inky pHAT with our text
