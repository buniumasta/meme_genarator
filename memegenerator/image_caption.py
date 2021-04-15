# """Module defines image with caption capability."""
# from PIL import Image


# class ImageCaption():
#     """Image Caption classs."""

#     def __init__(self, image_path):
#         """Initialize image caption object."""
#         self.image_path = image_path
#         try:
#             with Image.open(image_path) as self.image:
#                 pass
#         except OSError:
#             self.image = None

#     def image_resize(self, width: int):
#         """Re-size image to width."""
#         size = self.image.size
#         width = size[0]
#         height = size[1]
#         # print(f'{width}x{height}')
#         im = self.image.resize((500, 500))
#         #print(im)
#         #im.save('./resized.image','*.jpg')

#     def resize_needed(self, width: int) -> bool:
#         """Return True if resize of image is needed."""
#         if self.image.size[1] != width:
#             return True
#         return False

#     def add_caption(self, body: str, author: str):
#         """Add caption to an image with random place."""

#     def __str__(self):
#         """Provide information about the picture."""
#         if self.image is not None:
#             return f'{self.image_path}, {self.image.format},' \
#                 f' {self.image.size}x{self.image.mode}'
#         return ""


# # if __name__ == '__main__':
# #     image = ImageCaption('../_data/photos/art/pexels-ag-z-3459967.jpg')
# #     print(image)
# #     image.image_resize(300)
