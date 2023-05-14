#include <iostream>

using namespace std;


void reverse(int* arr, int start, int end){
  int* temp = (int*)malloc(sizeof(int)*100);
  int tempSize = end-start+1;

  for (int i=0; i<tempSize; i++) temp[i] = arr[end-i];
  for (int i=0; i<tempSize; i++) arr[start+i] = temp[i];
  
  free(temp);
  return;
}

int main() {
  int basket[101];
  for (int i=0; i<101; i++){
    basket[i] = i;
  }
  int n, m; //n: 바구니의 수
  cin >> n >> m;
  for (int i=0; i<m; i++){
    int start, end;
    cin >> start >> end;
    reverse(basket, start, end);
  }
  for(int i=1;i<=n;i++){
    cout << basket[i] << " ";
  }
  return 0;
}