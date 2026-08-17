#include <string>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 1;
    
    priority_queue<int> pq;
    queue<pair<int,int>> q;
    
    for (int i = 0; i < priorities.size(); i++) {
        pq.push(priorities[i]);
        q.push({priorities[i], i});
    }
    
    while(!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();
        
        int priority = cur.first;
        int idx = cur.second;
        
        if (priority < pq.top()) {
            q.push({priority, idx});
        } else {
            if (idx == location) {
                return answer;
            } else {
                pq.pop();
                ++answer;
            }
            
        }
    }
    return answer;
}