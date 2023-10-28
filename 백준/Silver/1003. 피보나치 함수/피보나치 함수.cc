#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

pair<int, int> dp[41];
int T, n;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    dp[0] = {1, 0};
    dp[1] = {0, 1};

    for (int i = 2; i < 41; i++)
    {
        dp[i] = {dp[i - 1].first + dp[i - 2].first, dp[i - 1].second + dp[i - 2].second};
    }

    for (int t = 0; t < T; t++)
    {
        cin >> n;
        cout << dp[n].first << ' ' << dp[n].second << "\n";
    }
    return 0;
}