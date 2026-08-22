#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

# Setting default programs
export EDITOR="vim"
export VISUAL="vim"
export TERM="st"
export TERMINAL="st"
export BROWSER="waterfox"
export BROWSER2="helium"

# add scripts to path
export PATH="$XDG_CONFIG_HOME/scripts:$PATH"

# Created by `pipx` on 2026-05-12 14:43:12
export PATH="$PATH:/home/isarker/.local/bin"

# Setting env variable for Qt
export QT_QPA_PLATFORMTHEME="qt5ct"
