from datetime import datetime
from database.mongodb import MongoDB
import pandas as pd
import os


class UpdateAttendance:
    def __init__(self):
        # self.file_name = "Attendance.csv"
        self.student_db = MongoDB(data_base="Student", collection="face_encode")
        self.students = sorted(self.student_db.get_student_list())
        self.attendance_path = "attendance/Attendance.csv"
        self.today = datetime.today().strftime("%d-%m-%Y")

    def update_attendance(self, person_name):
        entry_dict = {}
        for i in self.students:
            if i == person_name:
                entry_dict[i] = 1
            else:
                entry_dict[i] = 0
        if not os.path.exists(self.attendance_path):
            entry = []
            name = []
            for key, value in entry_dict.items():
                name.append(key)
                entry.append(value)
            csv_file = pd.DataFrame({"Name": name, today: entry})
            csv_file.to_csv(self.attendance_path, sep=",", index=False)
        else:
            entry = []
            name = []
            for key, value in entry_dict.items():
                name.append(key)
                entry.append(value)
            df = pd.read_csv(self.attendance_path)

            new_names = []
            for i in self.students:
                if i not in list(df['Name']):
                    new_names.append(i)

            if len(new_names) != 0:
                for i in new_names:
                    df.loc[len(df)] = 0
                    df["Name"].iloc[-1] = i

            if self.today not in df.columns:
                df[self.today] = 0
                df.loc[df["Name"] == person_name, self.today] = 1
            elif self.today in df.columns:
                df.loc[df['Name'] == person_name, self.today] = 1

            df.to_csv(self.attendance_path, index=False)

        return True
