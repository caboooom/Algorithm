#include <iostream>

using namespace std;


int main() {
  double score[1000];
  int n;
  cin >> n;
  for(int i=0; i<n; i++){
    int temp; cin >> temp;
    score[i] = temp;
  }
  int maxScore = 0;
  for(int i=0; i<n; i++){
    if (score[i] > maxScore) maxScore = score[i];
  }
  double total = 0;
  for(int i=0; i<n; i++){
    score[i] = score[i]/maxScore * 100;
    total += score[i];
  }
  cout << total/n;
  
  return 0;
}