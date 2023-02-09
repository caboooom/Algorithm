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