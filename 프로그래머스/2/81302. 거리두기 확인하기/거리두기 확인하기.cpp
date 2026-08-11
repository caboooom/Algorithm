#include <string>
#include <vector>
#include <queue>

using namespace std;

int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, 1, 0, -1};

struct Point {
    int row;
    int col;
    int dist;
};

bool bfs(int startRow, int startCol, vector<string>& place) {
    
    queue<Point> q;
    bool visited[5][5] = {false};
 
    q.push({startRow, startCol, 0});
    visited[startRow][startCol] = true;
    
    while(!q.empty()) {
        int curRow = q.front().row;
        int curCol = q.front().col;
        int curDist = q.front().dist;
        q.pop();
        if (curDist > 0 && place[curRow][curCol] == 'P') {
            return false;
        }
        if (curDist < 2) {
            for (int i = 0; i < 4; i++) {
                int nextRow = curRow + dr[i];
                int nextCol = curCol + dc[i];
                if (nextRow >= 0 && nextRow < 5 &&
                   nextCol >= 0 && nextCol < 5 &&
                    !visited[nextRow][nextCol] &&
                   place[nextRow][nextCol] != 'X') {
                    q.push({nextRow, nextCol, curDist + 1});
                    visited[nextRow][nextCol] = true;
                }
            }
        }
    }
    
    return true;
}

int checkPlace(vector<string>& place) {
    
    
    
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if(place[i][j] == 'P' && // bfs 는 P에서부터 돌려야함.
               !bfs(i, j, place)) {
                return 0;
            }
        }
    }  
    
    return 1;
}

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    
    for (int i = 0; i < 5; i++) {
        answer.push_back(checkPlace(places[i]));
    }
    
    return answer;
}

