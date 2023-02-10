#include <iostream>

using namespace std;

int main(){
	int c = 10007;
	
	int n; cin>>n;
	int dp[n+1][10];	//행:1~10, 열:0~9 
	
	for(int i=0;i<10;i++) dp[1][i]=1;
	
	for(int i=2;i<=n;i++){
		for(int j=0;j<10;j++){
			if(j==0) dp[i][j]=1;
			else {
				dp[i][j]=dp[i][j-1]+dp[i-1][j];
				dp[i][j] %= c;
			}
		}
	}
	
	int sum=0;
	for(int i=0;i<10;i++){
		sum += dp[n][i];
	}
	
	cout<< sum % c;
	
	return 0;
}