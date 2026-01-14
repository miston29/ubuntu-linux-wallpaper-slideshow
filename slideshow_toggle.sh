#!/bin/bash

SCRIPT_FULL_PATH="/home/CHANGE/PATH/TO/slideshow.py"
JSON_PATH="/homeCHANGE/PATH/TO/slideshow_settings.json"

PID=$(pgrep -f "python3 $SCRIPT_FULL_PATH")

if [ -z "$PID" ]; then
    python3 "$SCRIPT_FULL_PATH" &
    notify-send "Slideshow" "Enabled"
else
    kill $PID
    DEFAULT_IMG=$(grep -oP '(?<="default_image": ")[^"]*' "$JSON_PATH")
    
    gsettings set org.gnome.desktop.background picture-uri "file://$DEFAULT_IMG"
    gsettings set org.gnome.desktop.background picture-uri-dark "file://$DEFAULT_IMG"
    gsettings set org.gnome.desktop.background picture-options "zoom"
    
    notify-send "Slideshow" "Disabled - Reset to default"
fi
