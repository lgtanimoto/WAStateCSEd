from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
from pandas.core.accessor import delegate_names

schoolTeachers = pd.read_excel('./2022-23-k-12-computer-science-education-data-summary-report.xlsx','Teachers_School', header=1)

print (schoolTeachers.dtypes)

#schoolCSEnrollment.columns = ['schoolYear','DistrictCode','DistrictName','SchoolCode','SchoolName','Program','StudentGroup','TotalStudents','CSE-All','Pct-CSE-All','CSE-CourseCode','Pct-CSE-CourseCode']
schoolTeachers.columns = ['SchoolYear','LEACode','LEAName','SchoolCode','SchoolName','Category','TeacherGroup','CSTeacherCount','GroupCount','GroupTeacherPct']


temp_list=[]

s_schoolYear = 'temp'
s_districtCode = -1
s_schoolCode = -1
s_schoolName = "temp"
s_csteachers = 0

g_female = 0
g_male = 0

r_native = 0
r_asian = 0
r_black = 0
r_hisp_lat = 0
r_hpi = 0
r_notprovided = 0
r_twoormore = 0
r_white = 0

e_5ormore = 0
e_lessthan5 = 0
e_notprovided = 0

d_master = 0
d_bachelor = 0
d_doctor = 0
d_other = 0
d_specialist = 0

c_ctefull = 0
c_ctelimited = 0
c_certfull = 0
c_certlimited = 0

q_infield = 0
q_outfield = 0
q_certfull = 0
q_certlimit = 0


for index, row in schoolTeachers.iterrows():
    
    if (s_schoolCode != row['SchoolCode']):

        if (s_schoolCode != -1):
            print ("add row for school code: " + str(s_schoolCode) + " Year: " + str(s_schoolYear))
            temp_list.append(
                {   'SchoolYear': s_schoolYear,
                    'DistrictCode': s_districtCode,
                    'SchoolCode': s_schoolCode,
					'SchoolName': s_schoolName,
                    'SchoolCSTeachers' : s_csteachers,
                    'G_Female' : g_female,
                    'G_Male': g_male,
                    'R_Native': r_native,
                    'R_Asian': r_asian,
                    'R_Black': r_black,
                    'R_Hisp_Lat': r_hisp_lat,
                    'R_HPI': r_hpi,
                    'R_NotProvided': r_notprovided,
                    'R_TwoOrMore': r_twoormore,
                    'R_White': r_white,
                    'E_5OrMore': e_5ormore,
                    'E_LessThan5': e_lessthan5,
                    'E_NotProvided': e_notprovided,
                    'D_Master':  d_master,
                    'D_Bachelor': d_bachelor,
                    'D_Doctor': d_doctor,
                    'D_Other': d_other,
                    'C_CteFull': c_ctefull,
                    'C_CteLimited': c_ctelimited,
                    'C_CertFull': c_certfull,
                    'C_CertLimited': c_certlimited,
                    'Q_InField': q_infield,
                    'Q_OutField': q_outfield,
                    'Q_CertFull': q_certfull,
                    'Q_CertLimit': q_certlimit
                 })
         
        s_schoolYear = row['SchoolYear']    
        s_schoolCode = row['SchoolCode']
        s_districtCode = row['LEACode']
        s_schoolName = str(row['SchoolName'])
        s_csteachers = int(row['CSTeacherCount'])

        g_female = 0
        g_male = 0

        r_native = 0
        r_asian = 0
        r_black = 0
        r_hisp_lat = 0
        r_hpi = 0
        r_notprovided = 0
        r_twoormore = 0
        r_white = 0

        e_5ormore = 0
        e_lessthan5 = 0
        e_notprovided = 0

        d_master = 0
        d_bachelor = 0
        d_doctor = 0
        d_other = 0
        d_specialist = 0

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
        group = str(row['TeacherGroup']).upper()[0:3]

        if (group == 'FEM'):
            g_female = row['GroupCount']
        elif (group == 'MAL'):
            g_male = row['GroupCount']
        else:
            print ("Invalid data" + category + ", " + group)

    elif (category == 'FED'):   #Race/Ethincity
        group = str(row['TeacherGroup']).upper()[0:3]

        if (group == 'AME'):  #American Indian
            r_native = row['GroupCount']
        elif (group== 'ASI'):
            r_asian = row['GroupCount']
        elif (group == 'BLA'):
            r_black = row['GroupCount']
        elif (group == 'HIS'):
            r_hisp_lat = row['GroupCount']
        elif (group == 'NAT'):     #Native Hawaiian/Pacific Islander
            r_hpi = row['GroupCount']
        elif (group == 'RAC'):
            r_notprovided = row['GroupCount']
        elif (group == 'TWO'):
            r_twoormore = row['GroupCount']
        elif (group== 'WHI'):
            r_white = row['GroupCount']
        else:
            print ("Invalid data" + category + ", " + group)

    elif (category == 'HIG'):  #Highest Degree
        group = str(row['TeacherGroup']).upper()[0:3]

        if (group =='BAC'):
            d_bachelor = row['GroupCount']
        elif (group == 'DOC'):
            d_doctor =  row['GroupCount']
        elif (group == 'MAS'):
            d_master =  row['GroupCount']
        elif (group == 'OTH'):
            d_other =  row['GroupCount']
        elif (group == 'SPE'):
            d_specialist =  row['GroupCount']
        else:
            print ("Invalid data" + category + ", " + group)

    elif (category == 'TEA'):  #Teacher Qualification

        group = str(row['TeacherGroup']).upper()[0:3]

        if (group =='IN-'):
            q_infield = row['GroupCount']
        elif (group == 'OUT'):
            q_outfield =  row['GroupCount']
        elif (group == 'FUL'):
            q_certfull =  row['GroupCount']
        elif (group == 'LIM'):
            q_certlimit =  row['GroupCount']
        elif (group == 'SPE'):
            d_specialist =  row['GroupCount']
        else:
            print ("Invalid data" + category + ", " + group)
 
    elif (category == 'CER'):  # Certificates Held or Certificated Experience

        category = row['Category'].upper()  #get full category string

        if (category == 'CERTIFICATES HELD'):

            group = str(row['TeacherGroup']).upper()
            if (group[0:3] == 'FUL'):  # 5 or more
                if 'CTE' in group:
                    c_ctefull = row['GroupCount']
                else:
                    c_certfull = row['GroupCount']
            elif (group[0:3] == 'LIM'): # less than 5
                if 'CTE' in group:
                    c_ctelimited = row['GroupCount']
                else:
                    c_certlimited = row['GroupCount']
            else:
                print ("Invalid data " + category + ", " + group)
     
        elif (category == 'CERTIFICATED EXPERIENCE'): 
            
            group = str(row['TeacherGroup']).upper()[0:3]
            if (group == '5 O'):  # 5 or more
                e_5ormore = row['GroupCount']
            elif (group == 'LES'): # less than 5
                e_lessthan5 = row['GroupCount']
            elif (group == 'EXP'): # experience not provided
                e_notprovided = row['GroupCount']
            else:
                print ("Invalid data " + category + ", " + group)
 
        else:
            print ("Invalid data" + category )
 
    else:
         print ("Invalid data" + category )
    # end of row processing
            
print ("add row for school code: " + str(s_schoolCode) + " Year: " + str(s_schoolYear))
temp_list.append(
{   'SchoolYear': s_schoolYear,
    'DistrictCode': s_districtCode,
    'SchoolCode': s_schoolCode,
	'SchoolName': s_schoolName,
    'SchoolCSTeachers' : s_csteachers,
    'G_Female' : g_female,
    'G_Male': g_male,
    'R_Native': r_native,
    'R_Asian': r_asian,
    'R_Black': r_black,
    'R_Hisp_Lat': r_hisp_lat,
    'R_HPI': r_hpi,
    'R_NotProvided': r_notprovided,
    'R_TwoOrMore': r_twoormore,
    'R_White': r_white,
    'E_5OrMore': e_5ormore,
    'E_LessThan5': e_lessthan5,
    'E_NotProvided': e_notprovided,
    'D_Master':  d_master,
    'D_Bachelor': d_bachelor,
    'D_Doctor': d_doctor,
    'D_Other': d_other,
    'C_CteFull': c_ctefull,
    'C_CteLimited': c_ctelimited,
    'C_CertFull': c_certfull,
    'C_CertLimited': c_certlimited,
    'Q_InField': q_infield,
    'Q_OutField': q_outfield,
    'Q_CertFull': q_certfull,
    'Q_CertLimit': q_certlimit
})

school_df = pd.DataFrame(temp_list) 
school_df.to_excel("teachers_2018_2023_pt.xlsx", columns=
		['SchoolYear', 'DistrictCode', 'SchoolCode','SchoolName', 'SchoolCSTeachers', 'G_Female', 'G_Male', 
         'R_Native', 'R_Asian', 'R_Black', 'R_Hisp_Lat', 'R_HPI', 'R_NotProvided', 'R_TwoOrMore', 'R_White', 
         'E_5OrMore', 'E_LessThan5', 'E_NotProvided', 'D_Master', 'D_Bachelor', 'D_Doctor', 'D_Other',
         'C_CteFull', 'C_CteLimited', 'C_CertFull', 'C_CertLimited', 
         'Q_InField', 'Q_OutField', 'Q_CertFull', 'Q_CertLimit'])

print ("Completed")

#FILEROOT = ""