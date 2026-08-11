#!/usr/bin/env bash

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

## ALIASES

# Navigation Shortcuts
alias ..="cd .."
alias ...="cd ..."
