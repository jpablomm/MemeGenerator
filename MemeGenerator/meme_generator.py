import os
import random
from PIL import Image, ImageDraw, ImageFont

class MemeEngine:
    """Engine that generates image with text."""

    def __init__(self, out_dir):
        self.out_dir = out_dir

    def make_meme(self, img_path, text, author, width=500):
        """Loads image. Resize if necessary. Adds text in random position."""
        try:
            img = Image.open(img_path)
        except Exception:
            raise Exception('Invalid file path.')

        width = 500 if width > 500 else width
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))

        img = img.resize((width, height), Image.NEAREST)

        font_size = 30
        quote = ' - '.join([text, author])
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('MemeGenerator/Roboto-Light.ttf', font_size)
        ch_width = font.getsize('A')[0]
        ch_height = font.getsize('A')[1]
        x = random.randint(0, len(text))
        text = self.wrap_text(quote, width, ch_width, x)
        y = random.randint(0, height - (text[1] * ch_height))
        draw.text(
            (x, y),
            text=text[0],
            font=font,
            fill='white'
        )

        out_path = os.path.join(self.out_dir, f'img{random.randint(0,10000000)}.png')
        img.save(out_path)

        return out_path

    @staticmethod
    def wrap_text(text, width, ch_width, offset):
        """ Wraps the text if needed. Returns wrapped text and no. of lines"""

        txt_length = len(text) * ch_width
        num_of_lines = 1
        if (txt_length + offset) < width:
            return (text, num_of_lines)
        else:
            new_text = ''
            index = 0
            line_length = 0
            while index < len(text):
                if (line_length + offset) > width:
                    new_text += '\n'
                    line_length = 0
                    num_of_lines += 1
                
                new_text += text[index]
                index += 1
                line_length += ch_width

            return (new_text, num_of_lines)
