###### [N 皇后](https://leetcode-cn.com/problems/n-queens/)

```c++
vector<vector<string>> res;
vector<vector<string>> solveNQueens(int n) {
	vector<string> board(n, string(n, '.'));
    backtrack(board, 0);
    return res;
}
void backtrack(vector<string>& board, int row) {
    if (row == board.size()) {
        res.push_back(board);
        return;
    }
    int n = board[row].size();
    for (int col = 0; col < n; col++) {
        if (!isValid(board, row, col)) continue;
        board[row][col] = 'Q';
        backtrack(board, row + 1);
        board[row][col] = '.';
    }
}
bool isValid(vector<string>& board, int row, int col) {
    int n = board.size();
    // 检查列是否有皇后互相冲突
    for (int i = 0; i < n; i++) {
        if (board[i][col] == 'Q')
            return false;
    }
    // 检查右上方是否有皇后互相冲突
    for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
        if (board[i][j] == 'Q')
            return false;
    }
    // 检查左上方是否有皇后互相冲突
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 'Q')
            return false;
    }
    return true;
}
```

###### [解数独](https://leetcode-cn.com/problems/sudoku-solver/)

```c++

```

###### [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)

```c++
int n, m, ans;
int numIslands(vector<vector<char>>& grid) {
    if (!grid.size() || !grid[0].size()) return 0;
    n = grid.size(); m = grid[0].size(); ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '1') {
                dfs(grid, i, j);
                ans++;
            }
        }
    }
    return ans;
}
void dfs(vector<vector<char>> &grid, int row, int col) {
    if (row < 0 || col < 0 || row >= n || col >= m || grid[row][col] == '0') return;
    grid[row][col] = '0';
    dfs(grid, row, col - 1);
    dfs(grid, row - 1, col);
    dfs(grid, row, col + 1);
    dfs(grid, row + 1, col);
}
```

###### [岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/)

```c++
int n, m, ans, temp;
int maxAreaOfIsland(vector<vector<int>>& grid) {
    if (!grid.size() || !grid[0].size()) return 0;
    n = grid.size(); m = grid[0].size(); ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 1) {
                temp = 0;
                dfs(grid, i, j);
                ans = max(ans, temp);
            }
        }
    }
    return ans;
}
void dfs(vector<vector<int>>& grid, int row, int col) {
    if (row < 0 || row >= n || col < 0 || col >= m || grid[row][col] == 0) return;
    grid[row][col] = 0;
    temp++;
    dfs(grid, row, col - 1);
    dfs(grid, row, col + 1);
    dfs(grid, row - 1, col);
    dfs(grid, row + 1, col);
}
```

###### [统计封闭岛屿的数目](https://leetcode-cn.com/problems/number-of-closed-islands/)

```c++

```

