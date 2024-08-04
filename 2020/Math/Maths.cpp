//Camden Bruce
#include <iostream>
using namespace std;

int main()
{
  string input;
  cout << "Add, Multiply, Divide or Subtract? (a/m/d/s): ";
  cin >> input;
  
  if (input == "a")
  {
	  int aa1;
      int aa2;
	  cout << "please enter a number: ";
      cin >> aa1;
      cout << "please enter another number: ";
      cin >> aa2;
      cout << aa1 << " + " << aa2 << " + " << aa1+aa2 << "\n";
  
  }
  if (input == "m")
  {
	  int am1;
      int am2;
	  cout << "please enter a number: ";
      cin >> am1;
      cout << "please enter another number: ";
      cin >> am2;
      cout << am1 << " x " << am2 << " = " << am1*am2 << "\n";
  
  }
  if (input == "d")
  {
	  int ad1;
      int ad2;
	  cout << "please enter a number: ";
      cin >> ad1;
      cout << "please enter another number: ";
      cin >> ad2;
      cout << ad1 << " ÷ " << ad2 << " = " << ad1/ad2 << "\n";
  
  }
  if (input == "s")
  {
	  int as1;
      int as2;
	  cout << "please enter a number: ";
      cin >> as1;
      cout << "please enter another number: ";
      cin >> as2;
      cout << as1 << " - " << as2 << " = " << as1-as2 << "\n";
  
  }
}

