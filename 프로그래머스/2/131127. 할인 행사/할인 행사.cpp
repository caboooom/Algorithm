#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    map<string, int> wantmap;
    for (int i = 0; i < want.size(); i++) {
        wantmap[want[i]] = number[i];
    }
    
    map<string, int> windowmap;
    for (int i = 0; i < 10; i++) {
        windowmap[discount[i]]++;
    }
    if (wantmap == windowmap) {
        answer++;
    }
    
    for (int i = 10; i < discount.size(); i++) {
        windowmap[discount[i-10]]--;
        if (windowmap[discount[i-10]] == 0) {
            windowmap.erase(discount[i-10]);
        }
        if (i < discount.size()) {
            windowmap[discount[i]]++;
        }
        if (wantmap == windowmap) {
            answer++;
        }
    }
    return answer;
}