#include <iostream>
using namespace std;

int main(){
	int c = 1000000000;

	int n; cin>>n;
	int dp[n][9];
	for(int i=0;i<9;i++) dp[0][i]=1;
	
	for(int i=1;i<n;i++){
		for(int j=0;j<9;j++){
			if(j==0) { 
				if(i==1) dp[i][j]=2;
				else dp[i][j]=((dp[i-2][0]%c)+ (dp[i-1][1]%c))%c;}
			else if(j==8) dp[i][j] = dp[i-1][7]%c;
			else dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1])%c;
		}
	}
	
	int sum=0;
	for(int i=0;i<9;i++) sum=(sum+dp[n-1][i])%c;
	cout<<sum%c;
	return 0;
}