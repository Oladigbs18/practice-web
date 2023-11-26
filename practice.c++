// my first learning using c++ or Cpp.

#include <iostream>
using namespace std;

int main(){
    cout << "Hello World!\n";
    cout<<"My name is Aaliyah." << endl;
    cout<< "I love coding";

    // float annualSalary = 150000.99;
    //float monthlySalary = annualSalary / 12;
    //cout << "Your monthly salary is " << monthlySalary;

    float annualSalary;
    cout << "Please enter your annual salary ";
    cin >> annualSalary;
    float monthlySalary = annualSalary / 12;
    cout << "Your monthly salary is " << monthlySalary  << endl;
    cout << "In 10 years you will earn " << annualSalary * 10;

    char myCharacter = 'b';
    int myAge = 14;
    float myHeight = 6.2;
    bool iAmOlderThan18 = true;
    double amount = 5784473209454529485;

    cout << "The size of int is " << sizeof(int) << "bytes\n";
    cout << "The size of float is " << sizeof(float) << "bytes\n";
    cout << "The min value of int is " << INT_MIN << endl;
    cout << "The max value of int is " << INT_MAX << endl;
    system("pause>0"); 
}