"""Meme generator Engine."""
import os
from random import randint
from PIL import Image, ImageDraw, ImageFont


FONT = './_data/fonts/Caveat-Bold.ttf'


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
                font = ImageFont.truetype(FONT, size=30)
                quote = text + '\n' + author
                textsize = draw.textbbox(
                    (0, 0),
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
                if img.size[0]-textsize[2] < 0:
                    x_dim=0
                else:
                    x_dim = randint(0, img.size[0]-textsize[2])
                if im.size[1]-textsize[3] < 0:
                    y_dim=0
                else:
                    y_dim = randint(0, img.size[1]-textsize[3])
                draw.multiline_text(
                    (x_dim, y_dim),
                    quote,
                    font=font,
                    align='right',
                    fill='white')
        random_str = str(randint(1000000, 9999999))
        img_path = self._output_dir + '/' + random_str + '.jpg'
        try:
            img.save(img_path)
        except ValueError:
            print('The output format could not be'
                  ' determined from the file name.')
            return None
        except OSError:
            print('The file could not be written.')
            return None
        return img_path

    @property
    def output_dir(self) -> str:
        """Return output_dir."""
        return self._output_dir
