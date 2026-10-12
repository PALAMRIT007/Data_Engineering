#include <iostream>
#include <queue>
#include <stack>
#include <list>
#include <unordered_map>
using namespace std;
template <typename T >    //--> using this we are making our graph more generic, we just need to define the datatype we are using in graph, and it will be made for that specific datatype
class graph{
    public:
        unordered_map<T, list<T>> adj;

        void addnode(T u, T v, bool direction){
            // direction =0 --> undirected
            // direction =1 --> directed

            adj[u].push_back(v);

            if(direction == 0){
                adj[v].push_back(u);
            }
            
        }

        // abhi print karwate hai

        void printgraph(){

            for(auto i: adj){
                cout<< i.first << "-> ";

                for(auto j : i.second){
                    cout<< j<<",";
                }
                cout<<endl;
            }
        }
};

int main(){

    int n;
    cout<<"Enter number of nodes"<<endl;

    cin>>n;

    int m;
    cout<<"Enter number of edges"<<endl;
    cin>>m;
    graph<int> g;       // here we are declaring the datatype, need to tell here what kinf of data we will be passing.

    cout<<"start entering connections"<<endl;

    for(int i=0;i<m;i++){
        int u,v;
        cin>>u>>v;
        g.addnode(u,v,0);
    }

    g.printgraph();



    return 0;
}