
#include <iostream>

using namespace std;

int main(){
  int a,b,c,d,e,f;
  cin >> a >> b >> c >> d >> e >> f;

  int x, y;
  bool flag = false;
  for (x=-999;x<1000;x++){
    for (y=-999;y<1000;y++){
      if ((a*x+b*y==c) && (d*x+e*y==f)){
        cout << x << " " << y;
        flag = true;
        break;
      }
    } if(flag) break;
  }

  return 0;
}