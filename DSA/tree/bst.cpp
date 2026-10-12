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
            this->data=d;
            this->left=NULL;
            this->right=NULL;
        }
};


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

node* maxnode(node* root){
    if(root == NULL){
        return NULL;
    }
    while(root->right !=NULL){
        root=root->right;
    }
    return root;
}
node* minnode(node* root){
    if(root == NULL){
        return NULL;
    }
    while(root->left !=NULL){
        root=root->left;
    }
    return root;
}

node* search(node* root,int x){
    if(root == NULL){
        return NULL;
    }
    if(root->data == x){
        return root;
    }

    if(root->data<x){
        search(root->right,x);
    }else{
        search(root->left,x);
    }
}

void inordertraversal(node* root,vector<int> inorder){
    if(root == NULL){
        return;
    }
    inordertraversal(root->left,inorder);
    inorder.push_back(root->data);
    cout<<root->data<<" ";
    inordertraversal(root->right,inorder);
}

node* deletefrombst(node* root,int x){
    // base case
    if(root == NULL){
        return NULL;
    }

    if(root->data == x){
        // deletion
        // 0 child
        if(root->left == NULL && root->right == NULL){
            delete root;
            return NULL;
        }

        // 1 child
        // left child
        if(root->left!=NULL && root->right == NULL){
            node* temp = root->left;
            delete root;
            return temp;
        }

        // right child
        if(root->left==NULL && root->right != NULL){
            node* temp = root->right;
            delete root;
            return temp;
        }

        // two child
        if(root->left !=NULL && root->right !=NULL){
            // right side se element uthanke lata hu, copy karo, us element ko delete karo.
            node* mini = minnode(root->right);
            root->data=mini->data;
            root->right = deletefrombst(root->right,mini->data);
            return root;
        }

    }else if(root->data>x){
        root->left = deletefrombst(root->left,x);
        return root;
    }else{
        root->right = deletefrombst(root->right,x);
        return root;
    }
}

node* insertbst(node* root,int d){
    // base case
    if(root == NULL){
        node* root = new node(d);
        return root;
    }

    if(d>root->data){
        // right me jaao
        root->right = insertbst(root->right,d);
    }else{
        // left me jaao
        root->left = insertbst(root->left,d);
    }

    return root;
}


node*  takeinput(node* root){
    int d;
    cin>>d;
    while(d!=-1){
        root = insertbst(root,d);
        cin>>d;
    }
    return root;
}

int main(){
    node* root = NULL;
    cout<<"plr provide the input for bst"<<endl;
    root = takeinput(root);

    levelordertraversal(root);

    cout<<endl;
    node* maxinode = maxnode(root);
    node* mininode = minnode(root);

    // cout<<"max : "<<maxinode->data<<" min :"<<mininode->data;
    // vector<int> inorder;
    // inordertraversal(root,inorder);

    // deletion
    root = deletefrombst(root,5);
    levelordertraversal(root);
}
