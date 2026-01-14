from os import listdir, chdir, path
from random import choice
from time import sleep
from subprocess import run
import imagesize
import json

def scaling(image_path, sheight, swidth):
	try:
		width, height = imagesize.get(image_path)
				    
		if width <= 0 or height <= 0:
			return "zoom"
				
		if width < (swidth * 0.8) and height < (sheight * 0.8):
			return "centered"
				

		screen_ratio = swidth/swidth
		img_ratio = width / height
		if abs(img_ratio - screen_ratio) > 0.6:
			return "scaled"
				
		return "zoom"
		        
	except Exception:
		return "zoom"


def main(PATH, INTERVAL, SHEIGHT, SWIDTH):
	image_list = listdir(PATH)

	while True:
		image = choice(image_list)
		
		full_path = f"{PATH}/{image}"
		uri = f"file://{full_path}"
		
		run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', uri])
		run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri-dark', uri])
		run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-options', scaling(full_path, SHEIGHT, SWIDTH)])
		
		sleep(INTERVAL)


if __name__ == "__main__":
	chdir(path.dirname(path.abspath(__file__)))

	with open("slideshow_settings.json", "r") as fl:
		config = json.load(fl)

	main(config["slideshow_folder"], config["sleep_time"], config["screen_height"], config["screen_width"])
	

