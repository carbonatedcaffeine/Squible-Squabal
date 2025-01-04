class Student:
    def __init__(self,studentid,name,email) -> None:
        self._name = name
        self._id = studentid
        self._email = email

    def __str__(self):
        return f"Student ID: {self._id}\nName: {self._name}\nEmail: {self._email}"

s = Student("1234","Bob","bob@email.com")
print(f"{s._email = }")
print(s)