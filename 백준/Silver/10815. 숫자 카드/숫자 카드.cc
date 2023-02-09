#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> v;

int bSearch(int k, int first, int last){
	while(first<=last){
		int mid = (first+last) /2;
		
		if(k==v[mid]) return 1;
		
		if(k<v[mid]) last=mid-1;
		else if(k>v[mid]) first=mid+1;
	}
	return 0;
}

int main(){
	int n,m,x;
	
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>x;
		v.push_back(x);
	}
	sort(v.begin(),v.end());
	
	cin>>m;
	int result[m];
	for(int i=0;i<m;i++){
		cin>>x;
		result[i] = bSearch(x,0,n-1);
	}
	
	for(int i=0;i<m;i++){
		cout<<result[i]<<" ";
	}
	return 0;
}