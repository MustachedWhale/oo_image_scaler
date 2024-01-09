import os
import sys
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

# Portrait image sizes.
size_dict_4x5 = {'8x10in.jpg': (2400, 3000),
                 '12x15in.jpg': (3600, 4500),
                 '16x20in.jpg': (4800, 6000)}
size_dict_4x6 = {'6x9in.jpg': (1800, 2700),
                 '8x12in.jpg': (2400, 3600),
                 '10x15in.jpg': (3000, 4500),
                 '12x18in.jpg': (3600, 5400),
                 '16x24in.jpg': (4800, 7200),
                 '20x30in.jpg': (6000, 9000),
                 '24x36in.jpg': (7200, 10800)}
size_dict_5x7 = {}
size_dict_6x8 = {'9x12in.jpg': (2700, 3600),
                 '12x16in.jpg': (3600, 4800),
                 '15x20in.jpg': (4500, 6000),
                 '18x24in.jpg': (5400, 7200)}
size_dict_11x14 = {}
size_dict_A5P = {'A4P.jpg': (2481, 3508),
                 'A3P.jpg': (3508, 4962),
                 'A2P.jpg': (4961, 7016),
                 'A1P.jpg': (7016, 9934)}

# Landscape Image Sizes
size_dict_5x4 = {'10x8in.jpg': (3000, 2400),
                 '15x12in.jpg': (4500, 3600),
                 '20x16in.jpg': (6000, 4800)}
size_dict_6x4 = {'9x6in.jpg': (2700, 1800),
                 '12x8in.jpg': (3600, 2400),
                 '15x10in.jpg': (4500, 3000),
                 '18x12in.jpg': (5400, 3600),
                 '24x16in.jpg': (7200, 4800),
                 '30x20in.jpg': (9000, 6000),
                 '36x24in.jpg': (10800, 7200)}
size_dict_7x5 = {}
size_dict_8x6 = {'12x9in.jpg': (3600, 2700),
                 '16x12in.jpg': (4800, 3600),
                 '20x15in.jpg': (6000, 4500),
                 '24x18in.jpg': (7200, 5400)}
size_dict_14x11 = {}
size_dict_A5L = {'A4L.jpg': (3508, 2481),
                 'A3L.jpg': (4961, 3508),
                 'A2L.jpg': (7016, 4961),
                 'A1L.jpg': (9934, 7016)}

# Square Image Sizes
size_dict_8x8 = {'10x10in.jpg': (3000, 3000),
                 '12x12in.jpg': (3600, 3600),
                 '16x16in.jpg': (4800, 4800)}

# Dict of all sizes.
size_dicts = {'4x5': size_dict_4x5,
              '4x6': size_dict_4x6,
              '5x7': size_dict_5x7,
              '6x8': size_dict_6x8,
              '11x14': size_dict_11x14,
              'A5P': size_dict_A5P,
              '5x4': size_dict_5x4,
              '6x4': size_dict_6x4,
              '7x5': size_dict_7x5,
              '8x6': size_dict_8x6,
              '14x11': size_dict_14x11,
              'A5L': size_dict_A5L,
              '8x8': size_dict_8x8}

## Main Code ##

root_folder_path = sys.argv[1]

ill_dir_list = os.listdir(root_folder_path)
for ill_dir in ill_dir_list:
    ill_folder_path = os.path.join(root_folder_path, ill_dir)
    for root, dirs, files in os.walk(ill_folder_path):
        for file in files:
            file_size = file.replace('in.jpg', '')
            size_dict = size_dicts.get(file_size)
            if size_dict is None:
                print(f'Undefined aspect ratio in {ill_dir}.')
                exit()
    scaler = PhotoScaler(ill_folder_path, size_dict)
    scaler.scale_photos()