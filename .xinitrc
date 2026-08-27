export XDG_SESSION_TYPE=x11
export XDG_CURRENT_DESKTOP=dwm

if [ -z "${DBUS_SESSION_BUS_ADDRESS}" ] && command -v dbus-launch >/dev/null 2>&1; then
    eval "$(dbus-launch --sh-syntax --exit-with-session)"
fi

dbus-update-activation-environment \
    DISPLAY \
    XAUTHORITY \
    XDG_CURRENT_DESKTOP \
    XDG_SESSION_TYPE \
    XDG_RUNTIME_DIR

picom -b &
xrandr -s 1920x1080 &
redshift &
wal -R &
xbindkeys &
xrdb -merge ~/.Xresources &
clipmenud &
dwmblocks &
dunst &
prayer-times daemon &

exec dwm
