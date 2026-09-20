#!/usr/bin/env bash

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'

# Import pywal colors if the cache file exists
[ -f ~/.cache/wal/colors.sh ] && source ~/.cache/wal/colors.sh 
NEWLINE=$'\n'
PS1='${NEWLINE}\[\e[48;5;0m\e[38;5;6m\]$(date +%_I:%M%P) \[\e[38;5;14m\]\u \[\e[38;5;6m\]\w \[\e[0m\]${NEWLINE}\[\e[1;36m\]❯ \[\e[0m\]'

# Reminders
cat ~/reminders

# Import colorscheme from 'wal' asynchronously
# &   # Run the process in the background.
# ( ) # Hide shell job control messages.
# Not supported in the "fish" shell.
(cat ~/.cache/wal/sequences &)

# Alternative (blocks terminal for 0-3ms)
# cat ~/.cache/wal/sequences

# To add support for TTYs this line can be optionally added.
source ~/.cache/wal/colors-tty.sh

## ALIASES

# Safety
alias rm='trash-put'
alias cp='cp -i'
alias mv='mv -i'
# -> Prevents accidentally clobbering files.
alias mkdir='mkdir -p'

# Navigation Shortcuts
alias ..="cd .."

# Cd Suckless
alias cds="cd ~/clones/Suckless"
