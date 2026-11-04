require("typst-preview").setup({
  open_cmd = "xdg-open %s",
})

-- Typst LSP configuration
if vim.fn.executable("tinymist") == 1 or vim.fn.executable("typst-lsp") == 1 then
  vim.lsp.config.tinymist = {
    cmd = { "tinymist" },
    filetypes = { "typst" },
    root_dir = function(fname)
      return vim.fs.dirname(vim.fs.find({ ".git", "*.typ" }, { upward = true, path = fname })[1])
    end,
  }
  vim.lsp.enable("tinymist")
end
