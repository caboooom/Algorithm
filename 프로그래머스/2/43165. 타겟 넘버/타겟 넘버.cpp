#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int answer;
vector<int> gNumbers;

void dfs(vector<int> numbers, int idx, int sum, int target) {
    if (idx == numbers.size()) {
        if (sum == target) {
            ++answer;
        }
        return;
    }
    dfs(numbers, idx + 1, sum + numbers[idx], target);
    dfs(numbers, idx + 1, sum - numbers[idx], target);       
}

int solution(vector<int> numbers, int target) {
    gNumbers = numbers;
    answer = 0;
    
    dfs(numbers, 0, 0, target);
    
    
    return answer;
}