#include<iostream>
using namespace std;
class VC{
 public : int index,ch;
 public : string name,phone,city;
 public : void menu(){
   cout<<"********VISITING CARD SYSTEM********\n";
   cout<<"\n1)ADD VC\n2)REMOVE vc\n3)VIEW VC\nENTER YOUR CHOICE\n";
   cin>>ch;
  }
  public : void add() {
    /* code */
  }
  public : void remove() {
    /* code */
  }
  public : void view() {
    /* code */
  switch(ch)
  {
    case 1:
         add();
         break;
    case 2:
         remove();
         break;
    case 3:
        view();
         break;
  }
}
};
int main(){
  VC ub,ob1;
  ob1.menu();
  return 0;
}
