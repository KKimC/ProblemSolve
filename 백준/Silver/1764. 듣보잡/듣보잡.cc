#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

unordered_map<string, string> h;
int n, m;
vector<string> v;
string name;
string a;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        cin >> name;
        h[name] = name;
    }
    for (int i = 0; i < m; i++)
    {
        cin >> a;
        if (h.find(a) != h.end())
        {
            v.push_back(h[a]);
        }
    }
    cout << v.size() << "\n";
    sort(v.begin(), v.end());
    for (string s : v)
    {
        cout << s << "\n";
    }

    return 0;
}