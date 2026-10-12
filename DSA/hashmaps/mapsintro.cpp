#include<iostream>
#include<map>
#include<unordered_map>
#include<vector>
using namespace std;

int main(){

    unordered_map<string,int> m;

    // inserting

    //1
    pair<string,int> p = make_pair("ashu",2);
    m.insert(p);

    //2
    pair<string,int> q("is",3);
    m.insert(q);

    //3
    m["good"] = 5;

    //searching
    cout<<m["good"]<<endl;
    cout<<m.at("ashu")<<endl;
    // cout<<m.at("unknownkey")<<endl;
    cout<<m["unknownkey"]<<endl;   //----> BE CAREFUL FOR THESE THINGS, TRYING TO ACCESS A KEY DIRECTLY CAN CAUSE THE HARM, its making an entry and storing the value 0 for it.
    cout<<m.at("unknownkey")<<endl;   

    // counting for a key
    cout<<m.count("bro")<<endl;

    // checking size
    cout<<m.size()<<endl;

    // traversal
    for(auto i:m){
        cout<<i.first<<endl;
    }

    // erasing an element
    m.erase("unknownkey");
    cout<<m.size()<<endl;

}