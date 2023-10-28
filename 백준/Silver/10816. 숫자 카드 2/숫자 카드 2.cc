#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

int n, a;
string b;

struct AgeName
{
    int age;
    string name;
};

bool compareAN(const AgeName &a, const AgeName &b)
{
    return a.age < b.age;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    unordered_map<int, int> hash;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> a;
        hash[a]++;
    }
    int m;
    cin >> m;
    for (int i = 0; i < m; i++)
    {
        cin >> a;
        if (hash.find(a) != hash.end())
        {
            cout << hash[a] << " ";
        }
        else
        {
            cout << 0 << " ";
        }
    }

    return 0;
}