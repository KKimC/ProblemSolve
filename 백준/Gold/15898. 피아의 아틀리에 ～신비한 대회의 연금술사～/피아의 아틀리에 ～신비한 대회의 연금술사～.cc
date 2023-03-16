#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

const int INF = 987654321;
struct state {
	int x;
	char c;
};

int n, res = -INF;
int visited[10];

state material[10][4][4][4];
vector<vector<state> > map(5, vector<state>(5));

int cal(vector<vector<state>> tmap) {
	int r = 0, b = 0, g = 0, y=0;

	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			char t = tmap[i][j].c;

			if (t == 'R') {
				r += tmap[i][j].x;
			}
			else if (t == 'B') {
				b += tmap[i][j].x;
			}
			else if (t == 'G') {
				g += tmap[i][j].x;
			}
			else if (t == 'Y') {
				y += tmap[i][j].x;
			}
		}
	}

	return 7 * r + 5 * b + 3 * g + 2 * y;
}

vector<vector<state>> take_material(vector<vector<state>> tmap, int seq ,int pos, int dir) {
	//material[seq][dir][i][j]
	int px, py;

	switch (pos) {
	case 0:
		px = 0; py = 0;
		break;
	case 1:
		px = 1; py = 0;
		break;
	case 2:
		px = 0; py = 1;
		break;
	case 3:
		px = 1; py = 1;
		break;
	default:
		break;
	}

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			int y = i + py, x = j + px;
			tmap[y][x].x += material[seq][dir][i][j].x;

			if (tmap[y][x].x > 9) {
				tmap[y][x].x = 9;
			}
			else if (tmap[y][x].x < 0) {
				tmap[y][x].x = 0;
			}


			if (material[seq][dir][i][j].c != 'W') {
				tmap[y][x].c = material[seq][dir][i][j].c;
			}
		}
	}

	return tmap;
}

void dfs(int dep, vector<vector<state>> v) {
	if (dep == 3) {
		res = max(cal(v), res);
		return;
	}
	for (int i = 0; i < n; i++) {
		if (visited[i] == 1) continue;
		visited[i] = 1;

		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				vector<vector<state>> tmp = take_material(v, i, j, k);

				dfs(dep+1, tmp);
			}
		}

		visited[i] = 0;
	}
}

void make_rotated() {
	for (int z = 0; z < n; z++) {
		for (int r = 1; r < 4; r++) {
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					material[z][r][i][j].x = material[z][r - 1][3 - j][i].x;
					material[z][r][i][j].c = material[z][r - 1][3 - j][i].c;
				}
			}
		}
	}
}

int main() {
	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				int t;
				cin >> material[i][0][j][k].x;
			}
		}

		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				cin >> material[i][0][j][k].c;
			}
		}
	}

	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			map[i][j].x = 0;
			map[i][j].c = 'W';
		}
	}

	make_rotated();

	dfs(0, map);

	cout << res << '\n';

	return 0;
}