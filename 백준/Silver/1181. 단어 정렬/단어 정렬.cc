#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;

string a;
vi arr(200, 0);
int maxN = 0, maxE;

int cmp(string a, string b)
{
    if (a.length() == b.length())
    {
        return a < b;
    }
    else
    {
        return a.length() < b.length();
    }
}

string word[20000];

int main()
{
    int N;
    //freopen("input.txt", "r", stdin);
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> word[i];
    }

    sort(word, word + N, cmp);

    for (int i = 0; i < N; i++)
    {
        if (word[i] == word[i - 1])
        {
            continue;
        }
        cout << word[i] << "\n";
    }

    return 0;
}