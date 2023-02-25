
x = int(input())

dp = [0]*(x+1)

for i in range(2,x+1):
  dp[i]=dp[i-1]+1
  if i%2==0:
    dp[i]=min(dp[i],dp[i//2]+1)
  if i%3==0:
    dp[i]=min(dp[i],dp[i//3]+1)

print(dp[x])


'''
예전에 작성했던 c++ 코드

#include <iostream>
#include <vector>
using namespace std;

int main(){
	
	vector<int> DP={0,0,1,1};
	
	int n; cin >> n;

	for(int i=4;i<n+1;i++) {
		int result = DP[i-1]+1;
		if(i%3==0) result= min(result,DP[i/3]+1);
		if(i%2==0) result = min(result,DP[i/2]+1);
		DP.push_back(result);
		}
		
	cout<<DP[n];
	return 0;
}
'''