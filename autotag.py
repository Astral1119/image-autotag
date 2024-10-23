import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import model
import exiftool
from tqdm import tqdm

def process_image(image_path, tags):
    try:
        with exiftool.ExifToolHelper() as et:
            et.set_tags(
                image_path, 
                tags = {"IPTC:Keywords": tags},
                params=["-P", "-overwrite_original"]
            )
    except exiftool.exceptions.ExifToolExecuteError as e:
        print(f"ExifTool error for {image_path}: {e}")
    except OSError as e:
        if e.errno == 93:  # Attribute not found error
            print(f"No extended attribute found for {image_path}")
        else:
            print(f"Error processing {image_path}: {e}")

class addAnimeTags():
    def __init__(self):
        self.model = model.deepdanbooruModel()

    def navigateDir(self, path):
        if os.path.isdir(path): 
            for root, dirs, files in os.walk(path):
                for filename in tqdm(files):
                    self.addTagsToImage(root + '/' + filename)
        else:
            self.addTagsToImage(path)

    def addTagsToImage(self, path):
        if not self.has_tags(path):
            status, tags = self.model.classify_image(path)
        else:
            return 'already tagged ' + path
        if status == 'success':
            process_image(path, tags)
            print('added ' + str(len(tags)) + ' tags to ' + path)
            return 'added ' + str(len(tags)) + ' tags to ' + path
        else:
            return 'failed to add tags for ' + path

    def has_tags(self, file):
        try:
            with exiftool.ExifToolHelper() as et:
                metadata = et.get_tags(file, tags=["IPTC:Keywords"])
                return bool(metadata and metadata[0].get('IPTC:Keywords'))
        except Exception as e:
            print(f"Error reading metadata from {file}: {e}")
            return False
    
def parseArgs():
    if len(sys.argv) < 2:
        print("no path")
        sys.exit()
    if not os.path.exists(sys.argv[1]):
        print('path does not exist')
        sys.exit()

if __name__ == "__main__":
    parseArgs()
    addAnimeTags = addAnimeTags()
    addAnimeTags.navigateDir(sys.argv[1])