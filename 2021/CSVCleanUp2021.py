from numpy.core.numeric import NaN
import pandas as pd
import numpy as np


#FILEROOT = ""

def coursesPlyData():
    courses = pd.read_excel('../Computer Science Course Enrollment and Educator Data 2020-21 SY.xlsx','Comp Sci Courses by School')
    print (courses.dtypes)

    courses.columns = ['DistrictName','SchoolName','Term','CourseCode','CourseName']
    #state = state.drop(state[state.SchoolYear==NaN].index, inplace=True) 

    courses.dropna(axis='index',how='any',inplace=True) # drop null lines
    courses = courses.astype({'CourseCode':str})

    courses.to_csv("2021_courses_t.csv") 


def statePlyData():

    state = pd.read_excel('../Computer Science Course Enrollment and Educator Data 2020-21 SY.xlsx','State')
    print (state.dtypes)


    state.columns = ['SchoolYear','Program','StudentGroup','TotalStudents9-12','CSStudentsCIPorCourse',
                   'PctCSStudentsCIPorCourse','CSStudentsCourseOnly','PctCSStudentsCourseOnly']
    #state = state.drop(state[state.SchoolYear==NaN].index, inplace=True) 

    state.dropna(axis='index',how='all',inplace=True) # drop null lines
    state = state.astype({'SchoolYear':int,'TotalStudents9-12':int,'CSStudentsCIPorCourse':int,'CSStudentsCourseOnly':int})

    state.to_csv("2021_state_t.csv") 

def schoolAddressData():

    schoolAddressMainT = pd.read_csv("Washington_Education_School_Directory_07_17_2020-geocode.csv")
    print (schoolAddressMainT.dtypes)

    schoolAddressExtraT = pd.read_csv("MissingSchools-2021_geocodio.csv")
    print (schoolAddressExtraT.dtypes)

    schoolAddressMain = schoolAddressMainT[['LEACode','SchoolCode','SchoolName','AddressLine1','City','State','ZipCode',
                                           'Latitude','Longitude','State Legislative District House Number','Congressional District']].copy()

    schoolAddressExtra = schoolAddressExtraT[['DistrictCode','SchoolCode','SchoolName','Address','City','State','ZIP',
                                           'Latitude.1','Longitude.1','State Legislative District House Number','Congressional District']].copy()

    schoolAddressMain.columns = ['DistrictCode','SchoolCode','SchoolName','Address','City','State','ZipCode',
                                           'Latitude','Longitude','StateDistrictNo','CongressionalDistrict']

    schoolAddressMain.drop(schoolAddressMain[schoolAddressMain.Latitude==0].index, inplace=True)
   
    schoolAddressExtra.columns = ['DistrictCode','SchoolCode','SchoolName','Address','City','State','ZipCode',
                                           'Latitude','Longitude','StateDistrictNo','CongressionalDistrict']

    total = pd.concat([schoolAddressMain,schoolAddressExtra],ignore_index=True)

    total['StateDistrictNo'] = "#" + total['StateDistrictNo'].astype('str')
    total.to_csv("SchoolLocations_2021.csv")
    
    districtAddressT = pd.read_csv("Washington_District_Directory_20230626_geocodio.csv")
    print (districtAddressT.dtypes)

    districtAddress = districtAddressT[['ESDCode','DistrictCode','DistrictName','AddressLine1','City','State','Zipcode','Latitude','Longitude','Congressional District','State Legislative District House Number']].copy()

    districtAddress.columns = ['ESDCode','DistrictCode','DistrictName','D-Address','D-City','D-State','D-ZipCode','D-Latitude','D-Longitude','D-CongressionalDistrict','D-StateDistrictNo']

    districtAddress['ESDCode'] = "_" + districtAddress['ESDCode'].astype('str')

    districtAddress.to_csv("DistrictLocations_2021.csv")

    ESDAddressT = pd.read_csv("ESDInfo-2021_geocodio.csv")
    print (ESDAddressT.dtypes)


    ESDAddress = ESDAddressT[['ESDCode','ESDAbbv','AddressLIne','City','State','Zip','Latitude','Longitude','Congressional District','State Legislative District House Number']].copy()

    ESDAddress.columns = ['ESDCode','ESDAbbv','E-Address','E-City','E-State','E-ZipCode','E-Latitude','E-Longitude','E-CongressionalDistrict','E-StateDistrictNo']

    ESDAddress['ESDCode'] = "_" + ESDAddress['ESDCode'].astype('str')
    ESDAddress.to_csv("ESDLocations_2021.csv")

def SchoolEnrollmentData():

     schoolCSEnrollmentT = pd.read_excel('../Computer Science Course Enrollment and Educator Data 2020-21 SY.xlsx','School')
     print (schoolCSEnrollmentT.dtypes)

     schoolCSEnrollmentT.columns = ['schoolYear','DistrictCode','DistrictName','SchoolCode','SchoolName','Program','StudentGroup','TotalStudents','CSE-All','Pct-CSE-All','CSE-CourseCode','Pct-CSE-CourseCode']

     schoolCSEnrollment = schoolCSEnrollmentT[['DistrictCode','SchoolCode','SchoolName','Program','StudentGroup','TotalStudents','CSE-All','CSE-CourseCode']].copy()
          
     schoolCSEnrollment.drop(schoolCSEnrollment[schoolCSEnrollment['Program'] != 'AllStudents'].index,inplace=True)
     
     schoolCSEnrollment.to_csv("SchoolCSEEnrollmentOnly_2021.csv")

def teacherPlyData():

    teacher = pd.read_excel('../Computer Science Course Enrollment and Educator Data 2020-21 SY.xlsx','Comp Sci Educator Info')
    print (teacher.dtypes)
    teacher.reset_index()

    temp_list=[]
    s_school = ""
    s_district = ""
    s_totalcount = 0
    d_bachelor = 0
    d_doctor = 0
    d_master = 0
    d_other = 0
    d_unk = 0
    g_female = 0
    g_male = 0
    g_unk = 0
    r_natame = 0
    r_asian = 0
    r_black = 0
    r_hisplat = 0
    r_hpi = 0
    r_notprovided = 0
    r_twoormore = 0
    r_white = 0
    r_unk = 0

    for index, row in teacher.iterrows():
    
        if (s_school != row['SchoolName'] or s_district != row['DistrictName']):

            print (row['SchoolName'] + " " + row['DistrictName'])
            if (s_school != ""):
                print ("added row")
                temp_list.append(
                    {'DistrictName': s_district,
                     'SchoolName': s_school,
                     'TotalCount': s_totalcount,
                     'D_Bachelor': d_bachelor,
                     'D_Doctor': d_doctor,
                     'D_Master': d_master,
                     'D_Other': d_other,
                     'D_UNK': d_unk,
                     'G_Female' : g_female,
                     'G_Male': g_male,
                     'G_UNK': g_unk,
                     'R_NatAme': r_natame,
                     'R_Asian': r_asian,
                     'R_Black': r_black,
                     'R_HispLat': r_hisplat,
                     'R_HPI': r_hpi,
                     'R_NotProvided': r_notprovided,
                     'R_TwoOrMore': r_twoormore,
                     'R_White': r_white,
                     'R_UNK': r_unk}
                    )
            
            s_school = row['SchoolName']
            s_district = row['DistrictName']
            s_totalcount = row['TotalCount']
            d_bachelor = 0
            d_doctor = 0
            d_master = 0
            d_other = 0
            d_unk = 0
            g_female = 0
            g_male = 0
            g_unk = 0
            r_natame = 0
            r_asian = 0
            r_black = 0
            r_hisplat = 0
            r_hpi = 0
            r_notprovided = 0
            r_twoormore = 0
            r_white = 0
            r_unk = 0

        if (row['Category'] == 'Gender'):
            dg =  row['Subcategory'].upper()[0:3]
            cnt = int(row['Count'])
            if (dg == 'FEM'):
                g_female = g_female + cnt
            elif (dg == 'MAL'):
                g_male = g_male + cnt
            else:
                g_unk = g_unk + cnt
                print ("Unknown gender: " + row['Subcategory'] )
        elif (row['Category'] == 'Degree'):
            dg =  row['Subcategory'].upper()[0:3]
            cnt = int(row['Count'])
            if (dg == 'BAC'):
                d_bachelor = d_bachelor + cnt
            elif (dg == 'DOC'):
                d_doctor = d_doctor + cnt
            elif (dg == 'MAS'):
                d_master = d_master + cnt
            elif (dg == 'OTH'):
                d_other = d_other + cnt
            else:
                d_unk = d_unk + cnt
                print ("Unknown degree: " + row['Subcategory'] )
        elif (row['Category'] == 'RaceEthnicity'):
            dg =  row['Subcategory'].upper()[0:3]
            cnt = int(row['Count'])
            if (dg == 'AME'):
                r_natame = r_natame + cnt
            elif (dg == 'ASI'):
                r_asian = r_asian + cnt
            elif (dg == 'BLA'):
                r_black = r_black + cnt
            elif (dg == 'HIS'):
                r_hisplat = r_hisplat + cnt
            elif (dg == 'NAT'):
                r_hpi = r_hpi + cnt
            elif (dg == 'NOT'):
                r_notprovided = r_notprovided + cnt
            elif (dg == 'TWO'):
                r_twoormore = r_twoormore + cnt
            elif (dg == 'WHI'):
                r_white = r_white + cnt
            else:
                r_unk = r_unk + cnt
                print ("Unknown race/ethnicity: " + row['Subcategory'] )
        else:
            print(row['Category'])

        
    temp_list.append(
        {'DistrictName': s_district,
            'SchoolName': s_school,
            'TotalCount': s_totalcount,
            'D_Bachelor': d_bachelor,
            'D_Doctor': d_doctor,
            'D_Master': d_master,
            'D_Other': d_other,
            'D_UNK': d_unk,
            'G_Female' : g_female,
            'G_Male': g_male,
            'G_UNK': g_unk,
            'R_NatAme': r_natame,
            'R_Asian': r_asian,
            'R_Black': r_black,
            'R_HispLat': r_hisplat,
            'R_HPI': r_hpi,
            'R_NotProvided': r_notprovided,
            'R_TwoOrMore': r_twoormore,
            'R_White': r_white,
            'R_UNK': r_unk}
        )
   
    teacher_df = pd.DataFrame(temp_list) 
    teacher_df.to_csv("2021_teacher_t.csv") 


#teacherPlyData()

#coursesPlyData()       

schoolAddressData()

#SchoolEnrollmentData()                




            





#print (state[['SchoolYear','TotalStudents9-12']].head(20)
#state = state.drop

#numeric_fields = ['TotalStudents9-12','CSStudentsCIPorCourse','PctCSStudentsCIPorCourse','CSStudentsCourseOnly','PctCSStudentsCourseOnly']
#state[numeric_fields] = state[numeric_fields].apply(pd.to_numeric, errors='coerce')
#state = state.astype({'TotalStudents9-12':int,'CSStudentsCIPorCourse':int,'CSStudentsCourseOnly':int})

#state = pd.read_csv('../2021_State.csv')
#rint (state[[]].head())

#state.rename(columns = {'schoolYear':'SchoolYear',
#                        ' Total Students Grade 9-12':'TotalStudents9-12',
#                        ' Computer Science Enrollments using CIP or State Course Code':'CSStudentsCIPorCourse',
#                        'Percentage of Computer Science Enrollments using CIP or State Course Code': 'PctCSStudentsCIPorCourse',
#                        ' Computer Science Enrollments using State Course Code only':'CSStudentsCourseOnly',
#                        'Percentage of Computer Science Enrollments using State Course Code only': 'PctCSStudentsCourseOnly'}, inplace = True)

#state.rename(columns = {'schoolYear':'SchoolYear'},inplace=True)
#state.rename(columns = {' Total Students Grade 9-12':'TotalStudents9-12'},inplace=True)
#state.rename(columns = {' Computer Science Enrollments using CIP or State Course Code':'CSStudentsCIPorCourse'},inplace=True)
#state.rename(columns = { 'Percentage of Computer Science Enrollments using CIP or State Course Code': 'PctCSStudentsCIPorCourse'},inplace=True)
#state.rename(columns = {' Computer Science Enrollments using State Course Code only':'CSStudentsCourseOnly'},inplace=True)
#state.rename(columns = {'Percentage of Computer Science Enrollments using State Course Code only': 'PctCSStudentsCourseOnly'},inplace=True)
