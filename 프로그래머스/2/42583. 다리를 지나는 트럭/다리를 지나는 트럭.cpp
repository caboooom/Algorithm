#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int currSec = 0;
    int currWeight = 0;
    int num = 0;
    queue<pair<int, int>> q; // {트럭 인덱스, 빠져나갈 시간}
    
    while (currSec < 100000001) {
        ++currSec;
        
        if (!q.empty() && q.front().second == currSec) {
            currWeight -= truck_weights[q.front().first];
            ;
            if (q.front().first == truck_weights.size() - 1) {
                break;
            }
            q.pop();
        }
        
        if (num < truck_weights.size() && 
            currWeight + truck_weights[num] <= weight && 
            q.size() < bridge_length) {
            q.push({num, currSec + bridge_length});
            currWeight += truck_weights[num];
            num++;
        }
        
    }
    
    return currSec;
}