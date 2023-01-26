import pandas as pd #dependency
import numpy as np #dependency

df_teacher = pd.DataFrame({
    "name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
    "married": [True, True, False, True],
    "school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
    })

df_student = pd.DataFrame({
    "teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
    "name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino",
    "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
    "age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
    "height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m']
    })

df_teacher_copy = pd.DataFrame({
    "teacher": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
    "school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan],
    "married": [True, True, False, True]
    })

df_grouped_student = df_student.groupby('teacher').agg(list)

name_list = []
age_list = []
height_list = []

for i in range(3):
    name_list.extend(df_grouped_student['name'].to_list()[i])
    age_list.extend(df_grouped_student['age'].to_list()[i])
    height_list.extend(df_grouped_student['height'].to_list()[i])


df_result =pd.DataFrame({
    "name": name_list,
    "age": age_list,
    "height": height_list
})

df_teacher_copy["Students"] = [df_result.loc[0:2].transpose().to_dict()], [df_result.loc[3:5].transpose().to_dict()], [df_result.loc[6:8].transpose().to_dict()],"np.nan"

print(df_teacher_copy.to_dict("records"))
print(df_teacher_copy)