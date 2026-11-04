-- 1. General Neovim UI Settings
vim.opt.termguicolors = true
vim.opt.number = true
vim.opt.relativenumber = true
vim.g.mapleader = " "

-- Transparent Background Overrides
vim.api.nvim_create_autocmd("ColorScheme", {
  pattern = "*",
  callback = function()
    vim.cmd([[
      highlight Normal guibg=NONE ctermbg=NONE
      highlight NormalNC guibg=NONE ctermbg=NONE
      highlight NormalFloat guibg=NONE ctermbg=NONE
      highlight SignColumn guibg=NONE ctermbg=NONE
      highlight EndOfBuffer guibg=NONE ctermbg=NONE
    ]])
  end,
})

require("config.options")
require("config.keybinds")
require("plugins").setup()
------------------------------
require("config.neopywal")
require("config.telescope")
require("config.colorizer")
require("config.lualine")
require("config.typst")
