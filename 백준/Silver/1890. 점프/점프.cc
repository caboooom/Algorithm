#include <iostream>

using namespace std;

int n;
int arr[101][101];
long dp[101][101]; 

int main(){
	
	cin>>n;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin>>arr[i][j];
		}
	}
	if(n==1 || arr[0][0]==0) {
		cout<<"0"; return 0;}
		
	dp[0][0]=1;
	
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			int jump = arr[i][j];
			if(i==n-1 && j==n-1) continue;
			if(i+jump<n) dp[i+jump][j] += dp[i][j];
			if(j+jump<n) dp[i][j+jump] += dp[i][j];
			}
	}
	

	cout<<dp[n-1][n-1];
	return 0;
} 