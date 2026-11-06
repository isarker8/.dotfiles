" 1. Define the servers
let lspServers = [
      \ #{
      \   name: 'tinymist',
      \   filetype: ['typst'],
      \   path: 'tinymist',
      \   args: []
      \ }
      \ ]

" 2. Configure LSP behavior when it starts
autocmd User LspSetup call LspAddServer(lspServers)
autocmd User LspSetup call LspOptionsSet(#{
    \   autoHighlightDiags: v:true,
    \   diagSignErrorText: '✘',
    \   diagSignWarningText: '▲',
    \   diagSignInfoText: '»',
    \   diagSignHintText: '⚑',
    \ })

" 3. Key mappings
nnoremap gd :LspGotoDefinition<CR>
nnoremap gr :LspShowReferences<CR>
nnoremap K  :LspHover<CR>
nnoremap gl :LspDiag current<CR>
nnoremap <leader>nd :LspDiag next \| LspDiag current<CR>
nnoremap <leader>pd :LspDiag prev \| LspDiag current<CR>
inoremap <silent> <C-Space> <C-x><C-o>

" 4. Automatically trigger omnifunc completion while typing
set completeopt=menu,menuone,noselect
autocmd FileType typst setlocal omnifunc=lsp#complete

" This map allows you to press Tab to trigger the LSP completion menu
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<C-x>\<C-o>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

