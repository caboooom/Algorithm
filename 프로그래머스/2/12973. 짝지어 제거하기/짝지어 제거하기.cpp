#include <string>
#include <stack>
using namespace std;

int solution(string s)
{
    stack<char> st;
    st.push(s[0]);
    int idx = 1;
    while (idx < s.size()) {
        if (!st.empty() && st.top() == s[idx]) {
            st.pop();
        } else {
            st.push(s[idx]);
        }
        idx++;
    }
    return st.empty();
}