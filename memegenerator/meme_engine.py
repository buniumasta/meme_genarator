"""Meme generator Engine."""
import os
from random import randint
from PIL import Image, ImageDraw, ImageFont

class MemeEngine():
    """MemeEngine class generates meme on pictures."""

    def __init__(self, output_dir: str):
        """Initialize MemeEngine Object."""
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        self._output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make meme and return generated image path."""
        with Image.open(img_path) as img:
            # if crop is not None:
            #     img = img.crop(crop)
            if width is not None:
                ratio = width/float(img.size[0])
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)

            if text is not None:
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('./_data/fonts/Caveat-Bold.ttf', size=30)
                quote = text + '\n' + author
                textsize = draw.textbbox(
                    (0,0),
                    quote,
                    font=font,
                    anchor=None,
                    spacing=4,
                    align='right',
                    direction=None,
                    features=None,
                    language=None,
                    stroke_width=0,
                    embedded_color=False)
                x_dim = randint(0,img.size[0]-textsize[2])
                y_dim = randint(0,img.size[1]-textsize[3])
                draw.multiline_text((x_dim,y_dim), quote, font=font, align='right', fill='white')
            img_path = self._output_dir + '/' + str(randint(80000,89999)) + '.jpg'
            img.save(img_path)
        return img_path

    @property
    def output_dir(self) -> str:
        """Return output_dir."""
        return self._output_dir
