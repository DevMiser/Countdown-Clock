import sys
from datetime import date
from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

TARGET_DATE = date(2025, 11, 18)
TODAY = date.today()

def update_display():

    try:
        inky_display = auto()
    except RuntimeError:
        print("Inky pHAT not detected.")
        sys.exit(1)

    inky_display.set_border(inky_display.WHITE)

    # Create canvas
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)

    days_left = (TARGET_DATE - TODAY).days
    
    if days_left > 0:
        message = str(days_left)
        font_size = 100
    else:
        message = "PARTY"
        font_size = 55

    print(f"{message} DAYS")

    font = ImageFont.truetype(FredokaOne, font_size)

    center_x = inky_display.WIDTH / 2
    center_y = inky_display.HEIGHT / 2

    draw.text(
        (center_x, center_y), 
        message, 
        fill=inky_display.RED, 
        font=font, 
        anchor="mm"
    )

    inky_display.set_image(img)
    inky_display.show()

if __name__ == "__main__":
    update_display()
