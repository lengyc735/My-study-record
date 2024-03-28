import tkinter as tk
from tkinter import messagebox
import random

def is_valid(board, row, col, num):
    # 检查行
    if num in board[row]:
        return False

    # 检查列
    if num in [board[i][col] for i in range(9)]:
        return False

    # 检查九宫格
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0  # 回溯
                return False
    return True

def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)
    for _ in range(40):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board

class SudokuUI:
    def __init__(self, root):
        self.root = root
        self.root.title("数独游戏")

        self.board = generate_sudoku()

        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                cell = tk.Entry(root, width=5, font=('Arial', 16, 'bold'))
                cell.grid(row=i, column=j)
                row.append(cell)
            self.cells.append(row)

        self.fill_board()

        solve_button = tk.Button(root, text="解决", command=self.solve_board)
        solve_button.grid(row=9, columnspan=9)

    def fill_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.cells[i][j].insert(0, str(self.board[i][j]))
                    self.cells[i][j].config(state='disabled')

    def solve_board(self):
        for i in range(9):
            for j in range(9):
                value = self.cells[i][j].get()
                if value == '':
                    continue

                # 检查用户输入的值是否是1到9之间的数字
                if not value.isdigit() or int(value) < 1 or int(value) > 9:
                    messagebox.showinfo("提示", "请输入1到9之间的数字！")
                    return

                self.board[i][j] = int(value)

        if solve_sudoku(self.board):
            self.fill_board()
        else:
            messagebox.showinfo("提示", "此数独无解或者解有误！")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuUI(root)
    root.mainloop()
