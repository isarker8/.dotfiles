#!/usr/bin/env bash

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# Running fastfetch on startup
if [ -f /usr/bin/fastfetch ]; then
	fastfetch
fi

# Created by `pipx` on 2026-05-12 14:43:12
export PATH="$PATH:/home/isarker/.local/bin"

# Initializing starship
eval "$(starship init bash)"

## ALIASES

# Navigation Shortcuts
alias ..="cd .."
alias ...="cd ..."
