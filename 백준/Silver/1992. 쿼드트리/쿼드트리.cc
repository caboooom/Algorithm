#include <iostream>
#include <string>
#include <vector>

using namespace std;

char table[64][64];

string quad(int row, int col, int qSize){ // 시작행, 시작열, 체크할 영역 크기
  
  string result; result += '(';

  int checkSize = qSize/2;
  
  int startR[4] = {row, row, row+checkSize, row+checkSize};
  int startC[4] = {col, col+checkSize, col, col+checkSize};

  for(int k=0; k<4; k++){
      //current row, current col
    int cr = startR[k]; int cc = startC[k];
    char first = table[cr][cc];
    bool flag = true;
    for(int i=cr; i<cr+checkSize; i++){
      for(int j=cc; j<cc+checkSize; j++){
        if (table[i][j]!=first){
          result += quad(cr, cc, checkSize);
          flag = false;
          break;
        }
      }
    if (!flag) break;
    }
  if (flag) result += first;
  }
return result+')';
}

int main() {

  // 인풋 입력받고 저장하기
  int n; cin >> n;
  for (int i=0; i<n; i++){
    string temp; cin >> temp;
    for (int j=0;j<n;j++){
      table[i][j] = temp[j];
    }
  }

  bool flag = true;
  char first = table[0][0];
  for(int i=0; i<n; i++){
    for(int j=0; j<n; j++){
      if(first != table[i][j]){
        flag = false; break;
      }
    }
    if (!flag) break;
  }

  if(flag){
    cout<<first;
  } else{
    cout << quad(0,0,n);
  }
  return 0;
 
}