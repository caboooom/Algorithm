#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;


int bfs(int w1, int w2, int n, vector<vector<int>>& graph) {
    graph[w1][w2] = 0;
    graph[w2][w1] = 0;
    
    vector<int> visited(n, 0);
    
    int count = 0;
    queue<int> q;
    q.push(w1);
    visited[w1] = 1;
    ++count;
    
    
    while(!q.empty()) {
        int cur = q.front();
        q.pop();
        for (int i = 0; i < n; i++) { 
            if (graph[cur][i] == 1 && visited[i] == 0) {
                q.push(i);
                visited[i] = 1;
                ++count;
            }
        }
    }
    
    graph[w1][w2] = 1;
    graph[w2][w1] = 1;
    
    return abs((n - count) - count);
}

int solution(int n, vector<vector<int>> wires) {
    int answer = 101;
    
    vector<vector<int>> graph(n, vector<int>(n, 0));
    
    for (int i = 0; i < wires.size(); i++) {
        int n1 = wires[i][0] - 1;
        int n2 = wires[i][1] - 1;
        graph[n1][n2] = 1;
        graph[n2][n1] = 1;
    }
    
    for (int i = 0; i < wires.size(); i++) {
        answer = min(answer, bfs(wires[i][0] - 1, wires[i][1] - 1, n, graph));
    }
    return answer;
}