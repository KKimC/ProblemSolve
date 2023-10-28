#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

int n, a;
string b;
queue<int> v;

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
            v.push(a);
        }
        else if (b == "pop")
        {
            if (v.empty())
            {
                cout << -1 << "\n";
            }
            else
            {
                cout << v.front() << "\n";
                v.pop();
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
        else if (b == "back")
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
        else if (b == "front")
        {
            if (v.empty())
            {
                cout << -1 << "\n";
            }
            else
            {
                cout << v.front() << "\n";
            }
        }
    }

    return 0;
}