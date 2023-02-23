#include <iostream>
#include <queue>

using namespace std;

int n,m;
int maze[101][101];
bool visited[101][101];
int dist[101][101];
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
queue<pair<int,int>> q;

void bfs(int x, int y){
	visited[x][y]=1;
	q.push(make_pair(x,y));
	dist[x][y]=1;
	
	while(!q.empty()){
		int x=q.front().first;
		int y=q.front().second;
		q.pop();
		
		for(int i=0;i<4;i++){
			int x_ = x+dx[i];
			int y_ = y+dy[i];
			
			if(0<=x_ && x_<n & 0<=y_ && y_<m){
				if(maze[x_][y_]==1 && !visited[x_][y_]){
					dist[x_][y_]=dist[x][y]+1;
					visited[x_][y_]=1;
					q.push(make_pair(x_,y_));
				}
			}
		}
	}
return;	}


int main(){
	cin>>n>>m;
	
	for(int i=0;i<n;i++){
		string str; cin>>str;
		for(int j=0;j<m;j++) maze[i][j]=str[j]-'0';
	}

	bfs(0,0);
	cout<<dist[n-1][m-1];
	
	return 0;
}