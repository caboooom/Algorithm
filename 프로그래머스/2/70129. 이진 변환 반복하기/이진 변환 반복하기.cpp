#include <string>
#include <vector>

using namespace std;

string binary_change(int n) {
    string result;
    while (n > 0) {
        result += to_string(n % 2);
        n /= 2;
    }
    return result;
}

vector<int> solution(string s) {
    int count = 0;
    int zero_count = 0;
    while (s != "1") {
        int one_count = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '1') {
                one_count++;
            } else {
                zero_count++;
            }
        }
        s = binary_change(one_count);
        count++;
    }
    return {count, zero_count};
}