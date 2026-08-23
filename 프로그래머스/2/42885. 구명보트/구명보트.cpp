#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    sort(people.begin(), people.end());
    int answer = 0;
    int p_left = 0;
    int p_right = people.size() - 1;
    while (p_left <= p_right) {
        int weight1 = people[p_left];
        int weight2 = people[p_right];
        if (weight1 + weight2 <= limit) {
            p_left++;
            p_right--;
        } else {
            p_right--;
        }
        answer++;
    }
    
    return answer;
}