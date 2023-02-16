#include <iostream>
int m,n;
int graph[500][500];
int dp[500][500];
int dx[4]={-1,0,1,0};
int dy[4]={0,1,0,-1};

using namespace std;

int dfs(int x, int y){
    if(x==m-1 && y==n-1) return 1;
    if(dp[x][y]!=-1) return dp[x][y];
    
    dp[x][y]=0;
    
    for(int i=0;i<4;i++){
        int nextX=x+dx[i];
        int nextY=y+dy[i];
        if(nextX>=0 && nextX<m && nextY>=0 && nextY<n){
            if(graph[x][y] > graph[nextX][nextY]){
                dp[x][y] = dp[x][y]+ dfs(nextX,nextY);
            }
        }
    }

    return dp[x][y];
    
}

int main()
{
    cin>>m>>n;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            cin>>graph[i][j];
            dp[i][j]=-1;
        }
    }
    
    cout<<dfs(0,0)<<endl;
 
    
    
    

    return 0;
}
