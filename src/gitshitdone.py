import vim
import inspect

def show_boards():
    win_width = vim.current.window.width
    one_third = win_width // 3
    vim.command(':vsp Boards')
    vim.command(f':vertical resize {one_third}')