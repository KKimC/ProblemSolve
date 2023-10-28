#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

int n, a;
string b;
vi v;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> b;

        if (b == "push")
        {
            cin >> a;
            v.push_back(a);
        }
        else if (b == "pop")
        {
            if (v.empty())
            {
                cout << -1 << "\n";
            }
            else
            {
                cout << v.back() << "\n";
                v.pop_back();
            }
        }
        else if (b == "size")
        {
            cout << v.size() << "\n";
        }
        else if (b == "empty")
        {
            if (v.empty())
            {
                cout << 1 << "\n";
            }
            else
            {
                cout << 0 << "\n";
            }
        }
        else if (b == "top")
        {
            if (v.empty())
            {
                cout << -1 << "\n";
            }
            else
            {
                cout << v.back() << "\n";
            }
        }
    }

    return 0;
}