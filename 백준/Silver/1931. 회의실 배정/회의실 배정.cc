#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

unordered_map<string, string> h;

vector<string> v;
string name;
string a;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    vector<pair<int, int>> schedule;
    int N, end, begin;

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> begin >> end;
        schedule.push_back(make_pair(end, begin));
    }

    sort(schedule.begin(), schedule.end());

    int time = schedule[0].first;
    int count = 1;
    for (int i = 1; i < N; i++)
    {
        if (time <= schedule[i].second)
        {
            count++;
            time = schedule[i].first;
        }
    }

    cout << count;

    return 0;
}