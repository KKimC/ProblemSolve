#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

int n, k;
pair<int, int> b;
vector<pair<int, int>> v;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> b.first >> b.second;
        v.push_back(b);
    }

    sort(v.begin(), v.end());

    for (pair<int, int> p : v)
    {
        cout << p.first << " " << p.second << "\n";
    }

    return 0;
}