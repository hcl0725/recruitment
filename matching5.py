import streamlit as st
import math

# ===== Data =====
# MAJORS
Advertising = ['Abby Sanders', 'Catherine Favoriti', 'Jillian Taylor', 'Kaylie Ngo', 'Marley Page', 'Sienna Shutts','Allie Harter','Sarah Thompson']
AerospaceEngineering = ['Madeleine Mazingo']
Anthropology = ['Zoe Veliz']
AppliedMovementScience = ['Karlie Haigood','Julia Lindstrom']
Architecture = ['Chloe Lim', 'Riley Avery']
BFAActing = ['Katelyn Quintanilla']
BehavioralAndSocialDataScience = ['Delaney Vanderpool']
BilingualEducation = ['Emily Robles']
Biochemistry = ['Mia Vasquez']
Biology = ['Audrey Cooper', 'Brianna Salaices', 'Emmerich Benavides', 'Izzy Davies', 'Rishona Mopur','Megan Garza','Lindsay McCullough', 'Sydney Fern']
MicrobiologyAndInfectiousDiseases = ['Megan Garza']
BiomedicalEngineering = ['Gabrielle Beck']
Business = ['Ava Dahlander', 'Haylee Martin', 'Catherine Dooley', 'Madison Taylor', 'Larkin Seidel', 'Meredith Moreland', 'Meredith Moreland', 'Brianna']
BusinessHonors = ['Brianna']
Finance = ['Brianna']
CivilEngineering = ['Anna Woodson', 'Mae Trahan', 'Maggie Shaw','Emily Bull']
CommunicationAndLeadership = ['Emma Schneidau', 'Delaney O’Brien']
ComputerScience = ['Krissily Estacio']
CorporateCommunications = ['Valentina Markov','Allie Harter']
ESLGeneralistEarlyChildhood = ['Erika Sandberg']
EarlyChildhoodEducation = ['Anika Novak', 'Meghna Sunkureddi', 'Ella Pitts', 'Erika Sandberg']
Economics = ['Elyse Miller', 'Shelby Williamson', 'Sofie Arroyo']
English = ['Isabella Bartz']
EnvironmentalEngineering = ['Abby OGuynn', 'Katie Windell']
FrenchStudies = ['Sarah Solomon']
GeosystemsEngineering = ['Nids Pappu']
Government = ['Catalina Cruz', 'Ellie Berman', 'Jovanni Carrillo', 'Lola Daffin', 'Piper Buck', 'Charlie Stone', 'Heidi Chapin']
HealthPromotionAndBehavioralScience = ['Rachel Dolan, Claire Savage']
HealthAndSociety = ['Bella Champion', 'Hazel Wells', 'Jasmine Valdez', 'Maya Sajan']
HumanBiology = ['Lindsay McCullough', 'Sydney Fern']
HumanDevelopmentAndFamilySciences = ['Mazzy Bledsoe']
HumanDimensionsOfOrganization = ['Zoe Alvarado', 'Alice Hudson']
InternationalRelationsAndGlobalStudies = ['Maya Abraham', 'Riley Wanasek', 'Abrielle Gallini', 'Josie Mandrea', 'Hana Sawaf']
Journalism = ['Bella Anderson', 'Carly Schmidt', 'Celeste Tomberlin', 'Ferzine Sanjana', 'Katie Walsh', 'Kirthi Gummadi', 'Sarah Sims']
KinesiologyExerciseScience = ['Kamryn Jean']
Mathematics = ['Amelia Klyap', 'Jenn Rosado']
MechanicalEngineering = ['Alexandra Nicholls', 'Ollie Mae Harrison', 'Morgan Baumel']
MusicAndMedia = ['Ava Hurst']
Neuroscience = ['Abby Kant', 'Caitlin Van Sant', 'Regan Hill', 'Jannae Ailawadhi']
Nursing = ['Bailey Alsup', 'Gabrielle Green', 'Maria Sepulveda Salazar']
Physics = ['Nids Pappu']
PoliticalCommunications = ['Heidi Chapin','Hannah Greenhill', 'Meadow Votis']
Psychology = ['Alyssa Bouloy','Delaney Vanderpool', 'Ella Leininger', 'Taylor Jennings', 'Riley Wanasek', 'Kate Neiman', 'Arabella Savener']
PublicRelations = ['Liz Keegan', 'Georgia Key', 'Brooke Walker', 'Sophie Robins']
RTF = ['Diyaa Dossani', 'Sophie Shapiro']
Sociology = ['Abby Alsup','Bella Wernli']
SpecialEducation = ['Chasiti Tyeryar']
SpeechLanguageAndHearingSciences = ['Avery McClure']
SportsManagement = ['Hailey Brooks']
TheatreEducation = ['Jessica Paine']
Undeclared = ['Angie Andersen']
WritingAndRhetoric = ['Ellen Meltzer','Aliyana Martinez']
Mathematics = ['Suzie Hudgens']
Korean = ['Regan Hill']
SocialAndBehavioralSciences = ['Regan Hill']
AnalyticsAndBusinessOfSports = ['Hailey Brooks', 'Valentina Markov']
YouthAndCommunityStudies = ['Haley Hooper']
JewishStudies = ['Josie Mandrea']
PoliticalScience = ['Aliyana Martinez']
TextilesAndApparel = ['Bridget Flatow']

# MINORS
BusinessMinor = ['Audrey Cooper', 'Gabrielle Beck', 'Jillian Taylor', 'Alexandra Nicholls', 'Allie Harter', 'Erika Sandberg', 'Morgan Baumel', 'Amelia Klyap', 'Katelyn Quintanilla', 'Josie Mandrea', 'Isabella Bartz', 'Alice Hudson', 'Sydney Fern']
BusinessAndPublicPolicyMinor = ['Katie Walsh', 'Meadow Votis', 'Heidi Chapin']
ReligiousStudiesMinor = ['Sydney Fern']
StatsandDataScienceMinor = ['Amelia Klyap', 'Brianna Salaices', 'Emmerich Benavides']
CreativeWritingMinor = ['Isabella Bartz']
KoreanMinor = ['Isabella Bartz']
ChineseMinor = ['Isabella Bartz']
HealthProfessionsMinor = ['Rachel Dolan']
CommunicatingSocialIssuesMinor = ['Georgia Key', 'Aliyana Martinez']
CommunicationStudiesMinor = ['Jenn Rosado']
ComputerScienceMinor = ['Delaney Vanderpool']
CriminalLawJusticeandInequalityBridgingDisciplinesProgramMinor = ['Abby Alsup']
DesignStrategiesMinor = ['Ollie Mae Harrison']
EducationalPsychologyMinor = ['Ella Pitts', 'Chasiti Tyeryar', 'Aliyana Martinez']
EntrepreneurshipMinor = ['Diyaa Dossani', 'Haley Hooper']
FinanceMinor = ['Shelby Williamson']
FrenchMinor = ['Piper Buck']
GlobalCommunicationsMinor = ['Ellen Meltzer']
EthicsAndLeadershipInLawGovernmentandPoliticsMinor = ['Ellen Meltzer']
GlobalManagementMinor = ['Krissily Estacio']
GovernmentMinor = ['Kirthi Gummadi', 'Bella Wernli']
HealthReformandInnovationMinor = ['Megan Garza']
HealthCommunicationsMinor = ['Caitlin Van Sant', 'Alice Hudson']
HealthcareReformAndInnovationMinor = ['Gabrielle Green']
InteriorDesignMinor = ['Sarah Solomon']
ItalianMinor = ['Abrielle Gallini']
JeffersonScholarCTIMinor = ['Katie Windell', 'Arabella Savener']
KinesiologyMinor = ['Genesis Martinez', 'Emerson Oliver', 'Brianna']
LawJusticeAndSocietyMinor = ['Hannah Greenhill']
MediaAndEntertainmentIndustriesMinor = ['Bella Anderson', 'Ferzine Sanjana']
PhysiciansAssistantMinor = ['Hazel Wells']
PatientsPractitionersAndCareMinor = ['Jasmine Valdez']
PreHealthMinor = ['Abby Kant', 'Izzy Davies', 'Maya Sajan', 'Mazzy Bledsoe', 'Kamryn Jean', 'Mia Vasquez']
ProfessionalSalesAndBusinessDevelopmentMinor = ['Marley Page']
SocialAndBehavioralSciencesMinor = ['Charlie Stone']
SportsProductionandBroadcastMinor = ['Carly Schmidt']
SpanishforMedicalProfessionsMinor = ['Brianna Salaices']
BusinessSpanishMinor = ['Zoe Alvarado']
FitnessandRehabSpecializationMinor = ['Julia Lindstrom']
PremedMinor = ['Alyssa Bouloy']
PreHealthDentalMinor = ['Abby Sanders']
ProfessionalSalesMinor = ['Sarah Thompson']
RiskManagementStatisticsMinor = ['Suzie Hudgens']
SpanishMinor = ['Josie Mandrea']

# COLLEGE/TRACK
CockrellSchoolofEngineering = ['Abby OGuynn', 'Alexandra Nicholls', 'Anna Woodson', 'Emily Bull', 'Gabrielle Beck', 'Katie Windell', 'Madeleine Mazingo', 'Mae Trahan', 'Maggie Shaw', 'Morgan Baumel', 'Ollie Mae Harrison', 'Nids Pappu']
CollegeofEducation = ['Anika Novak', 'Chasiti Tyeryar', 'Claire Savage', 'Ella Pitts', 'Emily Robles', 'Erika Sandberg', 'Erika Sandberg', 'Hailey Brooks', 'Julia Lindstrom', 'Kamryn Jean', 'Karlie Haigood', 'Rachel Dolan', 'Meghna Sunkureddi', 'Haley Hooper']
CollegeofFineArts = ['Ava Hurst', 'Jessica Paine', 'Katelyn Quintanilla']
CollegeofLiberalArts = ['Abrielle Gallini', 'Alice Hudson', 'Alyssa Bouloy', 'Angie Andersen', 'Arabella Savener', 'Heidi Chapin', 'Kirthi Gummadi', 'Catalina Cruz', 'Delaney Vanderpool', 'Ella Leininger', 'Ellen Meltzer', 'Ellie Berman', 'Elyse Miller', 'Hazel Wells', 'Isabella Bartz', 'Jasmine Valdez', 'Jovanni Carrillo', 'Kate Neiman', 'Maya Abraham', 'Piper Buck', 'Riley Wanasek', 'Shelby Williamson', 'Sofie Arroyo', 'Taylor Jennings', 'Sarah Solomon', 'Zoe Alvarado', 'Josie Mandrea', 'Hana Sawaf', 'Aliyana Martinez']
CollegeofNaturalSciences = ['Amelia Klyap', 'Brianna Salaices', 'Caitlin Van Sant', 'Emerson Oliver', 'Genesis Martinez', 'Izzy Davies', 'Jannae Ailawadhi', 'Jenn Rosado', 'Krissily Estacio', 'Lindsay McCullough', 'Mazzy Bledsoe', 'Megan Garza', 'Mia Vasquez', 'Suzie Hudgens', 'Sydney Fern', 'Rishona Mopur', 'Bridget Flatow', 'Regan Hill']
McCombsSchoolofBusiness = ['Ava Dahlander', 'Catherine Dooley', 'Haylee Martin', 'Larkin Seidel', 'Diyaa Dossani', 'Meredith Moreland']
MoodyCollegeofCommunication = ['Allie Harter', 'Avery McClure', 'Bella Anderson', 'Brooke Walker', 'Carly Schmidt', 'Catherine Favoriti', 'Celeste Tomberlin', 'Heidi Chapin', 'Kirthi Gummadi', 'Delaney O’Brien', 'Emma Schneidau', 'Ferzine Sanjana', 'Jillian Taylor', 'Diyaa Dossani', 'Katie Walsh', 'Kaylie Ngo', 'Liz Keegan', 'Marley Page', 'Meadow Votis', 'Sarah Sims', 'Sienna Shutts', 'Sophie Robins', 'Valentina Markov', 'Sarah Thompson', 'Aliyana Martinez', 'Sophie Shapiro']
SchoolofArchitecture = ['Chloe Lim', 'Riley Avery']
SchoolofNursing = ['Bailey Alsup', 'Gabrielle Green', 'Maria Sepulveda Salazar']
JacksonSchoolofGeosciences = ['Nids Pappu']
PreMed = ['Abby Kant', 'Audrey Cooper', 'Emmerich Benavides', 'Maya Sajan', 'Abby Sanders']
PreLaw = ['Abby Alsup', 'Bella Wernli', 'Charlie Stone', 'Lola Daffin', 'Zoe Veliz', 'Brianna', 'Madison Taylor', 'Hannah Greenhill', 'Georgia Key', 'Josie Mandrea']
PrePharmacy = ['Bella Champion']

# HOMETOWNS
ArlingtonTX = ['Bella Wernli']
ArlingtonVA = ['Abby Kant', 'Catherine Dooley']
AustinTX = ['Abby Alsup', 'Arabella Savener', 'Bailey Alsup', 'Bella Anderson', 'Jannae Ailawadhi', 'Kaitlin Black', 'Marley Page', 'Charlie Stone', 'Regan Hill']
BeeCaveTX = ['Jessica Paine']
BeltonTX = ['Riley Avery']
BoerneTX = ['Sofie Arroyo']
BurlesonTX = ['Hannah Greenhill']
CleburneTX = ['Angie Andersen']
CollegeStationTX = ['Taylor Jennings', 'Celeste Tomberlin']
ColleyvilleTX = ['Anika Novak']
CorpusChristiTX = ['Jovanni Carrillo', 'Karlie Haigood']
DallasTX = ['Abby Sanders', 'Ava Dahlander', 'Carly Schmidt', 'Diyaa Dossani', 'Hazel Wells', 'Riley Wanasek', 'Claire Savage', 'Izzy Davies', 'Gabrielle Green', 'Delaney O’Brien', 'Zoe Veliz', 'Hana Sawaf']
DanvilleCA = ['Nids Pappu']
DaytonOH = ['Valentina Markov']
EaglePassTX = ['Ella Pitts']
ElPasoTX = ['Catalina Cruz']
FriendswoodTX = ['Meghna Sunkureddi', 'Sienna Shutts']
FriscoTX = ['Haylee Martin', 'Piper Buck', 'Sydney Fern', 'Kirthi Gummadi']
GardenCityNY = ['Jenn Rosado']
GrapevineTX = ['Brianna Salaices']
HoustonTX = ['Emma Schneidau', 'Isabella Bartz', 'Jillian Taylor', 'Sarah Sims', 'Sarah Solomon', 'Meredith Moreland', 'Sophie Robins', 'Heidi Chapin', 'Mia Vasquez', 'Suzie Hudgens', 'Ollie Mae Harrison', 'Catherine Favoriti', 'Avery McClure', 'Mae Trahan', 'Zoe Alvarado', 'Abby Oguynn', 'Aliyana Martinez', 'Sophie Shapiro', 'Shelby Williamson, Maya Abraham']
HumbleTX = ['Megan Garza']
IrvingTX = ['Chloe Lim']
JupiterFL = ['Anna Woodson']
KatyTX = ['Kaylie Ngo', 'Alyssa Bouloy']
LaredoTX = ['Jasmine Valdez', 'Maria Sepulveda Salazar']
LeanderTx = ['Emmerich Benavides']
LibertyHillTX = ['Emerson Oliver']
LongviewTX = ['Larkin Seidel']
LosAngelesCA = ['Hailey Brooks']
LubbockTX = ['Bella Champion', 'Katelyn Quintanilla']
MansfieldTX = ['Georgia Key']
McAllenTX = ['Genesis Martinez']
MckinneyTX = ['Maya Sajan']
MissouriCityTX = ['Maya Abraham']
NewBraunfelsTX = ['Ella Leininger', 'Lola Daffin', 'Chasiti Tyeryar']
NewYorkNY = ['Ellie Berman', 'Amelia Klyap']
PearlandTX = ['Audrey Cooper']
PleasantonCA = ['Emily Bull', 'Julia Lindstrom']
RichardsonTX = ['Delaney Vanderpool']
RockwallTX = ['Katie Windell', 'Brooke Walker']
RoundRockTX = ['Alice Hudson', 'Abrielle Gallini']
SacramentoCA = ['Sarah Thompson']
SanAntonioTX = ['Brianna', 'Emily Robles', 'Ferzine Sanjana', 'Ellen Meltzer', 'Elyse Miller', 'Gabrielle Beck', 'Kate Neiman', 'Rachel Dolan', 'Krissily Estacio']
HonoluluHawaii = ['Krissily Estacio']
SeabrookTX = ['Shelby Williamson']
SeattleWA = ['Liz Keegan']
SnoqualmieWA = ['Caitlin Van Sant']
SomersNY = ['Lindsay McCullough']
SpringTX = ['Allie Harter', 'Madeleine Mazingo', 'Morgan Baumel']
SugarLandTX = ['Erika Sandberg']
TexarkanaTX = ['Kamryn Jean']
TheWoodlandsTX = ['Alexandra Nicholls']
WestfieldNJ = ['Katie Walsh']
PleasantonCA = ['Emily Bull', 'Julia Lindstrom']
PensacolaFL = ['Julia Lindstrom']
FortWorthTX = ['Haley Hooper', 'Hannah Greenhill']
NorthbrookIL = ['Josie Mandrea']
LufkinTX = ['Rishona Mopur']
NewCanaanCT = ['Bridget Flatow']

# SCHOOLS
AlvaradoHighSchool = ['Mazzy Bledsoe']
AlvinHighSchool = ['Madison Taylor']
AmadorValleyHighSchool = ['Emily Bull', 'Julia Lindstrom']
ArlingtonHighSchool = ['Bella Wernli']
AtascocitaHighSchool = ['Jillian Taylor']
BeltonHighSchool = ['Riley Avery']
BishopDunneCatholicSchool = ['Gabrielle Green']
BoerneHighSchool = ['Sofie Arroyo']
BookerTWashingtonHSPVA = ['Diyaa Dossani']
BowieHighSchool = ['Bailey Alsup']
BrooklynTechnicalHighSchool = ['Amelia Klyap']
CalabasasHighSchool = ['Hailey Brooks']
CalallenHighSchool = ['Karlie Haigood']
CedarParkHighSchool = ['Regan Hill']
CentennialHighSchool = ['Hannah Greenhill']
ClearCreekHighschool = ['Sophie Robins']
ClearFallsHighSchool = ['Shelby Williamson']
CleburneHighSchool = ['Angie Andersen']
CollegeStationHighSchool = ['Taylor Jennings', 'Celeste Tomberlin']
ColleyvilleHeritageHighSchool = ['Anika Novak', 'Brianna Salaices']
DuchesneAcademyoftheSacredHeart = ['Sarah Sims']
EaglePassHighSchool = ['Ella Pitts']
EastViewHighSchool = ['Abrielle Gallini']
EastsideCatholicHighSchool = ['Liz Keegan']
ElkinsHighSchool = ['Meadow Votis']
HeightsHighSchool = ['Isabella Bartz']
FortBendChristianAcademy = ['Isabella Bartz']
FranklinHighSchool = ['Catalina Cruz']
FrenshipHighschool = ['Katelyn Quintanilla']
FriendswoodHighSchool = ['Sienna Shutts', 'Meghna Sunkureddi']
FriscoMemorialHighSchool = ['Haylee Martin']
FtBendTravisHighSchool = ['Erika Sandberg', 'Erika Sandberg']
FulshearHighSchool = ['Ollie Mae Harrison']
GardenCityHighSchool = ['Jenn Rosado']
GeorgetownDaySchool = ['Catherine Dooley']
RegentsHighSchool = ['Jannae Ailawadhi']
GlennHighSchool = ['Emmerich Benavides']
LiberalArtsandScienceAcademy = ['Jannae Ailawadhi']
GraniteBahHighSchool = ['Sarah Thompson']
GuyerHighSchool = ['Izzy Davies']
HeightsHighSchool = ['Abby OGuynn']
HillcrestHighSchool = ['Ava Dahlander']
HoustonAcademyforInternationalStudies = ['Heidi Chapin']
IncarnateWordHighSchoolsanantonio = ['Rachel Dolan']
IncarnateWordAcademyhtx = ['Avery McClure']
IndependenceHighSchool = ['Sydney Fern']
JJPearceHighSchool = ['Zoe Veliz', 'Delaney Vanderpool']
JamesBowieHighSchool = ['Abby Alsup']
JamesETaylorHighSchool = ['Kaylie Ngo']
JudsonHighSchool = ['Emily Robles']
KleinHighSchool = ['Madeleine Mazingo', 'Allie Harter']
LakeTravisHighSchool = ['Jessica Paine', 'Charlie Stone']
LamarHighSchool = ['Catherine Favoriti']
LibertyCreekHighSchool = ['Ava Hurst']
LibertyHighSchool = ['Kirthi Gummadi']
LibertyHillHighSchool = ['Emerson Oliver']
LouisDBrandeisHighSchool = ['Krissily Estacio']
LutheranSouthAcademy = ['Mia Vasquez']
MansfieldHighSchool = ['Georgia Key']
MaryCarrollHighSchool = ['Jovanni Carrillo']
McNeilHighSchool = ['Alice Hudson']
MckinneyHighSchool = ['Maya Sajan']
MemorialHighSchool = ['Piper Buck']
MonteVistaHighSchool = ['Nids Pappu']
MontereyHighSchool = ['Bella Champion']
MountSiHighSchool = ['Caitlin Van Sant']
NYCLabSchool = ['Ellie Berman']
NYOSCharterSchool = ['Arabella Savener']
NewBraunfelsHighSchool = ['Lola Daffin', 'Ella Leininger']
NorthernHighlands = ['Maggie Shaw']
OakwoodHighSchool = ['Valentina Markov']
PearlandHighSchool = ['Audrey Cooper']
PineTreeHighSchool = ['Larkin Seidel']
ProsperHighSchool = ['Riley Wanasek']
RidgePointHighSchool = ['Maya Abraham']
RockHillHighSchool = ['Carly Schmidt']
RockwallHighSchool = ['Katie Windell']
RockwallHeathHighSchool = ['Brooke Walker']
SPWaltripHighSchool = ['Meredith Moreland']
SaintMarysHall = ['Ellen Meltzer', 'Ferzine Sanjana']
SmithsonValleyHighSchool = ['Chasiti Tyeryar']
SomersHighSchool = ['Lindsay McCullough']
StAgnesAcademy = ['Emma Schneidau']
StratfordHighSchool = ['Mae Trahan', 'Sarah Solomon']
SummerCreekHighSchool = ['Megan Garza']
TMIEpiscopal = ['Gabrielle Beck', 'Kate Neiman']
TexasHighSchool = ['Kamryn Jean']
TheWoodlandsCollegePark = ['Alexandra Nicholls']
TomCClarkHighSchool = ['Elyse Miller']
TomballHighSchool = ['Suzie Hudgens']
TompkinsHighSchool = ['Alyssa Bouloy']
UnitedHighSchool = ['Jasmine Valdez', 'Maria Sepulveda Salazar']
UpliftNorthHillsPreparatory = ['Chloe Lim']
UrsulineAcademyofDallas = ['Abby Sanders', 'Claire Savage']
ValleyViewHighSchool = ['Genesis Martinez']
VandegriftHighSchool = ['Marley Page', 'Kaitlin Black']
WTWhiteHighSchool = ['Delaney O’Brien']
WarrenHighSchool = ['Brianna']
WashingtonLibertyHighSchool = ['Abby Kant']
WestfieldHighSchool = ['Katie Walsh']
WestlakeHighSchool = ['Bella Anderson']
WilliamTDwyerHighSchool = ['Anna Woodson']
WoodrowWilsonHighSchool = ['Hazel Wells']
KleinOakHighSchool = ['Morgan Baumel']
LanghamCreekHighSchool = ['Zoe Alvarado']
GlenbrookNorthHighSchool = ['Josie Mandrea']
CoppellHighSchool = ['Hana Sawaf']
JerseyVillageHighSchool = ['Aliyana Martinez']
EpiscopalHighSchool = ['Sophie Shapiro']
NewCanaanHighSchool = ['Bridget Flatow']

# EXTRACURRICULARS
ACappella = ['Chloe Lim', 'Maya Sajan']
ASB = ['Caitlin Van Sant']
ASLClub = ['Alyssa Bouloy', 'Isabella Bartz', 'Arabella Savener', 'Anna Woodson', 'Carly Schmidt']
ElementarySchoolStudentTeaching = ['Abby Alsup']
BETAClub = ['Ava Hurst']
Band = ['Marley Page', 'Ferzine Sanjana', 'Suzie Hudgens', 'Sydney Fern', 'Kirthi Gummadi']
BestBuddies = ['Brianna Salaices', 'Meghna Sunkureddi', 'Lindsay McCullough', 'Izzy Davies', 'Zoe Veliz', 'Catherine Dooley']
BookClub = ['Isabella Bartz']
BoosterClub = ['Madison Taylor', 'Erika Sandberg']
Cheer = ['Meredith Moreland', 'Genesis Martinez', 'Anna Woodson', 'Catalina Cruz', 'Allie Harter', 'Brooke Walker', 'Delaney O’Brien', 'Ella Pitts', 'Erika Sandberg', 'Izzy Davies', 'Kaylie Ngo', 'Meadow Votis', 'Erika Sandberg', 'Amelia Klyap', 'Heidi Chapin', 'Angie Andersen', 'Gabrielle Green', 'Kate Neiman', 'Rishona Mopur']
Choir = ['Maya Sajan', 'Ellen Meltzer', 'Katelyn Quintanilla', 'Meadow Votis', 'Ava Dahlander', 'Jenn Rosado', 'Jessica Paine', 'Liz Keegan', 'Kaylie Ngo', 'Valentina Markov']
ColorGuard = ['Sydney Fern', 'Carly Schmidt']
DistributiveEducationClubsofAmericaDECA = ['Brianna Salaices', 'Madison Taylor', 'Katelyn Quintanilla', 'Delaney Vanderpool', 'Haylee Martin', 'Nids Pappu']
DoSomething = ['Morgan Baumel']
EnglishHonorSocietyNEHS = ['Isabella Bartz', 'Shelby Williamson', 'Marley Page', 'Ferzine Sanjana', 'Meghna Sunkureddi', 'Sophie Robins', 'Zoe Alvarado', 'Madeleine Mazingo']
FamilyCareerandCommunityLeaderofAmericaFCCLA = ['Meghna Sunkureddi', 'Jovanni Carrillo', 'Emily Robles']
FellowshipofChristianAthletesFCA = ['Erika Sandberg', 'Meadow Votis', 'Ava Dahlander', 'Kate Neiman', 'Bella Wernli', 'Alice Hudson']
FeminismGenderEqualityClub = ['Maya Abraham']
FilmClub = ['Sarah Thompson', 'Regan Hill', 'Celeste Tomberlin', 'Diyaa Dossani', 'Sienna Shutts', 'Sophie Shapiro']
FormulaClub = ['Bella Wernli']
FrenchClub = ['Piper Buck']
FutureFarmersofAmericaFFA = ['Meadow Votis', 'Hannah Greenhill', 'Aliyana martinez']
GIS = ['Gabrielle Green']
GayStraightAllianceClub = ['Ellen Meltzer', 'Maya Abraham', 'Delaney Vanderpool', 'Regan Hill']
GeneticsandNeuroscienceClub = ['Regan Hill']
GeographyClub = ['Regan Hill']
GirlScouts = ['Arabella Savener', 'Suzie Hudgens', 'Erika Sandberg', 'Jenn Rosado', 'Catherine Favoriti', 'Riley Avery', 'Heidi Chapin', 'Avery McClure', 'Maggie Shaw', 'Sarah Sims', 'Abby OGuynn', 'Amelia Klyap', 'Haley Hooper']
HealthOccupationsStudentsofAmericaHOSA = ['Sydney Fern', 'Jasmine Valdez', 'Sofie Arroyo', 'Maria Sepulveda Salazar', 'Bailey Alsup', 'Meredith Moreland', 'Krissily Estacio', 'Emmerich Benavides', 'Megan Garza', 'Bella Champion']
IBProgram = ['Chloe Lim', 'Lindsay McCullough', 'Ava Dahlander', 'Katie Windell', 'Abby Kant', 'Hazel Wells', 'Hana Sawaf']
InternationalThespianSocietyITS = ['Arabella Savener', 'Jessica Paine', 'Liz Keegan', 'Regan Hill', 'Kaitlin Black', 'Emerson Oliver']
JROTC = ['Gabrielle Beck']
KeepTexasBeautiful = ['Anika Novak']
KeyClub = ['Isabella Bartz', 'Marley Page', 'Izzy Davies', 'Zoe Alvarado', 'Riley Avery', 'Emma Schneidau', 'Mae Trahan', 'Katie Walsh', 'Aliyana Martinez']
LatinClub = ['Gabrielle Beck']
LatinosUnidos = ['Gabrielle Green']
LeoClub = ['Celeste Tomberlin']
MockTrial = ['Kirthi Gummadi', 'Heidi Chapin', 'Emma Schneidau']
ModelUN = ['Maya Abraham', 'Kate Neiman', 'Heidi Chapin', 'Maria Sepulveda Salazar', 'Riley Wanasek', 'Mia Vasquez', 'Hana Sawaf']
NationalCharityLeagueNCL = ['Ferzine Sanjana', 'Izzy Davies', 'Ava Dahlander', 'Kaylie Ngo', 'Madeleine Mazingo', 'Heidi Chapin', 'Bailey Alsup', 'Hazel Wells', 'Kaitlin Black', 'Sarah Solomon', 'Ollie Mae Harrison', 'Brooke Walker', 'Abby Alsup', 'Allie Harter']
NewspaperJournalismClub = ['Isabella Bartz', 'Carly Schmidt', 'Ellen Meltzer', 'Maya Abraham', 'Marley Page', 'Ferzine Sanjana', 'Kirthi Gummadi', 'Zoe Veliz', 'Catherine Dooley', 'Ava Dahlander', 'Kate Neiman', 'Regan Hill', 'Sienna Shutts', 'Heidi Chapin', 'Sarah Sims', 'Kamryn Jean', 'Hazel Wells', 'Katie Walsh', 'Abrielle Gallini', 'Elyse Miller', 'Bella Anderson', 'Ellie Berman', 'Haley Hooper']
Orchestra = ['Izzy Davies', 'Madeleine Mazingo', 'Bella Wernli', 'Krissily Estacio', 'Gabrielle Beck', 'Brianna']
PeerAssistanceLeadershipandServicePALS = ['Brianna Salaices', 'Lindsay McCullough', 'Meadow Votis', 'Ava Dahlander', 'Sophie Robins', 'Emmerich Benavides', 'Katie Walsh', 'Charlie Stone', 'Haley Hooper']
PhotographyClub = ['Carly Schmidt', 'Ava Dahlander', 'Celeste Tomberlin', 'Abrielle Gallini', 'Gabrielle Beck', 'Sophie Shapiro']
Piano = ['Valentina Markov']
PsychologyClub = ['Regan Hill']
PupsforPeople = ['Valentina Markov']
QuillandScrollHonorSociety = ['Regan Hill']
RedCross = ['Ava Dahlander', 'Sophie Robins', 'Rachel Dolan', 'Hana Sawaf']
RoboticsComputerScienceClub = ['Suzie Hudgens', 'Riley Avery', 'Krissily Estacio', 'Alexandra Nicholls', 'Sophie Shapiro']
ScienceOlympiad = ['Suzie Hudgens']
ServiceCouncil = ['Jannae Ailawadhi']
SkillsUSA = ['Angie Andersen']
SpeechandDebateClub = ['Nids Pappu', 'Regan Hill', 'Heidi Chapin', 'Rachel Dolan', 'Brianna', 'Charlie Stone', 'hana Sawaf']
StudentAthleticCouncil = ['Lindsay McCullough']
StudentAthleticTrainer = ['Brianna']
StudentCouncilSTUCO = ['Isabella Bartz', 'Carly Schmidt', 'Ellen Meltzer', 'Maya Abraham', 'Gabrielle Green', 'Marley Page', 'Suzie Hudgens', 'Meghna Sunkureddi', 'Lindsay McCullough', 'Izzy Davies', 'Zoe Veliz', 'Katelyn Quintanilla', 'Sophie Robins', 'Jovanni Carrillo', 'Alice Hudson', 'Diyaa Dossani', 'Hannah Greenhill', 'Riley Avery', 'Heidi Chapin', 'Maria Sepulveda Salazar', 'Bailey Alsup', 'Krissily Estacio', 'Emmerich Benavides', 'Kamryn Jean', 'Hazel Wells', 'Riley Wanasek', 'Mia Vasquez', 'Rachel Dolan', 'Abby Alsup', 'Allie Harter', 'Gabrielle Beck', 'Brianna', 'Emily Robles', 'Ella Pitts', 'Jillian Taylor', 'Caitlin Van Sant', 'Morgan Baumel', 'Anika Novak', 'Ella Leininger', 'Charlie Stone', 'Hana Sawaf', 'Aliyana Martinez']
StudentVoterEmpowermentClub = ['Zoe Veliz']
TEDX = ['Charlie Stone']
Theatre = ['Celeste Tomberlin', 'Katelyn Quintanilla']
TutoringPeerMentoringProgram = ['Sydney Fern', 'Izzy Davies', 'Madeleine Mazingo', 'Jovanni Carrillo', 'Bella Wernli', 'Riley Avery', 'Heidi Chapin', 'Bailey Alsup', 'Katie Walsh', 'Rachel Dolan', 'Abby Alsup', 'Emily Robles', 'Claire Savage', 'Hailey Brooks', 'Josie Mandrea', 'Hana sawaf']
UniversityInterscholasticLeagueUIL = ['Marley Page', 'Sydney Fern', 'Madison Taylor', 'Jessica Paine', 'Jovanni Carrillo', 'Regan Hill', 'Diyaa Dossani', 'Heidi Chapin', 'Maria Sepulveda Salazar', 'Bailey Alsup', 'Krissily Estacio', 'Kamryn Jean', 'Kaitlin Black', 'Brianna', 'Audrey Cooper', 'Haley Hooper']
WeCareClub = ['Shelby Williamson']
WellnessCouncil = ['Kate Neiman']
WomeninSTEM = ['Madeleine Mazingo']
YearbookClub = ['Isabella Bartz', 'Arabella Savener', 'Carly Schmidt', 'Maya Abraham', 'Marley Page', 'Zoe Veliz', 'Ava Dahlander', 'Liz Keegan', 'Diyaa Dossani', 'Abrielle Gallini', 'Gabrielle Beck', 'Ava Hurst', 'Bella Anderson', 'Ellie Berman', 'Haley Hooper']
Younglife = ['Maya Abraham', 'Erika Sandberg', 'Ava Dahlander', 'Heidi Chapin', 'Bella Champion', 'Kaitlin Black', 'Mia Vasquez', 'Allie Harter', 'Emily Robles', 'Ella Leininger', 'Haley Hooper']
ZontaZClub = ['Larkin Seidel']
AcademicDecathlon = ['Bella Wernli']
ClassPresident = ['Meredith Moreland']
IsraeliCultureClub = ['Josie Mandrea']
RotaryInteractClub = ['Aliyana Martinez']
AthleticTraining = ['Emerson Oliver']
Ballet = ['Catalina Cruz', 'Chloe Lim', 'Ava Dahlander', 'Georgia Key']
Basketball = ['Ellie Berman', 'Maya Abraham', 'Lindsay McCullough', 'Caitlin Van Sant', 'Bella Champion', 'Morgan Baumel', 'Karlie Haigood', 'Hazel Wells']
Boxing = ['Valentina Markov']
CrossCountry = ['Chloe Lim', 'Ellie Berman', 'Meadow Votis', 'Riley Avery', 'Mia Vasquez', 'Brianna Salaices', 'Gabrielle Beck', 'Abby Alsup', 'Bailey Alsup', 'Delaney Vanderpool', 'Hailey Brooks', 'Hannah Greenhill', 'Lola Daffin', 'Sophie Shapiro']
DanceTeam = ['Catalina Cruz', 'Chloe Lim', 'Ava Dahlander', 'Georgia Key', 'Maya Abraham', 'Erika Sandberg', 'Amelia Klyap', 'Bella Anderson', 'Emily Robles', 'Isabella Bartz', 'Alexandra Nicholls', 'Claire Savage', 'Jasmine Valdez', 'Kamryn Jean', 'Shelby Williamson', 'Sophie Robins', 'Abrielle Gallini', 'Ollie Mae Harrison', 'Sarah Thompson']
DrillTeam = ['Catalina Cruz', 'Ava Dahlander', 'Georgia Key', 'Maya Abraham', 'Alexandra Nicholls', 'Claire Savage', 'Jasmine Valdez', 'Kamryn Jean', 'Shelby Williamson', 'Sophie Robins', 'Abrielle Gallini', 'Zoe Alvarado', 'Larkin Seidel']
FieldHockey = ['Katie Walsh', 'Maggie Shaw', 'Valentina Markov']
FigureSkating = ['Rachel Dolan', 'Bridget Flatow']
FlagFootball = ['Caitlin Van Sant']
Golf = ['Riley Avery', 'Avery McClure', 'Haylee Martin', 'Mae Trahan', 'Elyse Miller']
Lacrosse = ['Lindsay McCullough', 'Caitlin Van Sant', 'Mia Vasquez', 'Katie Walsh', 'Emerson Oliver', 'Jannae Ailawadhi']
RockClimbing = ['Heidi Chapin', 'Hana Sawaf']
Rowing = ['Valentina Markov', 'Jenn Rosado']
Skiing = ['Emerson Oliver', 'Liz Keegan', 'Josie Mandrea']
Soccer = ['Lindsay McCullough', 'Bella Champion', 'Brianna Salaices', 'Sophie Robins', 'Sarah Thompson', 'Larkin Seidel', 'Julia Lindstrom', 'Maria Sepulveda Salazar', 'Regan Hill', 'Taylor Jennings', 'Ellen Meltzer', 'Jenn Rosado', 'Megan Garza', 'Audrey Cooper']
Softball = ['Caitlin Van Sant', 'Morgan Baumel', 'Amelia Klyap', 'Emily Bull', 'Piper Buck', 'Jovanni Carrillo']
StudentAthleticTraining = ['Mazzy Bledsoe']
SwimmingDiving = ['Gabrielle Beck', 'Alice Hudson', 'Kirthi Gummadi', 'Catherine Dooley', 'Rachel Dolan', 'Katie Windell', 'Hana Sawaf', 'Hana Sawaf', 'Sophie Shapiro']
Tennis = ['Catalina Cruz', 'Angie Andersen', 'Maggie Shaw', 'Jannae Ailawadhi', 'Ellen Meltzer', 'Catherine Dooley', 'Rachel Dolan', 'Abby Sanders', 'Anika Novak', 'Riley Wanasek', 'Haley Hooper', 'Josie Mandrea']
Track = ['Bella Champion', 'Karlie Haigood', 'Riley Avery', 'Mia Vasquez', 'Gabrielle Beck', 'Abby Alsup', 'Bailey Alsup', 'Delaney Vanderpool', 'Hailey Brooks', 'Hannah Greenhill', 'Lola Daffin', 'Abrielle Gallini', 'Jenn Rosado', 'Chasiti Tyeryar', 'Emma Schneidau', 'Sarah Sims', 'Sophie Shapiro']
Volleyball = ['Bella Champion', 'Karlie Haigood', 'Hazel Wells', 'Gabrielle Green', 'Kate Neiman', 'Elyse Miller', 'Jannae Ailawadhi', 'Megan Garza', 'Jovanni Carrillo', 'Abby Kant', 'Ava Hurst', 'Bella Wernli', 'Emmerich Benavides', 'Nids Pappu', 'Madison Taylor', 'Haley hooper']
WaterPolo = ['Valentina Markov', 'Audrey Cooper', 'Katie Windell', 'Hana Sawaf']
Rowing = ['Valentina Markov', 'Jenn Rosado']

# UT ORGS
AdvertisingClub = ['Elyse Miller']
ArchitectureClub = ['Riley Avery']
BroadcastingClub = ['Bella Anderson', 'Carly Schmidt', "Delaney O'Brien", 'Sienna Shutts', 'Celeste Tomberlin', 'Diyaa Dossani', 'Isabella Bartz', 'Kirthi Gummadi', 'Catalina Cruz', 'Regan Hill', 'Catherine Favoriti', 'Sophie Shapiro']
BusinessFinanceMarketingEconomicsClub = ['Alice Hudson', 'Allie Harter', 'Haylee Martin', 'Jillian Taylor', 'Kaylie Ngo', 'Marley Page', 'Shelby Williamson', 'Madison Taylor', 'Sarah Thompson', 'Brianna', 'Suzie Hudgens', 'Katie Walsh', 'Catherine Dooley', 'Lola Daffin', 'Brooke Walker', 'Nids Pappu', 'Amelia Klyap', 'Meredith Moreland', 'Hana Sawaf']
Challengers = ['Chasiti Tyeryar', 'Haley Hooper']
UTChoir = ['Ava Hurst']
CulturalClub = ['Diyaa Dossani', 'Isabella Bartz', 'Brianna', 'Julia Lindstrom', 'Sarah Solomon', 'Maria Sepulveda Salazar', 'Meghna Sunkureddi', 'Hana Sawaf']
EnvironmentalSustainabilityClub = ['Katie Windell']
EventHostingClub = ['Liz Keegan', 'Josie Mandrea']
GovernmentClub = ['Kirthi Gummadi', 'Zoe Veliz', 'Brianna Salaices', 'Maya Abraham', 'Chloe Lim', 'Charlie Stone', 'Heidi Chapin', 'Riley Wanasek', 'Josie Mandrea', 'hana Sawaf']
WomeninMedicine = ['Jannae Ailawadhi']
Ignite = ['Haley Hooper','Audrey Cooper','Jessica Paine']
IntramuralSports = ['Isabella Bartz', 'Regan Hill', 'Suzie Hudgens', 'Brianna Salaices', 'Maya Abraham', 'Angie Andersen', 'Bella Champion', 'Hazel Wells', 'Sophie Robins', 'Abby Kant', 'Abby Sanders', 'Lindsay McCullough', 'Jovanni Carrillo', 'Audrey Cooper', 'Erika Sandberg', 'Erika Sandberg', 'Abby OGuynn', 'Emmerich Benavides', 'Gabrielle Beck', 'Morgan Baumel', 'Riley Avery', 'Ellen Meltzer', 'Hana Sawaf']
JournalismMagazineOrganization = ['Katie Walsh', 'Catalina Cruz', 'Ellen Meltzer']
NursingClub = ['Gabrielle Green']
PerformingArtsClub = ['Catherine Favoriti', 'Chloe Lim', 'Abrielle Gallini', 'Kate Neiman', 'Katelyn Quintanilla', 'Kamryn Jean', 'Jessica Paine', 'Kaitlin Black', 'Emily Bull', 'Georgia Key']
PhilosophyClub = ['Katie Windell', 'Arabella Savener']
PreHealthClub = ['Brianna', 'Maria Sepulveda Salazar', 'Brianna Salaices', 'Abby Kant', 'Abby Sanders', 'Lindsay McCullough', 'Kamryn Jean', 'Avery McClure', 'Claire Savage', 'Genesis Martinez', 'Karlie Haigood', 'Maya Sajan', 'Mazzy Bledsoe', 'Megan Garza', 'Sofie Arroyo', 'Bailey Alsup', 'Izzy Davies', 'Sydney Fern', 'Rachel Dolan', 'Alyssa Bouloy']
PreLawClub = ['Aliyana Martinez Kirthi Gummadi', 'Brianna', 'Catherine Dooley', 'Lola Daffin', 'Charlie Stone', 'Heidi Chapin', 'Riley Wanasek', 'Jovanni Carrillo', 'Bella Wernli', 'Ella Leininger', 'Hannah Greenhill', 'Piper Buck', 'Abby Alsup', 'Ferzine Sanjana', 'Josie Mandrea', 'Aliyana Martinez']
ReligiousClub = ['Isabella Bartz', 'Brooke Walker', 'Maya Abraham', 'Heidi Chapin', 'Audrey Cooper', 'Erika Sandberg', 'Erika Sandberg', 'Jessica Paine', 'Kaitlin Black', 'Arabella Savener', 'Bailey Alsup', 'Izzy Davies', 'Sydney Fern', 'Abby Alsup', 'Ava Dahlander', 'Ella Pitts', 'Ellie Berman', 'Liz Keegan', 'Mia Vasquez', 'Emily Robles', 'Meadow Votis', 'Haley Hooper', 'Josie Mandrea']
ResidenceHallAssociation = ['Anna Woodson']
STEMClub = ['Regan Hill', 'Suzie Hudgens', 'Nids Pappu', 'Amelia Klyap', 'Katie Windell', 'Chloe Lim', 'Abby OGuynn', 'Emmerich Benavides', 'Gabrielle Beck', 'Morgan Baumel', 'Riley Avery', 'Emily Bull', 'Rachel Dolan', 'Mia Vasquez', 'Alexandra Nicholls', 'Caitlin Van Sant', 'Jasmine Valdez', 'Jenn Rosado', 'Krissily Estacio', 'Madeleine Mazingo', 'Mae Trahan', 'Maggie Shaw', 'Taylor Jennings', 'Emerson Oliver', 'Ollie Mae Harrison']
SocialInterestActivismClub = ['Isabella Bartz', 'Kirthi Gummadi', 'Regan Hill', 'Amelia Klyap', 'Chloe Lim', 'Riley Avery', 'Ferzine Sanjana', 'Delaney Vanderpool', 'Emma Schneidau', 'Aliyana Martinez']
SpiritOrg = ['Riley Wanasek', 'Emily Robles']
SteelDanceCompany = ['Georgia Key']
TeachersofTomorrow = ['Anika Novak', 'Meghna Sunkureddi', 'Haley hooper']
TexasSupportsLiveMusic = ['Emerson Oliver', 'Sarah Sims']
TheDailyTexan = ['Ellen Meltzer']
ThemeParkEngineeringClub = ['Ollie Mae Harrison']
WaterSkiingClub = ['Valentina Markov', 'Meadow Votis']
WomeninBusinessAssociation = ['Meredith Moreland']
WomeninPsychology = ['Alyssa Bouloy']

# ACTIVITIES FOR FUN
Basketballfun = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Morgan Baumel', 'Karlie Haigood']
Biking = ['Julia Lindstrom', 'Caitlin Van Sant', 'Delaney Vanderpool', 'Charlie Stone', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley Avery', 'Riley Wanasek', 'Kate Neiman', 'Katie Walsh', 'Josie Mandrea', 'Hana Sawaf', 'Sophie Shapiro']
Boating = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Delaney Vanderpool', 'Charlie Stone', 'Amelia Klyap', 'Lindsay McCullough', 'Shelby Williamson', 'Sofie Arroyo', 'Erika Sandberg', 'Liz Keegan', 'Emerson Oliver', 'Hana Sawaf']
Camping = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Delaney Vanderpool', 'Charlie Stone', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley Avery', 'Riley Wanasek', 'Shelby Williamson', 'Meadow Votis', 'Ava Dahlander', 'Ava Hurst', 'Heidi Chapin', 'Ellie Berman', 'Mae Trahan', 'Regan Hill', 'Hana Sawaf', 'Sophie Shapiro']
ConcertsLiveMusic = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Morgan Baumel', 'Delaney Vanderpool', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Kate Neiman', 'Katie Walsh', 'Sofie Arroyo', 'Erika Sandberg', 'Liz Keegan', 'Emerson Oliver', 'Meadow Votis', 'Ava Dahlander', 'Ava Hurst', 'Heidi Chapin', 'Ellie Berman', 'Mae Trahan', 'Madeleine Mazingo', 'Diyaa Dossani', 'Isabella Bartz', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'Madison Taylor', 'Jessica Paine', 'Jillian Taylor', 'Katelyn Quintanilla', 'Abrielle Gallini', 'Ellen Meltzer', 'Chloe Lim', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Ollie Mae Harrison', 'Kirthi Gummadi', 'Zoe Alvarado', 'Claire Savage', 'Georgia Key', 'Sarah Thompson', 'Sarah Solomon', 'Avery McClure', 'Haylee Martin', 'Krissily Estacio', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Brianna', 'Ella Leininger', 'Emily Bull', 'Taylor Jennings', 'Delaney O’Brien', 'Jannae Ailawadhi', 'Mia Vasquez', 'Anika Novak', 'Chasiti Tyeryar', 'Alice Hudson', 'Lola Daffin', 'Megan Garza', 'Emma Schneidau', 'Katie Windell', 'Allie Harter', 'Suzie Hudgens', 'Audrey Cooper', 'Abby Sanders', 'Hazel Wells', 'Marley Page', 'Hannah Greenhill', 'Meredith Moreland', 'Emmerich Benavides', 'Anna Woodson', 'Zoe Veliz', 'Elyse Miller', 'Ella Pitts', 'Celeste Tomberlin', 'Mazzy Bledsoe', 'Catherine Favoriti', 'Kaylie Ngo', 'Nids Pappu', 'Maya Sajan', 'Catherine Dooley', 'Piper Buck', 'Ferzine Sanjana', 'Carly Schmidt', 'Hana Sawaf', 'Aliyana Martinez', 'Sophie Shapiro', 'Emily Robles']
CountryDancing = ['Elyse Miller']
Dancing = ['Maya Abraham', 'Amelia Klyap', 'Kaitlin Black', 'Alexandra Nicholls', 'Kate Neiman', 'Shelby Williamson', 'Sofie Arroyo', 'Erika Sandberg', 'Meadow Votis', 'Ava Dahlander', 'Madeleine Mazingo', 'Diyaa Dossani', 'Isabella Bartz', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'Madison Taylor', 'Jessica Paine', 'Jillian Taylor', 'Katelyn Quintanilla', 'Abrielle Gallini', 'Ellen Meltzer', 'Chloe Lim', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Ollie Mae Harrison', 'Kirthi Gummadi', 'Zoe Alvarado', 'Claire Savage', 'Georgia Key', 'Sarah Thompson', 'Gabrielle Green', 'Sienna Shutts', 'Larkin Seidel', 'Catalina Cruz', 'Kamryn Jean', 'Emily Robles', 'Brooke Walker', 'Rishona Mopur']
ExploringAustin = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Delaney Vanderpool', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Gabrielle Beck', 'Riley Avery', 'Kate Neiman', 'Katie Walsh', 'Shelby Williamson', 'Sofie Arroyo', 'Erika Sandberg', 'Liz Keegan', 'Meadow Votis', 'Ava Dahlander', 'Ava Hurst', 'Heidi Chapin', 'Ellie Berman', 'Diyaa Dossani', 'Isabella Bartz', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'Madison Taylor', 'Jessica Paine', 'Jillian Taylor', 'Katelyn Quintanilla', 'Abrielle Gallini', 'Ellen Meltzer', 'Chloe Lim', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Ollie Mae Harrison', 'Kirthi Gummadi', 'Sarah Solomon', 'Avery McClure', 'Haylee Martin', 'Krissily Estacio', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Brianna', 'Ella Leininger', 'Emily Bull', 'Taylor Jennings', 'Delaney O’Brien', 'Jannae Ailawadhi', 'Mia Vasquez', 'Anika Novak', 'Chasiti Tyeryar', 'Alice Hudson', 'Lola Daffin', 'Megan Garza', 'Emma Schneidau', 'Katie Windell', 'Allie Harter', 'Suzie Hudgens', 'Audrey Cooper', 'Abby Sanders', 'Hazel Wells', 'Marley Page', 'Hannah Greenhill', 'Meredith Moreland', 'Emmerich Benavides', 'Anna Woodson', 'Zoe Veliz', 'Elyse Miller', 'Ella Pitts', 'Celeste Tomberlin', 'Mazzy Bledsoe', 'Catherine Favoriti', 'Larkin Seidel', 'Catalina Cruz', 'Kamryn Jean', 'Genesis Martinez', 'Abby OGuynn', 'Maggie Shaw', 'Brianna Salaices', 'Meghna Sunkureddi', 'Alyssa Bouloy', 'Izzy Davies', 'Haley Hooper ', 'Josie Mandrea', 'Hana Sawaf', 'Aliyana Martinez', 'Sophie Shapiro']
FieldHockeyfun = ['Valentina Markov', 'Katie Walsh', 'Bridget Flatow']
Fishing = ['Julia Lindstrom', 'Valentina Markov', 'Sarah Sims', 'Lindsay McCullough', 'Kaitlin Black', 'Sofie Arroyo', 'Emerson Oliver', 'Meadow Votis', 'Sarah Solomon', 'Jenn Rosado']
Football = ['Valentina Markov', 'Emerson Oliver']
Golfingfun = ['Caitlin Van Sant', 'Bella Champion', 'Riley Avery', 'Katie Walsh', 'Mae Trahan', 'Diyaa Dossani', 'Isabella Bartz', 'Avery McClure', 'Haylee Martin', 'Emily Robles']
Hiking = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Morgan Baumel', 'Delaney Vanderpool', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley Avery', 'Kate Neiman', 'Shelby Williamson', 'Liz Keegan', 'Meadow Votis', 'Ava Hurst', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'Madison Taylor', 'Jessica Paine', 'Jillian Taylor', 'Katelyn Quintanilla', 'Krissily Estacio', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Brianna', 'Ella Leininger', 'Emily Bull', 'Taylor Jennings', 'Kaylie Ngo', 'Abby OGuynn', 'Maggie Shaw', 'Bella Wernli', 'Haley Hooper', 'Josie Mandrea', 'Hana Sawaf', 'Sophie shapiro']
HorsebackRiding = ['Valentina Markov', 'Kate Neiman', 'Ava Hurst', 'Diyaa Dossani', 'Sydney Fern', 'Abrielle Gallini', 'Delaney O’Brien']
Hunting = ['Valentina Markov', 'Karlie Haigood', 'Kaitlin Black', 'Sofie Arroyo', 'Meadow Votis', 'Sarah Solomon']
IceSkating = ['Sydney Fern', 'Rachel Dolan', 'Krissily Estacio']
Lacrossefun = ['Emerson Oliver', 'Jannae Ailawadhi', 'Mia Vasquez']
PaddleboardingKayaking = ['Julia Lindstrom', 'Caitlin Van Sant', 'Delaney Vanderpool', 'Lindsay McCullough', 'Riley Avery', 'Erika Sandberg', 'Ava Dahlander', 'Ava Hurst', 'Sydney Fern', 'Sophie Robins', 'Hailey Brooks', 'Abrielle Gallini', 'Sarah Solomon', 'Krissily Estacio', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Brianna', 'Ella Leininger', 'Jannae Ailawadhi', 'Anika Novak', 'Chasiti Tyeryar', 'Alice Hudson', 'Lola Daffin', 'Megan Garza', 'Emma Schneidau', 'Katie Windell', 'Abby OGuynn', 'Brianna Salaices', 'Arabella Savener', 'Josie Mandrea', 'Hana Sawaf', 'Aliyana Martinez', 'Sophie shapiro']
Pickleball = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Bella Champion', 'Lindsay McCullough', 'Kaitlin Black', 'Riley Wanasek', 'Erika Sandberg', 'Isabella Bartz', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'Madison Taylor', 'Ellen Meltzer', 'Zoe Alvarado', 'Avery McClure', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Brianna', 'Emily Bull', 'Jannae Ailawadhi', 'Anika Novak', 'Chasiti Tyeryar', 'Alice Hudson', 'Allie Harter', 'Suzie Hudgens', 'Audrey Cooper', 'Abby Sanders', 'Hazel Wells', 'Nids Pappu', 'Larkin Seidel', 'Emily Robles', 'Maggie Shaw', 'Brianna Salaices', 'Meghna Sunkureddi', 'Angie Andersen', 'Haley hooper', 'Josie Mandrea', 'Sophie Shapiro']
Picnics = ['Caitlin Van Sant', 'Maya Abraham', 'Sarah Sims', 'Delaney Vanderpool', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Jovanni Carrillo', 'Riley Avery', 'Shelby Williamson', 'Liz Keegan', 'Meadow Votis', 'Heidi Chapin', 'Isabella Bartz', 'Sydney Fern', 'Sophie Robins', 'Hailey Brooks', 'Jessica Paine', 'Chloe Lim', 'Haylee Martin', 'Krissily Estacio', 'Abby Alsup', 'Delaney O’Brien', 'Anika Novak', 'Chasiti Tyeryar', 'Marley Page', 'Catalina Cruz', 'Meghna Sunkureddi', 'Alyssa Bouloy', 'Haley Hooper', 'Sophie Shapiro']
Pilates = ['Julia Lindstrom', 'Caitlin Van Sant', 'Maya Abraham', 'Bella Champion', 'Amelia Klyap', 'Lindsay McCullough', 'Jovanni Carrillo', 'Riley Avery', 'Kate Neiman', 'Shelby Williamson', 'Heidi Chapin', 'Isabella Bartz', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'Madison Taylor', 'Jillian Taylor', 'Ellen Meltzer', 'Chloe Lim', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Ollie Mae Harrison', 'Claire Savage', 'Georgia Key', 'Krissily Estacio', 'Abby Kant', 'Taylor Jennings', 'Mia Vasquez', 'Alice Hudson', 'Lola Daffin', 'Allie Harter', 'Suzie Hudgens', 'Hannah Greenhill', 'Meredith Moreland', 'Nids Pappu', 'Maya Sajan', 'Catherine Dooley', 'Piper Buck', 'Larkin Seidel', 'Catalina Cruz', 'Emily Robles', 'Alyssa Bouloy', 'Izzy Davies', 'Josie Mandrea', 'Hana Sawaf']
RockClimbingfun = ['Caitlin Van Sant', 'Delaney Vanderpool', 'Gabrielle Beck', 'Katie Walsh', 'Heidi Chapin', 'Sophie Robins', 'Catalina Cruz', 'Sophie Shapiro']
RunningJoggingfun = ['Julia Lindstrom', 'Caitlin Van Sant', 'Sarah Sims', 'Delaney Vanderpool', 'Kaitlin Black', 'Gabrielle Beck', 'Riley Avery', 'Riley Wanasek', 'Kate Neiman', 'Katie Walsh', 'Ava Dahlander', 'Isabella Bartz', 'Sophie Robins', 'Hailey Brooks', 'Madison Taylor', 'Katelyn Quintanilla', 'Abrielle Gallini', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Kirthi Gummadi', 'Krissily Estacio', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Emily Bull', 'Taylor Jennings', 'Jannae Ailawadhi', 'Lola Daffin', 'Allie Harter', 'Audrey Cooper', 'Hannah Greenhill', 'Emmerich Benavides', 'Maya Sajan', 'Larkin Seidel', 'Jenn Rosado', 'Sophie Shapiro ', 'Sophie Shapiro']
ScubaDiving = ['Valentina Markov', 'Kate Neiman', 'Hana Sawaf']
Soccerfun = ['Larkin Seidel']
Surfing = ['Julia Lindstrom', 'Kate Neiman', 'Lola Daffin', 'Brooke Walker', 'Hana Sawaf', 'Rishona Mopur']
SwimmingDivingfun = ['Julia Lindstrom', 'Bella Champion', 'Karlie Haigood', 'Charlie Stone', 'Amelia Klyap', 'Gabrielle Beck', 'Katie Walsh', 'Madison Taylor', 'Jillian Taylor', 'Ellen Meltzer', 'Chloe Lim', 'Krissily Estacio', 'Alice Hudson', 'Audrey Cooper', 'Anna Woodson', 'Catherine Dooley', 'Aliyana Martinez', 'Sophie Shapiro']
Tanning = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Delaney Vanderpool', 'Charlie Stone', 'Amelia Klyap', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley Avery', 'Riley Wanasek', 'Kate Neiman', 'Erika Sandberg', 'Meadow Votis', 'Ava Dahlander', 'Ava Hurst', 'Heidi Chapin', 'Regan Hill', 'Sydney Fern', 'Sophie Robins', 'Hailey Brooks', 'Madison Taylor', 'Jillian Taylor', 'Abrielle Gallini', 'Ellen Meltzer', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Ollie Mae Harrison', 'Georgia Key', 'Sarah Thompson', 'Avery McClure', 'Haylee Martin', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Ella Leininger', 'Emily Bull', 'Taylor Jennings', 'Anika Novak', 'Chasiti Tyeryar', 'Alice Hudson', 'Lola Daffin', 'Megan Garza', 'Abby Sanders', 'Hazel Wells', 'Marley Page', 'Emmerich Benavides', 'Anna Woodson', 'Zoe Veliz', 'Elyse Miller', 'Ella Pitts', 'Kaylie Ngo', 'Piper Buck', 'Larkin Seidel', 'Catalina Cruz', 'Emily Robles', 'Alyssa Bouloy', 'Izzy Davies', 'Jenn Rosado', 'Bella Wernli', 'Jasmine Valdez', 'Hana Sawaf', 'Aliyana Martinez','Sofie Arroyo']
Tennisfun = ['Riley Wanasek', 'Kate Neiman', 'Rachel Dolan', 'Sophie Robins', 'Jessica Paine', 'Ellen Meltzer', 'Abby Sanders', 'Hazel Wells', 'Catherine Dooley', 'Ferzine Sanjana', 'Catalina Cruz', 'Emily Robles', 'Maggie Shaw', 'Angie Andersen', 'Sophie Shapiro']
Thrifting = ['Julia Lindstrom', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Morgan Baumel', 'Delaney Vanderpool', 'Amelia Klyap', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Emerson Oliver', 'Meadow Votis', 'Ava Hurst', 'Heidi Chapin', 'Ellie Berman', 'Regan Hill', 'Diyaa Dossani', 'Isabella Bartz', 'Sophie Robins', 'Madison Taylor', 'Jessica Paine', 'Katelyn Quintanilla', 'Ellen Meltzer', 'Chloe Lim', 'Kirthi Gummadi', 'Krissily Estacio', 'Abby Alsup', 'Ella Leininger', 'Taylor Jennings', 'Delaney O’Brien', 'Jannae Ailawadhi', 'Lola Daffin', 'Emma Schneidau', 'Katie Windell', 'Marley Page', 'Hannah Greenhill', 'Elyse Miller', 'Celeste Tomberlin', 'Carly Schmidt', 'Catalina Cruz', 'Emily Robles', 'Abby OGuynn', 'Izzy Davies', 'Bridget Flatow']
Traveling = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Morgan Baumel', 'Delaney Vanderpool', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley Avery', 'Kate Neiman', 'Shelby Williamson', 'Sofie Arroyo', 'Erika Sandberg', 'Liz Keegan', 'Meadow Votis', 'Ava Dahlander', 'Ava Hurst', 'Ellie Berman', 'Regan Hill', 'Diyaa Dossani', 'Isabella Bartz', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'Madison Taylor', 'Jessica Paine', 'Jillian Taylor', 'Bella Anderson', 'Zoe Alvarado', 'Georgia Key', 'Haylee Martin', 'Krissily Estacio', 'Abby Alsup', 'Abby Kant', 'Brianna', 'Ella Leininger', 'Emily Bull', 'Taylor Jennings', 'Jannae Ailawadhi', 'Mia Vasquez', 'Anika Novak', 'Lola Daffin', 'Emma Schneidau', 'Abby Sanders', 'Hazel Wells', 'Marley Page', 'Meredith Moreland', 'Emmerich Benavides', 'Elyse Miller', 'Ella Pitts', 'Celeste Tomberlin', 'Mazzy Bledsoe', 'Catherine Favoriti', 'Kaylie Ngo', 'Catherine Dooley', 'Piper Buck', 'Carly Schmidt', 'Larkin Seidel', 'Emily Robles', 'Meghna Sunkureddi', 'Alyssa Bouloy', 'Izzy Davies', 'Bella Wernli', 'Josie Mandrea', 'Aliyana Martinez', 'Charlie Stone']
Triathlons = ['Katie Walsh']
Volleyballfun = ['Bella Champion', 'Gabrielle Beck', 'Kate Neiman', 'Meadow Votis', 'Sydney Fern', 'Madison Taylor', 'Maria Sepulveda Salazar', 'Abby Kant', 'Emmerich Benavides', 'Elyse Miller', 'Nids Pappu', 'Abby OGuynn', 'Bella Wernli']
WalksOutdoors = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Sarah Sims', 'Morgan Baumel', 'Delaney Vanderpool', 'Charlie Stone', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley Avery', 'Kate Neiman', 'Shelby Williamson', 'Sofie Arroyo', 'Liz Keegan', 'Emerson Oliver', 'Ava Dahlander', 'Ellie Berman', 'Mae Trahan', 'Regan Hill', 'Isabella Bartz', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'Madison Taylor', 'Jessica Paine', 'Jillian Taylor', 'Katelyn Quintanilla', 'Ellen Meltzer', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Kirthi Gummadi', 'Sarah Thompson', 'Abby Alsup', 'Bailey Alsup', 'Brianna', 'Ella Leininger', 'Emily Bull', 'Delaney O’Brien', 'Jannae Ailawadhi', 'Chasiti Tyeryar', 'Lola Daffin', 'Emma Schneidau', 'Katie Windell', 'Allie Harter', 'Audrey Cooper', 'Abby Sanders', 'Hazel Wells', 'Marley Page', 'Hannah Greenhill', 'Emmerich Benavides', 'Elyse Miller', 'Kaylie Ngo', 'Nids Pappu', 'Maya Sajan', 'Catherine Dooley', 'Larkin Seidel', 'Kamryn Jean', 'Abby OGuynn', 'Meghna Sunkureddi', 'Alyssa Bouloy', 'Izzy Davies', 'Bella Wernli', 'Jasmine Valdez', 'Josie Mandrea', 'Aliyana Martinez', 'Sophie Shapiro']
WaterSkiing = ['Delaney Vanderpool', 'Gabrielle Beck', 'Erika Sandberg', 'Meadow Votis', 'Sophie Robins', 'Chasiti Tyeryar', 'Hana Sawaf', 'Rishona Mopur']
WorkingOut = ['Julia Lindstrom', 'Valentina Markov', 'Maya Abraham', 'Bella Champion', 'Karlie Haigood', 'Delaney Vanderpool', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley Wanasek', 'Kate Neiman', 'Katie Walsh', 'Shelby Williamson', 'Sofie Arroyo', 'Meadow Votis', 'Heidi Chapin', 'Ellie Berman', 'Regan Hill', 'Diyaa Dossani', 'Isabella Bartz', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'Madison Taylor', 'Jillian Taylor', 'Abrielle Gallini', 'Ellen Meltzer', 'Chloe Lim', 'Maria Sepulveda Salazar', 'Kirthi Gummadi', 'Georgia Key', 'Avery McClure', 'Abby Alsup', 'Abby Kant', 'Emily Bull', 'Jannae Ailawadhi', 'Lola Daffin', 'Allie Harter', 'Audrey Cooper', 'Abby Sanders', 'Hazel Wells', 'Marley Page', 'Hannah Greenhill', 'Emmerich Benavides', 'Elyse Miller', 'Ella Pitts', 'Catherine Favoriti', 'Kaylie Ngo', 'Nids Pappu', 'Maya Sajan', 'Catherine Dooley', 'Piper Buck', 'Larkin Seidel', 'Emily Robles', 'Meghna Sunkureddi', 'Izzy Davies', 'Arabella Savener', 'Jasmine Valdez', 'Josie Mandrea', 'Hana Sawaf', 'Aliyana Martinez', 'sophie shaprio']
Yoga = ['Julia Lindstrom', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Amelia Klyap', 'Lindsay McCullough', 'Kate Neiman', 'Katie Walsh', 'Shelby Williamson', 'Sofie Arroyo', 'Erika Sandberg', 'Liz Keegan', 'Meadow Votis', 'Heidi Chapin', 'Ellie Berman', 'Diyaa Dossani', 'Isabella Bartz', 'Rachel Dolan', 'Sophie Robins', 'Jillian Taylor', 'Katelyn Quintanilla', 'Ellen Meltzer', 'Chloe Lim', 'Maria Sepulveda Salazar', 'Ollie Mae Harrison', 'Georgia Key', 'Avery McClure', 'Krissily Estacio', 'Abby Kant', 'Taylor Jennings', 'Jannae Ailawadhi', 'Mia Vasquez', 'Anika Novak', 'Alice Hudson', 'Lola Daffin', 'Katie Windell', 'Allie Harter', 'Suzie Hudgens', 'Abby Sanders', 'Hazel Wells', 'Hannah Greenhill', 'Elyse Miller', 'Catherine Favoriti', 'Nids Pappu', 'Maya Sajan', 'Piper Buck', 'Larkin Seidel', 'Catalina Cruz', 'Emily Robles', 'Izzy Davies', 'Jasmine Valdez', 'Haley Hooper', 'Josie Mandrea', 'Aliyana Martinez', 'Sophie Shapiro']
Animals = ['Sarah Sims', 'Shelby Williamson', 'Piper Buck', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'Madison Taylor', 'Kirthi Gummadi', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'Zoe Alvarado', 'Erika Sandberg', 'Riley Avery', 'Bailey Alsup', 'Anika Novak', 'Delaney O’Brien', 'Sarah Solomon', 'Liz Keegan', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Mae Trahan', 'Kaylie Ngo', 'Brianna', 'Alexandra Nicholls', 'Valentina Markov', 'Zoe Veliz', 'Sofie Arroyo', 'Emma Schneidau', 'Marley Page', 'Gabrielle Green', 'Karlie Haigood', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'Brianna Salaices', 'Georgia Key', 'Megan Garza', 'Catherine Favoriti', 'Audrey Cooper', 'Kamryn Jean', 'Meredith Moreland', 'Hana Sawaf', 'Aliyana Martinez']
ArtsandCrafts = ['Sarah Sims', 'Shelby Williamson', 'Piper Buck', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'Madison Taylor', 'Kirthi Gummadi', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'Zoe Alvarado', 'Erika Sandberg', 'Riley Avery', 'Bailey Alsup', 'Anika Novak', 'Delaney O’Brien', 'Sarah Solomon', 'Liz Keegan', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'Meghna Sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'Sarah Thompson', 'Angie Andersen', 'Gabrielle Beck', 'Bella Champion', 'Catalina Cruz', 'Isabella Bartz', 'Katie Windell', 'Jillian Taylor', 'Ferzine Sanjana', 'Abby Sanders', 'Alyssa Bouloy', 'Jenn Rosado', 'Carly Schmidt', 'Haley Hooper']
Baking = ['Sarah Sims', 'Shelby Williamson', 'Piper Buck', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'Madison Taylor', 'Kirthi Gummadi', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'Zoe Alvarado', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Mae Trahan', 'Kaylie Ngo', 'Brianna', 'Alexandra Nicholls', 'Valentina Markov', 'Zoe Veliz', 'Sofie Arroyo', 'Emma Schneidau', 'Marley Page', 'Gabrielle Green', 'Karlie Haigood', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'Meghna Sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'Sarah Thompson', 'Angie Andersen', 'Gabrielle Beck', 'Rachel Dolan', 'Anna Woodson', 'Maggie Shaw', 'Suzie Hudgens', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Jannae Ailawadhi', 'Allie Harter', 'Ella Pitts', 'Emmerich Benavides', 'Haylee Martin', 'Madeleine Mazingo', 'Avery McClure', 'Arabella Savener', 'Abby OGuynn', 'Catherine Dooley', 'Haley Hooper']
Boardgames = ['Sarah Sims', 'Shelby Williamson', 'Erika Sandberg', 'Ella Leininger', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'Meghna Sunkureddi', 'Bella Champion', 'Catalina Cruz', 'Rachel Dolan', 'Anna Woodson']
CoffeeTea = ['Sarah Sims', 'Piper Buck', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'Madison Taylor', 'Erika Sandberg', 'Riley Avery', 'Bailey Alsup', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Mae Trahan', 'Kaylie Ngo', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'Brianna Salaices', 'Georgia Key', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'Meghna Sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'Sarah Thompson', 'Bella Champion', 'Isabella Bartz', 'Katie Windell', 'Jillian Taylor', 'Ferzine Sanjana', 'Abby Sanders', 'Alyssa Bouloy', 'Rachel Dolan', 'Maggie Shaw', 'Suzie Hudgens', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Jannae Ailawadhi', 'Allie Harter', 'Ella Pitts', 'Emmerich Benavides', 'Haylee Martin', 'Madeleine Mazingo', 'Avery McClure', 'Diyaa Dossani', 'Hazel Wells', 'Maya Sajan', 'Ollie Mae Harrison', 'Mia Vasquez', 'Ava Dahlander', 'Taylor Jennings', 'Riley Wanasek', 'Lindsay McCullough', 'Alice Hudson', 'Delaney Vanderpool', 'Elyse Miller', 'Sienna Shutts', 'Hailey Brooks', 'Bella Wernli', 'Celeste Tomberlin', 'Abby Kant', 'Chasiti Tyeryar', 'Genesis Martinez', 'Emily Robles', 'Josie Mandrea', 'Aliyana Martinez']
Cooking = ['Sarah Sims', 'Piper Buck', 'Kirthi Gummadi', 'Jovanni Carrillo', 'Riley Avery', 'Anika Novak', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Brianna', 'Alexandra Nicholls', 'Valentina Markov', 'Ava Hurst', 'Megan Garza', 'Catherine Favoriti', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'Meghna Sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'Angie Andersen', 'Gabrielle Beck', 'Isabella Bartz', 'Jenn Rosado', 'Rachel Dolan', 'Anna Woodson', 'Suzie Hudgens', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Jannae Ailawadhi', 'Allie Harter', 'Ella Pitts', 'Arabella Savener', 'Diyaa Dossani', 'Hazel Wells', 'Maya Sajan', 'Ollie Mae Harrison', 'Mia Vasquez', 'Heidi Chapin', 'Haley Hooper', 'Hana Sawaf','Emily Robles']
CrochetKnitting = ['Amelia Klyap', 'Kirthi Gummadi', 'Delaney O’Brien', 'Krissily Estacio', 'Zoe Veliz', 'Lola Daffin', 'Sarah Thompson', 'Angie Andersen', 'Catalina Cruz', 'Katie Windell', 'Suzie Hudgens', 'Arabella Savener', 'Ava Dahlander', 'Haley Hooper', 'Abrielle Gallini']
Drawing = ['Piper Buck', 'Chloe Lim', 'Sophie Robins', 'Erika Sandberg', 'Riley Avery', 'Delaney O’Brien', 'Mae Trahan', 'Ellen Meltzer', 'Sarah Thompson', 'Angie Andersen', 'Bella Champion', 'Catalina Cruz', 'Jenn Rosado', 'Abby OGuynn', 'Regan Hill']
ExploringNewRestaurants = ['Sarah Sims', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'Madison Taylor', 'Kirthi Gummadi', 'Sophie Robins', 'Erika Sandberg', 'Riley Avery', 'Bailey Alsup', 'Anika Novak', 'Sarah Solomon', 'Liz Keegan', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Zoe Veliz', 'Sofie Arroyo', 'Emma Schneidau', 'Hannah Greenhill', 'Morgan Baumel', 'Audrey Cooper', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'Meghna Sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'Sarah Thompson', 'Angie Andersen', 'Bella Champion', 'Catalina Cruz', 'Jillian Taylor', 'Rachel Dolan', 'Anna Woodson', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Jannae Ailawadhi', 'Emmerich Benavides', 'Haylee Martin', 'Catherine Dooley', 'Ava Dahlander', 'Taylor Jennings', 'Riley Wanasek', 'Lindsay McCullough', 'Alice Hudson', 'Delaney Vanderpool', 'Elyse Miller', 'Sienna Shutts', 'Regan Hill', 'Caitlin Van Sant', 'Bella Anderson', 'Haley Hooper', 'Hana sawaf']
Formula1 = ['Sarah Sims', 'Liz Keegan', 'Brianna Salaices', 'Sarah Thompson', 'Carly Schmidt', 'Suzie Hudgens', 'Diyaa Dossani', 'Taylor Jennings', 'Regan Hill', 'Brooke Walker', 'Nids Pappu']
Governmentfun = ['Sarah Sims', 'Piper Buck', 'Chloe Lim', 'Abby Alsup', 'Jovanni Carrillo', 'Zoe Veliz', 'Hannah Greenhill', 'Morgan Baumel', 'Ellen Meltzer', 'Maya Abraham', 'Catalina Cruz', 'Ferzine Sanjana', 'Kaitlin Black', 'Arabella Savener', 'Riley Wanasek', 'Hailey Brooks', 'Bella Wernli', 'Heidi Chapin', 'Katie Walsh', 'Ellie Berman', 'Charlie Stone', 'Josey Mandrea', 'Aliyana Martinez', 'Aliyana Martinez']
GraphicDesign = ['Liz Keegan', 'Maya Abraham', 'Catalina Cruz', 'Carly Schmidt', 'Celeste Tomberlin']
Health = ['Shelby Williamson', 'Mazzy Bledsoe', 'Bailey Alsup', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Sofie Arroyo', 'Brianna Salaices', 'Megan Garza', 'Kamryn Jean', 'Sydney Fern', 'Lola Daffin', 'Bella Champion', 'Isabella Bartz', 'Abby Sanders', 'Rachel Dolan', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Emmerich Benavides', 'Hazel Wells', 'Maya Sajan', 'Lindsay McCullough', 'Alice Hudson', 'Abby Kant', 'Regan Hill', 'Caitlin Van Sant', 'Emerson Oliver', 'Josie Mandrea', 'Hana sawaf']
Instagram = ['Sarah Sims', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'Madison Taylor', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'Erika Sandberg', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Mae Trahan', 'Emma Schneidau', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'Georgia Key', 'Catherine Favoriti', 'Audrey Cooper', 'Sydney Fern', 'Meghna Sunkureddi', 'Maya Abraham', 'Katelyn Quintanilla', 'Angie Andersen', 'Bella Champion', 'Catalina Cruz', 'Isabella Bartz', 'Jillian Taylor', 'Ferzine Sanjana', 'Abby Sanders', 'Alyssa Bouloy', 'Jenn Rosado', 'Carly Schmidt', 'Kaitlin Black', 'Izzy Davies', 'Maria Sepulveda Salazar', 'Ella Pitts', 'Haylee Martin', 'Avery McClure', 'Diyaa Dossani', 'Hazel Wells', 'Maya Sajan', 'Ava Dahlander', 'Taylor Jennings', 'Alice Hudson', 'Elyse Miller', 'Sienna Shutts', 'Hailey Brooks', 'Celeste Tomberlin', 'Chasiti Tyeryar', 'Genesis Martinez', 'Emily Robles', 'Heidi Chapin', 'Regan Hill', 'Bella Anderson', 'Brooke Walker', 'Katie Walsh', 'Abrielle Gallini']
ListeningtoMusic = ['Sarah Sims', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'Madison Taylor', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'Zoe Alvarado', 'Erika Sandberg', 'Riley Avery', 'Bailey Alsup', 'Anika Novak', 'Delaney O’Brien', 'Liz Keegan', 'Ella Leininger', 'Kate Neiman', 'Larkin Seidel', 'Krissily Estacio', 'Mae Trahan', 'Kaylie Ngo', 'Brianna', 'Alexandra Nicholls', 'Valentina Markov', 'Zoe Veliz', 'Sofie Arroyo', 'Emma Schneidau', 'Marley Page', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'Georgia Key', 'Megan Garza', 'Catherine Favoriti', 'Audrey Cooper', 'Kamryn Jean', 'Meredith Moreland', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'Meghna Sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'Sarah Thompson', 'Angie Andersen', 'Gabrielle Beck', 'Bella Champion', 'Catalina Cruz', 'Jillian Taylor', 'Ferzine Sanjana', 'Jenn Rosado', 'Carly Schmidt', 'Rachel Dolan', 'Anna Woodson', 'Suzie Hudgens', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Jannae Ailawadhi', 'Allie Harter', 'Ella Pitts', 'Emmerich Benavides', 'Haylee Martin', 'Madeleine Mazingo', 'Avery McClure', 'Arabella Savener', 'Abby OGuynn', 'Catherine Dooley', 'Diyaa Dossani', 'Hazel Wells', 'Maya Sajan', 'Ollie Mae Harrison', 'Ava Dahlander', 'Taylor Jennings', 'Riley Wanasek', 'Lindsay McCullough', 'Delaney Vanderpool', 'Elyse Miller', 'Sienna Shutts', 'Hailey Brooks', 'Celeste Tomberlin', 'Abby Kant', 'Chasiti Tyeryar', 'Genesis Martinez', 'Heidi Chapin', 'Regan Hill', 'Bella Anderson', 'Katie Walsh', 'Emerson Oliver', 'Claire Savage', 'Jasmine Valdez', 'Josie Mandrea', 'Hana sawaf']
Musicals = ['Sarah Sims', 'Amelia Klyap', 'Sophie Robins', 'Zoe Alvarado', 'Liz Keegan', 'Krissily Estacio', 'Mae Trahan', 'Brianna', 'Alexandra Nicholls', 'Zoe Veliz', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'Katelyn Quintanilla', 'Isabella Bartz', 'Jillian Taylor', 'Ferzine Sanjana', 'Alyssa Bouloy', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Ella Pitts', 'Arabella Savener', 'Diyaa Dossani', 'Hazel Wells', 'Ava Dahlander', 'Delaney Vanderpool', 'Regan Hill', 'Emerson Oliver']
Pageants = ['Catalina Cruz']
Painting = ['Shelby Williamson', 'Piper Buck', 'Chloe Lim', 'Abby Alsup', 'Jovanni Carrillo', 'Sophie Robins', 'Riley Avery', 'Bailey Alsup', 'Ava Hurst', 'Ellen Meltzer', 'Meadow Votis', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'Sarah Thompson', 'Angie Andersen', 'Gabrielle Beck', 'Catalina Cruz', 'Haley Hooper']
Philosophyfun = ['Marley Page', 'Lola Daffin', 'Suzie Hudgens', 'Hailey Brooks', 'Sophie Shapiro,']
Photography = ['Amelia Klyap', 'Chloe Lim', 'Kirthi Gummadi', 'Jovanni Carrillo', 'Liz Keegan', 'Julia Lindstrom', 'Kaylie Ngo', 'Zoe Veliz', 'Marley Page', 'Ava Hurst', 'Jessica Paine', 'Lola Daffin', 'Maya Abraham', 'Sarah Thompson', 'Gabrielle Beck', 'Carly Schmidt', 'Kaitlin Black', 'Ava Dahlander', 'Lindsay McCullough', 'Elyse Miller', 'Sienna Shutts', 'Regan Hill', 'Bella Anderson', 'Abrielle Gallini', 'Josie Mandrea']
PlayingaBrassInstrument = ['Amelia Klyap', 'Suzie Hudgens']
PlayingaPercussionInstrument = ['Chloe Lim', 'Valentina Markov', 'Marley Page', 'Ava Hurst', 'Angie Andersen', 'Kaitlin Black', 'Maria Sepulveda Salazar', 'Arabella Savener', 'Abrielle Gallini']
PlayingaStringInstrument = ["Delaney O'Brien", 'Krissily Estacio', 'Marley Page', 'Lola Daffin', 'Gabrielle Beck', 'Madeleine Mazingo', 'Arabella Savener', 'Elyse Miller', 'Bella Wernli', 'Brooke Walker']
PlayingaWindInstrument = ['Kirthi Gummadi', 'Marley Page', 'Maya Abraham', 'Ferzine Sanjana']
Podcasts = ['Madison Taylor', 'Jovanni Carrillo', 'Erika Sandberg', 'Julia Lindstrom', 'Krissily Estacio', 'Sofie Arroyo', 'Marley Page', 'Kamryn Jean', 'Meredith Moreland', 'Sydney Fern', 'Jessica Paine', 'Maya Abraham', 'Katelyn Quintanilla', 'Jillian Taylor', 'Ferzine Sanjana', 'Anna Woodson', 'Izzy Davies', 'Taylor Jennings', 'Elyse Miller', 'Hailey Brooks', 'Bella Wernli', 'Emerson Oliver', 'Josie Mandrea']
PotteryCeramics = ['Shelby Williamson', 'Chloe Lim', 'Jovanni Carrillo', 'Riley Avery', 'Liz Keegan', 'Krissily Estacio', 'Meadow Votis', 'Lola Daffin', 'Maya Abraham', 'Angie Andersen', 'Katie Windell', 'Heidi Chapin', 'Aliyana Martinez']
Reading = ['Sarah Sims', 'Shelby Williamson', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'Zoe Alvarado', 'Bailey Alsup', 'Anika Novak', 'Liz Keegan', 'Kate Neiman', 'Krissily Estacio', 'Kaylie Ngo', 'Brianna', 'Zoe Veliz', 'Emma Schneidau', 'Georgia Key', 'Kamryn Jean', 'Ellen Meltzer', 'Sydney Fern', 'Jessica Paine', 'Lola Daffin', 'Maya Abraham', 'Sarah Thompson', 'Gabrielle Beck', 'Bella Champion', 'Isabella Bartz', 'Katie Windell', 'Jillian Taylor', 'Ferzine Sanjana', 'Alyssa Bouloy', 'Jenn Rosado', 'Carly Schmidt', 'Rachel Dolan', 'Anna Woodson', 'Suzie Hudgens', 'Kaitlin Black', 'Izzy Davies', 'Jannae Ailawadhi', 'Ella Pitts', 'Haylee Martin', 'Madeleine Mazingo', 'Arabella Savener', 'Diyaa Dossani', 'Hazel Wells', 'Maya Sajan', 'Ollie Mae Harrison', 'Mia Vasquez', 'Ava Dahlander', 'Taylor Jennings', 'Riley Wanasek', 'Delaney Vanderpool', 'Elyse Miller', 'Celeste Tomberlin', 'Abby Kant', 'Heidi Chapin', 'Regan Hill', 'Caitlin Van Sant', 'Bella Anderson', 'Nids Pappu', 'Abrielle Gallini']
RoadTrips = ['Sarah Sims', 'Abby Alsup', 'Sophie Robins', 'Mazzy Bledsoe', 'Zoe Alvarado', 'Erika Sandberg', 'Riley Avery', 'Bailey Alsup', 'Liz Keegan', 'Kaylie Ngo', 'Valentina Markov', 'Emma Schneidau', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'Georgia Key', 'Audrey Cooper', 'Kamryn Jean', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'Meghna Sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Gabrielle Beck', 'Bella Champion', 'Katie Windell', 'Jillian Taylor', 'Suzie Hudgens', 'Kaitlin Black', 'Izzy Davies', 'Jannae Ailawadhi', 'Ella Pitts', 'Emmerich Benavides', 'Haylee Martin', 'Diyaa Dossani', 'Mia Vasquez', 'Riley Wanasek', 'Delaney Vanderpool', 'Bella Wernli', 'Chasiti Tyeryar', 'Regan Hill', 'Ellie Berman', 'Abrielle Gallini', 'Hana sawaf']
ScienceMarineScienceEcology = ['Amelia Klyap', 'Julia Lindstrom', 'Krissily Estacio', 'Ellen Meltzer', 'Lola Daffin', 'Bella Champion', 'Anna Woodson', 'Izzy Davies', 'Madeleine Mazingo', 'Mia Vasquez', 'Regan Hill', 'Caitlin Van Sant', 'Hana Sawaf']
Scrapbooking = ['Shelby Williamson', 'Chloe Lim', 'Madison Taylor', 'Sophie Robins', 'Zoe Alvarado', 'Erika Sandberg', 'Anika Novak', 'Meadow Votis', 'Jessica Paine', 'Meghna Sunkureddi', 'Maya Abraham', 'Katelyn Quintanilla', 'Angie Andersen', 'Gabrielle Beck', 'Isabella Bartz', 'Delaney Vanderpool', 'Celeste Tomberlin', 'Haley Hooper']
Sewing = ['Jessica Paine','Meadow Votis','Celeste Tomberlin']
Shopping = ['Sarah Sims', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'Madison Taylor', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'Zoe Alvarado', 'Riley Avery', 'Anika Novak', 'Liz Keegan', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Kaylie Ngo', 'Alexandra Nicholls', 'Zoe Veliz', 'Sofie Arroyo', 'Emma Schneidau', 'Marley Page', 'Ava Hurst', 'Hannah Greenhill', 'Brianna Salaices', 'Georgia Key', 'Catherine Favoriti', 'Audrey Cooper', 'Kamryn Jean', 'Meredith Moreland', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'Meghna Sunkureddi', 'Maya Abraham', 'Katelyn Quintanilla', 'Gabrielle Beck', 'Bella Champion', 'Catalina Cruz', 'Isabella Bartz', 'Jillian Taylor', 'Ferzine Sanjana', 'Alyssa Bouloy', 'Jenn Rosado', 'Rachel Dolan', 'Anna Woodson', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Jannae Ailawadhi', 'Ella Pitts', 'Emmerich Benavides', 'Madeleine Mazingo', 'Avery McClure', 'Catherine Dooley', 'Maya Sajan', 'Taylor Jennings', 'Riley Wanasek', 'Lindsay McCullough', 'Elyse Miller', 'Sienna Shutts', 'Bella Wernli', 'Celeste Tomberlin', 'Chasiti Tyeryar', 'Emily Robles', 'Heidi Chapin', 'Regan Hill', 'Caitlin Van Sant', 'Bella Anderson', 'Jasmine Valdez', 'Abrielle Gallini', 'Josie Mandrea', 'Aliyana Martinez']
Singing = ['Chloe Lim', 'Liz Keegan', 'Krissily Estacio', 'Kaylie Ngo', 'Valentina Markov', 'Marley Page', 'Ava Hurst', 'Catherine Favoriti', 'Ellen Meltzer', 'Meadow Votis', 'Jessica Paine', 'Katelyn Quintanilla', 'Jenn Rosado', 'Kaitlin Black', 'Arabella Savener', 'Diyaa Dossani', 'Maya Sajan', 'Ava Dahlander', 'Regan Hill', 'Bella Anderson', 'Katie Walsh', 'Emerson Oliver']
Skincare = ['Sarah Sims', 'Chloe Lim', 'Madison Taylor', 'Jovanni Carrillo', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Kaylie Ngo', 'Emma Schneidau', 'Gabrielle Green', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'Georgia Key', 'Megan Garza', 'Catherine Favoriti', 'Audrey Cooper', 'Kamryn Jean', 'Meredith Moreland', 'Ellen Meltzer', 'Jessica Paine', 'Meghna Sunkureddi', 'Lola Daffin', 'Bella Champion', 'Catalina Cruz', 'Isabella Bartz', 'Jillian Taylor', 'Rachel Dolan', 'Izzy Davies', 'Maria Sepulveda Salazar', 'Ella Pitts', 'Avery McClure', 'Hazel Wells', 'Maya Sajan', 'Ollie Mae Harrison', 'Ava Dahlander', 'Taylor Jennings', 'Lindsay McCullough', 'Abby Kant', 'Emily Robles', 'Heidi Chapin', 'Caitlin Van Sant', 'Jasmine Valdez', 'Josie Mandrea']
SocialMedia = ['Sarah Sims', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'Madison Taylor', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'Erika Sandberg', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Mae Trahan', 'Emma Schneidau', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'Georgia Key', 'Catherine Favoriti', 'Audrey Cooper', 'Sydney Fern', 'Meghna Sunkureddi', 'Maya Abraham', 'Katelyn Quintanilla', 'Angie Andersen', 'Bella Champion', 'Catalina Cruz', 'Isabella Bartz', 'Jillian Taylor', 'Ferzine Sanjana', 'Abby Sanders', 'Alyssa Bouloy', 'Jenn Rosado', 'Carly Schmidt', 'Kaitlin Black', 'Izzy Davies', 'Maria Sepulveda Salazar', 'Ella Pitts', 'Haylee Martin', 'Avery McClure', 'Diyaa Dossani', 'Hazel Wells', 'Maya Sajan', 'Ava Dahlander', 'Taylor Jennings', 'Alice Hudson', 'Elyse Miller', 'Sienna Shutts', 'Hailey Brooks', 'Celeste Tomberlin', 'Chasiti Tyeryar', 'Genesis Martinez', 'Emily Robles', 'Heidi Chapin', 'Regan Hill', 'Bella Anderson', 'Brooke Walker', 'Katie Walsh', 'Abrielle Gallini']
VideoGames = ['Sarah Sims','Krissily Estacio','Angie Angersen','Arabella Savener','Sarah Solomon','Bella Champion']
Vlogging = ['Piper Buck', 'Madison Taylor', 'Sophie Robins', 'Kate Neiman', 'Catherine Favoriti', 'Katelyn Quintanilla', 'Catalina Cruz', 'Jillian Taylor', 'Carly Schmidt', 'Anna Woodson', 'Emily Robles', 'Regan Hill', 'Brooke Walker', 'Nids Pappu']
WatchingSports = ['Julia Lindstrom']
WatchingTVMovies = ['Julia Lindstrom']
Writing = ['Sarah Sims', 'Chloe Lim', 'Kate Neiman', 'Marley Page', 'Ellen Meltzer', 'Jessica Paine', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'Isabella Bartz', 'Kaitlin Black', 'Diyaa Dossani', 'Elyse Miller', 'Bella Wernli', 'Bella Anderson', 'Katie Walsh', 'Ellie Berman']
Karaoke = ['Morgan Baumel']
Plants = ['Morgan Baumel']
RollerCoasters = ['Morgan Baumel']

# SUMMER CAMPS
AHECScienceSummerCamp = ['Maria Sepulveda Salazar']
AllStarsSportsCamp = ['Regan Hill']
BrookhillRanchCamp = ['Sydney Fern']
CampAllen = ['Emerson Oliver']
CampAlonim = ['Hailey Brooks']
CampBalconesSprings = ['Jessica Paine']
CampChoYeh = ['Erika Sandberg', 'Audrey Cooper']
CampEagle = ['Meadow Votis']
CampFireCamp = ['Angie Andersen']
CampHoneyCreek = ['Gabrielle Beck']
CampOzark = ['Catherine Favoriti', 'Mae Trahan', 'Madeleine Mazingo', 'Sophie Shapiro']
CampRamahintheBerkshires = ['Ellie Berman']
CampTallowood = ['Abby OGuynn']
CampWaldemar = ['Sienna Shutts', 'Krissily Estacio', 'Emerson Oliver', 'Heidi Chapin']
ChurchCamp = ['Emily Robles']
FrostValleyYMCA = ['Amelia Klyap']
FueledbyEnvision = ['Madeleine Mazingo']
GrammyCamp = ['Liz Keegan']
HinduHeritageYouthCamp = ['Meghna Sunkureddi']
KidsActing = ['Regan Hill']
PalaceTheatre = ['Regan Hill']
PineCove = ['Bailey Alsup', 'Abby Alsup']
RiceELITETechCamp = ['Madeleine Mazingo']
RiceUniversityAerospaceandAviationAcademy = ['Madeleine Mazingo']
RioGrandeSocietySummerCamp = ['Maria Sepulveda Salazar']
RockyRiverRanch = ['Avery McClure']
SierraVista = ['Meredith Moreland']
SkillsUSATexasLeadershipCamp = ['Sienna Shutts']
SkyRanch = ['Ava Dahlander', 'Diyaa Dossani']
StMaryComputerScienceCamp = ['Maria Sepulveda Salazar']
TCUTennisCamp = ['Angie Andersen']
TexasAMStemCamp = ['Madeleine Mazingo']
UTLatinAmericanStudies = ['Maria Sepulveda Salazar']
UCBerkeleyMET = ['Nids Pappu']
UniversityofDallasComputerScienceCamp = ['Maria Sepulveda Salazar']
UTAustinNursingCamp = ['Maria Sepulveda Salazar']
WetandWildCamp = ['Regan Hill']
LakeoftheWoods = ['Josie Mandrea']
CLTC = ['Josie Mandrea']
BBYO = ['Josie Mandrea']

# NICHE INTERESTS
Astrology = ['Genesis Martinez']
Balloons = ['Krissily Estacio', 'Delaney Vanderpool']
SelfCare = ['Emily Robles']
LineDancing = ['Abrielle Gallini', 'Ella Pitts']
Dachsunds = ['Meredith Moreland']
Documentaries = ['Meredith Moreland', 'Sarah Thompson']
GoingtoBibleStudies = ['Abby Alsup']
EMT = ['Brianna Salaices']
FilmCameras = ['Ava Hurst']
Beach = ['Karlie Haigood']
CollegeFootball = ['Megan Garza', 'Mazzy Bledsoe', 'Emerson Oliver']
Cycling = ['Karli Haigood']
Guitar = ['Elyse Miller']
Trivia = ['Bella Wernli', 'Claire Savage']
HistoryNerd = ['Bella Wernli', 'Kamryn Jean', 'Emerson Oliver', 'Anika Novak']
PassionateAboutSports = ['Katie Walsh']
TaylorSwift = ['Katie Walsh', 'Mazzy Bledsoe', 'Larkin Seidel']
MissTexasCompetition = ['Heidi Chapin']
CrossStitching = ['Abby Sanders']
ObsessedwithMedicine = ['Hazel Wells']
GreysAnatomy = ['Hazel Wells', 'Mazzy Bledsoe']
Goodreads = ['Hazel Wells']
Letterboxd = ['Hazel Wells']
ConspiracyTheories = ['Hazel Wells']
TrueCrime = ['Hazel Wells', 'Rachel Dolan', 'Taylor Jennings', 'Ella Leininger']
PopCulture = ['Hazel Wells', 'Hannah Greenhill']
HarryPotter = ['Hazel Wells']
MammaMiatheMusical = ['Shelby Williamson']
VampireDiaries = ['Shelby Williamson']
TheSummerITurnedPretty = ['Shelby Williamson']
FunHairstyles = ['Jessica Paine']
MusicHistory = ['Delaney Oâ€™Brien']
Cats = ['Catalina Cruz', 'Madison Taylor']
Pinterest = ['Catalina Cruz', 'Madison Taylor']
CleanGirlAesthetic = ['Catalina Cruz']
LoveshackFancy = ['Catalina Cruz']
RunwayModeling = ['Catalina Cruz']
EventPlanning = ['Haylee Martin', 'Ellen Meltzer']
ThemeParks = ['Haylee Martin', 'Ollie Mae Harrison', 'Morgan Baumel']
FriendsTVShow = ['Abby OGuynn']
RealityTV = ['Abby Oguynn', 'Riley Avery']
Xbox = ['Piper Buck', 'Angie Andersen']
TheHungerGames = ['Sarah Sims']
LegendofZelda = ['Sarah Sims']
LittleWomen = ['Sarah Sims']
PrideandPrejudice = ['Sarah Sims']
Meteorology = ['Gabrielle Beck']
HouseandEDMMusic = ['Catherine Favoriti', 'Nids Pappu']
Puzzles = ['Bella Anderson', 'Katie Windell', 'Haley Hooper']
PassionateAboutHealthcare = ['Maria Sepulveda Salazar']
Dogs = ['Maria Sepulveda Salazar']
LizzyMcAlpine = ['Mazzy Bledsoe']
Finneas = ['Mazzy Bledsoe']
Seattle = ['Mazzy Bledsoe']
LeonBridges = ['Mazzy Bledsoe']
OwnsEtsyShop = ['Mazzy Bledsoe']
PearlJam = ['Mazzy Bledsoe']
FrenchBulldogs = ['Mazzy Bledsoe']
Crepes = ['Mazzy Bledsoe']
Foodie = ['Mazzy Bledsoe']
GossipGirl = ['Mazzy Bledsoe']
Chipotle = ['Mazzy Bledsoe']
Flowers = ['Mazzy Bledsoe', 'Madison Taylor']
GilmoreGirls = ['Mazzy Bledsoe']
TexasRoadhouse = ['Mazzy Bledsoe']
ScreamMovies = ['Zoe Veliz']
Marvel = ['Zoe Veliz', 'Liz Keegan', 'Aliyana Martinez']
NewGirl = ['Zoe Veliz']
LovesTalkingAboutArchitecture = ['Chloe Lim']
Coloring = ['Taylor Jennings']
RealHousewives = ['Taylor Jennings']
VanderpumpRules = ['Taylor Jennings']
MusicalComposition = ['Marley Page']
ArchitecturalDesign = ['Marley Page']
CreativeWriting = ['Marley Page', 'Kate Neiman']
Cinematography = ['Marley Page']
Fashion = ['Marley Page', 'Celeste Tomberlin', 'Regan Hill', 'Kate Peters']
KPop = ['Mae Trahan', 'Isabella Bartz']
Pets = ['Abby Kant']
Harmonica = ['Audrey Cooper', 'Maya Abraham']
Pizookies = ['Anna Woodson']
PlayingCards = ['Erika Sandberg']
Sailing = ['Ellen Meltzer']
Space = ['Madeleine Mazingo']
Sims = ['Madeleine Mazingo', 'Kate Neiman', 'Bailey Alsup']
WomenEmpowerment = ['Madeleine Mazingo']
Minecraft = ['Madeleine Mazingo', 'Kate Neiman']
Hamilton = ['Sophie Robins']
HorrorMovies = ['Kate Neiman', 'Isabella Bartz']
InteriorDesign = ['Kate Neiman']
SportsMedicine = ['Emerson Oliver']
USHistory = ['Emerson Oliver']
WWIandII = ['Emerson Oliver']
Sustainability = ['Riley Avery']
Makeup = ['Larkin Seidel']
TexasBaseball = ['Bailey Alsup']
IceHockey = ['Liz Keegan']
Fortnite = ['Angie Andersen', 'Rishona Mopur']
SpiderMan = ['Angie Andersen']
Deadpool = ['Angie Andersen']
MiraculousLadybug = ['Angie Andersen']
ActionMovies = ['Angie Andersen']
HighSchoolMascot = ['Angie Andersen']
Pastries = ['Maggie Shaw']
Skydiving = ['Nids Pappu']
BungeeJumping = ['Nids Pappu']
NBAFan = ['Nids Pappu']
CreatingRecipes = ['Nids Pappu']
Bedazzling = ['Madison Taylor']
Depop = ['Madison Taylor']
HoustonRodeo = ['Madison Taylor']
CollectingRubberDucks = ['Madison Taylor']
TraderJoes = ['Madison Taylor']
Astros = ['Madison Taylor']
BraceletMaking = ['Jenn Rosado']
HarryStyles = ['Jenn Rosado']
Powerlifting = ['Julia Lindstrom']
EqualityinWomensSports = ['Hailey Brooks']
Harmonica = ['Audrey Cooper', 'Maya Abraham']
Hayday = ['Suzie Hudgens']
MarioKart = ['Arabella Savener']
SmashBros = ['Arabella Savener']
AnimalCrossing = ['Arabella Savener']
LoveIsland = ['Izzy Davies']
Roblox = ['Charlie Stone', 'Rishona Mopur', 'Rishona Mopur']
Disney = ['Morgan Baumel']
StudyAbroad = ['Morgan Baumel']
StarWars = ['Morgan Baumel', 'Aliyana Martinez']
GoingtotheZoo = ['Haley Hooper']
NYTGames = ['Haley Hooper']
Legos = ['Aliyana Martinez']
StudyAbroad = ['Marley Page','Catherine Favoriti','Zoe Alvarado','Brianna Salaices','Piper Buck','Morgan Baumel','Alexandra Nicholls','Heidi Chapin','Bailey Alsup','Meghna Sunkureddi']

# TRANSFERS
UTEP = ['Catalina Cruz']
UTSA = ['Emma Schneidau', 'Erika Sandberg', 'Maya Abraham', 'Alyssa Bouloy']

# Dictionaries mapping interest name → list of people
majors = {
    "Advertising Major": Advertising,
    "Aerospace Engineering Major": AerospaceEngineering,
    "Anthropology Major": Anthropology,
    "Applied Movement Science Major": AppliedMovementScience,
    "Architecture Major": Architecture,
    "BFA Acting Major": BFAActing,
    "Behavioral And Social Data Science Major": BehavioralAndSocialDataScience,
    "Bilingual Education Major": BilingualEducation,
    "Biochemistry Major": Biochemistry,
    "Biology Major": Biology,
    "Microbiology And Infectious Diseases Major": MicrobiologyAndInfectiousDiseases,
    "Biomedical Engineering Major": BiomedicalEngineering,
    "Business Major": Business,
    "Business Honors Major": BusinessHonors,
    "Finance Major": Finance,
    "Civil Engineering Major": CivilEngineering,
    "Communication And Leadership Major": CommunicationAndLeadership,
    "Computer Science Major": ComputerScience,
    "Corporate Communications Major": CorporateCommunications,
    "ESL Generalist Early Childhood Major": ESLGeneralistEarlyChildhood,
    "Early Childhood Education Major": EarlyChildhoodEducation,
    "Economics Major": Economics,
    "English Major": English,
    "Environmental Engineering Major": EnvironmentalEngineering,
    "French Studies Major": FrenchStudies,
    "Geosystems Engineering Major": GeosystemsEngineering,
    "Government Major": Government,
    "Health Promotion And Behavioral Science Major": HealthPromotionAndBehavioralScience,
    "Health And Society Major": HealthAndSociety,
    "Human Biology Major": HumanBiology,
    "Human Development And Family Sciences Major": HumanDevelopmentAndFamilySciences,
    "Human Dimensions Of Organization Major": HumanDimensionsOfOrganization,
    "International Relations And Global Studies Major": InternationalRelationsAndGlobalStudies,
    "Journalism Major": Journalism,
    "Kinesiology Exercise Science Major": KinesiologyExerciseScience,
    "Mathematics Major": Mathematics,
    "Mechanical Engineering Major": MechanicalEngineering,
    "Music And Media Major": MusicAndMedia,
    "Neuroscience Major": Neuroscience,
    "Nursing Major": Nursing,
    "Physics Major": Physics,
    "Political Communications Major": PoliticalCommunications,
    "Psychology Major": Psychology,
    "Public Relations Major": PublicRelations,
    "RTF Major": RTF,
    "Sociology Major": Sociology,
    "Special Education Major": SpecialEducation,
    "Speech Language And Hearing Sciences Major": SpeechLanguageAndHearingSciences,
    "Sports Management Major": SportsManagement,
    "Theatre Education Major": TheatreEducation,
    "Undeclared Major": Undeclared,
    "Writing And Rhetoric Major": WritingAndRhetoric,
    "Korean Major": Korean,
    "Social And Behavioral Sciences Major": SocialAndBehavioralSciences,
    "Analytics And Business Of Sports Major": AnalyticsAndBusinessOfSports,
    "Youth And Community Studies Major": YouthAndCommunityStudies,
    "Jewish Studies Major": JewishStudies,
    "Political Science Major": PoliticalScience,
    "Textiles And Apparel Major": TextilesAndApparel
}

minors = {
    "Business Minor": BusinessMinor,
    "Business And Public Policy Minor": BusinessAndPublicPolicyMinor,
    "Religious Studies Minor (Christian)": ReligiousStudiesMinor,
    "Stats And Data Science Minor": StatsandDataScienceMinor,
    "Creative Writing Minor": CreativeWritingMinor,
    "Korean Minor": KoreanMinor,
    "Chinese Minor": ChineseMinor,
    "Health Professions Minor": HealthProfessionsMinor,
    "Communicating Social Issues Minor": CommunicatingSocialIssuesMinor,
    "Communication Studies Minor": CommunicationStudiesMinor,
    "Computer Science Minor": ComputerScienceMinor,
    "Criminal Law, Justice, And Inequality Bridging Disciplines Program Minor": CriminalLawJusticeandInequalityBridgingDisciplinesProgramMinor,
    "Design Strategies Minor": DesignStrategiesMinor,
    "Educational Psychology Minor": EducationalPsychologyMinor,
    "Entrepreneurship Minor": EntrepreneurshipMinor,
    "Finance Minor": FinanceMinor,
    "French Minor": FrenchMinor,
    "Global Communications Minor": GlobalCommunicationsMinor,
    "Ethics And Leadership In Law, Government, and Politics Minor": EthicsAndLeadershipInLawGovernmentandPoliticsMinor,
    "Global ManagementMinor": GlobalManagementMinor,
    "Government Minor": GovernmentMinor,
    "Health Reform and Innovation Minor": HealthReformandInnovationMinor,
    "Health Communications Minor": HealthCommunicationsMinor,
    "Healthcare Reform And Innovation Minor": HealthcareReformAndInnovationMinor,
    "Interior Design Minor": InteriorDesignMinor,
    "Italian Minor": ItalianMinor,
    "Jefferson Scholar CTI Minor": JeffersonScholarCTIMinor,
    "Kinesiology Minor": KinesiologyMinor,
    "Law Justice And Society Minor": LawJusticeAndSocietyMinor,
    "Media And Entertainment Industries Minor": MediaAndEntertainmentIndustriesMinor,
    "Physicians Assistant Minor": PhysiciansAssistantMinor,
    "Patients Practitioners And Care Minor": PatientsPractitionersAndCareMinor,
    "Pre Health Minor": PreHealthMinor,
    "Professional Sales And Business Development Minor": ProfessionalSalesAndBusinessDevelopmentMinor,
    "Social And Behavioral Sciences Minor": SocialAndBehavioralSciencesMinor,
    "Sports Production and Broadcast Minor": SportsProductionandBroadcastMinor,
    "Spanish for Medical Professions Minor": SpanishforMedicalProfessionsMinor,
    "Business Spanish Minor": BusinessSpanishMinor,
    "Fitness and Rehab Specialization Minor": FitnessandRehabSpecializationMinor,
    "Pre-Med Minor": PremedMinor,
    "Pre-Health Dental Minor": PreHealthDentalMinor,
    "Professional Sales Minor": ProfessionalSalesMinor,
    "Risk Management Statistics Minor": RiskManagementStatisticsMinor,
    "Spanish Minor": SpanishMinor
}

college = {
    "Cockrell School of Engineering": CockrellSchoolofEngineering,
    "College of Education": CollegeofEducation,
    "College of Fine Arts": CollegeofFineArts,
    "College of Liberal Arts": CollegeofLiberalArts,
    "College of Natural Sciences": CollegeofNaturalSciences,
    "McCombs School of Business": McCombsSchoolofBusiness,
    "Moody College of Communication": MoodyCollegeofCommunication,
    "School of Architecture": SchoolofArchitecture,
    "School of Nursing": SchoolofNursing,
    "Jackson School of Geosciences": JacksonSchoolofGeosciences,
    "Pre-Med": PreMed,
    "Pre-Law": PreLaw,
    "Pre-Pharmacy": PrePharmacy
}

hometowns = {
    "Arlington, TX": ArlingtonTX,
    "Arlington, VA": ArlingtonVA,
    "Austin, TX": AustinTX,
    "Bee Cave, TX": BeeCaveTX,
    "Belton, TX": BeltonTX,
    "Boerne, TX": BoerneTX,
    "Burleson, TX": BurlesonTX,
    "Cleburne, TX": CleburneTX,
    "College Station, TX": CollegeStationTX,
    "Colleyville, TX": ColleyvilleTX,
    "Corpus Christi, TX": CorpusChristiTX,
    "Dallas, TX": DallasTX,
    "Danville, CA": DanvilleCA,
    "Dayton, OH": DaytonOH,
    "Eagle Pass, TX": EaglePassTX,
    "El Paso, TX": ElPasoTX,
    "Friendswood, TX": FriendswoodTX,
    "Frisco, TX": FriscoTX,
    "Garden City, NY": GardenCityNY,
    "Grapevine, TX": GrapevineTX,
    "Houston, TX": HoustonTX,
    "Humble, TX": HumbleTX,
    "Irving, TX": IrvingTX,
    "Jupiter, FL": JupiterFL,
    "Katy, TX": KatyTX,
    "Laredo, TX": LaredoTX,
    "Leander, Tx": LeanderTx,
    "Liberty Hill, TX": LibertyHillTX,
    "Longview, TX": LongviewTX,
    "Los Angeles, CA": LosAngelesCA,
    "Lubbock, TX": LubbockTX,
    "Mansfield, TX": MansfieldTX,
    "McAllen, TX": McAllenTX,
    "Mckinney, TX": MckinneyTX,
    "Missouri City, TX": MissouriCityTX,
    "New Braunfels, TX": NewBraunfelsTX,
    "New York, NY": NewYorkNY,
    "Pearland, TX": PearlandTX,
    "Pleasanton, CA": PleasantonCA,
    "Richardson, TX": RichardsonTX,
    "Rockwall, TX": RockwallTX,
    "Round Rock, TX": RoundRockTX,
    "Sacramento, CA": SacramentoCA,
    "San Antonio, TX": SanAntonioTX,
    "Honolulu, Hawaii": HonoluluHawaii,
    "Seabrook, TX": SeabrookTX,
    "Seattle, WA": SeattleWA,
    "Snoqualmie, WA": SnoqualmieWA,
    "Somers, NY": SomersNY,
    "Spring, TX": SpringTX,
    "Sugar Land, TX": SugarLandTX,
    "Texarkana, TX": TexarkanaTX,
    "The Woodlands, TX": TheWoodlandsTX,
    "Westfield, NJ": WestfieldNJ,
    "Pleasanton, CA": PleasantonCA,
    "Pensacola, FL": PensacolaFL,
    "Fort Worth, TX": FortWorthTX,
    "Northbrook, IL": NorthbrookIL,
    "Lufkin, TX": LufkinTX,
    "New Canaan, CT": NewCanaanCT
}

schools = {
    "Alvarado High School": AlvaradoHighSchool,
    "Alvin High School": AlvinHighSchool,
    "Amador Valley High School": AmadorValleyHighSchool,
    "Arlington High School": ArlingtonHighSchool,
    "Atascocita High School": AtascocitaHighSchool,
    "Belton High School": BeltonHighSchool,
    "Bishop Dunne Catholic School": BishopDunneCatholicSchool,
    "Boerne High School": BoerneHighSchool,
    "Booker T Washington HSPVA": BookerTWashingtonHSPVA,
    "Bowie High School": BowieHighSchool,
    "Brooklyn Technical High School": BrooklynTechnicalHighSchool,
    "Calabasas High School": CalabasasHighSchool,
    "Calallen High School": CalallenHighSchool,
    "Cedar Park High School": CedarParkHighSchool,
    "Centennial High School": CentennialHighSchool,
    "Clear Creek Highschool": ClearCreekHighschool,
    "Clear Falls High School": ClearFallsHighSchool,
    "Cleburne High School": CleburneHighSchool,
    "College Station High School": CollegeStationHighSchool,
    "Colleyville Heritage High School": ColleyvilleHeritageHighSchool,
    "Duchesne Academy of the Sacred Heart": DuchesneAcademyoftheSacredHeart,
    "Eagle Pass High School": EaglePassHighSchool,
    "East View High School": EastViewHighSchool,
    "Eastside Catholic High School": EastsideCatholicHighSchool,
    "Elkins High School": ElkinsHighSchool,
    "HeightsHigh School": HeightsHighSchool,
    "Fort Bend Christian Academy": FortBendChristianAcademy,
    "Franklin High School": FranklinHighSchool,
    "Frenship Highschool": FrenshipHighschool,
    "Friendswood High School": FriendswoodHighSchool,
    "Frisco Memorial High School": FriscoMemorialHighSchool,
    "Ft. Bend Travis High School": FtBendTravisHighSchool,
    "Fulshear High School": FulshearHighSchool,
    "Garden City High School": GardenCityHighSchool,
    "Georgetown Day School": GeorgetownDaySchool,
    "Regents High School": RegentsHighSchool,
    "Glenn High School": GlennHighSchool,
    "Liberal Arts and Science Academy": LiberalArtsandScienceAcademy,
    "Granite Bah High School": GraniteBahHighSchool,
    "Guyer High School": GuyerHighSchool,
    "Heights High School": HeightsHighSchool,
    "Hillcrest High School": HillcrestHighSchool,
    "Houston Academy for International Studies": HoustonAcademyforInternationalStudies,
    "Incarnate Word High School (san antonio)": IncarnateWordHighSchoolsanantonio,
    "Incarnate Word Academy (htx)": IncarnateWordAcademyhtx,
    "Independence High School": IndependenceHighSchool,
    "J.J. Pearce High School": JJPearceHighSchool,
    "James Bowie High School": JamesBowieHighSchool,
    "James E Taylor High School": JamesETaylorHighSchool,
    "Judson High School": JudsonHighSchool,
    "Klein High School": KleinHighSchool,
    "Lake Travis High School": LakeTravisHighSchool,
    "Lamar High School": LamarHighSchool,
    "Liberty Creek High School": LibertyCreekHighSchool,
    "Liberty High School": LibertyHighSchool,
    "Liberty Hill High School": LibertyHillHighSchool,
    "Louis D. Brandeis High School": LouisDBrandeisHighSchool,
    "Lutheran South Academy": LutheranSouthAcademy,
    "Mansfield High School": MansfieldHighSchool,
    "Mary Carroll High School": MaryCarrollHighSchool,
    "McNeil High School": McNeilHighSchool,
    "Mckinney High School": MckinneyHighSchool,
    "Memorial High School": MemorialHighSchool,
    "Monte Vista High School": MonteVistaHighSchool,
    "Monterey High School": MontereyHighSchool,
    "Mount Si High School": MountSiHighSchool,
    "NYC Lab School": NYCLabSchool,
    "NYOS Charter School": NYOSCharterSchool,
    "New Braunfels High School": NewBraunfelsHighSchool,
    "Northern Highlands": NorthernHighlands,
    "Oakwood High School": OakwoodHighSchool,
    "Pearland High School": PearlandHighSchool,
    "Pine Tree High School": PineTreeHighSchool,
    "Prosper High School": ProsperHighSchool,
    "Ridge Point High School": RidgePointHighSchool,
    "Rock Hill High School": RockHillHighSchool,
    "Rockwall High School": RockwallHighSchool,
    "Rockwall-Heath High School": RockwallHeathHighSchool,
    "S.P. Waltrip High School": SPWaltripHighSchool,
    "Saint Mary's Hall": SaintMarysHall,
    "Smithson Valley High School": SmithsonValleyHighSchool,
    "Somers High School": SomersHighSchool,
    "St. Agnes Academy": StAgnesAcademy,
    "Stratford High School": StratfordHighSchool,
    "Summer Creek High School": SummerCreekHighSchool,
    "TMI Episcopal": TMIEpiscopal,
    "Texas High School": TexasHighSchool,
    "The Woodlands College Park": TheWoodlandsCollegePark,
    "Tom C. Clark High School": TomCClarkHighSchool,
    "Tomball High School": TomballHighSchool,
    "Tompkins High School": TompkinsHighSchool,
    "United High School": UnitedHighSchool,
    "Uplift North Hills Preparatory": UpliftNorthHillsPreparatory,
    "Ursuline Academy of Dallas": UrsulineAcademyofDallas,
    "Valley View High School": ValleyViewHighSchool,
    "Vandegrift High School": VandegriftHighSchool,
    "W T White High School": WTWhiteHighSchool,
    "Warren High School": WarrenHighSchool,
    "Washington-Liberty High School": WashingtonLibertyHighSchool,
    "Westfield High School": WestfieldHighSchool,
    "Westlake High School": WestlakeHighSchool,
    "William T. Dwyer High School": WilliamTDwyerHighSchool,
    "Woodrow Wilson High School": WoodrowWilsonHighSchool,
    "Klein Oak High School": KleinOakHighSchool,
    "Langham Creek High School": LanghamCreekHighSchool,
    "Glenbrook North High School": GlenbrookNorthHighSchool,
    "Coppell High School": CoppellHighSchool,
    "Jersey Village High School": JerseyVillageHighSchool,
    "Episcopal High School": EpiscopalHighSchool,
    "New Canaan High School": NewCanaanHighSchool
}

extras = {
    "A Cappella": ACappella,
    "ASB": ASB,
    "ASL Club": ASLClub,
    "Elementary School Student Teaching": ElementarySchoolStudentTeaching,
    "BETA Club": BETAClub,
    "Band": Band,
    "Best Buddies": BestBuddies,
    "Book Club": BookClub,
    "Booster Club": BoosterClub,
    "Cheer": Cheer,
    "Choir": Choir,
    "Color Guard": ColorGuard,
    "Distributive Education Clubs of America (DECA)": DistributiveEducationClubsofAmericaDECA,
    "DoSomething!": DoSomething,
    "English Honor Society  (NEHS)": EnglishHonorSocietyNEHS,
    "Family Career and Community Leader of America (FCCLA)": FamilyCareerandCommunityLeaderofAmericaFCCLA,
    "Fellowship of Christian Athletes (FCA)": FellowshipofChristianAthletesFCA,
    "Feminism/Gender Equality Club": FeminismGenderEqualityClub,
    "Film Club": FilmClub,
    "Formula Club": FormulaClub,
    "French Club": FrenchClub,
    "Future Farmers of America (FFA)": FutureFarmersofAmericaFFA,
    "GIS": GIS,
    "Gay Straight Alliance Club": GayStraightAllianceClub,
    "Genetics and Neuroscience Club": GeneticsandNeuroscienceClub,
    "Geography Club": GeographyClub,
    "Girl Scouts": GirlScouts,
    "Health Occupations Students of America (HOSA)": HealthOccupationsStudentsofAmericaHOSA,
    "IB Program": IBProgram,
    "International Thespian Society (ITS)": InternationalThespianSocietyITS,
    "JROTC": JROTC,
    "Keep Texas Beautiful": KeepTexasBeautiful,
    "Key Club": KeyClub,
    "Latin Club": LatinClub,
    "Latinos Unidos": LatinosUnidos,
    "Leo Club": LeoClub,
    "Mock Trial": MockTrial,
    "Model UN": ModelUN,
    "National Charity League (NCL)": NationalCharityLeagueNCL,
    "Newspaper/Journalism Club": NewspaperJournalismClub,
    "Orchestra": Orchestra,
    "Peer Assistance Leadership and Service (PALS)": PeerAssistanceLeadershipandServicePALS,
    "Photography Club": PhotographyClub,
    "Piano": Piano,
    "Psychology Club": PsychologyClub,
    "Pups for People": PupsforPeople,
    "Quill and Scroll Honor Society": QuillandScrollHonorSociety,
    "Red Cross": RedCross,
    "Robotics/Computer Science Club": RoboticsComputerScienceClub,
    "Science Olympiad": ScienceOlympiad,
    "Service Council": ServiceCouncil,
    "Skills USA": SkillsUSA,
    "Speech and Debate Club": SpeechandDebateClub,
    "Student Athletic Council": StudentAthleticCouncil,
    "Student Athletic Trainer": StudentAthleticTrainer,
    "Student Council (STUCO)": StudentCouncilSTUCO,
    "Student Voter Empowerment Club": StudentVoterEmpowermentClub,
    "TEDX": TEDX,
    "Theatre": Theatre,
    "Tutoring/Peer Mentoring Program": TutoringPeerMentoringProgram,
    "University Interscholastic League (UIL)": UniversityInterscholasticLeagueUIL,
    "We Care Club": WeCareClub,
    "Wellness Council": WellnessCouncil,
    "Women in STEM": WomeninSTEM,
    "Yearbook Club": YearbookClub,
    "Younglife": Younglife,
    "Zonta Z Club": ZontaZClub,
    "Academic Decathlon": AcademicDecathlon,
    "Class President": ClassPresident,
    "Israeli Culture Club": IsraeliCultureClub,
    "Rotary Interact Club": RotaryInteractClub,
    "Athletic Training": AthleticTraining,
    "Ballet": Ballet,
    "Basketball": Basketball,
    "Boxing": Boxing,
    "Cross Country": CrossCountry,
    "Dance Team": DanceTeam,
    "Drill Team": DrillTeam,
    "Field Hockey": FieldHockey,
    "Figure Skating": FigureSkating,
    "Flag Football": FlagFootball,
    "Golf": Golf,
    "Lacrosse": Lacrosse,
    "Rock Climbing": RockClimbing,
    "Rowing": Rowing,
    "Skiing": Skiing,
    "Soccer": Soccer,
    "Softball": Softball,
    "Student Athletic Training": StudentAthleticTraining,
    "Swimming/Diving": SwimmingDiving,
    "Tennis": Tennis,
    "Track": Track,
    "Volleyball": Volleyball,
    "Water Polo": WaterPolo,
    "Rowing": Rowing
}

activities = {
    "Basketball ": Basketballfun,
    "Biking": Biking,
    "Boating": Boating,
    "Camping": Camping,
    "Concerts/Live Music": ConcertsLiveMusic,
    "Country Dancing": CountryDancing,
    "Exploring Austin": ExploringAustin,
    "Field Hockey ": FieldHockeyfun,
    "Fishing": Fishing,
    "Football": Football,
    "Golfing ": Golfingfun,
    "Hiking": Hiking,
    "Horseback Riding": HorsebackRiding,
    "Hunting": Hunting,
    "Ice Skating": IceSkating,
    "Lacrosse ": Lacrossefun,
    "Paddleboarding/Kayaking": PaddleboardingKayaking,
    "Pickleball": Pickleball,
    "Picnics": Picnics,
    "Pilates": Pilates,
    "Rock Climbing ": RockClimbingfun,
    "Running/Jogging ": RunningJoggingfun,
    "Scuba Diving": ScubaDiving,
    "Soccer ": Soccerfun,
    "Surfing": Surfing,
    "Swimming/Diving ": SwimmingDivingfun,
    "Tanning": Tanning,
    "Tennis ": Tennisfun,
    "Thrifting": Thrifting,
    "Traveling": Traveling,
    "Triathlons": Triathlons,
    "Volleyball ": Volleyballfun,
    "Walks Outdoors": WalksOutdoors,
    "Water Skiing": WaterSkiing,
    "Working Out": WorkingOut,
    "Yoga": Yoga,
    "Animals": Animals,
    "Arts and Crafts": ArtsandCrafts,
    "Baking": Baking,
    "Boardgames": Boardgames,
    "Coffee/Tea": CoffeeTea,
    "Cooking": Cooking,
    "Crochet/Knitting": CrochetKnitting,
    "Drawing": Drawing,
    "Exploring New Restaurants": ExploringNewRestaurants,
    "Formula 1": Formula1,
    "Government ": Governmentfun,
    "Graphic Design": GraphicDesign,
    "Health": Health,
    "Instagram": Instagram,
    "Listening to Music": ListeningtoMusic,
    "Musicals": Musicals,
    "Pageants": Pageants,
    "Painting": Painting,
    "Philosophy ": Philosophyfun,
    "Photography": Photography,
    "Playing a Brass Instrument": PlayingaBrassInstrument,
    "Playing a Percussion Instrument": PlayingaPercussionInstrument,
    "Playing a String Instrument": PlayingaStringInstrument,
    "Playing a Wind Instrument": PlayingaWindInstrument,
    "Podcasts": Podcasts,
    "Pottery/Ceramics": PotteryCeramics,
    "Reading": Reading,
    "Road Trips": RoadTrips,
    "Science/Marine Science/Ecology": ScienceMarineScienceEcology,
    "Scrapbooking": Scrapbooking,
    "Sewing": Sewing,
    "Shopping": Shopping,
    "Singing": Singing,
    "Skincare": Skincare,
    "Social Media": SocialMedia,
    "Video Games": VideoGames,
    "Vlogging": Vlogging,
    "Watching Sports": WatchingSports,
    "Watching TV/Movies": WatchingTVMovies,
    "Writing": Writing,
    "Karaoke": Karaoke,
    "Plants": Plants,
    "Roller Coasters": RollerCoasters
}

utorgs = {
    "Advertising Club": AdvertisingClub,
    "Architecture Club": ArchitectureClub,
    "Broadcasting Club": BroadcastingClub,
    "Business/Finance/Marketing/Economics Club": BusinessFinanceMarketingEconomicsClub,
    "Challengers": Challengers,
    "Choir ": UTChoir,
    "Cultural Club": CulturalClub,
    "Environmental/Sustainability Club": EnvironmentalSustainabilityClub,
    "Event Hosting Club": EventHostingClub,
    "Government Club": GovernmentClub,
    "Women in Medicine": WomeninMedicine,
    "Ignite": Ignite,
    "Intramural Sports": IntramuralSports,
    "Journalism/Magazine Organization": JournalismMagazineOrganization,
    "Nursing Club": NursingClub,
    "Performing Arts Club": PerformingArtsClub,
    "Philosophy Club": PhilosophyClub,
    "Pre Health Club": PreHealthClub,
    "Pre Law Club": PreLawClub,
    "Religious Club": ReligiousClub,
    "Residence Hall Association": ResidenceHallAssociation,
    "STEM Club": STEMClub,
    "Social Interest/Activism Club": SocialInterestActivismClub,
    "Spirit Org": SpiritOrg,
    "Steel Dance Company": SteelDanceCompany,
    "Teachers of Tomorrow": TeachersofTomorrow,
    "Texas Supports Live Music": TexasSupportsLiveMusic,
    "The Daily Texan": TheDailyTexan,
    "Theme Park Engineering Club": ThemeParkEngineeringClub,
    "Water Skiing Club": WaterSkiingClub,
    "Women in Business Association": WomeninBusinessAssociation,
    "Women in Psychology": WomeninPsychology
}

summercamps = {
    "AHEC Science Summer Camp": AHECScienceSummerCamp,
    "All Stars Sports Camp": AllStarsSportsCamp,
    "Brookhill Ranch Camp": BrookhillRanchCamp,
    "Camp Allen": CampAllen,
    "Camp Alonim": CampAlonim,
    "Camp Balcones Springs": CampBalconesSprings,
    "Camp Cho Yeh": CampChoYeh,
    "Camp Eagle": CampEagle,
    "Camp Fire Camp": CampFireCamp,
    "Camp Honey Creek": CampHoneyCreek,
    "Camp Ozark": CampOzark,
    "Camp Ramah in the Berkshires": CampRamahintheBerkshires,
    "Camp Tallowood": CampTallowood,
    "Camp Waldemar": CampWaldemar,
    "Church Camp": ChurchCamp,
    "Frost Valley YMCA": FrostValleyYMCA,
    "Fueled by Envision": FueledbyEnvision,
    "Grammy Camp": GrammyCamp,
    "Hindu Heritage Youth Camp": HinduHeritageYouthCamp,
    "Kids Acting": KidsActing,
    "Palace Theatre": PalaceTheatre,
    "Pine Cove": PineCove,
    "Rice ELITE Tech Camp": RiceELITETechCamp,
    "Rice University Aerospace and Aviation Academy": RiceUniversityAerospaceandAviationAcademy,
    "Rio Grande Society Summer Camp": RioGrandeSocietySummerCamp,
    "Rocky River Ranch": RockyRiverRanch,
    "Sierra Vista": SierraVista,
    "SkillsUSA Texas Leadership Camp": SkillsUSATexasLeadershipCamp,
    "Sky Ranch": SkyRanch,
    "St Mary Computer Science Camp": StMaryComputerScienceCamp,
    "TCU Tennis Camp": TCUTennisCamp,
    "Texas A&M Stem Camp": TexasAMStemCamp,
    "UT Latin American Studies": UTLatinAmericanStudies,
    "UC Berkeley MET": UCBerkeleyMET,
    "University of Dallas Computer Science Camp": UniversityofDallasComputerScienceCamp,
    "UT Austin Nursing Camp": UTAustinNursingCamp,
    "Wet and Wild Camp": WetandWildCamp,
    "Lake of the Woods": LakeoftheWoods,
    "CLTC": CLTC,
    "BBYO": BBYO
}

nicheinterests = {
    "Astrology": Astrology,
    "Balloons": Balloons,
    "Self Care": SelfCare,
    "Line Dancing": LineDancing,
    "Dachsunds": Dachsunds,
    "Documentaries": Documentaries,
    "Going to Bible Studies": GoingtoBibleStudies,
    "EMT": EMT,
    "Film Cameras": FilmCameras,
    "Beach": Beach,
    "College Football": CollegeFootball,
    "Cycling": Cycling,
    "Guitar": Guitar,
    "Trivia": Trivia,
    "History Nerd": HistoryNerd,
    "Passionate About Sports": PassionateAboutSports,
    "Taylor Swift": TaylorSwift,
    "Miss Texas Competition": MissTexasCompetition,
    "Cross Stitching": CrossStitching,
    "Obsessed with Medicine": ObsessedwithMedicine,
    "Greys Anatomy": GreysAnatomy,
    "Goodreads": Goodreads,
    "Letterboxd": Letterboxd,
    "Conspiracy Theories": ConspiracyTheories,
    "True Crime": TrueCrime,
    "Pop Culture": PopCulture,
    "Harry Potter": HarryPotter,
    "Mamma Mia the Musical": MammaMiatheMusical,
    "Vampire Diaries": VampireDiaries,
    "The Summer I Turned Pretty": TheSummerITurnedPretty,
    "Fun Hairstyles": FunHairstyles,
    "Music History": MusicHistory,
    "Cats": Cats,
    "Pinterest": Pinterest,
    "Clean Girl Aesthetic": CleanGirlAesthetic,
    "Loveshack Fancy": LoveshackFancy,
    "Runway Modeling": RunwayModeling,
    "Event Planning": EventPlanning,
    "Theme Parks": ThemeParks,
    "Friends TV Show": FriendsTVShow,
    "Reality TV": RealityTV,
    "Xbox": Xbox,
    "The Hunger Games": TheHungerGames,
    "Legend of Zelda": LegendofZelda,
    "Little Women": LittleWomen,
    "Pride and Prejudice": PrideandPrejudice,
    "Meteorology": Meteorology,
    "House and EDM Music": HouseandEDMMusic,
    "Puzzles": Puzzles,
    "Passionate About Healthcare": PassionateAboutHealthcare,
    "Dogs": Dogs,
    "Lizzy McAlpine": LizzyMcAlpine,
    "Finneas": Finneas,
    "Seattle": Seattle,
    "Leon Bridges": LeonBridges,
    "Owns Etsy Shop": OwnsEtsyShop,
    "Pearl Jam": PearlJam,
    "French Bulldogs": FrenchBulldogs,
    "Crepes": Crepes,
    "Foodie": Foodie,
    "Gossip Girl": GossipGirl,
    "Chipotle": Chipotle,
    "Flowers": Flowers,
    "Gilmore Girls": GilmoreGirls,
    "Texas Roadhouse": TexasRoadhouse,
    "Scream Movies": ScreamMovies,
    "Marvel": Marvel,
    "New Girl": NewGirl,
    "Loves Talking About Architecture": LovesTalkingAboutArchitecture,
    "Coloring": Coloring,
    "Real Housewives": RealHousewives,
    "Vanderpump Rules": VanderpumpRules,
    "Musical Composition": MusicalComposition,
    "Architectural Design": ArchitecturalDesign,
    "Creative Writing": CreativeWriting,
    "Cinematography": Cinematography,
    "Fashion": Fashion,
    "KPop": KPop,
    "Pets": Pets,
    "Pizookies": Pizookies,
    "Playing Cards": PlayingCards,
    "Sailing": Sailing,
    "Space": Space,
    "Sims": Sims,
    "Women Empowerment": WomenEmpowerment,
    "Minecraft": Minecraft,
    "Hamilton": Hamilton,
    "Horror Movies": HorrorMovies,
    "Interior Design": InteriorDesign,
    "Sports Medicine": SportsMedicine,
    "US History": USHistory,
    "WWI and II": WWIandII,
    "Sustainability": Sustainability,
    "Makeup": Makeup,
    "Texas Baseball": TexasBaseball,
    "Ice Hockey": IceHockey,
    "Fortnite": Fortnite,
    "Spider Man": SpiderMan,
    "Deadpool": Deadpool,
    "Miraculous Ladybug": MiraculousLadybug,
    "Action Movies": ActionMovies,
    "High School Mascot": HighSchoolMascot,
    "Pastries": Pastries,
    "Skydiving": Skydiving,
    "Bungee Jumping": BungeeJumping,
    "NBA Fan": NBAFan,
    "Creating Recipes": CreatingRecipes,
    "Bedazzling": Bedazzling,
    "Depop": Depop,
    "Houston Rodeo": HoustonRodeo,
    "Collecting Rubber Ducks": CollectingRubberDucks,
    "Trader Joes": TraderJoes,
    "Astros": Astros,
    "Bracelet Making": BraceletMaking,
    "Harry Styles": HarryStyles,
    "Powerlifting": Powerlifting,
    "Equality in Womens Sports": EqualityinWomensSports,
    "Harmonica": Harmonica,
    "Hayday": Hayday,
    "Mario Kart": MarioKart,
    "Smash Bros": SmashBros,
    "Animal Crossing": AnimalCrossing,
    "Love Island": LoveIsland,
    "Roblox": Roblox,
    "Disney": Disney,
    "Study Abroad": StudyAbroad,
    "Star Wars": StarWars,
    "Going to the Zoo": GoingtotheZoo,
    "NYT Games": NYTGames,
    "Legos": Legos,
    "Study Abroad": StudyAbroad
}

transfers = {
    "University of Texas at El Paso": UTEP,
    "University of Texas at San Antonio": UTSA
}

# ===== Streamlit UI =====
st.title("Interest Finder")

def checkbox_columns(title, items, num_cols=2):
    st.markdown(f'### {title}')
    with st.expander('Select Here', expanded=False):
        cols = st.columns(num_cols)
        chunk_size = math.ceil(len(items) / num_cols)
        selected = []
        for i, interest in enumerate(items):
            col = cols[i // chunk_size]
            if col.checkbox(interest):
                selected.append(interest)
        return selected

selected_majors = checkbox_columns("Majors"+'\U0001F4DA', list(majors.keys()), num_cols=4)
selected_minors = checkbox_columns("Minors"+"\U0001F4DD", list(minors.keys()), num_cols=4)
selected_college = checkbox_columns("College/Track"+"\U0001FA7A", list(college.keys()), num_cols=4)
selected_hometowns = checkbox_columns("Hometowns"+"\U0001F3E0", list(hometowns.keys()), num_cols=4)
selected_schools = checkbox_columns("High Schools"+"\U0001F3EB", list(schools.keys()), num_cols=4)
selected_extras = checkbox_columns("HS Extracurriculars"+"\U0001F483", list(extras.keys()), num_cols=4)
selected_orgs = checkbox_columns("UT Organizations"+"\U0000266B", list(utorgs.keys()), num_cols=4)
selected_activities = checkbox_columns("Activities/Interests for Fun"+"\U0001F3C3", list(activities.keys()), num_cols=4)
selected_summercamps = checkbox_columns("Summer Camp"+"\U0001F525", list(summercamps.keys()), num_cols=4)
selected_nicheinterests = checkbox_columns("Niche Interests"+"\U0001F388", list(nicheinterests.keys()), num_cols=4)
selected_transfers = checkbox_columns("Transfer Students"+"\U0001F501", list(transfers.keys()), num_cols=4)

selected_interests = selected_majors + selected_minors + selected_college + selected_hometowns + selected_schools + selected_extras + selected_orgs + selected_activities + selected_summercamps + selected_nicheinterests + selected_transfers

# ===== Matching Logic =====
if selected_interests:
    people_matches = {}

    # Loop over all selected interests with category info
    for interest in selected_interests:
        # Determine which category dict it belongs to
        if interest in majors:
            names = majors[interest]
        elif interest in minors:
            names = minors[interest]
        elif interest in college:
            names = college[interest]
        elif interest in hometowns:
            names = hometowns[interest]
        elif interest in schools:
            names = schools[interest]
        elif interest in extras:
            names = extras[interest]
        elif interest in utorgs:
            names = utorgs[interest]
        elif interest in activities:
            names = activities[interest]
        elif interest in summercamps:
            names = summercamps[interest]
        elif interest in nicheinterests:
            names = nicheinterests[interest]
        elif interest in transfers:
            names = transfers[interest]
        else:
            continue

        # Store each match as a tuple (category, interest) to prevent confusion
        for name in names:
            if name not in people_matches:
                people_matches[name] = set()
            people_matches[name].add(interest)  # add the exact checkbox label

    all_selected = set(selected_interests)
    all_match = []
    some_match = []
    one_match = []

    for person, matched_set in people_matches.items():
        # intersection of what the person has with what was actually selected
        matched_selected = matched_set & all_selected
        if matched_selected == all_selected:
            all_match.append((person, matched_selected))
        elif len(matched_selected) > 1:
            some_match.append((person, matched_selected))
        elif len(matched_selected) == 1:
            one_match.append((person, matched_selected))
            
    # Color blues and whites
    blue_names = ['Abby Alsup','Abby OGuynn','Abby Sanders','Aliyana Martinez','Allie Harter','Alyssa Bouloy','Anika Novak','Ava Dahlander','Brianna Salaices','Bridget Flatow','Catherine Dooley','Celeste Tomberlin','Charlie Stone','Chloe Lim','Ellen Meltzer','Emily Bull','Emma Schneidau','Emmerich Benavides','Erika Sandberg','Ferzine Sanjana','Haley Hooper','Hana Sawaf','Haylee Martin','Isabella Bartz','Izzy Davies','Jasmine Valdez','Jess Paine','Jovanni Carrillo','Julia Lindstrom','Karlie Haigood','Kate Neiman','Katelyn Quintanilla','Katie Windell','Krissily Estacio','Larkin Seidel','Lindsay McCullough','Lola Daffin','Madeleine Mazingo','Maya Sajan','Ollie Mae Harrison','Piper Buck','Riley Avery','Sarah Solomon','Sofie Arroyo','Taylor Jennings','Zoe Veliz','Suzie Hudgens']
    violet_names = ['Alice Hudson','Audrey Cooper','Ava Hurst','Avery McClure','Bella Anderson','Bella Wernli','Caitlin Van Sant','Claire Savage','Ella Leininger','Ellie Berman','Georgia Key','Hannah Greenhill','Kaitlin Black','Kamryn Jean','Katie Walsh','Megan Garza','Meredith Moreland','Sophie Robins','Zoe Alvarado']
    gray_names = ['Arabella Savener','Gabby Beck','Kira Sanders','Marley Page','Meadow Votis','Meghna Sunkureddi','Nids Pappu','Regan Hill','Sienna Shutts']
    
    def coloring(names):
        if name in blue_names:
            return f"<span style='color:blue'>{name}</span></b>"
        elif name in violet_names:
            return f"<span style='color:darkviolet'>{name}</span></b>"
        elif name in gray_names:
            return f"<span style='color:darkgray'>{name}</span></b>"
        else:
            return f"<b>{name}</b>"

    # Display
    st.subheader("✅ All Matches")
    if all_match:
        for name, matches in all_match:
            colored_names = coloring(name)
            st.markdown(f"{colored_names}: {', '.join(matches)}", unsafe_allow_html=True)

    st.subheader("🔹 Some Matches")
    if some_match:
        for name, matches in some_match:
            colored_names = coloring(name)
            st.markdown(f"{colored_names}: {', '.join(matches)}", unsafe_allow_html=True)

    st.subheader("⚪ One Match")
    if one_match:
        for name, matches in one_match:
            colored_names = coloring(name)
            st.markdown(f"{colored_names}: {', '.join(matches)}", unsafe_allow_html=True)
    
    
    
    
    
    #st.subheader("✅ All Matches")
    #if all_match:
        #for name, matches in all_match:
            #st.write(f"**{name}**: {', '.join(matches)}")
    #else:
        #st.write("(none)")

    #st.subheader("🔹 Some Matches")
    #if some_match:
        #for name, matches in some_match:
            #st.write(f"**{name}**: {', '.join(matches)}")
    #else:
        #st.write("(none)")

    #st.subheader("⚪ One Match")
    #if one_match:
        #for name, matches in one_match:
            #st.write(f"**{name}**: {', '.join(matches)}")
    #else:
        #st.write("(none)")