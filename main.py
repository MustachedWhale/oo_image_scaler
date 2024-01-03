import os
from PIL import Image

class PhotoScaler:
    def __init__(self, root_folder, size_dict):
        self.root_folder = root_folder
        self.size_dict = size_dict

    def scale_photos(self):
        for filename in os.listdir(self.root_folder):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                photo = Photo(os.path.join(self.root_folder, filename))
                photo.create_folder()
                photo.move_photo()
                photo.scale_up(self.size_dict)

class Photo:
    def __init__(self, original_path):
        self.original_path = original_path
        self.new_folder = os.path.splitext(original_path)[0]

    def create_folder(self):
        os.makedirs(self.new_folder, exist_ok=True)

    def move_photo(self):
        os.rename(self.original_path, os.path.join(self.new_folder, os.path.basename(self.original_path)))

    def scale_up(self, size_dict):
        original_image = Image.open(os.path.join(self.new_folder, os.path.basename(self.original_path)))
        for new_size in size_dict.values():
            new_image = original_image.resize(new_size, Image.ANTIALIAS)
            new_image.save(os.path.join(self.new_folder, f"scaled_{new_size[0]}x{new_size[1]}.jpg"), quality=100, dpi=(300,300))

# Directory creation list.
dir_dict = {'4x5in.jpg': '4x5 Aspect Ratio',
            '4x6in.jpg': '2x3 Aspect Ratio',
            '5x7in.jpg': '5x7 Aspect Ratio',
            '6x8in.jpg': '3x4 Aspect Ratio',
            '11x14in.jpg': '11x14 Aspect Ratio',
            'A5P.jpg': 'ISO Sizes',
            '5x4in.jpg': '5x4 Aspect Ratio',
            '6x4in.jpg': '3x2 Aspect Ratio',
            '7x5in.jpg': '7x5 Aspect Ratio',
            '8x6in.jpg': '4x3 Aspect Ratio',
            '14x11in.jpg': '14x11 Aspect Ratio',
            'A5L.jpg': 'ISO Sizes'}

size_dict = {"large": (1200, 800), "medium": (600, 400)}
scaler = PhotoScaler("path/to/root/folder", size_dict)
scaler.scale_photos()