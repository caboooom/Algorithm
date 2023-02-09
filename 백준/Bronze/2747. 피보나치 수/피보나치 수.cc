#include <iostream>
using namespace std;

int dp[100] ={0,};

int fibo(int n){
	if(n<=1) return n;
	else{
		if(dp[n]>0) return dp[n];
		dp[n]=fibo(n-1)+fibo(n-2);
		return dp[n];
	}
}

int main(){
	int k;
	cin >> k;
	cout<<fibo(k);
	return 0;
}