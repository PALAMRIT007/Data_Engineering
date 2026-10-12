#include <iostream>
#include <queue>
#include <stack>

using namespace std;

class node{
    public:
    int data;
    node* left;
    node* right;

    node(int d){
        this->data = d;
        this->left = NULL;
        this->right = NULL;
    }
    
};

node* buildtree(node* root){
    cout<<"enter root node data";
    int data;
    cin>>data;
    root = new node(data);

    if(data ==-1){
        return NULL;
    }

    cout<<"enter element too insert at left of"<<data<<endl;
    root->left = buildtree(root->left);
    cout<<"enter data for inserting at right of "<< data << endl;
    root->right = buildtree(root->right);
    return root;


}

void levelordertraversal(node* root){
    queue<node*> q;
    q.push(root);
    q.push(NULL);
    while(!q.empty()){
        node* temp = q.front();
        q.pop();
        if(temp == NULL){   // purana level pura traverse ho chuka hai
            cout<< endl;
            if(!q.empty()){    // abhi bhi kuch baaki bacha hai
                q.push(NULL);
            }
        }
        else{
            cout<< temp->data<< ' ';
            if(temp->left){
            q.push(temp->left);
            }
            if(temp->right){
                q.push(temp->right);
                
            }
        }
    }
}

void reverselevelordertraversal(node* root){
    queue<node*> q;
    stack<node*> s;
    q.push(root);
    s.push(root);
    q.push(NULL);
    s.push(NULL);
    while(!q.empty()){
        node* temp = q.front();
        q.pop();
        if(temp == NULL){   // purana level pura traverse ho chuka hai
            cout<< endl;
            if(!q.empty()){    // abhi bhi kuch baaki bacha hai
                q.push(NULL);
                s.push(NULL);
            }
        }
        else{
            // cout<< temp->data<< ' ';
            if(temp->left){
            q.push(temp->left);
            s.push(temp->left);

            }
            if(temp->right){
                q.push(temp->right);
                s.push(temp->right);
                
            }
        }
    }
    while(!s.empty()){
        if(s.top() == NULL){
            cout<<endl;
            s.pop();
        }else{
            cout<<s.top() ->data<<" ";
            s.pop();
        }
    }
}

void inordertraversal(node* root){
    if(root == NULL){
        return;
    }
    inordertraversal(root->left);
    cout<<root->data<<" ";
    inordertraversal(root->right);
}
void preordertraversal(node* root){
    if(root == NULL){
        return;
    }
    cout<<root->data<<" ";
    preordertraversal(root->left);
    preordertraversal(root->right);
}
void postordertraversal(node* root){
    if(root == NULL){
        return;
    }
    postordertraversal(root->left);
    postordertraversal(root->right);
    cout<<root->data<<" ";
}

void buildfromlevelorder(node* &root){
    queue<node*> q;
    cout<<"enter data for root node : "<<endl;
    int data;
    cin>>data;
    root = new node(data);
    q.push(root);

    while (!q.empty()){
        node* temp = q.front();
        q.pop();

        cout<<"enter data for left of "<<temp->data<<endl;
        int leftdata;
        cin>>leftdata;

        if(leftdata != -1){
            temp->left = new node(leftdata);
            q.push(temp->left);
        }

        cout<<"enter data for right of "<<temp->data<<endl;
        int rightdata;
        cin>>rightdata;

        if(rightdata != -1){
            temp->right = new node(rightdata);
            q.push(temp->right);
        }
    }
    
}

void morristraversl(node* root){
    // starting morris traversal
    // alog
    // ek current node bnaker use root pr set karde
    // niche wale saare steps while ke ander hai unitll current!=NULL
    // agar current ka left nahi hai to 
        // current ka data print karde
        // current = current->right
    // uska else part(left exists karta hai)
        // find the precedecessor(matlab current ke ek left me ja, or phir uske right most me chla ja, jab tak null na mil jaaye and wo current ko point na karta ho )
        // if predecessor ka right == NULL hai(to yha apn temp link create karenge)
            // predecessor->right = current
            // current=current->left
        // else wala part predecessor ka right null nahi hai(yha us temp link ko htana hai)
            // predecessor->right = NULL
            // current ke data ko print karwado
            // current=current->right

    node* current = root;
    while(current!=NULL){
        if(!current->left){
            cout<<current->data<<" ";
            current=current->right;
        }
        else{
            node* pred = current;
            pred = pred->left;

            while(pred->right !=NULL && pred->right!=current){
                pred=pred->right;
            }
            if(pred->right == NULL){
                pred->right= current;
                current=current->left;
            }else{
                pred->right=NULL;
                cout<<current->data<<" ";
                current=current->right;
            }
        }
    }
}

// this function is for flattening the binary tree in a linked list, using pre order traversal using morris traversal;
void morristraversalpreorder(node* root){
    node* current = root;
        while(current!=NULL){
            if(current->left){
                node* pred = current->left;
                while(pred->right){
                    pred=pred->right;
                }
                pred->right=current->right;
                current->right=current->left;
                current->left=NULL;
            }
            current=current->right;
        }
}
int main(){
    node* root = NULL;
    // 1 3 7 -1 -1 11 -1 -1 5 17 -1 -1 -1

    // 1 3 5 7 11 17 -1 -1 -1 -1 -1 -1 -1 
    // buildfromlevelorder(root);
    // levelordertraversal(root);

    root = buildtree(root); 

    cout<<"printing the tree :"<<endl;
    // levelordertraversal(root);
    // reverselevelordertraversal(root);

    cout<<"inorder traversal : "<<endl;
    inordertraversal(root);
    cout<<endl;
    // mossirs traversal
    cout<<"mossirs traversal"<<endl;
    morristraversl(root);
    // cout<<"preorder traversal : "<<endl;
    // preordertraversal(root);
    // cout<<"postorder traversal : "<<endl;
    // postordertraversal(root);
}