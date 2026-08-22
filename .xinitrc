export XDG_SESSION_TYPE=x11

picom -b &
xrandr -s 1920x1080 &
redshift &
wal -R &
prayer-times daemon &
xbindkeys &
xrdb -merge ~/.Xresources &
dwmblocks &
exec dwm
