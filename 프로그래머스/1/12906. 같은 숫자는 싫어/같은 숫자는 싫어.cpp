#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;

    int oldValue = -1;
    for (int num : arr) {
        if (num != oldValue) {
            answer.push_back(num);
            oldValue = num;
        }
    }

    return answer;
}