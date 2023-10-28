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

    priority_queue<int, vector<int>, greater<int>> minHeap;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> m;
        if (m != 0)
        {
            minHeap.push(m);
        }
        else
        {
            if (minHeap.empty())
            {
                cout << 0 << "\n";
            }
            else
            {
                cout << minHeap.top() << "\n";
                minHeap.pop();
            }
        }
    }

    return 0;
}