#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> gDungeons;
vector<int> visited;
int answer;

// hp = 현재 남은 피로도 , count = 지금까지 돈 던전 수
void dfs(int hp, int count) {
    answer = max(answer, count);
    for (int i = 0; i < gDungeons.size(); i++) {
        if (visited[i]) {
            continue;
        }
        if (gDungeons[i][0] > hp) {
            continue;
        } 
        visited[i] = 1;
        dfs(hp - gDungeons[i][1], count+ 1);
        visited[i] = 0;
    }
}

int solution(int k, vector<vector<int>> dungeons) {
    
    gDungeons = dungeons;
    visited = vector<int>(dungeons.size(), 0);
    dfs(k, 0);
    
    
    return answer;
}