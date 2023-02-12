#include <iostream>
using namespace std;

int main(){

	int n,m; cin>>n>>m;
	int maze[n][m], DP[n][m];
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			int x; cin>>x;
			maze[i][j]=x; DP[i][j]=x;
		}
	}
	
	
	
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(i+1<n && DP[i][j]+maze[i+1][j] > DP[i+1][j]) DP[i+1][j]=DP[i][j]+maze[i+1][j];
			if(i+1<n && j+1<m && DP[i][j]+maze[i+1][j+1] > DP[i+1][j+1]) DP[i+1][j+1]=DP[i][j]+maze[i+1][j+1];
			if(j+1<m && DP[i][j]+maze[i][j+1]>DP[i][j+1]) DP[i][j+1]=DP[i][j]+maze[i][j+1];
		}		
	}
	cout<<DP[n-1][m-1];
	return 0;
}