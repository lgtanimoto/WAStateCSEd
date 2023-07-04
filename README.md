# WAStateCSEd
 WAState CS Ed Analytics


 WA State CSEd Metrics
# 2020-21

CS Enrollments in Washington

**Tableau location:** <https://public.tableau.com/app/profile/lawrence.tanimoto/viz/CSEnrollmentsinWashington2020-21/CSEnrollmentsinWashington2020-21>

**Tableau Source File**: WAStateSchools2021.twb

**Main Source Data File**: Computer Science Course Enrollment and Educator Data 2020-21 SY.xlsx taken from <https://www.k12.wa.us/sites/default/files/public/secondaryeducation/Operations/Computer%20Science%20Course%20Enrollment%20and%20Educator%20Data%202020-21%20SY.xlsx> taken from [Computer Science | OSPI (www.k12.wa.us)](https://www.k12.wa.us/student-success/resources-subject-area/computer-science) on 5/20/2023

For this dashboard, the file SchoolCSEEnrollmentOnly\_2021.csv was created by running the SchoolEnrollmentData() function in the Python file CSVCleanup2021.py.  This function took the “School” sheet from the main Excel file, kept only the “AllStudent” records, and eliminated unnecessary columns.

**Location Data for Schools and other entities**

Location data for schools (SchoolLocations\_2021.csv),  School districts (062723\_DistrictLocations\_2021.csv) , educational service districts (ESD) (ESDLocations\_2021.csv), state legislative districts (WALegislativeLocations\_2021.csv), and congressional districts (CongressLocations\_2021.csv).   For schools, school districts, and ESDs, addresses were found through queries on the OSPI website and Internet searches.  Once addresses were found for the entity, geocodio  ([https://www.geocod.io/]())  was used to get info on longitude, latitude, state legislative district, and US Congressional district.   Functions in the file CSVCleanup2021.py were also used to remove unnecessary data from the file. 

High Schools: <https://www.k12.wa.us/sites/default/files/public/dataadmin/dataportal/Washington_Education_School_Directory_07_17_2020.xlsx>  

District [Office of Superintendent of Public Instruction (ospi.k12.wa.us)](https://eds.ospi.k12.wa.us/DirectoryEDS.aspx).  In retrospect, this source should have been used for high schools and ESD as well. 

ESDs: <https://www.k12.wa.us/about-ospi/about-school-districts/educational-service-districts>

State Legislative and Congressional Districts: After getting state legislature and congressional districts for each school via Geocodio (<https://www.geocod.io/>), the address (with corresponding longitude and latitude) of the state legislative or congressional district was set to the address of the high school with the most students in the district 

### State-wide CS Ed participation 2020-21

**Tableau Location:** <https://public.tableau.com/app/profile/lawrence.tanimoto/viz/State-wideCSEdparticipation2020-21/State-wide>

**Tableau Source File:** 2021WAStateSummaruy.twb

**Main Source Data File**: Computer Science Course Enrollment and Educator Data 2020-21 SY.xlsx taken from <https://www.k12.wa.us/sites/default/files/public/secondaryeducation/Operations/Computer%20Science%20Course%20Enrollment%20and%20Educator%20Data%202020-21%20SY.xlsx> taken from [Computer Science | OSPI (www.k12.wa.us)](https://www.k12.wa.us/student-success/resources-subject-area/computer-science) on 5/20/2023

For this dashboard, the file 2021\_State.csv was created by taking the “State” sheet from the source Excel file, deleting the blank row, and renaming some columns.

## Washington State CS Education Teachers 2020-21

**Tableau Location:** <https://public.tableau.com/app/profile/lawrence.tanimoto/viz/WashingtonStateCSEducationTeachers2020-21/WashingtonStateCSEducationTeachers2020-21Alpha?publish=yes>

**Tableau Source File:** Washington State CS Education Teachers 2020-21.twb

**Source Data File:** 2021\_Comp Sci Educator Info.csv – taken by exporting the “Comp Sci Educator Info” sheet from the main Excel file in CSV format.  


