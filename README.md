# WAStateCSEd

# 2020-21 CSEd Metrics

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

For this dashboard, the file 2021_state_t.csv was from the source Excel file using CSVCleanup2021.py.   Basically, it deleted the blank row, and renaming some columns.

## Washington State CS Education Teachers 2020-21

**Tableau Location:** <https://public.tableau.com/app/profile/lawrence.tanimoto/viz/WashingtonStateCSEducationTeachers2020-21/WashingtonStateCSEducationTeachers2020-21Alpha?publish=yes>

**Tableau Source File:** Washington State CS Education Teachers 2020-21.twb

# 2020-21 CS within CTE Dashboard

**Subfolder: ** CTE21

**Tableau Locations:** 
<https://public.tableau.com/views/DemographicsbyCTEProgramArea-Washington2021/DemographicsbyProgramArea?:language=en-US&:display_count=n&:origin=viz_share_link>

<https://public.tableau.com/views/CTEProgramAreabyDistrict-Washington2021/CTEProgramsbyDistrict?:language=en-US&:display_count=n&:origin=viz_share_link>

<https://public.tableau.com/views/CTEEnrollmentsbyCIPCode-Washington2021/EnrollmentsbyCIPCode?:language=en-US&:display_count=n&:origin=viz_share_link>

<https://public.tableau.com/views/EnrollmentsbyCTEProgramArea-Washington2021/EnrollmentsbyProgramArea?:language=en-US&:display_count=n&:origin=viz_share_link>

**Tableau Source File:** cte121.twb  

**Source Data Files:** 
Enrollment_in_CTE_Courses_by_CIP_Code_clean.csv – Light reformatting from <https://data.wa.gov/Education/Enrollment-in-CTE-Courses-by-CIP-Code/xz2f-5ydn>

CIP_Code_Scraped with mapping2 - Scraped from <https://www.k12.wa.us/student-success/career-technical-education-cte/cte-resources-essentials/cip-codes> with a certain CIP Codes remapped to CS

# 2021-22 CSEd Metrics

**Subfolder:** 2022

**Tableau Locations:**
<https://public.tableau.com/views/CSEnrollmentsinWashington2021-22/CSEnrollmentsinWashington2021-22?:language=en-US&:display_count=n&:origin=viz_share_link>

<https://public.tableau.com/views/WashingtonCSEdparticipationDemographics2021-22/State-wide?:language=en-US&:display_count=n&:origin=viz_share_link>

<https://public.tableau.com/views/WashingtonStateCSEducationTeachers2021-22/WashingtonStateCSEducationTeachers2020-21Alpha?:language=en-US&:display_count=n&:origin=viz_share_link>

**Tableau Source Files: ** WAStateSchools2022.twb, 2022WAStateSummary.twb, Washington State CS Education Teachers 2021-22.twb

** Source Data Files: **
ComputerScienceEducationDataSummaryReport21-22.xlsx  (originally from <https://docs.google.com/document/d/1f3RpcEsX3XNdq-xE9YB0b5IjcEXbKjWEPybXGYDkyhM/edit?usp=sharing>)

2022_state_t.csv (generated from source xlsx using wastatemetrics22.py)

2022_Comp Sci Educator Info.csv (generated from source xlsx using wastatemetrics22.py)

SchoolCSEEnrollmentOnly_2022.csv (generated from source xlsx using wastatemetrics22.py)

DistrictLocations_2022.csv (same as 2021 version)

ESDLocations_2022.csv (same as 2021 version)

WALegislativeLocations_2022.csv (same as 2021 version)

CongressLocations_2022.csv (same as 2021 version)

SchoolLocations_2022.csv (started with 2021 version, added 26 schools with geocodio generated location)






