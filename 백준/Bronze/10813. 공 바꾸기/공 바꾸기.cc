#include <iostream>

using namespace std;


int main() {
  int basket[101];
  int n, m; cin >> n >> m;
  for(int i=1; i<=n; i++){
    basket[i] = i;
  }
  for(int i=0; i<m; i++){
    int a, b; cin >> a >> b;
    int temp = basket[a];
    basket[a] = basket[b];
    basket[b] = temp;
  }
  for(int i=1; i<=n; i++){
    cout << basket[i] << " ";
  }
  return 0;
}