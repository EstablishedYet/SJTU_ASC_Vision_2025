#include<opencv2/opencv.hpp>
#include<iostream>
#include<chrono>
#include<thread>
#include<filesystem>
#include<string>
#include<fstream>
using namespace std;
double getCurrentTimeInSeconds()
{
    auto now=chrono::system_clock::now();
    return now.time_since_epoch().count()*1e-6;
}
int main()
{
    cv::VideoCapture cap(0);
    cap.set(cv::CAP_PROP_FOURCC,  cv::VideoWriter::fourcc('M', 'J', 'P', 'G'));
    // cap.set(cv::CAP_PROP_FOURCC,cv::VideoWriter_fourcc(*'MJPG'))
    cap.set(cv::CAP_PROP_FPS, 30);
    int fw=1920;
    int fh=1080;
    cap.set(cv::CAP_PROP_FRAME_WIDTH, fw);
    cap.set(cv::CAP_PROP_FRAME_HEIGHT, fh);
    cap.set(cv::CAP_PROP_BUFFERSIZE, 1);
    this_thread::sleep_for(chrono::seconds(5));
    // auto now=chrono::system_clock::now();
    // auto curSeconds=static_cast<chrono::seconds>
    double t0=getCurrentTimeInSeconds();
    cv::Mat frame;
    double curTime;
    string path="/home/amov/buffertest/";
    filesystem::remove_all(path);
    filesystem::create_directory(path);
    ofstream file(path+"log.txt");
    int i=0;
    while(true)
    {
        curTime=getCurrentTimeInSeconds();
        cap>>frame;
        if(curTime-t0>10)
        {
            break;
        }
        cv::imwrite(path+to_string(i)+".jpg",frame);
        file<<i<<' '<<curTime<<endl;
    }
    return 0;
}