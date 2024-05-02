#include <bits/stdc++.h> 
using namespace std; 
 
int rec(int id1, int id2, string &s1, string &s2, int k, vector<vector<int>> &dp) { 
    if (id1 == (int)s1.size() || id2 == (int)s2.size()) { 
        return 0; 
    } 
    if (dp[id1][id2] != -1) { 
        return dp[id1][id2]; 
    } 
    int ans = 0, cnt = 1e9; 
    char a = s1[id1], b = s2[id2]; 
    if (a <= b) { 
        cnt = min({cnt, b - a, 26 - b + a}); 
    } else { 
        cnt = min({cnt, a - b, 26 - a + b}); 
    } 
    if (cnt <= k) { 
        ans = 1 + rec(id1 + 1, id2 + 1, s1, s2, k, dp); 
    } 
    ans = max({ans, rec(id1 + 1, id2, s1, s2, k, dp), rec(id1, id2 + 1, s1, s2, k, dp)}); 
    return dp[id1][id2] = ans; 
} 
 
int shyam_and_strings(string &s1, string &s2, int k) { 
    int n = s1.size(), m = s2.size(); 
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, -1)); 
    int ans = rec(0, 0, s1, s2, k, dp); 
    dp.assign(n + 1, vector<int>(m + 1, -1)); 
    ans = max(ans, rec(0, 0, s2, s1, k, dp)); 
    return ans; 
} 
 
int main() { 
    #ifndef ONLINE_JUDGE 
        freopen("input.txt", "r", stdin); 
    #endif 
    string s1, s2; 
    int k; 
    cin >> s1 >> s2 >> k; 
    cout << shyam_and_strings(s1, s2, k) << "\n"; 
    return 0; 
}