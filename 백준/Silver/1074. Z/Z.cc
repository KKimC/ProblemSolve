#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

pair<int, int> dp[41];
int N, r, c, ans = 0;

void dc(int x, int y, int size)
{
    if (c == x && r == y)
    {
        cout << ans;
        return;
    }
    else if (c < x + size && r < y + size && c >= x && r >= y)
    {

        dc(x, y, size / 2);
        dc(x + size / 2, y, size / 2);
        dc(x, y + size / 2, size / 2);
        dc(x + size / 2, y + size / 2, size / 2);
    }
    else
    {
        ans += size * size;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> r >> c;
    dc(0, 0, pow(2, N));
    return 0;

    return 0;
}