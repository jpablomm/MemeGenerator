import os
import random
from PIL import Image, ImageDraw, ImageFont

class MemeEngine:
    """Engine that generates image with text."""

    def __init__(self, out_dir):
        self.out_dir = out_dir

    def make_meme(self, img_path, text, author, width=500):
        """Loads image. Resize if necessary. Adds text in random position."""
        img = Image.open(img_path)

        width = 500 if width > 500 else width
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))

        img = img.resize((width, height), Image.NEAREST)

        text = ' - '.join([text, author])
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('MemeGenerator/Roboto-Light.ttf', 30)
        draw.text(
            (random.randint(0, len(text)), random.randint(0, height - 35)),
            text=text,
            font=font,
            fill='white'
        )

        out_path = os.path.join(self.out_dir, f'img{random.randint(0,10000000)}.png')
        img.save(out_path)

        return out_path
