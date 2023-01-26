from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pandas as pd #dependency
import numpy as np #dependency

@api_view(['GET'])
def get_params(request):
    df_teacher = pd.DataFrame({
    "name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
    "married": [True, True, False, True],
    "school": ["Manchester High School", "Liverpool High School", "Arsenal High", "np.nan"]
    })

    df_student = pd.DataFrame({
    "teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
    "name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino",
    "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
    "age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
    "height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m']
    })

    df_teacher_copy = pd.DataFrame({
    "teacher": ["Jurgen Klopp", "Mikel Arteta","Pep Guardiola", "Zinadine Zidane"],
    "school": ["Liverpool High School", "Arsenal High","Manchester High School", "np.nan"],
    "married": [True, False, True, True]
    })

    df_student_copy = pd.DataFrame({
    "teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
    "student": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino",
    "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
    "age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
    "height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m']
    })
    
    df_grouped_student = df_student.groupby('teacher').agg(list)
    df_test_group_student = df_grouped_student.to_dict("records")
    df_test_group_student2 =pd.DataFrame(df_test_group_student)

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
    
    #mydict = df_grouped_student
    student_list = df_grouped_student.values.tolist()
    #student_list.append("Student")
    #df = pd.DataFrame (student_list)
    #df.columns = ['student', 'age','height']
    df_teacher_copy["Students"] = [df_result.loc[0:2].transpose().to_dict()], [df_result.loc[3:5].transpose().to_dict()], [df_result.loc[6:8].transpose().to_dict()],"np.nan"

    #mydict = df_grouped_student.to_dict("records")
    mydict = df_teacher_copy.to_dict("records")
    #mydict = df_test2.to_dict("records")

    return Response(mydict)

#def get_params():
#    content = {

#    }

    #return Response(content, status=status.HTTP_200_OK)