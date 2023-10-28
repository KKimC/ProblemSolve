#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

int n, a;
string b;
deque<int> v;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> b;

        if (b == "push_front")
        {
            cin >> a;
            v.push_front(a);
        }
        else if (b == "push_back")
        {
            cin >> a;
            v.push_back(a);
        }
        else if (b == "pop_front")
        {
            if (v.empty())
            {
                cout << -1 << "\n";
            }
            else
            {
                cout << v.front() << "\n";
                v.pop_front();
            }
        }
        else if (b == "pop_back")
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