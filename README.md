# Ubuntu Wallpaper Slideshow Toggle


A small script and all that can enable or disable wallpaper slideshow using a desktop icon as toggle button.


### Files

* slideshow.py: main script with scaling function in case image is larger than screen size
* slideshow_settings.json: Configuration file. set wallpaper directory, default wallpaper, timeout, screen size
* slideshow_toggle.sh: A shell script that acts as the bridge.
* walls.desktop: The desktop entry file that creates the clickable icon.


## Setup Instructions

Follow these steps to get your slideshow toggle running:

#### 1. file organization
- place `slideshow.py` and `slideshow_settings.json` in same directory of choice.
- `slideshow_toggle.sh` can be placed anywhere
- `walls.desktop` is a desktop entry file and must be placed in desktop

#### 2. settings configuration
- Open `slideshow_settings.json` and update the `slideshow_folder` path to the directory where your wallpapers are stored
- set path of your default wallpaper in `default_wallpaper`
- set screen size
- set timeout
```
{
    "slideshow_folder": "/usr/share/backgrounds",
    "default_image": "/usr/share/backgrounds/warty-final-ubuntu.png",
    "screen_height": 1080,
    "screen_width" : 1920,
    "sleep_time": 60
}
```
above example uses ubuntu's default wallpapers 


#### 3. Update the Toggle Script
Open `slideshow_toggle.sh` and update the absolute paths for `slideshow.py` and the `slideshow_settings.json`:

```
SCRIPT_FULL_PATH="/path/to/your/slideshow.py"
JSON_PATH="/path/to/your/slideshow_settings.json"
```

#### 4. Update the Desktop Entry
Open walls.desktop using any text eidtor and change the Exec line to point to the location of `slideshow_toggle.sh`:

```
Exec=/path/to/your/slideshow_toggle.sh
```

#### 5. Permissions and Activation
grant appropriate permissions to `slideshow_toggle.sh` and `walls.desktop` to make them functional:

- for `slideshow_settings.sh`:
    - through terminal: `chmod +x slideshow_toggle.sh`
    - through GUI: right click > permissions tab > Allow executing file as program

- for `walls.desktop`:
    - right click `walls.desktop` and select "Allow Launching".

---
