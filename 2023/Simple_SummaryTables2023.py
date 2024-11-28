from numpy.core.numeric import NaN
import pandas as pd
import numpy as np

schoolCSEnrollment = pd.read_excel('./2022-23-k-12-computer-science-education-data-summary-report.xlsx','Students_School', header=1)
schoolGrades = pd.read_excel('./2022-23-k-12-computer-science-education-data-summary-report.xlsx','ProgramAvailability_School', header=1)
schoolLocations = pd.read_csv('./Washington_School_Directory_2024_geocodio.csv')
districtLocations = pd.read_csv('./Washington_District_Directory_2024_geocodio.csv')

print (schoolCSEnrollment.dtypes)
print (schoolLocations.dtypes)

#schoolCSEnrollment.columns = ['schoolYear','DistrictCode','DistrictName','SchoolCode','SchoolName','Program','StudentGroup','TotalStudents','CSE-All','Pct-CSE-All','CSE-CourseCode','Pct-CSE-CourseCode']
schoolCSEnrollment.columns = ['SchoolYear','LEACode','LEAName','SchoolCode','SchoolName','Category','StudentGroup','TotalStudents','CSStudents','Pct-CSStudents']
schoolGrades.columns = ['SchoolYear','LEACode','LEAName','SchoolCode','SchoolName','GradeSpan','CSOffered']

# determines whether a school is high school or middle school
def isSchoolType(stype, srange):
    schoolRange = srange.split("-")
    if len(schoolRange) == 1:              # only one grade max = min
        schoolRange.append(schoolRange[0])

    fixgrade = lambda x: 0 if schoolRange[x] == "K" else int(schoolRange[x])
    mingrade = fixgrade(0)
    maxgrade = fixgrade(1)

    if (stype=="HS"):
        if (maxgrade >= 11) and maxgrade > mingrade:
            return 1
        else:
            return 0
    elif (stype=="MS"):
        if (mingrade <= 6 and maxgrade >= 8):
           return 1
        elif (maxgrade > mingrade):
            if (mingrade == 6 or mingrade == 7) or (maxgrade == 8 or maxgrade == 7):
                return 1
            else:
                return 0
    else:
        return 0
# end def isSchoolType

temp_list=[]

s_schoolYear = 'temp'
s_districtCode = -1
s_schoolCode = -1
s_schoolName = "temp"
s_longitude = 0.0
s_latitude = 0.0
s_county = "temp"

s_allStudents = 0
sc_allStudents = 0

l_ell = 0
lc_ell = 0
l_noell = 0
lc_noell = 0

g_female = 0
gc_female = 0
g_male = 0
gc_male = 0
g_genderx = 0
gc_genderx = 0

r_native = 0
rc_native = 0
r_asian = 0
rc_asian = 0
r_black = 0
rc_black = 0
r_hisp_lat = 0
rc_hisp_lat = 0
r_hpi = 0
rc_hpi = 0
r_na = 0
rc_na = 0
r_twoormore = 0
rc_twoormore = 0
r_white = 0
rc_white = 0

i_lowincome = 0
ic_lowincome = 0
i_nolowincome = 0
ic_nolowincome = 0

d_disability = 0
dc_disability = 0
d_nodisability = 0
dc_nodisability = 0

a_6 = 0 
ac_6 = 0 
a_7 = 0 
ac_7 = 0
a_8 = 0 
ac_8 = 0 
a_9 = 0 
ac_9 = 0 
a_10 = 0 
ac_10 = 0
a_11 = 0 
ac_11 = 0 
a_12 = 0
ac_12 = 0

schoolGradeRange = "temp"
is_hs = 0
is_ms = 0


for index, row in schoolCSEnrollment.iterrows():
    
    if (s_schoolCode != row['SchoolCode']):

        if (s_schoolCode != -1):
            print ("add row for school code: " + str(s_schoolCode) + " Year: " + str(s_schoolYear))
            temp_list.append(
                {   'SchoolYear': s_schoolYear,
                    'DistrictCode': s_districtCode,
                    'SchoolCode': s_schoolCode,
					'SchoolName': s_schoolName,
					'Longitude': s_longitude,
					'Latitude': s_latitude,
					'County' : s_county,
                    'AllStudents': s_allStudents,
                    'C_AllStudents': sc_allStudents,
                    'G_Female' : g_female,
                    'GC_Female' : gc_female,
                    'G_Male': g_male,
                    'GC_Male': gc_male,
                    'G_GenderX': g_genderx,
                    'GC_GenderX': gc_genderx,
                    'R_Native': r_native,
                    'RC_Native': rc_native,
                    'R_Asian': r_asian,
                    'RC_Asian': rc_asian,
                    'R_Black': r_black,
                    'RC_Black': rc_black,
                    'R_Hisp_Lat': r_hisp_lat,
                    'RC_Hisp_Lat': rc_hisp_lat,
                    'R_HPI': r_hpi,
                    'RC_HPI': rc_hpi,
                    'R_NA': r_na,
                    'RC_NA': rc_na,
                    'R_TwoOrMore': r_twoormore,
                    'RC_TwoOrMore': rc_twoormore,
                    'R_White': r_white,
                    'RC_White': rc_white,
                    'L_ELL': l_ell,
                    'LC_ELL': lc_ell,
                    'L_NoELL': l_noell,
                    'LC_NoELL':  lc_noell,
                    'I_LowIncome': i_lowincome,
                    'IC_LowIncome': ic_lowincome,
                    'I_NoLowIncome': i_nolowincome,
                    'IC_NoLowIncome': ic_nolowincome,
                    'D_Disability': d_disability,
                    'DC_Disability': dc_disability,
                    'D_NoDisability': d_nodisability,
                    'DC_NoDisability': dc_nodisability,
                    'A_6': a_6,
                    'AC_6': ac_6,
                    'A_7': a_7,
                    'AC_7': ac_7,
                    'A_8': a_8,
                    'AC_8': ac_8,
                    'A_9': a_8,
                    'AC_9': ac_9,
                    'A_10': a_10,
                    'AC_10': ac_10,
                    'A_11': a_11,
                    'AC_11': ac_11,
                    'A_12': a_12,
                    'AC_12': ac_12,
                    'GradeRange' : schoolGradeRange,
                    'IS_HS': is_hs,
                    'IS_MS': is_ms
                 })
         
        s_schoolYear = row['SchoolYear']    
        s_schoolCode = row['SchoolCode']
        s_districtCode = row['LEACode']
        s_schoolName = str(row['SchoolName'])
        temp_schoolrow = schoolLocations.loc[schoolLocations['SchoolCode']==s_schoolCode]
        if len(temp_schoolrow) > 0:
            s_longitude = float(temp_schoolrow.iloc[0]['Longitude'])
            s_latitude = float(temp_schoolrow.iloc[0]['Latitude'])
            temp_county = str(temp_schoolrow.iloc[0]['County'])
            s_county = temp_county[0:len(temp_county)-7].strip()
        else:
            temp_districtrow = districtLocations.loc[districtLocations['DistrictCode']==s_districtCode]
            if len(temp_districtrow) > 0:
                s_longitude = float(temp_districtrow.iloc[0]['Longitude'])
                s_latitude = float(temp_districtrow.iloc[0]['Latitude'])
                temp_county = str(temp_districtrow.iloc[0]['County'])
                s_county = temp_county[0:len(temp_county)-7].strip()
            else:
                s_longitude = 0
                s_latitude = 0
                s_county = "Unknown"



        schoolGradeRange = "0-0"
        schoolGrades_row = schoolGrades.loc[(schoolGrades['SchoolCode']==s_schoolCode) & (schoolGrades['SchoolYear']==s_schoolYear)]
        if len(schoolGrades_row) > 0:
            schoolGradeRange =  (schoolGrades_row.iloc[0]['GradeSpan'])
        else:
            print ("No grade range record found for ", s_schoolCode, " ", s_schoolYear)

        is_hs = isSchoolType("HS",schoolGradeRange)
        is_ms = isSchoolType("MS",schoolGradeRange)

        s_allStudents = 0
        sc_allStudents = 0
        l_ell = 0
        lc_ell = 0
        l_noell = 0
        lc_noell = 0
        g_female = 0
        gc_female = 0
        g_male = 0
        gc_male = 0
        g_genderx = 0
        gc_genderx = 0
        r_native = 0
        rc_native = 0
        r_asian = 0
        rc_asian = 0
        r_black = 0
        rc_black = 0
        r_hisp_lat = 0
        rc_hisp_lat = 0
        r_hpi = 0
        rc_hpi = 0
        r_na = 0
        rc_na = 0
        r_twoormore = 0
        rc_twoormore = 0
        r_white = 0
        rc_white = 0
        i_lowincome = 0
        ic_lowincome = 0
        i_nolowincome = 0
        ic_nolowincome = 0
        d_disability = 0
        dc_disability = 0
        d_nodisability = 0
        dc_nodisability = 0
        a_6 = 0 
        ac_6 = 0 
        a_7 = 0 
        ac_7 = 0
        a_8 = 0 
        ac_8 = 0 
        a_9 = 0 
        ac_9 = 0 
        a_10 = 0 
        ac_10 = 0
        a_11 = 0 
        ac_11 = 0 
        a_12 = 0
        ac_12 = 0
               
    category = row['Category'].upper()[0:3]

    if (category == 'ALL'):   #AllStudents
        s_allStudents = row['TotalStudents']
        sc_allStudents = row['CSStudents']

    elif (category == 'ELL'):  #ELL
        group = str(row['StudentGroup']).upper()[0:3]

        if (group =='ENG'):
            l_ell = row['TotalStudents']
            lc_ell = row['CSStudents']
        elif (group == 'NON'):
            l_noell =  row['TotalStudents']
            lc_noell = row['CSStudents']
        else:
            print ("Invalid data" + category + ", " + group)

    elif (category == 'GEN'): #Gender
        group = str(row['StudentGroup']).upper()[0:3]

        if (group == 'FEM'):
            g_female = row['TotalStudents']
            gc_female = row['CSStudents']
        elif (group == 'MAL'):
            g_male = row['TotalStudents']
            gc_male = row['CSStudents']
        elif (group == 'GEN'):  #Gender X
            g_genderx = row['TotalStudents']
            gc_genderx = row['CSStudents']
        else:
            print ("Invalid data" + category + ", " + group)

    elif (category == 'FED'):   #Race/Ethincity
        group = str(row['StudentGroup']).upper()[0:3]

        if (group == 'AME'):  #American Indian
            r_native = row['TotalStudents']
            rc_native = row['CSStudents']
        elif (group== 'ASI'):
            r_asian = row['TotalStudents']
            rc_asian = row['CSStudents']
        elif (group == 'BLA'):
            r_black = row['TotalStudents']
            rc_black = row['CSStudents']
        elif (group == 'HIS'):
            r_hisp_lat = row['TotalStudents']
            rc_hisp_lat = row['CSStudents']
        elif (group == 'NAT'):     #Native Hawaiian/Pacific Islander
            r_hpi = row['TotalStudents']
            rc_hpi = row['CSStudents']
        elif (group == 'RAC'):
            r_na = row['TotalStudents']
            rc_na = row['CSStudents']
        elif (group == 'TWO'):
            r_twoormore = row['TotalStudents']
            rc_twoormore = row['CSStudents']
        elif (group== 'WHI'):
            r_white = row['TotalStudents']
            rc_white = row['CSStudents']
        else:
            print ("Invalid data" + category + ", " + group)

    elif (category == 'FRE'):  #Free and reduced lunch
        group = str(row['StudentGroup']).upper()[0:3]

        if (group =='LOW'):
            i_lowincome = row['TotalStudents']
            ic_lowincome = row['CSStudents']
        elif (group == 'NON'):
            i_nolowincome =  row['TotalStudents']
            ic_nolowincome = row['CSStudents']
        else:
            print ("Invalid data" + category + ", " + group)

    elif (category == 'SWD'):  #Students with Disabilities

        hasout = row['StudentGroup'].find("out")  # distinguish between students with or without disabilities

        if (hasout == -1):     # with disability
            d_disability = row['TotalStudents']
            dc_disability = row['CSStudents']
        else:
            d_nodisability =  row['TotalStudents']
            dc_nodisability = row['CSStudents']
 
    elif (category == 'GRA'):  #Students with Disabilities
 
        group = str(row['StudentGroup']).upper()[0:2]

        if (group =='6T'):     
            a_6 = row['TotalStudents'] 
            ac_6 = row['CSStudents'] 
        elif (group =='7T'):     
            a_7 = row['TotalStudents'] 
            ac_7 = row['CSStudents'] 
        elif (group =='8T'):     
            a_8 = row['TotalStudents'] 
            ac_8 = row['CSStudents'] 
        elif (group =='9T'):     
            a_9 = row['TotalStudents'] 
            ac_9 = row['CSStudents'] 
        elif (group == '10'):
            a_10 = row['TotalStudents'] 
            ac_10 = row['CSStudents']
        elif (group == '11'):
            a_11 = row['TotalStudents'] 
            ac_11 = row['CSStudents'] 
        elif (group == '12'):
            a_12 = row['TotalStudents']
            ac_12 = row['CSStudents']
        else:
            print ("Invalid data " + category + ", " + group)

    else:
        print ("Invalid data" + category )
    # end of row processing
            
print ("add row for school code: " + str(s_schoolCode) + " Year: " + str(s_schoolYear))
temp_list.append(
    {'SchoolYear': s_schoolYear,
        'DistrictCode': s_districtCode,
        'SchoolCode': s_schoolCode,
		'SchoolName': s_schoolName,
		'Longitude' : s_longitude,
		'Latitude' : s_latitude,
		'County' : s_county,
        'AllStudents': s_allStudents,
        'C_AllStudents': sc_allStudents,
        'G_Female' : g_female,
        'GC_Female' : gc_female,
        'G_Male': g_male,
        'GC_Male': gc_male,
        'G_GenderX': g_genderx,
        'GC_GenderX': gc_genderx,
        'R_Native': r_native,
        'RC_Native': rc_native,
        'R_Asian': r_asian,
        'RC_Asian': rc_asian,
        'R_Black': r_black,
        'RC_Black': rc_black,
        'R_Hisp_Lat': r_hisp_lat,
        'RC_Hisp_Lat': rc_hisp_lat,
        'R_HPI': r_hpi,
        'RC_HPI': rc_hpi,
        'R_NA': r_na,
        'RC_NA': rc_na,
        'R_TwoOrMore': r_twoormore,
        'RC_TwoOrMore': rc_twoormore,
        'R_White': r_white,
        'RC_White': rc_white,
        'L_ELL': l_ell,
        'LC_ELL': lc_ell,
        'L_NoELL': l_noell,
        'LC_NoELL':  lc_noell,
        'I_LowIncome': i_lowincome,
        'IC_LowIncome': ic_lowincome,
        'I_NoLowIncome': i_nolowincome,
        'IC_NoLowIncome': ic_nolowincome,
        'D_Disability': d_disability,
        'DC_Disability': dc_disability,
        'D_NoDisability': d_nodisability,
        'DC_NoDisability': dc_nodisability,
        'A_6': a_6,
        'AC_6': ac_6,
        'A_7': a_7,
        'AC_7': ac_7,
        'A_8': a_8,
        'AC_8': ac_8,
        'A_9': a_9,
        'AC_9': ac_9,
        'A_10': a_10,
        'AC_10': ac_10,
        'A_11': a_11,
        'AC_11': ac_11,
        'A_12': a_12,
        'AC_12': ac_12,
        'GradeRange' : schoolGradeRange,
        'IS_HS': is_hs,
        'IS_MS': is_ms
        }
    )

school_df = pd.DataFrame(temp_list) 
school_df.to_excel("simple_2018_2023_school_pt.xlsx", columns=
		['SchoolYear', 'DistrictCode', 'SchoolCode', 'SchoolName','Longitude', 'Latitude', 'County', 'AllStudents','C_AllStudents','GradeRange','IS_HS','IS_MS']
		) 

print ("Completed")

#FILEROOT = ""