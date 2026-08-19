#include <string>
#include <vector>
#include <functional>

using namespace std;

int solution(vector<int> citations) {
    int n = citations.size();
    int answer = n;
    sort(citations.begin(), citations.end());
    for (int i = n - 1; i >= 0; i--) {
        if (citations[n - i - 1] >= answer) {
            return answer;
        } else {
            --answer;
        }
    }
    return answer;
}