#include <string>
#include <fstream>
#include <iostream>
#include "User.h"

int readUser(const std::string& file);

int main() {
    std::string fileName;
    std::cin >> fileName;
    if(!std::cin.good()) { std::cout << "Filename failed to read.\n"; return 1;}
    readUser(fileName);
    std::cout << "end of code" << std::endl;
    return 0;
}

int readUser(const std::string& file) {
    User* newUser;
    std::string fileName = file;
    std::ifstream inFile(fileName);
    if(!inFile.is_open()) { std::cout << "Error reading in file" << fileName << std::endl; return 1; }
    int key;
    inFile >> key;
    if(!inFile.good()) { std::cout << "failed to read in key." << std::endl; return 1; }
    std::string name;
    inFile >> name;
    if(!inFile.good()) { std::cout << "failed to read in name." << std::endl; return 1; }
    std::string userType;
    inFile >> userType >> std::ws;
    if(!inFile.good()) { std::cout << "failed to read in userType." << std::endl; return 1; }
    std::cout << "read in key, name, user type:" << key << ", " << name << ", " << userType << std::endl;
    if(userType == "student") {
        int grade;
        inFile >> grade;
        if(!inFile.good()) { std::cout << "failed to read in grade." << std::endl; return 1; }
        std::string major;
        inFile >> major;
        if(!inFile.good()) { std::cout << "failed to read in major." << std::endl; return 1; }
        int numClasses = 0;
        newUser = new Student(key, name, grade, major, numClasses);
    } else {
        if(userType == "employee") {
            int tenure;
            inFile >> tenure;
            if(!inFile.good()) { std::cout << "failed to read in tenure" << std::endl; return 1; }
            std::string job;
            inFile >> job;
            if(!inFile.good()) { std::cout << "failed to read in job." << std::endl; return 1; }
            std::string workDays;
            inFile >> workDays;
            if(!inFile.good()) { std::cout << "failed to read in work days" << std::endl; return 1; }
            int startTime;
            int endTime;
            inFile >> startTime;
            if(!inFile.good()) { std::cout << "failed to read in startTime." << std::endl; return 1; }
            inFile >> endTime;
            if(!inFile.good()) { std::cout << "failed to read in endTime." << std::endl; return 1; }
            
            newUser = new Employee(key, name, tenure, job, workDays, startTime, endTime);
        } else {
            std::cout << "error, user type passed in not recognized. \n" <<
                        "usage: key name usertype ...\n"; 
            return 1;
        }
    }
    newUser->printInfo();
    delete newUser;
}

