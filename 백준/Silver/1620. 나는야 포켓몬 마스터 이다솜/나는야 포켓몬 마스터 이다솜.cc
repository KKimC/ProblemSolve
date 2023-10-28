#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

unordered_map<string, string> h;
int n, m;
string name;
string a;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;

    for (int i = 1; i <= n; i++)
    {
        cin >> name;
        h[name] = to_string(i);
        h[to_string(i)] = name;
    }
    for (int i = 1; i < m + 1; i++)
    {
        cin >> a;
        cout << h[a] << '\n';
    }

    return 0;
}