#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

queue<int> q;
queue<int> v;
int n, m, a;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;

    for (int i = 1; i < n + 1; i++)
    {
        q.push(i);
    }
    int i = m;
    while (!q.empty())
    {
        if (i == 1)
        {
            v.push(q.front());
            i = m;
        }
        else
        {
            i--;
            a = q.front();
            q.push(a);
        }

        q.pop();
    }
    cout << "<" << v.front();
    v.pop();
    for (int i = 1; i < n; i++)
    {
        cout << ", " << v.front();
        v.pop();
    }
    cout << ">";
    return 0;
}