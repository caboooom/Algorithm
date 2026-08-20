#include <string>
#include <vector>

using namespace std;

string binary_change(int num_of_one) {
  // 1이 될때까지 2로 나눈 나머지를 나열한 뒤, 뒤집으면 됨. 그런데, 뒤집을 필요 없음. 왜냐면 문자열에서 1과 0의 갯수만 중요하기 때문에
    string result;
    while (num_of_one > 0) {
        result += to_string(num_of_one % 2);
        num_of_one /= 2;
    }
    return result;
} 

vector<int> solution(string s) {
    int num_of_zero = 0;
    int count = 0;
    while (s != "1") {
        int num_of_one = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '1') {
                num_of_one += 1;
            } else {
                num_of_zero += 1;
            }
        }
        s = binary_change(num_of_one);
        count++;
    }
    return {count, num_of_zero};
}