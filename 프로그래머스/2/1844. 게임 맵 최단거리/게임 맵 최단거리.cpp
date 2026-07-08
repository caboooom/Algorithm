#include<vector>
#include<queue>
using namespace std;

struct Position {
    int row;
    int col;
    int dist;
    
    Position(int row, int col, int dist) {
        this->row =row;
        this->col = col;
        this->dist = dist;
    }
};

int solution(vector<vector<int> > maps)
{
    int answer = -1; // 목적지에 도착 불가능한 경우에는 -1을 리턴
    queue<Position> q;
    int dRow[4] = {-1, 0, 1, 0};
    int dCol[4] = {0, 1, 0, -1};
    
    int n = maps.size();
    int m = maps[0].size();
    int cRow = 0;
    int cCol = 0;
    
    q.push(Position(cRow, cCol, 1));
    maps[cRow][cCol] = -1;
    
    while (!q.empty()) {
        Position cPos = q.front();
        q.pop();
        cRow = cPos.row;
        cCol = cPos.col;
        if (cRow == n-1 && cCol == m-1) {
            return cPos.dist;
        }
        
        for (int i = 0; i < 4; i++) {
            int nRow = cRow + dRow[i];
            int nCol = cCol + dCol[i];
            if (nRow >= 0 && nRow < n && nCol >= 0 && nCol < m) {
                if (maps[nRow][nCol] == 1) {
                    q.push(Position(nRow, nCol, cPos.dist + 1));
                    maps[nRow][nCol] = 0;
                }
            }
        }
    }
    
    return answer;
}