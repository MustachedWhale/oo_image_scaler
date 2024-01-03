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

size_dict = {"large": (1200, 800), "medium": (600, 400)}
scaler = PhotoScaler("path/to/root/folder", size_dict)
scaler.scale_photos()