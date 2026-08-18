#include<string>
#include <stack>

using namespace std;

bool solution(string s)
{
    stack<char> my_stack;

    for (int i = 0; i < s.size(); i++) {
        char c = s[i];
        if (c == '(') {
            my_stack.push(c);
        } else {
            if (my_stack.empty()) {
                return false;
            }
            my_stack.pop();
        }
    }

    return my_stack.empty();
}