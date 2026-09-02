#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

# Setting default programs
export EDITOR="vim"
export VISUAL="vim"
export TERM="alacritty"
export TERMINAL="alacritty"
export BROWSER="vimb"

export PATH="$PATH:/home/isarker/.local/bin"

# Setting env variable for Qt
export QT_QPA_PLATFORMTHEME="qt5ct"
