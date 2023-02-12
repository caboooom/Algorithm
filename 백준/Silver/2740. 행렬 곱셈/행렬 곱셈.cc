#include <iostream>

using namespace std;

int arr1[101][101];
int arr2[101][101];
int result[101][101];

int main(){
	int n,m,k; cin>>n>>m;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			int x; cin>>x;
			arr1[i][j]=x;
		}
	}
	cin>>m>>k;
	for(int i=0;i<m;i++){
		for(int j=0;j<k;j++){
			int x; cin>>x;
			arr2[i][j]=x;
		}
	}
	
	for(int i=0;i<n;i++){
		for(int j=0;j<k;j++){
			for(int l=0;l<m;l++){
				result[i][j] += arr1[i][l]*arr2[l][j];
			}
			cout<<result[i][j]<<" ";
		}
		cout<<"\n";
	}
	
	return 0;
}