let mapleader = " "

nnoremap <leader>cd :Ex<CR>

" Yank via OSCYank
nmap <leader>y <Plug>OSCYankOperator
vmap <leader>y <Plug>OSCYankVisual

" Map <leader>v to compile and view the current Typst file
nnoremap <leader>v :silent !typst watch % > /dev/null 2>&1 & zathura %:r.pdf &<CR>

