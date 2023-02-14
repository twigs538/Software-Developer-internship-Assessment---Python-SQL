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
    
    # Create a copy of the original dataframes
    df_teacher_copy = df_teacher.copy()
    df_student_copy = df_student.copy()

    # Create an empty list to store the output
    output = []

    # Iterate over the rows of the teachers dataframe
    for index, row in df_teacher_copy.iterrows():
        # Create a dictionary for the current teacher
        teacher = {
            "teacher": row["name"],
            "school": row["school"],
            "married": row["married"],
            "Students": []
        }
        
        # Filter the students dataframe to get only the students of the current teacher
        students = df_student_copy[df_student_copy["teacher"] == row["name"]]
        
        # Iterate over the rows of the filtered students dataframe
        for student_index, student_row in students.iterrows():
            # Append a dictionary for each student to the "Students" list of the current teacher
            teacher["Students"].append({
                "student": student_row["name"],
                "age": student_row["age"],
                "height": student_row["height"]
            })
        
        # Append the current teacher dictionary to the output list
        output.append(teacher)

    # The final output is stored in the "output" list
    #print(output)


    return Response(output)