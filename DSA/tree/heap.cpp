#include <iostream>
#include <queue>
#include <stack>

using namespace std;

class heap{
    public:
    int arr[100];
    int size;

    heap(){
        size=0;
        arr[size] = -1;
    }

    void insert(int d){
        size=size+1;
        int index=size;
        arr[index]= d;
        
        while(index>1){
            int parent = index/2;
            if(arr[parent]<arr[index]){
                swap(arr[parent],arr[index]);
                index=parent;
            }else{
                return;
            }
        }
    }
    
    void deletefromheap(){
        if(size==0){
            cout<<"ntg to delete";
            return;
        }

        // step 1 : replacement
        arr[1] = arr[size];

        // step 2: remove the last element
        size--;

        // step 3: take the root node(first node which we replaced) to right position
    int i=1;
        while(i<size){
            int leftindex = 2*i;
            int rightindex=2*i+1;
            

            if(leftindex<=size && arr[i]<arr[leftindex] && arr[leftindex]>arr[rightindex] ){
                swap(arr[i],arr[leftindex]);
                i=leftindex;
            }else if(rightindex<=size && arr[i]<arr[rightindex] && arr[rightindex]>arr[leftindex]){
                swap(arr[i],arr[rightindex]);
                i = rightindex;
            }else{
                return;
            }
        }
    }

    void print(){
        for(int i=1;i<=size;i++){
            cout<<arr[i]<<" ";
        }cout<<endl;
    }
};

void heapify(int arr[],int n,int index){
    int largest = index;
    int left=2*index;
    int right=2*index+1;

    if(left<=n && arr[largest]<arr[left]){
        largest = left;
    }
    if(right<=n && arr[largest]<arr[right]){
        largest=right;
    }

    if(largest!=index){
        swap(arr[largest],arr[index]);
        heapify(arr,n,largest);
    }
}

void heapsort(int arr[],int n){
    int size=n;
    while(size>1){
        // step 1: swap karwado or size ko ek se kam kardo
        swap(arr[size],arr[1]);
        size--;

        // step 2 : abhi jisko swap kiya hai usko sahi jagah pahuncha do 
        heapify(arr,size,1);            // Note: pass size instead of n, bcoz after reducing size we need to heapify the reduced heap,not the whole heap.
    }
}

int main(){
    heap h;
    h.insert(10);
    h.insert(7);
    h.insert(6);
    h.insert(5);
    h.insert(2);
    // h.insert(50);
    // h.insert(55);
    // h.insert(53);
    // h.insert(52);
    // h.insert(54);
    // h.print();
    h.deletefromheap();

    int arr[6] = {-1,54,53,55,52,50};
    int n=5;
    for(int i=n/2;i>0;i--){
        heapify(arr,n,i);
    }

    heapsort(arr,n);

    for(auto x:arr){
        cout<<x<<" ";
    }cout<<endl;
    
    // h.print();


    // not everytime we need to implement the heap logic from scratch, we can use the STL queue and use the inbuilt libraries
    // priority_queue    -- > max heap
    cout<<"priority_queue    -- > max heap"<<endl;
    priority_queue<int> maxheap;
    maxheap.push(54);
    maxheap.push(53);
    maxheap.push(55);
    maxheap.push(52);
    maxheap.push(50);
    cout<<maxheap.top()<<endl;

    maxheap.pop();
    cout<<maxheap.top()<<endl;
    cout<<maxheap.empty()<<endl;
    cout<<maxheap.size()<<endl;


    // min heap
    priority_queue<int,vector<int>,greater<int> > minheap;
    // all above functions/methods are same for min heap too :)

}

