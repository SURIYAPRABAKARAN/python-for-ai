import pandas as pd


students_df = pd.read_csv("students_datas_for_validation.csv")

print(f"students_df :\n{students_df}\n")

print(f"shape :\n{students_df.shape}\n")

print(f"columns :\n{students_df.columns}\n")

print(f"head :\n{students_df.head()}\n")

print(f"tail :\n{students_df.tail()}\n")

def getGradeByMark(mark):
    if mark >= 90 and mark <= 100:
        return "A"
    elif mark >= 75 and mark <= 89:
        return "B"
    elif mark <= 50:
        return "C"
    else:
        return "Fail"

students_df["Grade"] =  students_df["Marks"].apply(getGradeByMark)
    
print(f"averge marks :\n{students_df["Marks"].mean()}\n")

print(f"top students by marks :\n{students_df[students_df["Marks"] > 80]}\n")

top_students_by_makrs = students_df[students_df["Marks"] > 80]

top_students_by_makrs.to_csv("top_students_by_makrs.csv",index=False)

new_file_with_top_students_by_makrs = pd.read_csv("top_students_by_makrs.csv")
sorted_data = new_file_with_top_students_by_makrs.sort_values(by="Marks",ascending=False)

print(f"new_file_with_top_students_by_makrs :\n {new_file_with_top_students_by_makrs}\n")

print(f"sorting :\n{sorted_data}\n")
