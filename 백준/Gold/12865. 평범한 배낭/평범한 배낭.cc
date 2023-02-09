#include <iostream>

using namespace std;


int main(){
	int n, k, weight, value;
	cin >> n >> k;
	
	int w[n+1], v[n+1];
	
	for(int i=0;i<n;i++){
		cin >> weight >> value;
		w[i+1] = weight; v[i+1] = value;
	}
	
	int DP[n+1][k+1];
	
	for(int i=0;i<k+1;i++){
		DP[0][i] = 0;
	}
	for(int i=1;i<n+1;i++){
		for(int j=0;j<k+1;j++){			
			if(w[i] > j) DP[i][j] = DP[i-1][j];
			else DP[i][j] = max(DP[i-1][j-w[i]]+v[i], DP[i-1][j]);
			
		}
	}
	
	int max = 0;
	for(int i=1;i<n+1;i++){
		for (int j=0;j<k+1;j++){
			if(DP[i][j] > max) max = DP[i][j];
		}
	}
	
	cout<< max;
	return 0;
}