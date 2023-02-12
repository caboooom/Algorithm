#include <iostream>
#include <queue>
using namespace std;

int n,m,v;
int graph[1001][1001];
bool visited[1001];
queue<int> q;

void dfs(int v){
	visited[v]=true;
	cout<<v<<" ";
	
	for(int i=1;i<=n;i++){
		if(graph[v][i]==1 && !visited[i]) dfs(i);
	}
	return;
}

void bfs(int v){
	q.push(v);
	visited[v]=true;
	cout<<v<<" ";
	
	while(!q.empty()){
		v=q.front();
		q.pop();
		
		for(int i=1;i<=n;i++){
			if(graph[v][i]==1 && !visited[i]){
				q.push(i);
				visited[i]=true;
				cout<<i<<" ";
			}
		}
	}
	return;
}
int main(){
	cin>>n>>m>>v;
	
	for(int i=0;i<m;i++){
		int x,y; cin>>x>>y;
		graph[x][y]=1;
		graph[y][x]=1;
	}
	
	dfs(v);
	
	cout<<"\n";
	for(int i=0;i<=n;i++) if(visited[i]==true) visited[i]=false;
	bfs(v);
	return 0;
}