#include <iostream>
#include <queue>
#include <stack>

using namespace std;


class trienode{
    public:
        char data;
        trienode* children[26];
        bool isterminal;
    trienode(char ch){
        data=ch;
        for(int i=0;i<26;i++){
            children[i]=NULL;
        }
        isterminal=false;
    }
};

class trie{
    public:
    trienode* root;
    trie(){
        root = new trienode('\0');
    }

    void insertutil(trienode* root, string word){
        // rescursion se question solve hoga, ek case solve karenge, baaki recusrion sambhal lega
        // base case
        if(word.length() == 0){
            root->isterminal=true;
            return;
        }

        //el case solve karte hai
        // assumption hai ki words are CAPS

        int index= word[0]-'A';
        trienode* child;

        if(root->children[index]!=NULL){
            //aage bad jaayo
            child = root->children[index];
        }else{
            // create the child and aage bad jaayo
            child = new trienode(word[0]);
            root->children[index] = child;
        }

        // recurcive call maar denge, root ki jagah apn child paas karene, taaki next iteration me wo root bn jaaye
        // aur word ko index 1 se chalu karke bhejenge, uski length kam hoti jaayegi
        insertutil(child, word.substr(1));
    }

    void insertword(string word){
        insertutil(root,word);
    }

    bool searchutil(trienode* root, string word){
        // base case

        if(word.length() == 0){
            return root->isterminal;
        }

        trienode* child;
        int index = word[0]-'A';

        //present
        if(root->children[index] !=NULL){
            child=root->children[index];
        }else{
            // absent
            return false;
        }

        // recursive call
        return searchutil(child, word.substr(1));
    }

    bool searchword(string word){
        return searchutil(root,word);
    }


    void removeutil(trienode* root, string word){
        // base case
        if(word.length() == 0){
            root->isterminal = false;
            return;
        }

        int index = word[0]-'A';
        trienode* child;

        if(root->children[index] !=NULL){
            child=root->children[index];
        }

        removeutil(child, word.substr(1));
    }


    void removeword(string word){
        if(searchutil(root,word)){
            removeutil(root, word);
        }else{
            cout<<"word not present"<<endl;
        }
        
    }







};


int main(){
    trie* t =new trie();

    t->insertword("COL");
    t->insertword("CODE");
    t->insertword("CODING");
    t->insertword("CODDING");
    t->insertword("COLY");

    cout<<"present or not "<< t->searchword("CODDING")<<endl;

    t->removeword("TIME");

    cout<<"present or not "<< t->searchword("TIME")<<endl;






    return 0;
}