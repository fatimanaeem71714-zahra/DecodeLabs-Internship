#include<iostream>
#include<string>
using namespace std;
int main(){
    string input;
    while(true){
        cout<<"user :" ;
    
        getline(cin,input);
        if(input== "hi" || input== "hello" || input=="Hey"){
            cout<<"Hi! How can i help you?"<<endl;
        }
            else if (input=="exit" ||input=="bye" ||input=="quit"){
                cout<<"Goodbye!"<<endl;
                break;
        }
                else{
                    cout<<"Sorry!I dont understand.";
                }
            }
                return 0;

        
}