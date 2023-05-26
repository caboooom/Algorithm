#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<int> numbers, string hand) {
    map<int,pair<int,int>> location;
    for(int i=1; i<13; i++){
        location.insert({i, make_pair((i-1)/3, (i-1)%3)});
    }
    
    string answer = "";
    
    int left = 10;
    int right = 12;
    
    for(int i=0; i<numbers.size(); i++){
        int cur = numbers[i];
        
        if(cur==0) cur=11;
        
        if(location[cur].second == 0){
            answer += "L";
            left = cur;
        }
        else if (location[cur].second == 2){
            answer += "R";
            right = cur;
        }
        else{
            int ldist = abs(location[left].first - location[cur].first) + abs(location[left].second - location[cur].second);
            int rdist = abs(location[right].first - location[cur].first) + abs(location[right].second - location[cur].second);
            if (ldist > rdist){
                answer += "R";
                right = cur;
            }else if (ldist == rdist){
                if (hand == "left"){
                    answer += "L";
                    left = cur;
                }else{
                    answer += "R";
                    right = cur;
                }
            }else{
                answer += "L";
                left = cur;
            }
        }
    }
    return answer;
}