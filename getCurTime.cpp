#include<iostream>
#include<thread>
#include<chrono>
using namespace std;
double getCurTimeInSeconds()
{
    auto now=chrono::system_clock::now();
    return now.time_since_epoch().count()*1e-6;
}
int main()
{
    cout<<fixed;
    while(true)
    {
        cout<<getCurTimeInSeconds()<<endl;
    }
    return 0;
}