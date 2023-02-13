#include <iostream>
#include <queue>
using namespace std;

int n,m; 
int graph[101][101];
int visited[101];
queue<int> q;
int cnt=0;

int bfs(int x){
	visited[x]=1;
	q.push(x);
	cnt++;
	
	while(!q.empty()){
		int v=q.front();
		q.pop();
		for(int i=0;i<=n;i++){
			if(graph[v][i]==1 && !visited[i]){
				q.push(i);
				visited[i]=1;
				cnt++;
			}
		}
	}
	return cnt;
}

int main(){
	cin>>n>>m;
	for(int i=0;i<m;i++){
		int x,y; cin>>x>>y;
		graph[x][y]=1;
		graph[y][x]=1;
	}	
	
	cout<<bfs(1)-1;
	return 0;
}