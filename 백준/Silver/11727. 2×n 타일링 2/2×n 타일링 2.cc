#include <iostream>
#include <vector>

using namespace std;

int main(){
	vector<int> dp = {0,1,3};
//	int dp[1000] = {0,1,3,};
	int n; cin >> n;
	
	for(int i=3;i<n+3;i++)	dp.push_back((dp[i-1] + 2*dp[i-2])%10007);
	
	cout<< dp[n];
	
	return 0;
}
