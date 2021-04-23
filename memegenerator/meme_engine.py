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
        self._img = None

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make meme and return generated image path."""
        with Image.open(img_path) as image:

            self.img = image
            if width is not None:
                self.re_size(width)

            if text is not None:
                draw = ImageDraw.Draw(self.img)
                font = ImageFont.truetype(FONT, size=30)
                quote = text + '\n' + author
                textsize = draw.textbbox(
                    (0, 0),
                    quote,
                    font=font,
                    anchor=None,
                    spacing=4,
                    align='right')

                diff_x = int(self.img.size[0]-textsize[2])
                if diff_x < 0:
                    x_dim = 0
                else:
                    x_dim = randint(0, diff_x)

                diff_y = int(self.img.size[1]-textsize[3])
                if diff_y < 0:
                    y_dim = 0
                else:
                    y_dim = randint(0, diff_y)

                draw.multiline_text(
                    (x_dim, y_dim),
                    quote,
                    font=font,
                    align='right',
                    fill='white')

        return self.image_save()

    def re_size(self, width: int) -> Image:
        """Resize image to given width."""
        ratio = width/float(self.img.size[0])
        height = int(ratio*float(self.img.size[1]))
        self.img = self.img.resize((width, height), Image.NEAREST)

    def image_save(self) -> str:
        """Save image to the disk."""
        random_str = str(randint(1000000, 9999999))
        img_path = self._output_dir + '/' + random_str + '.jpg'
        try:
            self.img.save(img_path)
            return img_path
        except ValueError:
            print('The output format could not be'
                  ' determined from the file name.')
            return None
        except OSError:
            print('The file could not be written.')
            return None

    @property
    def output_dir(self) -> str:
        """Return output_dir."""
        return self._output_dir

    @property
    def img(self) -> Image:
        """Return image."""
        return self._img

    @img.setter
    def img(self, image: Image):
        """Set image."""
        self._img = image
