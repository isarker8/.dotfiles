# .dotfiles

Personal configuration files managed with [GNU Stow](https://www.gnu.org/software/stow/), built around a minimal `dwm` + `rofi` desktop.

## Dependencies

### Core

- [`dwm`](https://dwm.suckless.org/) — window manager

`dwm` is typically built from source with a local `config.h` and patches rather than installed from a package manager — clone, patch, `make`, `sudo make install`.

### Applications

| Tool | Purpose |
|---|---|
| [`alacritty`](https://alacritty.org/) | GPU-accelerated terminal emulator |
| [`dunst`](https://dunst-project.org/) | Lightweight notification daemon |
| [`mpv`](https://mpv.io/) | Media player |
| [`picom`](https://github.com/yshui/picom) | Compositor (transparency, shadows, vsync) |
| [`prayer-times`](https://github.com/) | Prayer time calculation/notification tool |
| [`redshift`](https://github.com/jonls/redshift) | Screen color temperature adjustment based on location/time |
| [`pywal`](https://github.com/dylanaraps/pywal) | Generates color schemes from wallpapers (`wal` command) |
| [`rofi`](https://github.com/davatorium/rofi) | Application launcher and window switcher |
| [`waterfox`](https://www.waterfox.net/) | Web browser |
| [`yazi`](https://yazi-rs.github.io/) | Terminal file manager |
| [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) | Media downloader |

### Arch Linux install

```bash
sudo pacman -S alacritty dunst mpv picom redshift python-pywal rofi yazi yt-dlp
# dwm is built from source — ['my dwm build'](https://github.com/isarker8/dwm)
# waterfox: available from the AUR (e.g. waterfox-bin)
# prayer-times: install from its own repo/AUR package if applicable
```

## Encrypted files

A few files in this repo contain personal data and are encrypted with [`git-crypt`](https://github.com/AGWA/git-crypt). They appear as unreadable binary blobs unless unlocked with the key (kept outside this repo). Without the key they simply stay encrypted — everything else in the repo is usable as-is.

See [`crypt.md`](crypt.md) for how encryption is managed in this repo.

## Installation

```bash
git clone https://github.com/isarker8/.dotfiles.git ~/.dotfiles
cd ~/.dotfiles
git-crypt unlock /path/to/dotfiles.key   # only if you have the key; otherwise skip

stow .
```

Stow will symlink each config into place under `$HOME`, matching the repo's directory structure (e.g. `.config/redshift/redshift.conf` → `~/.config/redshift/redshift.conf`).

## Notes

- `redshift` and `prayer-times` both rely on your latitude/longitude — set your own coordinates in their config files.
- Wallpaper-based theming is handled by `pywal`; run `wal -i /path/to/wallpaper` to regenerate colors, which feed into `dwm`/`dunst`/`rofi` styling where configured.
