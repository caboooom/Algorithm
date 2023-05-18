#include <iostream>

using namespace std;

int main(){
  int n; cin >> n;

  int x = 666;
  int cnt = 0;
  while(1){
    string temp = to_string(x);
    if (temp.find("666") != string::npos){
      // 666이 존재하면,
      cnt += 1;
      if (cnt == n) {
        cout << x;
        break;
      }
    }
    x += 1;
  }
  return 0;
}