/*
* This is some fun notes stuff that I want
* to keep note of when practicing C++ concepts
*/

/*Q12. According to C++23 standard, what is the output?*/
#include <iostream>

int main()
{
    static int a;
    std::cout << a;
}
/*Prints out 0 because a is a static local variable,
* which is initialized to 0. This wouldn't be 0 if 
* the static keyword is removed.
*
* Note: In C++, when a variable id declared as static at
* any scope (local or global), it gets zero-intialized for
* scalar type variables (int, float, long, bool, pointers)
*/

/*Q. 113 Accouring to the C++23 standard, what is the output?*/
#include <iostream>
template<typename T>
void f(T){
    std::cout << 1;
}

template<>
void f(int){
    std::cout << 2;
}

void f(int){
    std::cout << 3;
}

int main(){
    f(0.0);
    f(0);
    f<>(0);
}
/*
* Answer: 132
* Reason: There
* are 3 calls to f (f(0.0), f(0), and f<>(0)).
* f(0.0) has T deduced as a double. The non-template int
* is a good match, but the template-T is the best match. The
* specialization void f(double) is added as a candidate for
* overload resolution. So 1 is printed.
*
* f(0) has T deduced as an int. The non-template int
* is the best match. void f(int) is added as a candidate
* for overload resolution. So 3 is printed.
*
*
* f <>(0) is an empty template argument list; specified for
* template functions, but not for non-template functions. 
* It has T deduced to int, the spacialization for int is the 
* only candidate and only used template function. 2 is printed.
*/