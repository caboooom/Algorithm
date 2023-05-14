#include <iostream>

using namespace std;

int main() {
  int n, m;
  cin >> n >> m;
  int basket[101] = {0,};
  for(int i=0; i<m; i++){
    int start, end, number;
    cin >> start >> end >> number;
    start--; end--; //인덱스가 0부터 시작하므로
    while(start<=end){
      basket[start++] = number;
    }
  }
  for(int i=0; i<n; i++){
    cout << basket[i] << " ";
  }
}