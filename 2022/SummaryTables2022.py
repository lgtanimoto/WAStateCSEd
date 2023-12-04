from numpy.core.numeric import NaN
import pandas as pd
import numpy as np

schoolCSEnrollment = pd.read_excel('../ComputerScienceEducationDataSummaryReport21-22.xlsx','School')

print (schoolCSEnrollment.dtypes)

schoolCSEnrollment.columns = ['schoolYear','DistrictCode','DistrictName','SchoolCode','SchoolName','Program','StudentGroup','TotalStudents','CSE-All','Pct-CSE-All','CSE-CourseCode','Pct-CSE-CourseCode']


temp_list=[]
s_districtCode = -1
s_schoolCode = -1

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

a_9 = 0 
ac_9 = 0 
a_10 = 0 
ac_10 = 0
a_11 = 0 
ac_11 = 0 
a_12 = 0
ac_12 = 0

for index, row in schoolCSEnrollment.iterrows():
    
    if (s_schoolCode != row['SchoolCode']):

        if (s_schoolCode != -1):
            print ("add row for school code: " + str(s_schoolCode))
            temp_list.append(
                {'DistrictCode': s_districtCode,
                    'SchoolCode': s_schoolCode,
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
                    'IC_NOLowIncome': ic_nolowincome,
                    'D_Disability': d_disability,
                    'DC_Disability': dc_disability,
                    'D_NoDisability': d_nodisability,
                    'DC_NoDisability': dc_nodisability,
                    'A_9': a_9,
                    'AC_9': ac_9,
                    'A_10': a_10,
                    'AC_10': ac_10,
                    'A_11': a_11,
                    'AC_11': ac_11,
                    'A_12': a_12,
                    'AC_12': ac_12
                    }
                )
            
        s_schoolCode = row['SchoolCode']
        s_districtCode = row['DistrictCode']
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
        a_9 = 0 
        ac_9 = 0 
        a_10 = 0 
        ac_10 = 0
        a_11 = 0 
        ac_11 = 0 
        a_12 = 0
        ac_12 = 0

    program = row['Program'].upper()[0:3]

    if (program == 'ALL'):   #AllStudents
        s_allStudents = row['TotalStudents']
        sc_allStudents = row['CSE-All']

    elif (program == 'ELL'):  #ELL
        group = str(row['StudentGroup']).upper()[0:3]

        if (group =='ENG'):
            l_ell = row['TotalStudents']
            lc_ell = row['CSE-All']
        elif (group == 'NON'):
            l_noell =  row['TotalStudents']
            lc_noell = row['CSE-All']
        else:
            print ("Invalid data" + program + ", " + group)

    elif (program == 'GEN'): #Gender
        group = str(row['StudentGroup']).upper()[0:3]

        if (group == 'FEM'):
            g_female = row['TotalStudents']
            gc_female = row['CSE-All']
        elif (group == 'MAL'):
            g_male = row['TotalStudents']
            gc_male = row['CSE-All']
        elif (group == 'GEN'):  #Gender X
            g_genderx = row['TotalStudents']
            gc_genderx = row['CSE-All']
        else:
            print ("Invalid data" + program + ", " + group)

    elif (program == 'FED'):   #Race/Ethincity
        group = str(row['StudentGroup']).upper()[0:3]

        if (group == 'AME'):  #American Indian
            r_native = row['TotalStudents']
            rc_native = row['CSE-All']
        elif (group== 'ASI'):
            r_asian = row['TotalStudents']
            rc_asian = row['CSE-All']
        elif (group == 'BLA'):
            r_black = row['TotalStudents']
            rc_black = row['CSE-All']
        elif (group == 'HIS'):
            r_hisp_lat = row['TotalStudents']
            rc_hisp_lat = row['CSE-All']
        elif (group == 'NAT'):     #Native Hawaiian/Pacific Islander
            r_hpi = row['TotalStudents']
            rc_hpi = row['CSE-All']
        elif (group == 'NAN'):
            r_na = row['TotalStudents']
            rc_na = row['CSE-All']
        elif (group == 'TWO'):
            r_twoormore = row['TotalStudents']
            rc_twoormore = row['CSE-All']
        elif (group== 'WHI'):
            r_white = row['TotalStudents']
            rc_white = row['CSE-All']
        else:
            print ("Invalid data" + program + ", " + group)

    elif (program == 'FRL'):  #Free and reduced lunch
        group = str(row['StudentGroup']).upper()[0:3]

        if (group =='LOW'):
            i_lowincome = row['TotalStudents']
            ic_lowincome = row['CSE-All']
        elif (group == 'NON'):
            i_nolowincome =  row['TotalStudents']
            ic_nolowincome = row['CSE-All']
        else:
            print ("Invalid data" + program + ", " + group)

    elif (program == 'SWD'):  #Students with Disabilities

        hasout = row['StudentGroup'].find("out")  # distinguish between students with or without disabilities

        if (hasout == -1):     # with disability
            d_disability = row['TotalStudents']
            dc_disability = row['CSE-All']
        else:
            d_nodisability =  row['TotalStudents']
            dc_nodisability = row['CSE-All']
 
    elif (program == 'GRA'):  #Students with Disabilities
 
        group = str(row['StudentGroup'])

        if (group =='9'):     
            a_9 = row['TotalStudents'] 
            ac_9 = row['CSE-All'] 
        elif (group == '10'):
            a_10 = row['TotalStudents'] 
            ac_10 = row['CSE-All']
        elif (group == '11'):
            a_11 = row['TotalStudents'] 
            ac_11 = row['CSE-All'] 
        elif (group == '12'):
            a_12 = row['TotalStudents']
            ac_12 = row['CSE-All']
        else:
            print ("Invalid data " + program + ", " + group)


    else:
        print ("Invalid data" + program + ", " + group)

        
print ("add row for school code: " + str(s_schoolCode))
temp_list.append(
    {'DistrictCode': s_districtCode,
        'SchoolCode': s_schoolCode,
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
        'IC_NOLowIncome': ic_nolowincome,
        'D_Disability': d_disability,
        'DC_Disability': dc_disability,
        'D_NoDisability': d_nodisability,
        'DC_NoDisability': dc_nodisability,
        'A_9': a_9,
        'AC_9': ac_9,
        'A_10': a_10,
        'AC_10': ac_10,
        'A_11': a_11,
        'AC_11': ac_11,
        'A_12': a_12,
        'AC_12': ac_12
        }
    )

   
school_df = pd.DataFrame(temp_list) 
school_df.to_csv("2022_school_pt2.csv") 
print ("Completed")

#FILEROOT = ""