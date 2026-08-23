#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    bool isFirstChar = true;
    for (int i = 0; i < s.size(); i++) {
        if (isFirstChar && s[i] != ' ') {
            answer += toupper(s[i]);
            isFirstChar = false;
        } else {
            answer += tolower(s[i]);
            if (s[i] == ' ') {
                isFirstChar = true;
            }
        }
    }
    return answer;
}