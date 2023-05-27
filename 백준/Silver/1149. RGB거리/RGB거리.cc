#include <iostream>

using namespace std;

int dp[3][1000];
int cost[3][1000];

int main(){

  int n; cin >> n;
  for (int i=0; i<n; i++){
    cin >> cost[0][i] >> cost[1][i] >> cost[2][i];
  }

  dp[0][0] = cost[0][0];
  dp[1][0] = cost[1][0];
  dp[2][0] = cost[2][0];
  
  for(int i=1; i<n; i++){
    dp[0][i] = cost[0][i] + min(dp[1][i-1],dp[2][i-1]);
    dp[1][i] = cost[1][i] + min(dp[0][i-1],dp[2][i-1]);
    dp[2][i] = cost[2][i] + min(dp[0][i-1],dp[1][i-1]);
  }
  
  cout << min(min(dp[0][n-1],dp[1][n-1]),dp[2][n-1]);

  return 0;
}