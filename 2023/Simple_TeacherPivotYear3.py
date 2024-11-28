from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
from pandas.core.accessor import delegate_names

yearTeachers = pd.read_excel('./2022-23-k-12-computer-science-education-data-summary-report.xlsx','Teachers_State', header=1)

print (yearTeachers.dtypes)

#schoolCSEnrollment.columns = ['schoolYear','DistrictCode','DistrictName','SchoolCode','SchoolName','Program','StudentGroup','TotalStudents','CSE-All','Pct-CSE-All','CSE-CourseCode','Pct-CSE-CourseCode']
yearTeachers.columns = ['SchoolYear','Category','TeacherGroup','CSTeacherCount','GroupCount','GroupTeacherPct']

temp_list=[]

def listWrite(tyear, tcat, tgroup, allcount, gcount):
    temp_list.append(
    {   'SchoolYear': tyear,
        'Category' : tcat,
        'TeacherGroup' : tgroup,
        'CSTeacherCount' : allcount,
        'GroupCount' : gcount,
        'GroupTeacherPct': 1.0 * gcount / allcount
    })


s_schoolYear = 'temp'
s_csteachers = 0

c_ctefull = 0
c_ctelimited = 0
c_certfull = 0
c_certlimited = 0

q_infield = 0
q_outfield = 0
q_certfull = 0
q_certlimit = 0


for index, row in yearTeachers.iterrows():
    
    if (s_schoolYear != row['SchoolYear']):

        if (s_schoolYear != "temp"):
            print ("adding rows for school year: " + str(s_schoolYear))

            listWrite(s_schoolYear, 'All','All', s_csteachers, s_csteachers)
            listWrite(s_schoolYear, 'Field Status', 'In-Field Status', s_csteachers, s_csteachers - q_outfield)
            listWrite(s_schoolYear, 'Certificate Status', 'Full Certificate Status', s_csteachers, s_csteachers - q_certlimit)
            listWrite(s_schoolYear, 'CTE Certification Status', 'No CTE Certificate Est', s_csteachers, s_csteachers - c_ctefull - c_ctelimited)
            listWrite(s_schoolYear, 'Traditional Certification Status', 'No Traditional Certificate Est', s_csteachers, s_csteachers - c_certfull - c_certlimited)
         
        s_schoolYear = row['SchoolYear']    
        s_csteachers = int(row['CSTeacherCount'])
        

        c_ctefull = 0
        c_ctelimited = 0
        c_certfull = 0
        c_certlimited = 0

        q_infield = 0
        q_outfield = 0
        q_certfull = 0
        q_certlimit = 0
               
    category = row['Category'].upper()[0:3]

  
    if (category == 'GEN'): #Gender
        listWrite(s_schoolYear, row['Category'], row['TeacherGroup'],  s_csteachers, row['GroupCount'] )

    elif (category == 'FED'):   #Race/Ethincity
        listWrite(s_schoolYear, row['Category'], row['TeacherGroup'],  s_csteachers, row['GroupCount'] )

    elif (category == 'HIG'):  #Highest Degree
        listWrite(s_schoolYear, row['Category'], row['TeacherGroup'],  s_csteachers, row['GroupCount'] )

    elif (category == 'TEA'):  #Teacher Qualification

        group = str(row['TeacherGroup']).upper()[0:3]

        if (group =='IN-'):
            q_infield = row['GroupCount']
            listWrite(s_schoolYear, 'Field Status Non_Adj', row['TeacherGroup'], s_csteachers, row['GroupCount'],  )
        elif (group == 'OUT'):
            q_outfield =  row['GroupCount']
            listWrite(s_schoolYear, 'Field Status',  row['TeacherGroup'],  s_csteachers, row['GroupCount'])
        elif (group == 'FUL'):
            q_certfull =  row['GroupCount']
            listWrite(s_schoolYear, 'Certificate Status Non_Adj', row['TeacherGroup'], s_csteachers, row['GroupCount'])
        elif (group == 'LIM'):
            q_certlimit =  row['GroupCount']
            listWrite(s_schoolYear, 'Certificate Status',  row['TeacherGroup'], s_csteachers, row['GroupCount'])
        else:
            print ("Invalid data" + category + ", " + group)
 
    elif (category == 'CER'):  # Certificates Held or Certificated Experience

        category = row['Category'].upper()  #get full category string

        if (category == 'CERTIFICATES HELD'):

            group = str(row['TeacherGroup']).upper()
            if (group[0:3] == 'FUL'):  # 5 or more
                if 'CTE' in group:
                    c_ctefull = row['GroupCount']
                    listWrite(s_schoolYear, 'CTE Certification Status', row['TeacherGroup'], s_csteachers, row['GroupCount'])
                else:
                    c_certfull = row['GroupCount']
                    listWrite(s_schoolYear,  'Traditional Certification Status', row['TeacherGroup'], s_csteachers, row['GroupCount'])
            elif (group[0:3] == 'LIM'): # less than 5
                if 'CTE' in group:
                    c_ctelimited = row['GroupCount']
                    listWrite(s_schoolYear, 'CTE Certification Status',  row['TeacherGroup'], s_csteachers, row['GroupCount'])
                else:
                    c_certlimited = row['GroupCount']
                    listWrite(s_schoolYear, 'Traditional Certification Status',  row['TeacherGroup'], s_csteachers, row['GroupCount'])
            else:
                print ("Invalid data " + category + ", " + group)
     
        elif (category == 'CERTIFICATED EXPERIENCE'): 
            
            listWrite(s_schoolYear, row['Category'], row['TeacherGroup'],  s_csteachers, row['GroupCount'])
            
        else:
            print ("Invalid data" + category )
 
    else:
         print ("Invalid data" + category )
    # end of row processing
            
print ("add row for Year: " + str(s_schoolYear))
listWrite(s_schoolYear, 'All','All', s_csteachers, s_csteachers)
listWrite(s_schoolYear, 'Field Status', 'In-Field Status', s_csteachers, s_csteachers - q_outfield)
listWrite(s_schoolYear, 'Certificate Status', 'Full Certificate Status', s_csteachers, s_csteachers - q_certlimit)
listWrite(s_schoolYear, 'CTE Certification Status', 'No CTE Certificate Est', s_csteachers, s_csteachers - c_ctefull - c_ctelimited)
listWrite(s_schoolYear, 'Traditional Certification Status', 'No Traditional Certificate Est', s_csteachers, s_csteachers - c_certfull - c_certlimited)

teacher_df = pd.DataFrame(temp_list) 
teacher_df.to_excel("yearteachers_2018_2023_adj.xlsx", columns=
		['SchoolYear','Category','TeacherGroup','CSTeacherCount','GroupCount','GroupTeacherPct'])

print ("Completed")

#FILEROOT = ""