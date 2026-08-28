#include <string>
#include <vector>
#include <stack>

using namespace std;

bool is_correct(string s) {
    
    stack<char> st;
    for (int i = 0; i < s.size(); i++) {
        char c = s[i];
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else {
            if (st.empty()) {
                return false;
            }
            if (c == ')') {
                if (st.top() != '(') {
                    return false;
                }
                st.pop();
            } else if (c == ']') {
                if (st.top() != '[') {
                    return false;
                }
                st.pop();
            } else {
                if (st.top() != '{') {
                    return false;
                }
                st.pop();
            }
        }
    }
    return st.empty();
    
}

int solution(string s) {
    int answer = 0;
    
    int pointer = 0;
    while (pointer < s.size()) {
        answer += is_correct(s.substr(pointer) + s.substr(0, pointer));
        pointer++;
    }
    
    return answer;
}