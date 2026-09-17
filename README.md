# .dotfiles

Personal configuration files managed with [GNU Stow](https://www.gnu.org/software/stow/), built around a minimal `dwm` + `st` + `dmenu` (suckless) desktop.

## Dependencies

### Core (suckless stack)

- [`dwm`](https://dwm.suckless.org/) — window manager
- [`st`](https://st.suckless.org/) — terminal (used for suckless tools; day-to-day terminal is Alacritty, see below)
- [`dmenu`](https://tools.suckless.org/dmenu/) — application launcher

These are typically built from source with local `config.h` patches rather than installed from a package manager — clone, patch, `make`, `sudo make install` for each.

### Applications

| Tool | Purpose |
|---|---|
| [`alacritty`](https://alacritty.org/) | GPU-accelerated terminal emulator |
| [`dunst`](https://dunst-project.org/) | Lightweight notification daemon |
| [`mpv`](https://mpv.io/) | Media player |
| [`picom`](https://github.com/yshui/picom) | Compositor (transparency, shadows, vsync) |
| [`prayer-times`](https://github.com/) | Prayer time calculation/notification tool |
| [`qutebrowser`](https://www.qutebrowser.org/) | Keyboard-driven, vim-like web browser |
| [`redshift`](https://github.com/jonls/redshift) | Screen color temperature adjustment based on location/time |
| [`pywal`](https://github.com/dylanaraps/pywal) | Generates color schemes from wallpapers (`wal` command) |
| [`yazi`](https://yazi-rs.github.io/) | Terminal file manager |
| [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) | Media downloader |

### Arch Linux install

```bash
sudo pacman -S alacritty dunst mpv picom qutebrowser redshift python-pywal yazi yt-dlp
# dwm, st, dmenu are built from source — see suckless.org or your own fork/patches
# prayer-times: install from its own repo/AUR package if applicable
```

Adjust package names if you're on a different distro (Debian/Ubuntu use `apt`, Fedora `dnf`, etc.) — most of these are packaged under the same or a very similar name.

## Sensitive / private files

A few files contain personal data (bookmarks, location coordinates for `redshift`/`prayer-times`, and an unlock helper script) and are encrypted in this repo with [`git-crypt`](https://github.com/AGWA/git-crypt):

- `.bmks/urls`
- `.config/prayer-times/config.toml`
- `.config/redshift/redshift.conf`
- `scripts/unlock`

These will appear as unreadable binary blobs unless unlocked with the key (kept outside this repo).

```bash
git clone https://github.com/isarker8/.dotfiles.git ~/.dotfiles
cd ~/.dotfiles
git-crypt unlock /path/to/dotfiles.key
```

If you don't have the key, these four files will simply stay encrypted — everything else in the repo is usable as-is.

## Installation

```bash
git clone https://github.com/isarker8/.dotfiles.git ~/.dotfiles
cd ~/.dotfiles
git-crypt unlock /path/to/dotfiles.key   # only if you have the key; otherwise skip

stow .
```

Stow will symlink each config into place under `$HOME`, matching the repo's directory structure (e.g. `.config/redshift/redshift.conf` → `~/.config/redshift/redshift.conf`).

## Notes

- `redshift` and `prayer-times` both rely on your latitude/longitude — these live in the encrypted config files above, so update them post-unlock with your own coordinates.
- Wallpaper-based theming is handled by `pywal`; run `wal -i /path/to/wallpaper` to regenerate colors, which feed into `dwm`/`dunst`/`st` styling where configured.
