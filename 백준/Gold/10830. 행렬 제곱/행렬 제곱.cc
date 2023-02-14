#include <iostream>
using namespace std;
//풀이참고 gusdnr69.tistory.com/261
long long n,b;
long long arr[5][5];
long long temp[5][5];
long long result[5][5];

void matrix(long long arr1[5][5], long long arr2[5][5]){
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				temp[i][j]=0;
				for(int k=0;k<n;k++){
					temp[i][j] += arr1[i][k]*arr2[k][j];
					temp[i][j] %= 1000;
				}
			}
		}
	
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++) arr1[i][j]=temp[i][j];
	}
	return;
}


int main(){
	cin>>n>>b;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin>>arr[i][j];
		}
		result[i][i]=1;
	}
	
	
	while(b){
		if(b%2==1) matrix(result,arr);
		matrix(arr,arr);
		b/=2;
	}
	
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cout<<result[i][j]<<" ";
		}
		cout<<"\n";
	}
	
	
	return 0;
}