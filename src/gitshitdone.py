import vim
import inspect

is_boards_open = False

def toggle_boards():
    global is_boards_open 

    if is_boards_open:
        vim.command(':bdelete')
        is_boards_open = False
    else:
        win_width = vim.current.window.width
        one_third = win_width // 3
        vim.command(':vsp Boards')
        board_window = vim.current.window
        board_window.width = one_third
        is_boards_open = True