#include <string>
#include <vector>
#include <unordered_set>

using namespace std;


vector<int> solution(int n, vector<string> words) {
    
    unordered_set<string> spoken_words;
    char prev = words[0][0];
    for (int i = 0; i < words.size(); i++) {
        if (spoken_words.find(words[i]) != spoken_words.end() 
            || words[i].size() == 1
            || prev != words[i][0]) {
            return {i % n + 1, i / n + 1};
        } else {
            spoken_words.insert(words[i]);
            prev = words[i][words[i].size()-1];
        }
    }

    return {0, 0};
}