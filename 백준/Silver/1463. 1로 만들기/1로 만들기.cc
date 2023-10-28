#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

int dp[1000001];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    fill(dp, dp + 1000001, 1000000);
    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;

    for (int i = 2; i < 1000001; i++)
    {
        if (i + 1 < 1000001)
        {
            if (dp[i + 1] > dp[i] + 1)
            {
                dp[i + 1] = dp[i] + 1;
            }
        }
        if (i * 2 < 1000001)
        {
            if (dp[i * 2] > dp[i] + 1)
            {
                dp[i * 2] = dp[i] + 1;
            }
        }
        if (i * 3 < 1000001)
        {
            if (dp[i * 3] > dp[i] + 1)
            {
                dp[i * 3] = dp[i] + 1;
            }
        }
    }
    int n;
    cin >> n;
    cout << dp[n];

    return 0;
}