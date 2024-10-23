# Auto Anime Tag

This was cloned from https://github.com/Epsp0/auto-tag-anime and modified to specifically work with Digikam on MacOS using IPTC:Keywords.

Automatically adds booru style tags to an image or directory of images by using this neural net model: https://github.com/KichangKim/DeepDanbooru

## Instructions

1. Download the v3-20211112-sgd-e28 model from https://github.com/KichangKim/DeepDanbooru, put the folder 
containing the model in the auto-tag-anime folder

```zsh
python3 -m venv ./env
source env/bin/activate
python setup.py install
```

## How to use
`python3 auto-tag-anime.py "example.jpg"`

`python3 auto-tag-anime.py "/path/to/directory/"`


## Notes
* See a list of tags the model will predict in 'tags.txt' inside of the deepdanbooru-v3 folder
* checks for images in subdirectories 
