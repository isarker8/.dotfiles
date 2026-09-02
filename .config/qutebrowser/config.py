import os
import subprocess

config.load_autoconfig(False)

# Load Pywal colors from the fast raw colors file
wal_file = os.path.expanduser('~/.cache/wal/colors')

colors = []
if os.path.exists(wal_file):
    with open(wal_file) as f:
        colors = [line.strip() for line in f if line.strip()]

def c_get(idx, fallback="#000000"):
    if idx < len(colors):
        return colors[idx]
    return fallback

bg_color = c_get(0, "#101010")
fg_color = c_get(7, "#e0e0e0")

c.colors.statusbar.normal.bg = "#00000000"
c.colors.statusbar.command.bg = "#00000000"
# c.colors.statusbar.normal.bg = bg_color
# c.colors.statusbar.command.bg = bg_color
c.colors.statusbar.command.fg = fg_color
c.colors.statusbar.normal.fg = c_get(14, fg_color)
c.colors.statusbar.passthrough.fg = c_get(14, fg_color)
c.colors.statusbar.url.fg = c_get(13, fg_color)
c.colors.statusbar.url.success.https.fg = c_get(13, fg_color)
c.colors.statusbar.url.hover.fg = c_get(12, fg_color)
c.statusbar.show = "always"
c.colors.tabs.even.bg = "#00000000" # transparent tabs!!
c.colors.tabs.odd.bg = "#00000000"
c.colors.tabs.bar.bg = "#00000000"
# c.colors.tabs.even.bg = bg_color
# c.colors.tabs.odd.bg = bg_color
c.colors.tabs.even.fg = c_get(0, "#808080")
c.colors.tabs.odd.fg = c_get(0, "#808080")
c.colors.tabs.selected.even.bg = fg_color
c.colors.tabs.selected.odd.bg = fg_color
c.colors.tabs.selected.even.fg = bg_color
c.colors.tabs.selected.odd.fg = bg_color
c.colors.hints.bg = bg_color
c.colors.hints.fg = fg_color
c.hints.border = fg_color
c.tabs.show = "multiple"

c.colors.completion.item.selected.match.fg = c_get(6, fg_color)
c.colors.completion.match.fg = c_get(6, fg_color)

c.colors.tabs.indicator.start = c_get(10, fg_color)
c.colors.tabs.indicator.stop = c_get(8, fg_color)
c.colors.completion.odd.bg = bg_color
c.colors.completion.even.bg = bg_color
c.colors.completion.fg = fg_color
c.colors.completion.category.bg = bg_color
c.colors.completion.category.fg = fg_color
c.colors.completion.item.selected.bg = bg_color
c.colors.completion.item.selected.fg = fg_color

c.colors.messages.info.bg = bg_color
c.colors.messages.info.fg = fg_color
c.colors.messages.error.bg = bg_color
c.colors.messages.error.fg = fg_color
c.colors.downloads.error.bg = bg_color
c.colors.downloads.error.fg = fg_color

c.colors.downloads.bar.bg = bg_color
c.colors.downloads.start.bg = c_get(10, fg_color)
c.colors.downloads.start.fg = fg_color
c.colors.downloads.stop.bg = c_get(8, fg_color)
c.colors.downloads.stop.fg = fg_color

c.colors.tooltip.bg = bg_color
c.colors.webpage.bg = bg_color

c.url.start_pages = ["file:///home/isarker/.dotfiles/start.html"]
c.url.default_page = "file:///home/isarker/.dotfiles/start.html"
c.content.local_content_can_access_remote_urls = True

c.tabs.title.format = "{audio}{current_title}"
c.fonts.web.size.default = 20
config.set('scrolling.smooth', True)

c.url.searchengines = {
# note - if you use duckduckgo, you can make use of its built in bangs, of which there are many! https://duckduckgo.com/bangs
        'DEFAULT': 'https://duckduckgo.com/?q={}',
        '!aw': 'https://wiki.archlinux.org/?search={}',
        '!apkg': 'https://archlinux.org/packages/?sort=&q={}&maintainer=&flagged=',
        '!yt': 'https://www.youtube.com/results?search_query={}',
        }

c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']

c.auto_save.session = True # save tabs on quit/restart

# keybinding changes
config.bind('o', 'cmd-set-text -s :open')
config.bind('h', 'history')
config.bind('cc', 'hint images spawn sh -c "cliphist link {hint-url}"')
config.bind('T', 'hint links tab')
config.bind('pP', 'open -- {primary}')
config.bind('pp', 'open -- {clipboard}')
config.bind('pt', 'open -t -- {clipboard}')

# Watch and Download Hints (<ctrl-y> keymap)
config.bind('<ctrl-y>v', 'hint links spawn mpv "{hint-url}"')
config.bind('<ctrl-y>a', 'hint links spawn mpv --no-video "{hint-url}"')
config.bind('<ctrl-y>V', 'hint links spawn sh -c \'yt-dlp "{hint-url}" && notify-send "yt-dlp" "Video download complete!"\'')
config.bind('<ctrl-y>A', 'hint links spawn sh -c \'yt-dlp -x --audio-format mp3 "{hint-url}" && notify-send "yt-dlp" "Audio download complete!"\'')

config.bind('tT', 'config-cycle tabs.position top left')
config.bind('gJ', 'tab-move +')
config.bind('gK', 'tab-move -')
config.bind('gm', 'tab-move')

# dark mode setup
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.policy.images = 'never'
config.set('colors.webpage.darkmode.enabled', False, 'file://*')

# styles, cosmetics
# c.content.user_stylesheets = ["~/.config/qutebrowser/styles/youtube-tweaks.css"]
c.tabs.padding = {'top': 5, 'bottom': 5, 'left': 9, 'right': 9}
c.tabs.indicator.width = 0 # no tab indicators
c.window.transparent = True
c.tabs.width = '7%'

# fonts
c.fonts.default_family = ["JetBrainsMono Nerd Font"]
c.fonts.default_size = '13pt'
c.fonts.web.family.fixed = 'JetBrainsMono Nerd Font'
c.fonts.web.family.sans_serif = 'JetBrainsMono Nerd Font'
c.fonts.web.family.serif = 'JetBrainsMono Nerd Font'
c.fonts.web.family.standard = 'JetBrainsMono Nerd Font'

# privacy - adjust these settings based on your preference
# config.set("completion.cmd_history_max_items", 0)
config.set("content.private_browsing", False)
config.set("content.webgl", False, "*")
config.set("content.canvas_reading", False)
config.set("content.geolocation", False)
config.set("content.webrtc_ip_handling_policy", "default-public-interface-only")
config.set("content.cookies.accept", "all")
config.set("content.cookies.store", True)
# config.set("content.javascript.enabled", False) # tsh keybind to toggle

# Adblocking info -->
# For yt ads: place the greasemonkey script yt-ads.js in your greasemonkey folder (~/.config/qutebrowser/greasemonkey).
# The script skips through the entire ad, so all you have to do is click the skip button.
# Yeah it's not ublock origin, but if you want a minimal browser, this is a solution for the tradeoff.
# You can also watch yt vids directly in mpv, see qutebrowser FAQ for how to do that.
# If you want additional blocklists, you can get the python-adblock package, or you can uncomment the ublock lists here.
c.content.blocking.enabled = True
c.content.blocking.method = 'adblock' # uncomment this if you install python-adblock
c.content.blocking.adblock.lists = [
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/legacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2022.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2023.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2024.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-cookies.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-others.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/quick-fixes.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt"]
