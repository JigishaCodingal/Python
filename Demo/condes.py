class student:
    def __init__(self):
        print("student object created")
    def __del__(self):
        print("Student object is destroyed")
ob=student()
del ob
