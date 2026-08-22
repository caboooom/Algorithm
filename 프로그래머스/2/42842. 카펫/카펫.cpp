#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<pair<int, int>> pairs;
    for (int i = 1; i * i <= yellow; i++) {
        if (yellow % i == 0) {
            pairs.push_back({i, yellow / i});
        }
    }
    for (int i = 0; i < pairs.size(); i++) {
        int yellowH = pairs[i].first;
        int yellowW = pairs[i].second;
        if ((yellowH + 2) * (yellowW + 2) == brown + yellow) {
            return {yellowW + 2, yellowH + 2};
        }
    }
    return {0,0};
}
