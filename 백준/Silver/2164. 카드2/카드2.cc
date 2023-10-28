#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

int n;

int main()
{
    cin >> n;
    queue<int> q;
    for (int i = 1; i < n + 1; i++)
    {
        q.push(i);
    }
    int i = 0;
    int temp;
    while (q.size() != 1)
    {
        if (i % 2 == 1)
        {
            temp = q.front();
            q.pop();
            q.push(temp);
        }
        else
        {
            q.pop();
        }
        i++;
    }
    cout << q.front();
}