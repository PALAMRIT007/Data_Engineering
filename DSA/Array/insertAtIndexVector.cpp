#include <iostream>
#include <vector>
using namespace std;


int main() {
    vector<int> arr = {1,2,3,4,5,6};
    int n = arr.size();
    
    int j=2;
    int k=9;
    
    
    if(j>=n){
        arr.push_back(k);
        
    }
    
    int i=0;
    int temp=0;
    
    while(i<n){
        if(i == j){
            temp = arr[i];
            arr[i] = k;
            break;
        }
        i++;
    }
    
    i++;
    
    while(i<n){
        int x = arr[i];
        arr[i] = temp;
        temp=x;
        i++;
        
    }
    
    arr.push_back(temp);
    
    for(auto i:arr){
        cout<<i<<endl;
    }
    

    return 0;
}