#include <iostream>

using namespace std;

string input = "";
string alphabets = "abcdefghijklmnopqrstuvwxyz";
int result[26];

int main() {
  fill(result, result + 26, -1);
  
  cin >> input;
  for (int i = 0; i < 100; i++) {
    int currIdx = input[i] - 97;
    if (result[currIdx] < 0) {
      result[currIdx] = i;
    }
  }
  for (int i = 0; i < 26; i++) {
    cout << result[i] << " ";
  }
  return 0;
}