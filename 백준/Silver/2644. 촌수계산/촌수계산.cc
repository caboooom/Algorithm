#include <iostream>

using namespace std;


int n,m;
int graph[101][101];
bool visited[101];
int cnt=0; 
int ans=-1;

void dfs(int x,int y){
    if(x==y) ans=cnt;
    visited[x]=1;
    cnt++;
    for(int i=0;i<=n;i++){
        if(graph[x][i]==1 && !visited[i]){
            dfs(i,y);
        }
    }cnt--;
    return;
}

int main()
{
    cin>>n;
    int x,y;
    cin>>x>>y;
    cin>>m;
    for(int i=0;i<m;i++){
        int a,b;
        cin>>a>>b;
        graph[a][b]=1;
        graph[b][a]=1;
    }

    if(x==y){
        cout<<0; return 0;
    }
    dfs(x,y);
    
    cout<<ans;
    
    
    return 0;
}
