#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    
    int left = 0;
    int right = 1;
    int sum = left + right;
    
    while (true) {
        if (sum < n) {
            if (right > n) {
                break;
            }
            right++;
            sum += right;
        } else if (sum > n) {
            sum -= left;
            left++;
        } else {
            answer++;
            right++;
            sum += right;
        }
    }
    return answer;
}