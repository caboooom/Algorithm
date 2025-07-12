#include <iostream>
#include <cstring>
#include <stack>

using namespace std;

struct Point {
  int x, y;
};

int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };
int n;
int m;
#define MAX_N 500
#define MAX_M 500
int board[MAX_N][MAX_M];
bool visited[MAX_N][MAX_M];
int maxSize = 0;
int count = 0;

void dfs(int x, int y) {
  int size = 0;
  
  stack<Point> stack;
  stack.push({ x, y });
  visited[x][y] = true;
  
  while (!stack.empty()) {
    int cx = stack.top().x;
    int cy = stack.top().y;
    stack.pop();
    size++;
    for (int i = 0; i < 4; i++) {
      int nx = cx + dx[i];
      int ny = cy + dy[i];
      if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
        visited[nx][ny] = true;
        if (board[nx][ny] == 1) {
          stack.push({ nx, ny });
        }
      }
    }
    
  }
  count++;
  maxSize = max(maxSize, size);
}


int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> board[i][j];
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (board[i][j] == 1 && !visited[i][j]) {
        dfs(i, j);
      }
    }
  }
  cout << count << endl << maxSize;
  return 0;
}