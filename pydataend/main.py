class Class: # class that a student is enrolled in
    def __init__(self):
        #class has a name (ex: math011)
        self.class_name = ""
        #and a time (ex: MW, 3-5)
        self.class_time = 0

    def set_time(self, time):
        self.class_time = time

    def set_name(self, name):
        self.class_name = name

    def get_time(self):
        return self.class_time

    def get_name(self):
        return self.class_name


class User: #base class for users, classes student and employee inherit User
    def __init__(self, key=-1, name="noName"):
        #all users, students or employees have a name and a key 
        #key is the user's unqiue ID, it is also their position in the array of users
        self._name = name
        self._key = key

    def get_key(self):
        return self._key

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def print_info(self):
        print(f"User name: {self._name}")
        print(f"User Key: {self._key}")


class Student(User):
    def __init__(self, key=-1, name="noName", grade=-1, major="noMajor", num_classes=0):
        super().__init__(key, name)
        #students have a grade (ex: sophomore)
        self._grade = grade
        #students have a major (computer science)
        self._major = major
        #students have a number of classes
        self._num_classes = num_classes
        #and an array of class objects, aka the students schedule
        self._classes = []

    def set_grade(self, grade):
        self._grade = grade

    def set_major(self, major):
        self._major = major

    def get_grade(self):
        return self._grade

    def get_major(self):
        return self._major

    def print_info(self):
        super().print_info()
        print(f"Grade: {self._grade}")
        print(f"Major: {self._major}")


class Employee(User):
    def __init__(self, key=-1, name="noName", tenure=0, job="noJob", work_days="noWorkDays", start_time=-1, end_time=-1):
        super().__init__(key, name)
        #employeers have tenure (ex: 4 )
        self._tenure = tenure
        #and a job (ex: professor)
        self._job = job
        #and work days (ex: MTW)
        self._work_days = work_days
        #start time ex: 10am
        self._start_time = start_time
        #and an end time ex: 7 pm
        self._end_time = end_time

    def set_tenure(self, tenure):
        self._tenure = tenure

    def set_job(self, job):
        self._job = job

    def get_tenure(self):
        return self._tenure

    def get_job(self):
        return self._job

    def print_info(self):
        super().print_info()
        print(f"Tenure: {self._tenure}")
        print(f"Job: {self._job}")
        print(f"Work Days: {self._work_days}")
        print(f"{self._start_time} -- {self._end_time}")


def read_user(file_name): #read users in from input
    try:
        with open(file_name, 'r') as file:
            key = int(file.readline().strip())
            name = file.readline().strip()
            user_type = file.readline().strip()

            print(f"Read in key, name, user type: {key}, {name}, {user_type}")

            if user_type == "student":
                grade = int(file.readline().strip())
                major = file.readline().strip()
                num_classes = 0
                new_user = Student(key, name, grade, major, num_classes)

            elif user_type == "employee":
                tenure = int(file.readline().strip())
                job = file.readline().strip()
                work_days = file.readline().strip()
                start_time = int(file.readline().strip())
                end_time = int(file.readline().strip())
                new_user = Employee(key, name, tenure, job, work_days, start_time, end_time)

            else:
                print("Error: User type not recognized. Usage: key name usertype ...")
                return

            new_user.print_info()

    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")
    except ValueError as e:
        print(f"Error: Invalid data format. {e}")


if __name__ == "__main__":
    file_name = input("Enter the filename: ").strip()
    read_user(file_name)
    print("End of code")
