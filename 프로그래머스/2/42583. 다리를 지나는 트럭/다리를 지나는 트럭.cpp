#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    queue<pair<int, int>> q; // 트럭무게, 내리는 초
    int count = 0;
    int curr_idx = 0;
    int number_of_truck = 0;
    int curr_sum_weight = 0;
    
    while (true) {
        count++;
        while (!q.empty() && q.front().second <= count) {
            curr_sum_weight -= q.front().first;
            number_of_truck--;
            q.pop();
        }
        
        if (number_of_truck < bridge_length 
            && curr_sum_weight + truck_weights[curr_idx] <= weight) {
            q.push({truck_weights[curr_idx], count + bridge_length});
            curr_sum_weight += truck_weights[curr_idx];
            number_of_truck++;
            
            if (curr_idx == truck_weights.size() - 1) {
                return count + bridge_length;
            }
            
            curr_idx++;
        } 
        
    }
    
    return count;
}
