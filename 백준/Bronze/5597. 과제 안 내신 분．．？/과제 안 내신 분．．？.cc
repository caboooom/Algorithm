#include <iostream>

using namespace std;


int main() {
  int students[31] = {0,};
  int temp;
  for(int i=0;i<28;i++){
    cin >> temp;
    students[temp] = 1;
  }
  for(int i=1;i<31;i++){
    if(students[i] == 0){
      cout << i << "\n";
    }
  }
  
  return 0;
}