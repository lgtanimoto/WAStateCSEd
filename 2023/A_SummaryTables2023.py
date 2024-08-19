from numpy.core.numeric import NaN
import pandas as pd
import numpy as np

schoolCSEnrollmentAllYears = pd.read_excel('./2022-23-k-12-computer-science-education-data-summary-report.xlsx','Students_School', header=1)
schoolLocations = pd.read_csv('./Washington_School_Directory_2024_geocodio.csv')
districtLocations = pd.read_csv('./Washington_District_Directory_2024_geocodio.csv')
schoolReportCardInfo = pd.read_csv('./Report_Card_Enrollment_2022-23_School_Year_20240817.csv')

print (schoolCSEnrollmentAllYears.dtypes)
print (schoolLocations.dtypes)
print (schoolReportCardInfo.dtypes)


#schoolCSEnrollment.columns = ['schoolYear','DistrictCode','DistrictName','SchoolCode','SchoolName','Program','StudentGroup','TotalStudents','CSE-All','Pct-CSE-All','CSE-CourseCode','Pct-CSE-CourseCode']
schoolCSEnrollmentAllYears.columns = ['SchoolYear','LEACode','LEAName','SchoolCode','SchoolName','Category','StudentGroup','TotalStudents','CSStudents','Pct-CSStudents']

schoolCSEnrollment = schoolCSEnrollmentAllYears[schoolCSEnrollmentAllYears['SchoolYear']=='2022-23']

schoolReportCardInfo['SchoolCode'] = schoolReportCardInfo['SchoolCode'].fillna(0)
schoolReportCardInfo['SchoolCode'] = schoolReportCardInfo['SchoolCode'].astype(int)

# function to receive grade population from schoolReportCardInfo
def getGradePopulation(mySchoolCode, myGrade): 
    t_frame = schoolReportCardInfo[(schoolReportCardInfo['SchoolCode']==mySchoolCode) & (schoolReportCardInfo['GradeLevel']==myGrade)]
    if len(t_frame) > 0:
        return t_frame.iloc[0]['All Students']
    else:
        return 0


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

is_hs = 0
is_ms = 0
alt_allstudents = 0
orig_allstudents = 0

# unknown columns
l_unknown = 0
g_unknown = 0
r_unknown = 0
i_unknown = 0
d_unknown = 0
a_unknown = 0


for index, row in schoolCSEnrollment.iterrows():
    
    if (s_schoolCode != row['SchoolCode']):

        if (s_schoolCode != -1):
            print ("add row for school code: " + str(s_schoolCode) + " Year: " + str(s_schoolYear))

            reportCard = schoolReportCardInfo[(schoolReportCardInfo['SchoolCode']==s_schoolCode) & (schoolReportCardInfo['GradeLevel']=='All Grades')].to_dict(orient='list')

            if len(reportCard['All Students']) == 0:
                print ("No report card info for ", s_schoolCode)
            else:
                alt_allstudents = reportCard['All Students'][0]
 
                if alt_allstudents == 0:
                    print ("Report card exists, but no demographic info for ", s_schoolCode)

                elif sc_allStudents == 0:                   # demographic data not in CS data but in report card data

                    print ("School: ", s_schoolCode, " using report card demographic data")
                                   
                    l_ell = reportCard['English Language Learners'][0]
                    l_noell = reportCard['Non-English Language Learners'][0]

                    g_female = reportCard['Female'][0]
                    g_male = reportCard['Male'][0]
                    g_genderx = reportCard['Gender X'][0]

                    r_native =  reportCard['American Indian/ Alaskan Native'][0]
                    r_asian =  reportCard['Asian'][0]
                    r_black =  reportCard['Black/ African American'][0]
                    r_hisp_lat =  reportCard['Hispanic/ Latino of any race(s)'][0]
                    r_hpi =  reportCard['Native Hawaiian/ Other Pacific Islander'][0]
                    r_na =  0
                    r_twoormore =  reportCard['Two or More Races'][0]
                    r_white =  reportCard['White'][0]

                    i_lowincome =  reportCard['Low-Income'][0]
                    i_nolowincome =  reportCard['Non-Low Income'][0]

                    d_disability =  reportCard['Students with Disabilities'][0]
                    d_nodisability =  reportCard['Students without Disabilities'][0]

                    a_6 = getGradePopulation(s_schoolCode,'6th Grade')
                    a_7 = getGradePopulation(s_schoolCode,'7th Grade')
                    a_8 = getGradePopulation(s_schoolCode,'8th Grade')
                    a_9 = getGradePopulation(s_schoolCode,'9th Grade')
                    a_10 = getGradePopulation(s_schoolCode,'10th Grade')
                    a_11 = getGradePopulation(s_schoolCode,'11th Grade')
                    a_12 = getGradePopulation(s_schoolCode,'12th Grade')

                    s_allStudents = alt_allstudents  # use report card data for total student popuation
                # end of report card gathering

            if (a_11 + a_12) > 0:
                is_hs = 1

            if (a_7 + a_8) > 0:
                is_ms = 1

            l_unknown = s_allStudents - (l_ell + l_noell) 
            g_unknown = s_allStudents - (g_female + g_male + g_genderx)
            r_unknown = s_allStudents - (r_asian + r_black + r_hisp_lat + r_white + r_native + r_hpi + r_na + r_twoormore)
            i_unknown = s_allStudents - (i_lowincome + i_nolowincome)
            d_unknown = s_allStudents - (d_disability + d_nodisability)
            a_unknown = s_allStudents - (a_6 + a_7 + a_8 + a_9 + a_10 + a_11 + a_12)

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
                    'is_HS': is_hs,
                    'is_MS': is_ms,
                    'alt_AllStudents': alt_allstudents,
                    'orig_AllStudents': orig_allstudents,
                    'L_Unknown': l_unknown,
                    'G_Unknown': g_unknown,
                    'R_Unknown': r_unknown,
                    'I_Unknown': i_unknown,
                    'D_Unknown': d_unknown,
                    'A_Unknown': a_unknown
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
        is_hs = 0
        is_ms = 0
        alt_allstudents = 0
        orig_allstudents = 0
        l_unknown = 0
        g_unknown = 0
        r_unknown = 0
        i_unknown = 0
        d_unknown = 0
        a_unknown = 0

    category = row['Category'].upper()[0:3]

    if (category == 'ALL'):   #AllStudents
        s_allStudents = row['TotalStudents']
        orig_allstudents = s_allStudents   # orignal value comes from cs report
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
        elif (group == 'RAC'):     #Race not provided  was NAN in past
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
            
print ("add row for school code: " + str(s_schoolCode) + " Year: " + str(s_schoolYear))

if sc_allStudents == 0:

    reportCard = schoolReportCardInfo[(schoolReportCardInfo['SchoolCode']==s_schoolCode) & (schoolReportCardInfo['GradeLevel']=='All Grades')].to_dict(orient='list')

    if len(reportCard['All Students']) == 0:
        print ("No report card info for ", s_schoolCode)
    else:
        alt_allstudents = reportCard['All Students'][0]
 
        if alt_allstudents == 0:
            print ("Report card exists, but no demographic info for ", s_schoolCode)

        elif sc_allStudents == 0:                   # demographic data not in CS data but in report card data

            print ("School: ", s_schoolCode, " using report card demographic data")
                
            l_ell = reportCard['English Language Learners'][0]
            l_noell = reportCard['Non-English Language Learners'][0]

            g_female = reportCard['Female'][0]
            g_male = reportCard['Male'][0]
            g_genderx = reportCard['Gender X'][0]

            r_native =  reportCard['American Indian/ Alaskan Native'][0]
            r_asian =  reportCard['Asian'][0]
            r_black =  reportCard['Black/ African American'][0]
            r_hisp_lat =  reportCard['Hispanic/ Latino of any race(s)'][0]
            r_hpi =  reportCard['Native Hawaiian/ Other Pacific Islander'][0]
            r_na =  0
            r_twoormore =  reportCard['Two or More Races'][0]
            r_white =  reportCard['White'][0]

            i_lowincome =  reportCard['Low-Income'][0]
            i_nolowincome =  reportCard['Non-Low Income'][0]

            d_disability =  reportCard['Students with Disabilities'][0]
            d_nodisability =  reportCard['Students without Disabilities'][0]

            a_6 = getGradePopulation(s_schoolCode,'6th Grade')
            a_7 = getGradePopulation(s_schoolCode,'7th Grade')
            a_8 = getGradePopulation(s_schoolCode,'8th Grade')
            a_9 = getGradePopulation(s_schoolCode,'9th Grade')
            a_10 = getGradePopulation(s_schoolCode,'10th Grade')
            a_11 = getGradePopulation(s_schoolCode,'11th Grade')
            a_12 = getGradePopulation(s_schoolCode,'12th Grade')

            s_allStudents = alt_allstudents  # use report card data for total student popuation

        # end using report card data

if a_11 + a_12 > 0:
    is_hs = 1

if a_7 + a_8 > 0:
    is_ms = 1

l_unknown = s_allStudents - (l_ell + l_noell) 
g_unknown = s_allStudents - (g_female + g_male + g_genderx)
r_unknown = s_allStudents - (r_asian + r_black + r_hisp_lat + r_white + r_native + r_hpi + r_na + r_twoormore)
i_unknown = s_allStudents - (i_lowincome + i_nolowincome)
d_unknown = s_allStudents - (d_disability + d_nodisability)
a_unknown = s_allStudents - (a_6 + a_7 + a_8 + a_9 + a_10 + a_11 + a_12)


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
        'is_HS': is_hs,
        'is_MS': is_ms,
        'alt_AllStudents': alt_allstudents,
        'orig_AllStudents': orig_allstudents,
        'L_Unknown': l_unknown,
        'G_Unknown': g_unknown,
        'R_Unknown': r_unknown,
        'I_Unknown': i_unknown,
        'D_Unknown': d_unknown,
        'A_Unknown': a_unknown

        }
    )

   
school_df = pd.DataFrame(temp_list) 
school_df.to_excel("new_2023_school_pt.xlsx", columns=
		['SchoolYear', 'DistrictCode', 'SchoolCode', 'SchoolName','Longitude', 'Latitude', 'County', 'AllStudents','C_AllStudents', 'G_Female', 'GC_Female', 'G_Male','GC_Male',
		'G_GenderX', 'GC_GenderX', 'R_Native', 'RC_Native','R_Asian','RC_Asian','R_Black','RC_Black','R_Hisp_Lat','RC_Hisp_Lat','R_HPI','RC_HPI','R_NA','RC_NA',
        'R_TwoOrMore','RC_TwoOrMore','R_White','RC_White','L_ELL','LC_ELL','L_NoELL','LC_NoELL','I_LowIncome','IC_LowIncome','I_NoLowIncome','IC_NoLowIncome',
        'D_Disability','DC_Disability', 'D_NoDisability', 'DC_NoDisability','A_6','AC_6','A_7','AC_7','A_8','AC_8','A_9','AC_9','A_10','AC_10','A_11','AC_11','A_12','AC_12',
        'is_HS','is_MS','alt_AllStudents','orig_AllStudents','L_Unknown','G_Unknown','R_Unknown','I_Unknown', 'D_Unknown','A_Unknown']
		) 

print ("Completed")

#FILEROOT = ""