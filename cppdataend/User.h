#include <string>
#include <vector>
#include <iostream>

struct Class {

    void setTime (int time);
    void setName (const std::string& name);
    int getTime () const;
    std::string getName () const;
   private:
    std::string className;
    int classTime;
};

class User {
  public:
    User()
        :_name("noName"), _key(-1), _next(nullptr) {};
    User( const int key, const std::string& name)
        :_name(name), _key(key), _next(nullptr) {};
    // accessor
    int getKey() const { return _key; };
    std::string getName() const { return _name; }
    // mutator
    void setName(const std::string& newName) { _name = newName; }
    // print
    virtual void printInfo() {
        std::cout << "User name: " << _name << std::endl;
        std::cout << "User Key: "<< _key << std::endl;
    }

  private:
    std::string _name;
    int _key;
    User* _next;
};

class Student : public User {
  public :
    Student() : User(), _grade(-1), _major("noMajor"), _numClasses(0) {};
    Student(int key, const std::string& name, int grade, const std::string& major, int numClasses) 
        :User(key, name), _grade(grade), _major(major), _numClasses(numClasses) {};
    // mutator
    void setGrade(int grade) { _grade = grade;}
    void setMajor(const std::string& major) { _major = major;}
    // accessor
    int getGrade() const { return _grade;}
    std::string getMajor() const { return _major; }
    // print
    void printInfo() {
        User::printInfo();
        std::cout << "grade: "<< _grade << std::endl;
        std::cout << "major: "<< _major << std::endl;
    }

  private :
    int _grade;
    std::string _major;
    int _numClasses;
    std::vector<Class> _classes;
};

class Employee : public User {
  public :
    Employee() 
        :User(), _tenure(0), _job("noJob"), _workDays("noWorkDays"), _startTime(-1), _endTime(-1) {};
    Employee (int key, const std::string& name, int tenure, const std::string& job, const std::string& workDays, int start, int end)
        :User(key, name), _tenure(tenure), _job(job), _workDays(workDays), _startTime(start), _endTime(end) {};
    // mutator
    void setTenure (int tenure) { _tenure = tenure; }
    void setJob (const std::string& job) { _job = job; }
    // accessor
    int getTenure () const { return _tenure; }
    std::string getJob () const { return _job; }
    // print
    void printInfo() {
        User::printInfo();
        std::cout << "tenure: " << _tenure << std::endl;
        std::cout << "job: " << _job<< std::endl;
        std::cout << "work days: "<< _workDays << std::endl;
        std::cout << _startTime << " -- " << _endTime << std::endl;
    }

  private :
    int _tenure;
    std::string _job;
    std::string _workDays;
    int _startTime;
    int _endTime;
};