#include <iostream>

using namespace std;

long long int pow(long long int a, long long int exp,long long int c){
	
	if(exp==1) return a%c;
	
	long long int temp = pow(a,exp/2,c);
	
	if(exp%2==1) return ((temp*temp%c)*a)%c;
	
	return temp*temp%c;
	
}

int main(){
	long long int a,b,c;
	cin>>a>>b>>c;
	cout<<pow(a,b,c);
	return 0;
}