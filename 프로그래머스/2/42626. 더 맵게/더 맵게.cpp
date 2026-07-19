#include <string>
#include <vector>
#include <queue>

using namespace std;
int solution(vector<int> scoville, int K) {
    
    priority_queue<int, vector<int>, greater<int>> minHeap;
    
    for (int num : scoville) {
        minHeap.push(num);
    }
    int answer = 0;
    while (minHeap.top() < K) {
        if (minHeap.size() < 2) {
            return -1;
        }
        int min1 = minHeap.top();
        minHeap.pop();
        int min2 = minHeap.top();
        minHeap.pop();
        int scoville = min1 + (min2 * 2);
        minHeap.push(scoville);
        ++answer;
    }
    return answer;
}