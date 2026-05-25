# My dotfiles

This directory contains the dotfiles for my system

## Requirements

Ensure you have the following installed on your system

### Git

```
sudo pacman -S git
```

### Stow

```
sudo pacman -S stow
```

## Installation

First, check out the dotfiles repo in your $HOME directory using git

```
$ git clone git@github.com:isarker8/dotfiles.git
$ cd dotfiles
```

Then use GNU stow to create symlinks

```
$ stow .
```

# YouTube Tutorial

https://www.youtube.com/watch?v=y6XCebnB9gs
