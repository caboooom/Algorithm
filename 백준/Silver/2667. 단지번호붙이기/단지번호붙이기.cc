#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int map[25][25];
bool visited[25][25];
queue<pair<int,int>> q;
int result=0; int cnt=0;
vector<int> v;

int bfs(int x, int y){	
	visited[x][y]=true;
	q.push(make_pair(x,y));
	cnt++;
	while(!q.empty()){
		int a=q.front().first;
		int b=q.front().second;
		q.pop();
		
		if(b>=0 && b<n){
		if(a<n-1 && !visited[a+1][b] && map[a+1][b]==1){
			q.push(make_pair(a+1,b));
			visited[a+1][b]=1;
			cnt++;
		}
		if(a>0 && !visited[a-1][b] && map[a-1][b]==1){
			q.push(make_pair(a-1,b));
			visited[a-1][b]=1;
			cnt++;
		}
	}
	if(a>=0 && a<n){
		if(b<n-1 && !visited[a][b+1] && map[a][b+1]==1){
			q.push(make_pair(a,b+1));
			visited[a][b+1]=1;
			cnt++;
		}
		if(b>0 && !visited[a][b-1] && map[a][b-1]==1){
			q.push(make_pair(a,b-1));
			visited[a][b-1]=1;
			cnt++;
		}
}
	}
	return cnt;
}

int main(){
	cin>>n;
	for(int i=0;i<n;i++){
		string temp;
		cin>>temp;
		for(int j=0;j<n;j++) map[i][j]=temp[j]-'0';
	}
	
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(!visited[i][j]){
//				cout<<i<<" "<<j<<endl;
				if(map[i][j]==0) visited[i][j]=1;
				else v.push_back(bfs(i,j));
				cnt=0;
			}
		}
	}

	cout<<v.size()<<"\n";
	sort(v.begin(),v.end());
	for(int i=0;i<v.size();i++) cout<<v[i]<<"\n";
	return 0;
}