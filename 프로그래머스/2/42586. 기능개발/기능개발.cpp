#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int count = 1;
    
    int next = (100 - progresses[0] + speeds[0] - 1) / speeds[0];
    
    for (int i = 1; i < progresses.size(); i++) {
        int curr = (100 - progresses[i] + speeds[i] - 1) / speeds[i];
        
        if (curr <= next) {
            ++count;
        } else {
            answer.push_back(count);
            count = 1;
            next = curr;
        }
    }
    
    answer.push_back(count);
    
    return answer;
}
