#include <bits/stdc++.h>
using namespace std;
struct Node {
  int id;
  int parent;
  int dist;
};

bool operator<(const Node &a, const Node &b) { return a.dist < b.dist; }

int n, m, c, r, k;

vector<pair<int, int>> adjl[50005];

vector<vector<int>> distances;
vector<set<int>> ans;

void djikstra() {
  multiset<Node> curr;
  for(int i = 0; i < c; i++){
    curr.insert({i, i, 0});
    distances[i][i] = 0;
  }

  /*for(auto& e: curr){
    cout<<e.id<<" "<<e.parent<<" "<<e.dist<<endl;
  }*/



  while (!curr.empty()) {
    //cout<<curr.size()<<endl;
    Node node = *curr.begin();
    //cout<<"old"<<endl;
    /*for(auto& e: curr){
      cout<<e.id<<" "<<e.parent<<" "<<e.dist<<endl;
    }*/
    curr.erase(curr.begin());
    /*cout<<"new"<<endl;
    for(auto& e: curr){
      cout<<e.id<<" "<<e.parent<<" "<<e.dist<<endl;
    }
    
    cout<<node.id<<" "<<node.parent<<" "<<node.dist<<endl;*/
    
    for (auto &edge : adjl[node.id]) {
      if (node.dist + edge.second < distances[edge.first][node.parent]){
        distances[edge.first][node.parent] = node.dist + edge.second;
        curr.insert({edge.first, node.parent, node.dist + edge.second});
        if(distances[edge.first][node.parent] <= r && ans[edge.first].find(node.parent) == ans[edge.first].end()){
          ans[edge.first].insert(node.parent);
        }
      }
    }
  }
}

int main() {
  cin >> n >> m >> c >> r >> k;
  distances.assign(n, vector<int>(c, INT_MAX));
  ans.resize(n);
  for (int i = 0; i < m; i++) {
    int a, b, d;
    cin >> a >> b >> d;
    adjl[a - 1].push_back({b - 1, d});
    adjl[b - 1].push_back({a - 1, d});
  }

  djikstra();

  int num = 0;
  vector<int> dest;

  for(int i = c; i < n; i++){
    if(ans[i].size() >= k){
      num++;
      dest.push_back(i);
    }
  }

  cout<<num<<endl;
  for(auto& p: dest){
    cout<<p + 1<<endl;
  }
}






/*
#include <bits/stdc++.h>
using namespace std;
struct Node {
  int id;
  int dist;
};

bool operator<(const Node &a, const Node &b) { return a.dist < b.dist; }

int n, m, c, r, k;

vector<pair<int, int>> adjl[50005];

vector<int> distances;
void djikstra(int s) {
  multiset<Node> curr;
  curr.insert({s, 0});
  while (!curr.empty()) {
    Node node = *curr.begin();
    curr.erase(node);

    for (auto &edge : adjl[node.id]) {
      if (distances[edge.first] > distances[node.id] + edge.second) {
        distances[edge.first] = distances[node.id] + edge.second;
        curr.insert({edge.first, distances[edge.first]});
      }
    }
  }
}

int main() {
  cin >> n >> m >> c >> r >> k;
  for (int i = 0; i < m; i++) {
    int a, b, d;
    cin >> a >> b >> d;
    adjl[a - 1].push_back({b - 1, d});
    adjl[b - 1].push_back({a - 1, d});
  }

  int nearby[n];
  memset(nearby, 0, sizeof(nearby));

  set<int> ans;
  for (int i = 0; i < c; i++) {
    distances.assign(n, INT_MAX);
    distances[i] = 0;
    djikstra(i);
    for (int j = c; j < n; j++) {
      if (distances[j] <= r) {
        nearby[j]++;
        if (nearby[j] >= k && ans.find(j) == ans.end()) {
          ans.insert(j);
        }
      }
    }
  }

  cout << ans.size() << endl;
  while (!ans.empty()) {
    cout << *ans.begin() + 1 << endl;
    ans.erase(*ans.begin());
  }
}
*/