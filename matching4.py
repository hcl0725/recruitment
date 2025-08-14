import streamlit as st
import math

# ===== Data =====
# MAJORS
Advertising = ['Abby Sanders', 'Catherine Favoriti', 'Jillian Taylor', 'Kaylie Ngo', 'Marley Page', 'Sienna Shutts','Allie Harter','sarah thompson']
AerospaceEngineering = ['Madeleine Mazingo']
Anthropology = ['Zoe Veliz']
AppliedMovementScience = ['Karlie Haigood','Julia Lindstrom']
Architecture = ['Chloe Lim', 'Riley avery']
BFAActing = ['Katelyn Quintanilla']
BehavioralAndSocialDataScience = ['Delaney Vanderpool']
BilingualEducation = ['Emily Robles']
Biochemistry = ['Mia Vasquez']
Biology = ['Audrey Cooper', 'Brianna Salaices', 'Emmerich Benavides', 'Izzy Davies', 'Rishona Mopur','Megan Garza','Lindsay McCullough', 'Sydney Fern']
MicrobiologyAndInfectiousDiseases = ['Megan Garza']
BiomedicalEngineering = ['Gabrielle Beck']
Business = ['Ava Dahlander', 'Haylee Martin', 'Catherine Dooley', 'madison taylor', 'Larkin Seidel', 'Meredith Moreland', 'Meredith Moreland', 'Brianna']
BusinessHonors = ['Brianna']
Finance = ['Brianna']
CivilEngineering = ['Anna Woodson', 'Mae Trahan', 'Maggie Shaw','Emily Bull']
CommunicationAndLeadership = ['Emma Schneidau', 'Delaney O’Brien']
ComputerScience = ['Krissily Estacio']
CorporateCommunications = ['Valentina Markov','Allie Harter']
ESLGeneralistEarlyChildhood = ['Erika Sandberg']
EarlyChildhoodEducation = ['Anika Novak', 'meghna sunkureddi', 'Ella Pitts', 'Erika Sandberg']
Economics = ['Elyse Miller', 'Shelby', 'Sofia Arroyo']
English = ['Isabella Bartz']
EnvironmentalEngineering = ['Abby OGuynn', 'Katie Windell']
FrenchStudies = ['sarah solomon']
GeosystemsEngineering = ['Nidhi Pappu']
Government = ['Catalina Cruz', 'Ellie Berman', 'Jovanni Carrillo', 'Lola Daffin', 'Piper Buck', 'Charlize Stone', 'Heidi Chapin']
HealthPromotionAndBehavioralScience = ['Rachel Dolan, Claire Savage']
HealthAndSociety = ['Bella Champion', 'Hazel Wells', 'Jasmine Valdez', 'Maya Sajan']
HumanBiology = ['Lindsay McCullough', 'Sydney Fern']
HumanDevelopmentAndFamilySciences = ['Mazzy Bledsoe']
HumanDimensionsOfOrganization = ['zoe alvarado', 'Alice Hudson']
InternationalRelationsAndGlobalStudies = ['Maya Abraham', 'Riley Wanasek', 'Abrielle Gallini', 'Josie Mandrea', 'Hana Sawaf']
Journalism = ['Bella Anderson', 'Carly Schmidt', 'Celeste Tomberlin', 'Ferzine Sanjana', 'Katie Walsh', 'Kirthi Gummadi', 'Sarah Sims']
KinesiologyExerciseScience = ['Kamryn Jean']
Mathematics = ['Amelia Klyap', 'Jenn Rosado']
MechanicalEngineering = ['Alexandra Nicholls', 'Ollie Mae Harrison', 'Morgan Baumel']
MusicAndMedia = ['Ava Hurst']
Neuroscience = ['Abby Kant', 'Caitlin Van Sant', 'Regan Hill', 'Jannae Ailawadhi']
Nursing = ['Bailey Alsup', 'Gabrielle Green', 'Maria Sepulveda Salazar']
Physics = ['Nidhi Pappu']
PoliticalCommunications = ['Heidi Chapin','Hannah Greenhill', 'Meadow Votis']
Psychology = ['Alyssa Bouloy','Delaney Vanderpool', 'Ella Leininger', 'Taylor Jennings', 'Riley Wanasek', 'Kate Neiman', 'Arabella Savener']
PublicRelations = ['Liz Keegan', 'georgia key', 'Brooke Walker', 'Sophie Robins']
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
CommunicatingSocialIssuesMinor = ['georgia key', 'Aliyana Martinez']
CommunicationStudiesMinor = ['Jenn Rosado']
ComputerScienceMinor = ['Delaney Vanderpool']
CriminalLawJusticeandInequalityBridgingDisciplinesProgramMinor = ['Abby Alsup']
DesignStrategiesMinor = ['Ollie Mae Harrison']
EducationalPsychologyMinor = ['Ella Pitts', 'Chasiti Tyeryar', 'Aliyana Martinez']
EntrepreneurshipMinor = ['Diyaa Dossani', 'Haley Hooper']
FinanceMinor = ['Shelby']
FrenchMinor = ['Piper Buck']
GlobalCommunicationsMinor = ['Ellen Meltzer']
EthicsAndLeadershipInLawGovernmentandPoliticsMinor = ['Ellen Meltzer']
GlobalManagementMinor = ['Krissily Estacio']
GovernmentMinor = ['Kirthi Gummadi', 'Bella Wernli']
HealthReformandInnovationMinor = ['Megan Garza']
HealthCommunicationsMinor = ['Caitlin Van Sant', 'Alice Hudson']
HealthcareReformAndInnovationMinor = ['Gabrielle Green']
InteriorDesignMinor = ['sarah solomon']
ItalianMinor = ['Abrielle Gallini']
JeffersonScholarCTIMinor = ['Katie Windell', 'Arabella Savener']
KinesiologyMinor = ['Genesis Martinez', 'Emerson Oliver', 'Brianna']
LawJusticeAndSocietyMinor = ['Hannah Greenhill']
MediaAndEntertainmentIndustriesMinor = ['Bella Anderson', 'Ferzine Sanjana']
PhysiciansAssistantMinor = ['Hazel Wells']
PatientsPractitionersAndCareMinor = ['Jasmine Valdez']
PreHealthMinor = ['Abby Kant', 'Izzy Davies', 'Maya Sajan', 'Mazzy Bledsoe', 'Kamryn Jean', 'Mia Vasquez']
ProfessionalSalesAndBusinessDevelopmentMinor = ['Marley Page']
SocialAndBehavioralSciencesMinor = ['Charlize Stone']
SportsProductionandBroadcastMinor = ['Carly Schmidt']
SpanishforMedicalProfessionsMinor = ['Brianna Salaices']
BusinessSpanishMinor = ['zoe alvarado']
FitnessandRehabSpecializationMinor = ['Julia Lindstrom']
PremedMinor = ['Alyssa Bouloy']
PreHealthDentalMinor = ['Abby Sanders']
ProfessionalSalesMinor = ['sarah thompson']
RiskManagementStatisticsMinor = ['Suzie Hudgens']
SpanishMinor = ['Josie Mandrea']

# HOMETOWNS

ArlingtonTX = ['Bella Wernli']
ArlingtonVA = ['Abby Kant', 'Catherine Dooley']
AustinTX = ['Abby Alsup', 'Arabella Savener', 'Bailey Alsup', 'Bella Anderson', 'Jannae Ailawadhi', 'Kaitlin Black', 'Marley Page', 'Charlize Stone', 'Regan Hill']
BeeCaveTX = ['Jessica Paine']
BeltonTX = ['Riley avery']
BoerneTX = ['Sofia Arroyo']
BurlesonTX = ['Hannah Greenhill']
CleburneTX = ['Angie Andersen']
CollegeStationTX = ['Taylor Jennings', 'Celeste Tomberlin']
ColleyvilleTX = ['Anika Novak']
CorpusChristiTX = ['Jovanni Carrillo', 'Karlie Haigood']
DallasTX = ['Abby Sanders', 'Ava Dahlander', 'Carly Schmidt', 'Diyaa Dossani', 'Hazel Wells', 'Riley Wanasek', 'Claire Savage', 'Izzy Davies', 'Gabrielle Green', 'Delaney Oâ€™Brien', 'Zoe Veliz', 'Hana Sawaf']
DanvilleCA = ['Nidhi Pappu']
DaytonOH = ['Valentina Markov']
EaglePassTX = ['Ella Pitts']
ElPasoTX = ['Catalina Cruz']
FriendswoodTX = ['meghna sunkureddi', 'Sienna Shutts']
FriscoTX = ['Haylee Martin', 'Piper Buck', 'Sydney Fern', 'Kirthi Gummadi']
GardenCityNY = ['Jenn Rosado']
GrapevineTX = ['Brianna Salaices']
HoustonTX = ['Emma Schneidau', 'Isabella Bartz', 'Jillian Taylor', 'Sarah Sims', 'sarah solomon', 'Meredith Moreland', 'Sophie Robins', 'Heidi Chapin', 'Mia Vasquez', 'Suzie Hudgens', 'Ollie Mae Harrison', 'Catherine Favoriti', 'Avery McClure', 'Mae Trahan', 'zoe alvarado', 'Abby Oguynn', 'Aliyana Martinez', 'Sophie Shapiro', 'Shelby, Maya Abraham']
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
MansfieldTX = ['georgia key']
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
SacramentoCA = ['sarah thompson']
SanAntonioTX = ['Brianna', 'Emily Robles', 'Ferzine Sanjana', 'Ellen Meltzer', 'Elyse Miller', 'Gabrielle Beck', 'Kate Neiman', 'Rachel Dolan', 'Krissily Estacio']
HonoluluHawaii = ['Krissily Estacio']
SeabrookTX = ['Shelby']
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
AlvinHighSchool = ['madison taylor']
AmadorValleyHighSchool = ['Emily Bull', 'Julia Lindstrom']
ArlingtonHighSchool = ['Bella Wernli']
AtascocitaHighSchool = ['Jillian Taylor']
BeltonHighSchool = ['Riley avery']
BishopDunneCatholicSchool = ['Gabrielle Green']
BoerneHighSchool = ['Sofia Arroyo']
BookerTWashingtonHSPVA = ['Diyaa Dossani']
BowieHighSchool = ['Bailey Alsup']
BrooklynTechnicalHighSchool = ['Amelia Klyap']
CalabasasHighSchool = ['Hailey Brooks']
CalallenHighSchool = ['Karlie Haigood']
CedarParkHighSchool = ['Regan Hill']
CentennialHighSchool = ['Hannah Greenhill']
ClearCreekHighschool = ['Sophie Robins']
ClearFallsHighSchool = ['Shelby']
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
FriendswoodHighSchool = ['Sienna Shutts', 'meghna sunkureddi']
FriscoMemorialHighSchool = ['Haylee Martin']
FtBendTravisHighSchool = ['Erika Sandberg', 'Erika Sandberg']
FulshearHighSchool = ['Ollie Mae Harrison']
GardenCityHighSchool = ['Jenn Rosado']
GeorgetownDaySchool = ['Catherine Dooley']
RegentsHighSchool = ['Jannae Ailawadhi']
GlennHighSchool = ['Emmerich Benavides']
LiberalArtsandScienceAcademy = ['Jannae Ailawadhi']
GraniteBahHighSchool = ['sarah thompson']
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
LakeTravisHighSchool = ['Jessica Paine', 'Charlize Stone']
LamarHighSchool = ['Catherine Favoriti']
LibertyCreekHighSchool = ['Ava Hurst']
LibertyHighSchool = ['Kirthi Gummadi']
LibertyHillHighSchool = ['Emerson Oliver']
LouisDBrandeisHighSchool = ['Krissily Estacio']
LutheranSouthAcademy = ['Mia Vasquez']
MansfieldHighSchool = ['georgia key']
MaryCarrollHighSchool = ['Jovanni Carrillo']
McNeilHighSchool = ['Alice Hudson']
MckinneyHighSchool = ['Maya Sajan']
MemorialHighSchool = ['Piper Buck']
MonteVistaHighSchool = ['Nidhi Pappu']
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
StratfordHighSchool = ['Mae Trahan', 'sarah solomon']
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
WTWhiteHighSchool = ['Delaney Oâ€™Brien']
WarrenHighSchool = ['Brianna']
WashingtonLibertyHighSchool = ['Abby Kant']
WestfieldHighSchool = ['Katie Walsh']
WestlakeHighSchool = ['Bella Anderson']
WilliamTDwyerHighSchool = ['Anna Woodson']
WoodrowWilsonHighSchool = ['Hazel Wells']
KleinOakHighSchool = ['Morgan Baumel']
LanghamCreekHighSchool = ['zoe alvarado']
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
BestBuddies = ['Brianna Salaices', 'meghna sunkureddi', 'Lindsay McCullough', 'Izzy Davies', 'Zoe Veliz', 'Catherine Dooley']
BookClub = ['Isabella Bartz']
BoosterClub = ['madison taylor', 'Erika Sandberg']
Cheer = ['Meredith Moreland', 'Genesis Martinez', 'Anna Woodson', 'Catalina Cruz', 'Allie Harter', 'Brooke Walker', 'Delaney OÃ¢â‚¬â„¢Brien', 'Ella Pitts', 'Erika Sandberg', 'Izzy Davies', 'Kaylie Ngo', 'Meadow Votis', 'Erika Sandberg', 'Amelia Klyap', 'Heidi Chapin', 'Angie Andersen', 'Gabrielle Green', 'Kate Neiman', 'Rishona Mopur']
Choir = ['Maya Sajan', 'Ellen Meltzer', 'Katelyn Quintanilla', 'Meadow Votis', 'Ava Dahlander', 'Jenn Rosado', 'Jessica Paine', 'Liz Keegan', 'Kaylie Ngo', 'Valentina Markov']
ColorGuard = ['Sydney Fern', 'Carly Schmidt']
DistributiveEducationClubsofAmericaDECA = ['Brianna Salaices', 'madison taylor', 'Katelyn Quintanilla', 'Delaney Vanderpool', 'Haylee Martin', 'Nidhi Pappu']
DoSomething = ['Morgan Baumel']
EnglishHonorSocietyNEHS = ['Isabella Bartz', 'Shelby', 'Marley Page', 'Ferzine Sanjana', 'meghna sunkureddi', 'Sophie Robins', 'zoe alvarado', 'Madeleine Mazingo']
FamilyCareerandCommunityLeaderofAmericaFCCLA = ['meghna sunkureddi', 'Jovanni Carrillo', 'Emily Robles']
FellowshipofChristianAthletesFCA = ['Erika Sandberg', 'Meadow Votis', 'Ava Dahlander', 'Kate Neiman', 'Bella Wernli', 'Alice Hudson']
FeminismGenderEqualityClub = ['Maya Abraham']
FilmClub = ['sarah thompson', 'Regan Hill', 'Celeste Tomberlin', 'Diyaa Dossani', 'Sienna Shutts', 'Sophie Shapiro']
FormulaClub = ['Bella Wernli']
FrenchClub = ['Piper Buck']
FutureFarmersofAmericaFFA = ['Meadow Votis', 'Hannah Greenhill', 'Aliyana martinez']
GIS = ['Gabrielle Green']
GayStraightAllianceClub = ['Ellen Meltzer', 'Maya Abraham', 'Delaney Vanderpool', 'Regan Hill']
GeneticsandNeuroscienceClub = ['Regan Hill']
GeographyClub = ['Regan Hill']
GirlScouts = ['Arabella Savener', 'Suzie Hudgens', 'Erika Sandberg', 'Jenn Rosado', 'Catherine Favoriti', 'Riley avery', 'Heidi Chapin', 'Avery McClure', 'Maggie Shaw', 'Sarah Sims', 'Abby OGuynn', 'Amelia Klyap', 'Haley Hooper']
HealthOccupationsStudentsofAmericaHOSA = ['Sydney Fern', 'Jasmine Valdez', 'Sofia Arroyo', 'Maria Sepulveda Salazar', 'Bailey Alsup', 'Meredith Moreland', 'Krissily Estacio', 'Emmerich Benavides', 'Megan Garza', 'Bella Champion']
IBProgram = ['Chloe Lim', 'Lindsay McCullough', 'Ava Dahlander', 'Katie Windell', 'Abby Kant', 'Hazel Wells', 'Hana Sawaf']
InternationalThespianSocietyITS = ['Arabella Savener', 'Jessica Paine', 'Liz Keegan', 'Regan Hill', 'Kaitlin Black', 'Emerson Oliver']
JROTC = ['Gabrielle Beck']
KeepTexasBeautiful = ['Anika Novak']
KeyClub = ['Isabella Bartz', 'Marley Page', 'Izzy Davies', 'zoe alvarado', 'Riley avery', 'Emma Schneidau', 'Mae Trahan', 'Katie Walsh', 'Aliyana Martinez']
LatinClub = ['Gabrielle Beck']
LatinosUnidos = ['Gabrielle Green']
LeoClub = ['Celeste Tomberlin']
MockTrial = ['Kirthi Gummadi', 'Heidi Chapin', 'Emma Schneidau']
ModelUN = ['Maya Abraham', 'Kate Neiman', 'Heidi Chapin', 'Maria Sepulveda Salazar', 'Riley Wanasek', 'Mia Vasquez', 'Hana Sawaf']
NationalCharityLeagueNCL = ['Ferzine Sanjana', 'Izzy Davies', 'Ava Dahlander', 'Kaylie Ngo', 'Madeleine Mazingo', 'Heidi Chapin', 'Bailey Alsup', 'Hazel Wells', 'Kaitlin Black', 'sarah solomon', 'Ollie Mae Harrison', 'Brooke Walker', 'Abby Alsup', 'Allie Harter']
NewspaperJournalismClub = ['Isabella Bartz', 'Carly Schmidt', 'Ellen Meltzer', 'Maya Abraham', 'Marley Page', 'Ferzine Sanjana', 'Kirthi Gummadi', 'Zoe Veliz', 'Catherine Dooley', 'Ava Dahlander', 'Kate Neiman', 'Regan Hill', 'Sienna Shutts', 'Heidi Chapin', 'Sarah Sims', 'Kamryn Jean', 'Hazel Wells', 'Katie Walsh', 'Abrielle Gallini', 'Elyse Miller', 'Bella Anderson', 'Ellie Berman', 'Haley Hooper']
Orchestra = ['Izzy Davies', 'Madeleine Mazingo', 'Bella Wernli', 'Krissily Estacio', 'Gabrielle Beck', 'Brianna']
PeerAssistanceLeadershipandServicePALS = ['Brianna Salaices', 'Lindsay McCullough', 'Meadow Votis', 'Ava Dahlander', 'Sophie Robins', 'Emmerich Benavides', 'Katie Walsh', 'Charlize Stone', 'Haley Hooper']
PhotographyClub = ['Carly Schmidt', 'Ava Dahlander', 'Celeste Tomberlin', 'Abrielle Gallini', 'Gabrielle Beck', 'Sophie Shapiro']
Piano = ['Valentina Markov']
PsychologyClub = ['Regan Hill']
PupsforPeople = ['Valentina Markov']
QuillandScrollHonorSociety = ['Regan Hill']
RedCross = ['Ava Dahlander', 'Sophie Robins', 'Rachel Dolan', 'Hana Sawaf']
RoboticsComputerScienceClub = ['Suzie Hudgens', 'Riley avery', 'Krissily Estacio', 'Alexandra Nicholls', 'Sophie Shapiro']
ScienceOlympiad = ['Suzie Hudgens']
ServiceCouncil = ['Jannae Ailawadhi']
SkillsUSA = ['Angie Andersen']
SpeechandDebateClub = ['Nidhi Pappu', 'Regan Hill', 'Heidi Chapin', 'Rachel Dolan', 'Brianna', 'Charlize Stone', 'hana Sawaf']
StudentAthleticCouncil = ['Lindsay McCullough']
StudentAthleticTrainer = ['Brianna']
StudentCouncilSTUCO = ['Isabella Bartz', 'Carly Schmidt', 'Ellen Meltzer', 'Maya Abraham', 'Gabrielle Green', 'Marley Page', 'Suzie Hudgens', 'meghna sunkureddi', 'Lindsay McCullough', 'Izzy Davies', 'Zoe Veliz', 'Katelyn Quintanilla', 'Sophie Robins', 'Jovanni Carrillo', 'Alice Hudson', 'Diyaa Dossani', 'Hannah Greenhill', 'Riley avery', 'Heidi Chapin', 'Maria Sepulveda Salazar', 'Bailey Alsup', 'Krissily Estacio', 'Emmerich Benavides', 'Kamryn Jean', 'Hazel Wells', 'Riley Wanasek', 'Mia Vasquez', 'Rachel Dolan', 'Abby Alsup', 'Allie Harter', 'Gabrielle Beck', 'Brianna', 'Emily Robles', 'Ella Pitts', 'Jillian Taylor', 'Caitlin Van Sant', 'Morgan Baumel', 'Anika Novak', 'Ella Leininger', 'Charlize Stone', 'Hana Sawaf', 'Aliyana Martinez']
StudentVoterEmpowermentClub = ['Zoe Veliz']
TEDX = ['Charlize Stone']
Theatre = ['Celeste Tomberlin', 'Katelyn Quintanilla']
TutoringPeerMentoringProgram = ['Sydney Fern', 'Izzy Davies', 'Madeleine Mazingo', 'Jovanni Carrillo', 'Bella Wernli', 'Riley avery', 'Heidi Chapin', 'Bailey Alsup', 'Katie Walsh', 'Rachel Dolan', 'Abby Alsup', 'Emily Robles', 'Claire Savage', 'Hailey Brooks', 'Josie Mandrea', 'Hana sawaf']
UniversityInterscholasticLeagueUIL = ['Marley Page', 'Sydney Fern', 'madison taylor', 'Jessica Paine', 'Jovanni Carrillo', 'Regan Hill', 'Diyaa Dossani', 'Heidi Chapin', 'Maria Sepulveda Salazar', 'Bailey Alsup', 'Krissily Estacio', 'Kamryn Jean', 'Kaitlin Black', 'Brianna', 'Audrey Cooper', 'Haley Hooper']
WeCareClub = ['Shelby']
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
Ballet = ['Catalina Cruz', 'Chloe Lim', 'Ava Dahlander', 'georgia key']
Basketball = ['Ellie Berman', 'Maya Abraham', 'Lindsay McCullough', 'Caitlin Van Sant', 'Bella Champion', 'Morgan Baumel', 'Karlie Haigood', 'Hazel Wells']
Boxing = ['Valentina Markov']
CrossCountry = ['Chloe Lim', 'Ellie Berman', 'Meadow Votis', 'Riley avery', 'Mia Vasquez', 'Brianna Salaices', 'Gabrielle Beck', 'Abby Alsup', 'Bailey Alsup', 'Delaney Vanderpool', 'Hailey Brooks', 'Hannah Greenhill', 'Lola Daffin', 'Sophie Shapiro']
DanceTeam = ['Catalina Cruz', 'Chloe Lim', 'Ava Dahlander', 'georgia key', 'Maya Abraham', 'Erika Sandberg', 'Amelia Klyap', 'Bella Anderson', 'Emily Robles', 'Isabella Bartz', 'Alexandra Nicholls', 'Claire Savage', 'Jasmine Valdez', 'Kamryn Jean', 'Shelby', 'Sophie Robins', 'Abrielle Gallini', 'Ollie Mae Harrison', 'sarah thompson']
DrillTeam = ['Catalina Cruz', 'Ava Dahlander', 'georgia key', 'Maya Abraham', 'Alexandra Nicholls', 'Claire Savage', 'Jasmine Valdez', 'Kamryn Jean', 'Shelby', 'Sophie Robins', 'Abrielle Gallini', 'zoe alvarado', 'Larkin Seidel']
FieldHockey = ['Katie Walsh', 'Maggie Shaw', 'Valentina Markov']
FigureSkating = ['Rachel Dolan', 'Bridget Flatow']
FlagFootball = ['Caitlin Van Sant']
Golf = ['Riley avery', 'Avery McClure', 'Haylee Martin', 'Mae Trahan', 'Elyse Miller']
Lacrosse = ['Lindsay McCullough', 'Caitlin Van Sant', 'Mia Vasquez', 'Katie Walsh', 'Emerson Oliver', 'Jannae Ailawadhi']
RockClimbing = ['Heidi Chapin', 'Hana Sawaf']
Rowing = ['Valentina Markov', 'Jenn Rosado']
Skiing = ['Emerson Oliver', 'Liz Keegan', 'Josie Mandrea']
Soccer = ['Lindsay McCullough', 'Bella Champion', 'Brianna Salaices', 'Sophie Robins', 'sarah thompson', 'Larkin Seidel', 'Julia Lindstrom', 'Maria Sepulveda Salazar', 'Regan Hill', 'Taylor Jennings', 'Ellen Meltzer', 'Jenn Rosado', 'Megan Garza', 'Audrey Cooper']
Softball = ['Caitlin Van Sant', 'Morgan Baumel', 'Amelia Klyap', 'Emily Bull', 'Piper Buck', 'Jovanni Carrillo']
StudentAthleticTraining = ['Mazzy Bledsoe']
SwimmingDiving = ['Gabrielle Beck', 'Alice Hudson', 'Kirthi Gummadi', 'Catherine Dooley', 'Rachel Dolan', 'Katie Windell', 'Hana Sawaf', 'Hana Sawaf', 'Sophie Shapiro']
Tennis = ['Catalina Cruz', 'Angie Andersen', 'Maggie Shaw', 'Jannae Ailawadhi', 'Ellen Meltzer', 'Catherine Dooley', 'Rachel Dolan', 'Abby Sanders', 'Anika Novak', 'Riley Wanasek', 'Haley Hooper', 'Josie Mandrea']
Track = ['Bella Champion', 'Karlie Haigood', 'Riley avery', 'Mia Vasquez', 'Gabrielle Beck', 'Abby Alsup', 'Bailey Alsup', 'Delaney Vanderpool', 'Hailey Brooks', 'Hannah Greenhill', 'Lola Daffin', 'Abrielle Gallini', 'Jenn Rosado', 'Chasiti Tyeryar', 'Emma Schneidau', 'Sarah Sims', 'Sophie Shapiro']
Volleyball = ['Bella Champion', 'Karlie Haigood', 'Hazel Wells', 'Gabrielle Green', 'Kate Neiman', 'Elyse Miller', 'Jannae Ailawadhi', 'Megan Garza', 'Jovanni Carrillo', 'Abby Kant', 'Ava Hurst', 'Bella Wernli', 'Emmerich Benavides', 'Nidhi Pappu', 'madison taylor', 'Haley hooper']
WaterPolo = ['Valentina Markov', 'Audrey Cooper', 'Katie Windell', 'Hana Sawaf']
Rowing = ['Valentina Markov', 'Jenn Rosado']

# ACTIVITIES FOR FUN
Basketballfun = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Morgan Baumel', 'Karlie Haigood']
Biking = ['Julia Lindstrom', 'Caitlin Van Sant', 'Delaney Vanderpool', 'Charlize Stone', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley avery', 'Riley Wanasek', 'Kate Neiman', 'Katie Walsh', 'Josie Mandrea', 'Hana Sawaf', 'Sophie Shapiro ,']
Boating = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Delaney Vanderpool', 'Charlize Stone', 'Amelia Klyap', 'Lindsay McCullough', 'Shelby', 'Sofia Arroyo', 'Erika Sandberg', 'Liz Keegan', 'Emerson Oliver', 'Hana Sawaf']
Camping = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Delaney Vanderpool', 'Charlize Stone', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley avery', 'Riley Wanasek', 'Shelby', 'Meadow Votis', 'Ava Dahlander', 'Ava Hurst', 'Heidi Chapin', 'Ellie Berman', 'Mae Trahan', 'Regan Hill', 'Hana Sawaf', 'sophie shapiro']
ConcertsLiveMusic = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Morgan Baumel', 'Delaney Vanderpool', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Kate Neiman', 'Katie Walsh', 'Sofia Arroyo', 'Erika Sandberg', 'Liz Keegan', 'Emerson Oliver', 'Meadow Votis', 'Ava Dahlander', 'Ava Hurst', 'Heidi Chapin', 'Ellie Berman', 'Mae Trahan', 'Madeleine Mazingo', 'Diyaa Dossani', 'Isabella Bartz', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'madison taylor', 'Jessica Paine', 'Jillian Taylor', 'Katelyn Quintanilla', 'Abrielle Gallini', 'Ellen Meltzer', 'Chloe Lim', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Ollie Mae Harrison', 'Kirthi Gummadi', 'zoe alvarado', 'Claire Savage', 'georgia key', 'sarah thompson', 'sarah solomon', 'Avery McClure', 'Haylee Martin', 'Krissily Estacio', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Brianna', 'Ella Leininger', 'Emily Bull', 'Taylor Jennings', 'Delaney OÃ¢â‚¬â„¢Brien', 'Jannae Ailawadhi', 'Mia Vasquez', 'Anika Novak', 'Chasiti Tyeryar', 'Alice Hudson', 'Lola Daffin', 'Megan Garza', 'Emma Schneidau', 'Katie Windell', 'Allie Harter', 'Suzie Hudgens', 'Audrey Cooper', 'Abby Sanders', 'Hazel Wells', 'Marley Page', 'Hannah Greenhill', 'Meredith Moreland', 'Emmerich Benavides', 'Anna Woodson', 'Zoe Veliz', 'Elyse Miller', 'Ella Pitts', 'Celeste Tomberlin', 'Mazzy Bledsoe', 'Catherine Favoriti', 'Kaylie Ngo', 'Nidhi Pappu', 'Maya Sajan', 'Catherine Dooley', 'Piper Buck', 'Ferzine Sanjana', 'Carly Schmidt', 'Hana Sawaf', 'Aliyana Martinez', 'Sophie Shapiro']
CountryDancing = ['Elyse Miller']
Dancing = ['Maya Abraham', 'Amelia Klyap', 'Kaitlin Black', 'Alexandra Nicholls', 'Kate Neiman', 'Shelby', 'Sofia Arroyo', 'Erika Sandberg', 'Meadow Votis', 'Ava Dahlander', 'Madeleine Mazingo', 'Diyaa Dossani', 'Isabella Bartz', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'madison taylor', 'Jessica Paine', 'Jillian Taylor', 'Katelyn Quintanilla', 'Abrielle Gallini', 'Ellen Meltzer', 'Chloe Lim', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Ollie Mae Harrison', 'Kirthi Gummadi', 'zoe alvarado', 'Claire Savage', 'georgia key', 'sarah thompson', 'Gabrielle Green', 'Sienna Shutts', 'Larkin Seidel', 'Catalina Cruz', 'Kamryn Jean', 'Emily Robles', 'Brooke Walker', 'Rishona Mopur']
ExploringAustin = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Delaney Vanderpool', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Gabrielle Beck', 'Riley avery', 'Kate Neiman', 'Katie Walsh', 'Shelby', 'Sofia Arroyo', 'Erika Sandberg', 'Liz Keegan', 'Meadow Votis', 'Ava Dahlander', 'Ava Hurst', 'Heidi Chapin', 'Ellie Berman', 'Diyaa Dossani', 'Isabella Bartz', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'madison taylor', 'Jessica Paine', 'Jillian Taylor', 'Katelyn Quintanilla', 'Abrielle Gallini', 'Ellen Meltzer', 'Chloe Lim', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Ollie Mae Harrison', 'Kirthi Gummadi', 'sarah solomon', 'Avery McClure', 'Haylee Martin', 'Krissily Estacio', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Brianna', 'Ella Leininger', 'Emily Bull', 'Taylor Jennings', 'Delaney OÃ¢â‚¬â„¢Brien', 'Jannae Ailawadhi', 'Mia Vasquez', 'Anika Novak', 'Chasiti Tyeryar', 'Alice Hudson', 'Lola Daffin', 'Megan Garza', 'Emma Schneidau', 'Katie Windell', 'Allie Harter', 'Suzie Hudgens', 'Audrey Cooper', 'Abby Sanders', 'Hazel Wells', 'Marley Page', 'Hannah Greenhill', 'Meredith Moreland', 'Emmerich Benavides', 'Anna Woodson', 'Zoe Veliz', 'Elyse Miller', 'Ella Pitts', 'Celeste Tomberlin', 'Mazzy Bledsoe', 'Catherine Favoriti', 'Larkin Seidel', 'Catalina Cruz', 'Kamryn Jean', 'Genesis Martinez', 'Abby OGuynn', 'Maggie Shaw', 'Brianna Salaices', 'meghna sunkureddi', 'Alyssa Bouloy', 'Izzy Davies', 'Haley Hooper ', 'Josie Mandrea', 'Hana Sawaf', 'Aliyana Martinez', 'Sophie Shapiro']
FieldHockeyfun = ['Valentina Markov', 'Katie Walsh', 'Bridget Flatow']
Fishing = ['Julia Lindstrom', 'Valentina Markov', 'Sarah Sims', 'Lindsay McCullough', 'Kaitlin Black', 'Sofia Arroyo', 'Emerson Oliver', 'Meadow Votis', 'sarah solomon', 'Jenn Rosado']
Football = ['Valentina Markov', 'Emerson Oliver']
Golfingfun = ['Caitlin Van Sant', 'Bella Champion', 'Riley avery', 'Katie Walsh', 'Mae Trahan', 'Diyaa Dossani', 'Isabella Bartz', 'Avery McClure', 'Haylee Martin', 'Emily Robles']
Hiking = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Morgan Baumel', 'Delaney Vanderpool', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley avery', 'Kate Neiman', 'Shelby', 'Liz Keegan', 'Meadow Votis', 'Ava Hurst', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'madison taylor', 'Jessica Paine', 'Jillian Taylor', 'Katelyn Quintanilla', 'Krissily Estacio', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Brianna', 'Ella Leininger', 'Emily Bull', 'Taylor Jennings', 'Kaylie Ngo', 'Abby OGuynn', 'Maggie Shaw', 'Bella Wernli', 'Haley Hooper', 'Josie Mandrea', 'Hana Sawaf', 'Sophie shapiro']
HorsebackRiding = ['Valentina Markov', 'Kate Neiman', 'Ava Hurst', 'Diyaa Dossani', 'Sydney Fern', 'Abrielle Gallini', 'Delaney OÃ¢â‚¬â„¢Brien']
Hunting = ['Valentina Markov', 'Karlie Haigood', 'Kaitlin Black', 'Sofia Arroyo', 'Meadow Votis', 'sarah solomon']
IceSkating = ['Sydney Fern', 'Rachel Dolan', 'Krissily Estacio']
Lacrossefun = ['Emerson Oliver', 'Jannae Ailawadhi', 'Mia Vasquez']
PaddleboardingKayaking = ['Julia Lindstrom', 'Caitlin Van Sant', 'Delaney Vanderpool', 'Lindsay McCullough', 'Riley avery', 'Erika Sandberg', 'Ava Dahlander', 'Ava Hurst', 'Sydney Fern', 'Sophie Robins', 'Hailey Brooks', 'Abrielle Gallini', 'sarah solomon', 'Krissily Estacio', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Brianna', 'Ella Leininger', 'Jannae Ailawadhi', 'Anika Novak', 'Chasiti Tyeryar', 'Alice Hudson', 'Lola Daffin', 'Megan Garza', 'Emma Schneidau', 'Katie Windell', 'Abby OGuynn', 'Brianna Salaices', 'Arabella Savener', 'Josie Mandrea', 'Hana Sawaf', 'Aliyana Martinez', 'Sophie shapiro']
Pickleball = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Bella Champion', 'Lindsay McCullough', 'Kaitlin Black', 'Riley Wanasek', 'Erika Sandberg', 'Isabella Bartz', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'madison taylor', 'Ellen Meltzer', 'zoe alvarado', 'Avery McClure', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Brianna', 'Emily Bull', 'Jannae Ailawadhi', 'Anika Novak', 'Chasiti Tyeryar', 'Alice Hudson', 'Allie Harter', 'Suzie Hudgens', 'Audrey Cooper', 'Abby Sanders', 'Hazel Wells', 'Nidhi Pappu', 'Larkin Seidel', 'Emily Robles', 'Maggie Shaw', 'Brianna Salaices', 'meghna sunkureddi', 'Angie Andersen', 'Haley hooper', 'Josie Mandrea', 'sophie shapiro']
Picnics = ['Caitlin Van Sant', 'Maya Abraham', 'Sarah Sims', 'Delaney Vanderpool', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Jovanni Carrillo', 'Riley avery', 'Shelby', 'Liz Keegan', 'Meadow Votis', 'Heidi Chapin', 'Isabella Bartz', 'Sydney Fern', 'Sophie Robins', 'Hailey Brooks', 'Jessica Paine', 'Chloe Lim', 'Haylee Martin', 'Krissily Estacio', 'Abby Alsup', 'Delaney OÃ¢â‚¬â„¢Brien', 'Anika Novak', 'Chasiti Tyeryar', 'Marley Page', 'Catalina Cruz', 'meghna sunkureddi', 'Alyssa Bouloy', 'Haley Hooper', 'sophie shapiro']
Pilates = ['Julia Lindstrom', 'Caitlin Van Sant', 'Maya Abraham', 'Bella Champion', 'Amelia Klyap', 'Lindsay McCullough', 'Jovanni Carrillo', 'Riley avery', 'Kate Neiman', 'Shelby', 'Heidi Chapin', 'Isabella Bartz', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'madison taylor', 'Jillian Taylor', 'Ellen Meltzer', 'Chloe Lim', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Ollie Mae Harrison', 'Claire Savage', 'georgia key', 'Krissily Estacio', 'Abby Kant', 'Taylor Jennings', 'Mia Vasquez', 'Alice Hudson', 'Lola Daffin', 'Allie Harter', 'Suzie Hudgens', 'Hannah Greenhill', 'Meredith Moreland', 'Nidhi Pappu', 'Maya Sajan', 'Catherine Dooley', 'Piper Buck', 'Larkin Seidel', 'Catalina Cruz', 'Emily Robles', 'Alyssa Bouloy', 'Izzy Davies', 'Josie Mandrea', 'Hana Sawaf']
RockClimbingfun = ['Caitlin Van Sant', 'Delaney Vanderpool', 'Gabrielle Beck', 'Katie Walsh', 'Heidi Chapin', 'Sophie Robins', 'Catalina Cruz', 'sophie shapiro']
RunningJoggingfun = ['Julia Lindstrom', 'Caitlin Van Sant', 'Sarah Sims', 'Delaney Vanderpool', 'Kaitlin Black', 'Gabrielle Beck', 'Riley avery', 'Riley Wanasek', 'Kate Neiman', 'Katie Walsh', 'Ava Dahlander', 'Isabella Bartz', 'Sophie Robins', 'Hailey Brooks', 'madison taylor', 'Katelyn Quintanilla', 'Abrielle Gallini', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Kirthi Gummadi', 'Krissily Estacio', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Emily Bull', 'Taylor Jennings', 'Jannae Ailawadhi', 'Lola Daffin', 'Allie Harter', 'Audrey Cooper', 'Hannah Greenhill', 'Emmerich Benavides', 'Maya Sajan', 'Larkin Seidel', 'Jenn Rosado', 'sophie shapiro ', 'sophie shapiro']
ScubaDiving = ['Valentina Markov', 'Kate Neiman', 'Hana Sawaf']
Soccerfun = ['Larkin Seidel']
Surfing = ['Julia Lindstrom', 'Kate Neiman', 'Lola Daffin', 'Brooke Walker', 'Hana Sawaf', 'Rishona Mopur']
SwimmingDivingfun = ['Julia Lindstrom', 'Bella Champion', 'Karlie Haigood', 'Charlize Stone', 'Amelia Klyap', 'Gabrielle Beck', 'Katie Walsh', 'madison taylor', 'Jillian Taylor', 'Ellen Meltzer', 'Chloe Lim', 'Krissily Estacio', 'Alice Hudson', 'Audrey Cooper', 'Anna Woodson', 'Catherine Dooley', 'Aliyana Martinez', 'sophie shapiro']
Tanning = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Delaney Vanderpool', 'Charlize Stone', 'Amelia Klyap', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley avery', 'Riley Wanasek', 'Kate Neiman', 'Erika Sandberg', 'Meadow Votis', 'Ava Dahlander', 'Ava Hurst', 'Heidi Chapin', 'Regan Hill', 'Sydney Fern', 'Sophie Robins', 'Hailey Brooks', 'madison taylor', 'Jillian Taylor', 'Abrielle Gallini', 'Ellen Meltzer', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Ollie Mae Harrison', 'georgia key', 'sarah thompson', 'Avery McClure', 'Haylee Martin', 'Abby Alsup', 'Abby Kant', 'Bailey Alsup', 'Ella Leininger', 'Emily Bull', 'Taylor Jennings', 'Anika Novak', 'Chasiti Tyeryar', 'Alice Hudson', 'Lola Daffin', 'Megan Garza', 'Abby Sanders', 'Hazel Wells', 'Marley Page', 'Emmerich Benavides', 'Anna Woodson', 'Zoe Veliz', 'Elyse Miller', 'Ella Pitts', 'Kaylie Ngo', 'Piper Buck', 'Larkin Seidel', 'Catalina Cruz', 'Emily Robles', 'Alyssa Bouloy', 'Izzy Davies', 'Jenn Rosado', 'Bella Wernli', 'Jasmine Valdez', 'Hana Sawaf', 'Aliyana Martinez']
Tennisfun = ['Riley Wanasek', 'Kate Neiman', 'Rachel Dolan', 'Sophie Robins', 'Jessica Paine', 'Ellen Meltzer', 'Abby Sanders', 'Hazel Wells', 'Catherine Dooley', 'Ferzine Sanjana', 'Catalina Cruz', 'Emily Robles', 'Maggie Shaw', 'Angie Andersen', 'sophie shapiro']
Thrifting = ['Julia Lindstrom', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Morgan Baumel', 'Delaney Vanderpool', 'Amelia Klyap', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Emerson Oliver', 'Meadow Votis', 'Ava Hurst', 'Heidi Chapin', 'Ellie Berman', 'Regan Hill', 'Diyaa Dossani', 'Isabella Bartz', 'Sophie Robins', 'madison taylor', 'Jessica Paine', 'Katelyn Quintanilla', 'Ellen Meltzer', 'Chloe Lim', 'Kirthi Gummadi', 'Krissily Estacio', 'Abby Alsup', 'Ella Leininger', 'Taylor Jennings', 'Delaney OÃ¢â‚¬â„¢Brien', 'Jannae Ailawadhi', 'Lola Daffin', 'Emma Schneidau', 'Katie Windell', 'Marley Page', 'Hannah Greenhill', 'Elyse Miller', 'Celeste Tomberlin', 'Carly Schmidt', 'Catalina Cruz', 'Emily Robles', 'Abby OGuynn', 'Izzy Davies', 'Bridget Flatow']
Traveling = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Morgan Baumel', 'Delaney Vanderpool', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley avery', 'Kate Neiman', 'Shelby', 'Sofia Arroyo', 'Erika Sandberg', 'Liz Keegan', 'Meadow Votis', 'Ava Dahlander', 'Ava Hurst', 'Ellie Berman', 'Regan Hill', 'Diyaa Dossani', 'Isabella Bartz', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'madison taylor', 'Jessica Paine', 'Jillian Taylor', 'Bella Anderson', 'zoe alvarado', 'georgia key', 'Haylee Martin', 'Krissily Estacio', 'Abby Alsup', 'Abby Kant', 'Brianna', 'Ella Leininger', 'Emily Bull', 'Taylor Jennings', 'Jannae Ailawadhi', 'Mia Vasquez', 'Anika Novak', 'Lola Daffin', 'Emma Schneidau', 'Abby Sanders', 'Hazel Wells', 'Marley Page', 'Meredith Moreland', 'Emmerich Benavides', 'Elyse Miller', 'Ella Pitts', 'Celeste Tomberlin', 'Mazzy Bledsoe', 'Catherine Favoriti', 'Kaylie Ngo', 'Catherine Dooley', 'Piper Buck', 'Carly Schmidt', 'Larkin Seidel', 'Emily Robles', 'meghna sunkureddi', 'Alyssa Bouloy', 'Izzy Davies', 'Bella Wernli', 'Josie Mandrea', 'Aliyana Martinez', 'Charlize Stone']
Triathlons = ['Katie Walsh']
Volleyballfun = ['Bella Champion', 'Gabrielle Beck', 'Kate Neiman', 'Meadow Votis', 'Sydney Fern', 'madison taylor', 'Maria Sepulveda Salazar', 'Abby Kant', 'Emmerich Benavides', 'Elyse Miller', 'Nidhi Pappu', 'Abby OGuynn', 'Bella Wernli']
WalksOutdoors = ['Julia Lindstrom', 'Caitlin Van Sant', 'Valentina Markov', 'Maya Abraham', 'Sarah Sims', 'Morgan Baumel', 'Delaney Vanderpool', 'Charlize Stone', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley avery', 'Kate Neiman', 'Shelby', 'Sofia Arroyo', 'Liz Keegan', 'Emerson Oliver', 'Ava Dahlander', 'Ellie Berman', 'Mae Trahan', 'Regan Hill', 'Isabella Bartz', 'Sydney Fern', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'madison taylor', 'Jessica Paine', 'Jillian Taylor', 'Katelyn Quintanilla', 'Ellen Meltzer', 'Bella Anderson', 'Maria Sepulveda Salazar', 'Kirthi Gummadi', 'sarah thompson', 'Abby Alsup', 'Bailey Alsup', 'Brianna', 'Ella Leininger', 'Emily Bull', 'Delaney OÃ¢â‚¬â„¢Brien', 'Jannae Ailawadhi', 'Chasiti Tyeryar', 'Lola Daffin', 'Emma Schneidau', 'Katie Windell', 'Allie Harter', 'Audrey Cooper', 'Abby Sanders', 'Hazel Wells', 'Marley Page', 'Hannah Greenhill', 'Emmerich Benavides', 'Elyse Miller', 'Kaylie Ngo', 'Nidhi Pappu', 'Maya Sajan', 'Catherine Dooley', 'Larkin Seidel', 'Kamryn Jean', 'Abby OGuynn', 'meghna sunkureddi', 'Alyssa Bouloy', 'Izzy Davies', 'Bella Wernli', 'Jasmine Valdez', 'Josie Mandrea', 'Aliyana Martinez', 'sophie shapiro']
WaterSkiing = ['Delaney Vanderpool', 'Gabrielle Beck', 'Erika Sandberg', 'Meadow Votis', 'Sophie Robins', 'Chasiti Tyeryar', 'Hana Sawaf', 'Rishona Mopur']
WorkingOut = ['Julia Lindstrom', 'Valentina Markov', 'Maya Abraham', 'Bella Champion', 'Karlie Haigood', 'Delaney Vanderpool', 'Amelia Klyap', 'Lindsay McCullough', 'Kaitlin Black', 'Alexandra Nicholls', 'Gabrielle Beck', 'Jovanni Carrillo', 'Riley Wanasek', 'Kate Neiman', 'Katie Walsh', 'Shelby', 'Sofia Arroyo', 'Meadow Votis', 'Heidi Chapin', 'Ellie Berman', 'Regan Hill', 'Diyaa Dossani', 'Isabella Bartz', 'Rachel Dolan', 'Sophie Robins', 'Hailey Brooks', 'madison taylor', 'Jillian Taylor', 'Abrielle Gallini', 'Ellen Meltzer', 'Chloe Lim', 'Maria Sepulveda Salazar', 'Kirthi Gummadi', 'georgia key', 'Avery McClure', 'Abby Alsup', 'Abby Kant', 'Emily Bull', 'Jannae Ailawadhi', 'Lola Daffin', 'Allie Harter', 'Audrey Cooper', 'Abby Sanders', 'Hazel Wells', 'Marley Page', 'Hannah Greenhill', 'Emmerich Benavides', 'Elyse Miller', 'Ella Pitts', 'Catherine Favoriti', 'Kaylie Ngo', 'Nidhi Pappu', 'Maya Sajan', 'Catherine Dooley', 'Piper Buck', 'Larkin Seidel', 'Emily Robles', 'meghna sunkureddi', 'Izzy Davies', 'Arabella Savener', 'Jasmine Valdez', 'Josie Mandrea', 'Hana Sawaf', 'Aliyana Martinez', 'sophie shaprio']
Yoga = ['Julia Lindstrom', 'Maya Abraham', 'Sarah Sims', 'Bella Champion', 'Amelia Klyap', 'Lindsay McCullough', 'Kate Neiman', 'Katie Walsh', 'Shelby', 'Sofia Arroyo', 'Erika Sandberg', 'Liz Keegan', 'Meadow Votis', 'Heidi Chapin', 'Ellie Berman', 'Diyaa Dossani', 'Isabella Bartz', 'Rachel Dolan', 'Sophie Robins', 'Jillian Taylor', 'Katelyn Quintanilla', 'Ellen Meltzer', 'Chloe Lim', 'Maria Sepulveda Salazar', 'Ollie Mae Harrison', 'georgia key', 'Avery McClure', 'Krissily Estacio', 'Abby Kant', 'Taylor Jennings', 'Jannae Ailawadhi', 'Mia Vasquez', 'Anika Novak', 'Alice Hudson', 'Lola Daffin', 'Katie Windell', 'Allie Harter', 'Suzie Hudgens', 'Abby Sanders', 'Hazel Wells', 'Hannah Greenhill', 'Elyse Miller', 'Catherine Favoriti', 'Nidhi Pappu', 'Maya Sajan', 'Piper Buck', 'Larkin Seidel', 'Catalina Cruz', 'Emily Robles', 'Izzy Davies', 'Jasmine Valdez', 'Haley Hooper', 'Josie Mandrea', 'Aliyana Martinez', 'sophie shapiro']
Animals = ['Sarah Sims', 'Shelby', 'Piper Buck', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'madison taylor', 'Kirthi Gummadi', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'zoe alvarado', 'Erika Sandberg', 'Riley avery', 'Bailey Alsup', 'Anika Novak', 'Delaney OÃ¢â‚¬â„¢Brien', 'sarah solomon', 'Liz Keegan', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Mae Trahan', 'Kaylie Ngo', 'Brianna', 'Alexandra Nicholls', 'Valentina Markov', 'Zoe Veliz', 'Sofia Arroyo', 'Emma Schneidau', 'Marley Page', 'Gabrielle Green', 'Karlie Haigood', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'Brianna Salaices', 'georgia key', 'Megan Garza', 'Catherine Favoriti', 'Audrey Cooper', 'Kamryn Jean', 'Meredith Moreland', 'Hana Sawaf', '', 'Aliyana Martinez']
ArtsandCrafts = ['Sarah Sims', 'Shelby', 'Piper Buck', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'madison taylor', 'Kirthi Gummadi', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'zoe alvarado', 'Erika Sandberg', 'Riley avery', 'Bailey Alsup', 'Anika Novak', 'Delaney OÃ¢â‚¬â„¢Brien', 'sarah solomon', 'Liz Keegan', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'meghna sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'sarah thompson', 'Angie Andersen', 'Gabrielle Beck', 'Bella Champion', 'Catalina Cruz', 'Isabella Bartz', 'Katie Windell', 'Jillian Taylor', 'Ferzine Sanjana', 'Abby Sanders', 'Alyssa Bouloy', 'Jenn Rosado', 'Carly Schmidt', 'Haley Hooper']
Baking = ['Sarah Sims', 'Shelby', 'Piper Buck', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'madison taylor', 'Kirthi Gummadi', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'zoe alvarado', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Mae Trahan', 'Kaylie Ngo', 'Brianna', 'Alexandra Nicholls', 'Valentina Markov', 'Zoe Veliz', 'Sofia Arroyo', 'Emma Schneidau', 'Marley Page', 'Gabrielle Green', 'Karlie Haigood', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'meghna sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'sarah thompson', 'Angie Andersen', 'Gabrielle Beck', 'Rachel Dolan', 'Anna Woodson', 'Maggie Shaw', 'Suzie Hudgens', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Jannae Ailawadhi', 'Allie Harter', 'Ella Pitts', 'Emmerich Benavides', 'Haylee Martin', 'Madeleine Mazingo', 'Avery McClure', 'Arabella Savener', 'Abby OGuynn', 'Catherine Dooley', 'Haley Hooper']
Boardgames = ['Sarah Sims', 'Shelby', 'Erika Sandberg', 'Ella Leininger', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'meghna sunkureddi', 'Bella Champion', 'Catalina Cruz', 'Rachel Dolan', 'Anna Woodson']
CoffeeTea = ['Sarah Sims', 'Piper Buck', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'madison taylor', 'Erika Sandberg', 'Riley avery', 'Bailey Alsup', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Mae Trahan', 'Kaylie Ngo', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'Brianna Salaices', 'georgia key', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'meghna sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'sarah thompson', 'Bella Champion', 'Isabella Bartz', 'Katie Windell', 'Jillian Taylor', 'Ferzine Sanjana', 'Abby Sanders', 'Alyssa Bouloy', 'Rachel Dolan', 'Maggie Shaw', 'Suzie Hudgens', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Jannae Ailawadhi', 'Allie Harter', 'Ella Pitts', 'Emmerich Benavides', 'Haylee Martin', 'Madeleine Mazingo', 'Avery McClure', 'Diyaa Dossani', 'Hazel Wells', 'Maya Sajan', 'Ollie Mae Harrison', 'Mia Vasquez', 'Ava Dahlander', 'Taylor Jennings', 'Riley Wanasek', 'Lindsay McCullough', 'Alice Hudson', 'Delaney Vanderpool', 'Elyse Miller', 'Sienna Shutts', 'Hailey Brooks', 'Bella Wernli', 'Celeste Tomberlin', 'Abby Kant', 'Chasiti Tyeryar', 'Genesis Martinez', 'Emily Robles', 'Josie Mandrea', 'Aliyana Martinez']
Cooking = ['Sarah Sims', 'Piper Buck', 'Kirthi Gummadi', 'Jovanni Carrillo', 'Riley avery', 'Anika Novak', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Brianna', 'Alexandra Nicholls', 'Valentina Markov', 'Ava Hurst', 'Megan Garza', 'Catherine Favoriti', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'meghna sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'Angie Andersen', 'Gabrielle Beck', 'Isabella Bartz', 'Jenn Rosado', 'Rachel Dolan', 'Anna Woodson', 'Suzie Hudgens', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Jannae Ailawadhi', 'Allie Harter', 'Ella Pitts', 'Arabella Savener', 'Diyaa Dossani', 'Hazel Wells', 'Maya Sajan', 'Ollie Mae Harrison', 'Mia Vasquez', 'Heidi Chapin', 'Haley Hooper', 'Hana Sawaf']
CrochetKnitting = ['Amelia Klyap', 'Kirthi Gummadi', 'Delaney OÃ¢â‚¬â„¢Brien', 'Krissily Estacio', 'Zoe Veliz', 'Lola Daffin', 'sarah thompson', 'Angie Andersen', 'Catalina Cruz', 'Katie Windell', 'Suzie Hudgens', 'Arabella Savener', 'Ava Dahlander', 'Haley Hooper']
Drawing = ['Piper Buck', 'Chloe Lim', 'Sophie Robins', 'Erika Sandberg', 'Riley avery', 'Delaney OÃ¢â‚¬â„¢Brien', 'Mae Trahan', 'Ellen Meltzer', 'sarah thompson', 'Angie Andersen', 'Bella Champion', 'Catalina Cruz', 'Jenn Rosado', 'Abby OGuynn', 'Regan Hill']
ExploringNewRestaurants = ['Sarah Sims', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'madison taylor', 'Kirthi Gummadi', 'Sophie Robins', 'Erika Sandberg', 'Riley avery', 'Bailey Alsup', 'Anika Novak', 'sarah solomon', 'Liz Keegan', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Zoe Veliz', 'Sofia Arroyo', 'Emma Schneidau', 'Hannah Greenhill', 'Morgan Baumel', 'Audrey Cooper', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'meghna sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'sarah thompson', 'Angie Andersen', 'Bella Champion', 'Catalina Cruz', 'Jillian Taylor', 'Rachel Dolan', 'Anna Woodson', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Jannae Ailawadhi', 'Emmerich Benavides', 'Haylee Martin', 'Catherine Dooley', 'Ava Dahlander', 'Taylor Jennings', 'Riley Wanasek', 'Lindsay McCullough', 'Alice Hudson', 'Delaney Vanderpool', 'Elyse Miller', 'Sienna Shutts', 'Regan Hill', 'Caitlin Van Sant', 'Bella Anderson', 'Haley Hooper', 'Hana sawaf']
Formula1 = ['Sarah Sims', 'Liz Keegan', 'Brianna Salaices', 'sarah thompson', 'Carly Schmidt', 'Suzie Hudgens', 'Diyaa Dossani', 'Taylor Jennings', 'Regan Hill', 'Brooke Walker', 'Nidhi Pappu']
Governmentfun = ['Sarah Sims', 'Piper Buck', 'Chloe Lim', 'Abby Alsup', 'Jovanni Carrillo', 'Zoe Veliz', 'Hannah Greenhill', 'Morgan Baumel', 'Ellen Meltzer', 'Maya Abraham', 'Catalina Cruz', 'Ferzine Sanjana', 'Kaitlin Black', 'Arabella Savener', 'Riley Wanasek', 'Hailey Brooks', 'Bella Wernli', 'Heidi Chapin', 'Katie Walsh', 'Ellie Berman', 'Charlize Stone', 'Josey Mandrea', 'Aliyana Martinez', 'Aliyana Martinez']
GraphicDesign = ['Liz Keegan', 'Maya Abraham', 'Catalina Cruz', 'Carly Schmidt', 'Celeste Tomberlin']
Health = ['Shelby', 'Mazzy Bledsoe', 'Bailey Alsup', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Sofia Arroyo', 'Brianna Salaices', 'Megan Garza', 'Kamryn Jean', 'Sydney Fern', 'Lola Daffin', 'Bella Champion', 'Isabella Bartz', 'Abby Sanders', 'Rachel Dolan', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Emmerich Benavides', 'Hazel Wells', 'Maya Sajan', 'Lindsay McCullough', 'Alice Hudson', 'Abby Kant', 'Regan Hill', 'Caitlin Van Sant', 'Emerson Oliver', 'Josie Mandrea', 'Hana sawaf']
Instagram = ['Sarah Sims', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'madison taylor', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'Erika Sandberg', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Mae Trahan', 'Emma Schneidau', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'georgia key', 'Catherine Favoriti', 'Audrey Cooper', 'Sydney Fern', 'meghna sunkureddi', 'Maya Abraham', 'Katelyn Quintanilla', 'Angie Andersen', 'Bella Champion', 'Catalina Cruz', 'Isabella Bartz', 'Jillian Taylor', 'Ferzine Sanjana', 'Abby Sanders', 'Alyssa Bouloy', 'Jenn Rosado', 'Carly Schmidt', 'Kaitlin Black', 'Izzy Davies', 'Maria Sepulveda Salazar', 'Ella Pitts', 'Haylee Martin', 'Avery McClure', 'Diyaa Dossani', 'Hazel Wells', 'Maya Sajan', 'Ava Dahlander', 'Taylor Jennings', 'Alice Hudson', 'Elyse Miller', 'Sienna Shutts', 'Hailey Brooks', 'Celeste Tomberlin', 'Chasiti Tyeryar', 'Genesis Martinez', 'Emily Robles', 'Heidi Chapin', 'Regan Hill', 'Bella Anderson', 'Brooke Walker', 'Katie Walsh', 'Abrielle Gallini']
ListeningtoMusic = ['Sarah Sims', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'madison taylor', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'zoe alvarado', 'Erika Sandberg', 'Riley avery', 'Bailey Alsup', 'Anika Novak', 'Delaney OÃ¢â‚¬â„¢Brien', 'Liz Keegan', 'Ella Leininger', 'Kate Neiman', 'Larkin Seidel', 'Krissily Estacio', 'Mae Trahan', 'Kaylie Ngo', 'Brianna', 'Alexandra Nicholls', 'Valentina Markov', 'Zoe Veliz', 'Sofia Arroyo', 'Emma Schneidau', 'Marley Page', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'georgia key', 'Megan Garza', 'Catherine Favoriti', 'Audrey Cooper', 'Kamryn Jean', 'Meredith Moreland', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'meghna sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'sarah thompson', 'Angie Andersen', 'Gabrielle Beck', 'Bella Champion', 'Catalina Cruz', 'Jillian Taylor', 'Ferzine Sanjana', 'Jenn Rosado', 'Carly Schmidt', 'Rachel Dolan', 'Anna Woodson', 'Suzie Hudgens', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Jannae Ailawadhi', 'Allie Harter', 'Ella Pitts', 'Emmerich Benavides', 'Haylee Martin', 'Madeleine Mazingo', 'Avery McClure', 'Arabella Savener', 'Abby OGuynn', 'Catherine Dooley', 'Diyaa Dossani', 'Hazel Wells', 'Maya Sajan', 'Ollie Mae Harrison', 'Ava Dahlander', 'Taylor Jennings', 'Riley Wanasek', 'Lindsay McCullough', 'Delaney Vanderpool', 'Elyse Miller', 'Sienna Shutts', 'Hailey Brooks', 'Celeste Tomberlin', 'Abby Kant', 'Chasiti Tyeryar', 'Genesis Martinez', 'Heidi Chapin', 'Regan Hill', 'Bella Anderson', 'Katie Walsh', 'Emerson Oliver', 'Claire Savage', 'Jasmine Valdez', 'Josie Mandrea', 'Hana sawaf']
Musicals = ['Sarah Sims', 'Amelia Klyap', 'Sophie Robins', 'zoe alvarado', 'Liz Keegan', 'Krissily Estacio', 'Mae Trahan', 'Brianna', 'Alexandra Nicholls', 'Zoe Veliz', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'Katelyn Quintanilla', 'Isabella Bartz', 'Jillian Taylor', 'Ferzine Sanjana', 'Alyssa Bouloy', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Ella Pitts', 'Arabella Savener', 'Diyaa Dossani', 'Hazel Wells', 'Ava Dahlander', 'Delaney Vanderpool', 'Regan Hill', 'Emerson Oliver']
Pageants = ['Catalina Cruz']
Painting = ['Shelby', 'Piper Buck', 'Chloe Lim', 'Abby Alsup', 'Jovanni Carrillo', 'Sophie Robins', 'Riley avery', 'Bailey Alsup', 'Ava Hurst', 'Ellen Meltzer', 'Meadow Votis', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'sarah thompson', 'Angie Andersen', 'Gabrielle Beck', 'Catalina Cruz', 'Haley Hooper']
Philosophyfun = ['Marley Page', 'Lola Daffin', 'Suzie Hudgens', 'Hailey Brooks', 'Sophie Shapiro,']
Photography = ['Amelia Klyap', 'Chloe Lim', 'Kirthi Gummadi', 'Jovanni Carrillo', 'Liz Keegan', 'Julia Lindstrom', 'Kaylie Ngo', 'Zoe Veliz', 'Marley Page', 'Ava Hurst', 'Jessica Paine', 'Lola Daffin', 'Maya Abraham', 'sarah thompson', 'Gabrielle Beck', 'Carly Schmidt', 'Kaitlin Black', 'Ava Dahlander', 'Lindsay McCullough', 'Elyse Miller', 'Sienna Shutts', 'Regan Hill', 'Bella Anderson', 'Abrielle Gallini', 'Josie Mandrea']
PlayingaBrassInstrument = ['Amelia Klyap', 'Suzie Hudgens']
PlayingaPercussionInstrument = ['Chloe Lim', 'Valentina Markov', 'Marley Page', 'Ava Hurst', 'Angie Andersen', 'Kaitlin Black', 'Maria Sepulveda Salazar', 'Arabella Savener', 'Abrielle Gallini']
PlayingaStringInstrument = ["Delaney O'Brien", 'Krissily Estacio', 'Marley Page', 'Lola Daffin', 'Gabrielle Beck', 'Madeleine Mazingo', 'Arabella Savener', 'Elyse Miller', 'Bella Wernli', 'Brooke Walker']
PlayingaWindInstrument = ['Kirthi Gummadi', 'Marley Page', 'Maya Abraham', 'Ferzine Sanjana']
Podcasts = ['madison taylor', 'Jovanni Carrillo', 'Erika Sandberg', 'Julia Lindstrom', 'Krissily Estacio', 'Sofia Arroyo', 'Marley Page', 'Kamryn Jean', 'Meredith Moreland', 'Sydney Fern', 'Jessica Paine', 'Maya Abraham', 'Katelyn Quintanilla', 'Jillian Taylor', 'Ferzine Sanjana', 'Anna Woodson', 'Izzy Davies', 'Taylor Jennings', 'Elyse Miller', 'Hailey Brooks', 'Bella Wernli', 'Emerson Oliver', 'Josie Mandrea']
PotteryCeramics = ['Shelby', 'Chloe Lim', 'Jovanni Carrillo', 'Riley avery', 'Liz Keegan', 'Krissily Estacio', 'Meadow Votis', 'Lola Daffin', 'Maya Abraham', 'Angie Andersen', 'Katie Windell', 'Heidi Chapin', '', 'Aliyana Martinez']
Reading = ['Sarah Sims', 'Shelby', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'zoe alvarado', 'Bailey Alsup', 'Anika Novak', 'Liz Keegan', 'Kate Neiman', 'Krissily Estacio', 'Kaylie Ngo', 'Brianna', 'Zoe Veliz', 'Emma Schneidau', 'georgia key', 'Kamryn Jean', 'Ellen Meltzer', 'Sydney Fern', 'Jessica Paine', 'Lola Daffin', 'Maya Abraham', 'sarah thompson', 'Gabrielle Beck', 'Bella Champion', 'Isabella Bartz', 'Katie Windell', 'Jillian Taylor', 'Ferzine Sanjana', 'Alyssa Bouloy', 'Jenn Rosado', 'Carly Schmidt', 'Rachel Dolan', 'Anna Woodson', 'Suzie Hudgens', 'Kaitlin Black', 'Izzy Davies', 'Jannae Ailawadhi', 'Ella Pitts', 'Haylee Martin', 'Madeleine Mazingo', 'Arabella Savener', 'Diyaa Dossani', 'Hazel Wells', 'Maya Sajan', 'Ollie Mae Harrison', 'Mia Vasquez', 'Ava Dahlander', 'Taylor Jennings', 'Riley Wanasek', 'Delaney Vanderpool', 'Elyse Miller', 'Celeste Tomberlin', 'Abby Kant', 'Heidi Chapin', 'Regan Hill', 'Caitlin Van Sant', 'Bella Anderson', 'Nidhi Pappu', 'Abrielle Gallini']
RoadTrips = ['Sarah Sims', 'Abby Alsup', 'Sophie Robins', 'Mazzy Bledsoe', 'zoe alvarado', 'Erika Sandberg', 'Riley avery', 'Bailey Alsup', 'Liz Keegan', 'Kaylie Ngo', 'Valentina Markov', 'Emma Schneidau', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'georgia key', 'Audrey Cooper', 'Kamryn Jean', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'meghna sunkureddi', 'Lola Daffin', 'Maya Abraham', 'Gabrielle Beck', 'Bella Champion', 'Katie Windell', 'Jillian Taylor', 'Suzie Hudgens', 'Kaitlin Black', 'Izzy Davies', 'Jannae Ailawadhi', 'Ella Pitts', 'Emmerich Benavides', 'Haylee Martin', 'Diyaa Dossani', 'Mia Vasquez', 'Riley Wanasek', 'Delaney Vanderpool', 'Bella Wernli', 'Chasiti Tyeryar', 'Regan Hill', 'Ellie Berman', 'Abrielle Gallini', 'Hana sawaf']
ScienceMarineScienceEcology = ['Amelia Klyap', 'Julia Lindstrom', 'Krissily Estacio', 'Ellen Meltzer', 'Lola Daffin', 'Bella Champion', 'Anna Woodson', 'Izzy Davies', 'Madeleine Mazingo', 'Mia Vasquez', 'Regan Hill', 'Caitlin Van Sant', 'Hana Sawaf']
Scrapbooking = ['Shelby', 'Chloe Lim', 'madison taylor', 'Sophie Robins', 'zoe alvarado', 'Erika Sandberg', 'Anika Novak', 'Meadow Votis', 'Jessica Paine', 'meghna sunkureddi', 'Maya Abraham', 'Katelyn Quintanilla', 'Angie Andersen', 'Gabrielle Beck', 'Isabella Bartz', 'Delaney Vanderpool', 'Celeste Tomberlin', 'Haley Hooper']
Sewing = ['Jessica Paine']
Shopping = ['Sarah Sims', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'madison taylor', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'zoe alvarado', 'Riley avery', 'Anika Novak', 'Liz Keegan', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Kaylie Ngo', 'Alexandra Nicholls', 'Zoe Veliz', 'Sofia Arroyo', 'Emma Schneidau', 'Marley Page', 'Ava Hurst', 'Hannah Greenhill', 'Brianna Salaices', 'georgia key', 'Catherine Favoriti', 'Audrey Cooper', 'Kamryn Jean', 'Meredith Moreland', 'Ellen Meltzer', 'Sydney Fern', 'Meadow Votis', 'Jessica Paine', 'meghna sunkureddi', 'Maya Abraham', 'Katelyn Quintanilla', 'Gabrielle Beck', 'Bella Champion', 'Catalina Cruz', 'Isabella Bartz', 'Jillian Taylor', 'Ferzine Sanjana', 'Alyssa Bouloy', 'Jenn Rosado', 'Rachel Dolan', 'Anna Woodson', 'Kaitlin Black', 'Izzy Davies', 'Emily Bull', 'Maria Sepulveda Salazar', 'Jannae Ailawadhi', 'Ella Pitts', 'Emmerich Benavides', 'Madeleine Mazingo', 'Avery McClure', 'Catherine Dooley', 'Maya Sajan', 'Taylor Jennings', 'Riley Wanasek', 'Lindsay McCullough', 'Elyse Miller', 'Sienna Shutts', 'Bella Wernli', 'Celeste Tomberlin', 'Chasiti Tyeryar', 'Emily Robles', 'Heidi Chapin', 'Regan Hill', 'Caitlin Van Sant', 'Bella Anderson', 'Jasmine Valdez', 'Abrielle Gallini', 'Josie Mandrea', 'Aliyana Martinez']
Singing = ['Chloe Lim', 'Liz Keegan', 'Krissily Estacio', 'Kaylie Ngo', 'Valentina Markov', 'Marley Page', 'Ava Hurst', 'Catherine Favoriti', 'Ellen Meltzer', 'Meadow Votis', 'Jessica Paine', 'Katelyn Quintanilla', 'Jenn Rosado', 'Kaitlin Black', 'Arabella Savener', 'Diyaa Dossani', 'Maya Sajan', 'Ava Dahlander', 'Regan Hill', 'Bella Anderson', 'Katie Walsh', 'Emerson Oliver']
Skincare = ['Sarah Sims', 'Chloe Lim', 'madison taylor', 'Jovanni Carrillo', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Kaylie Ngo', 'Emma Schneidau', 'Gabrielle Green', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'georgia key', 'Megan Garza', 'Catherine Favoriti', 'Audrey Cooper', 'Kamryn Jean', 'Meredith Moreland', 'Ellen Meltzer', 'Jessica Paine', 'meghna sunkureddi', 'Lola Daffin', 'Bella Champion', 'Catalina Cruz', 'Isabella Bartz', 'Jillian Taylor', 'Rachel Dolan', 'Izzy Davies', 'Maria Sepulveda Salazar', 'Ella Pitts', 'Avery McClure', 'Hazel Wells', 'Maya Sajan', 'Ollie Mae Harrison', 'Ava Dahlander', 'Taylor Jennings', 'Lindsay McCullough', 'Abby Kant', 'Emily Robles', 'Heidi Chapin', 'Caitlin Van Sant', 'Jasmine Valdez', 'Josie Mandrea']
SocialMedia = ['Sarah Sims', 'Amelia Klyap', 'Chloe Lim', 'Abby Alsup', 'madison taylor', 'Jovanni Carrillo', 'Sophie Robins', 'Mazzy Bledsoe', 'Erika Sandberg', 'Ella Leininger', 'Kate Neiman', 'Julia Lindstrom', 'Larkin Seidel', 'Krissily Estacio', 'Mae Trahan', 'Emma Schneidau', 'Ava Hurst', 'Hannah Greenhill', 'Morgan Baumel', 'georgia key', 'Catherine Favoriti', 'Audrey Cooper', 'Sydney Fern', 'meghna sunkureddi', 'Maya Abraham', 'Katelyn Quintanilla', 'Angie Andersen', 'Bella Champion', 'Catalina Cruz', 'Isabella Bartz', 'Jillian Taylor', 'Ferzine Sanjana', 'Abby Sanders', 'Alyssa Bouloy', 'Jenn Rosado', 'Carly Schmidt', 'Kaitlin Black', 'Izzy Davies', 'Maria Sepulveda Salazar', 'Ella Pitts', 'Haylee Martin', 'Avery McClure', 'Diyaa Dossani', 'Hazel Wells', 'Maya Sajan', 'Ava Dahlander', 'Taylor Jennings', 'Alice Hudson', 'Elyse Miller', 'Sienna Shutts', 'Hailey Brooks', 'Celeste Tomberlin', 'Chasiti Tyeryar', 'Genesis Martinez', 'Emily Robles', 'Heidi Chapin', 'Regan Hill', 'Bella Anderson', 'Brooke Walker', 'Katie Walsh', 'Abrielle Gallini']
VideoGames = ['Sarah Sims']
Vlogging = ['Piper Buck', 'madison taylor', 'Sophie Robins', 'Kate Neiman', 'Catherine Favoriti', 'Katelyn Quintanilla', 'Catalina Cruz', 'Jillian Taylor', 'Carly Schmidt', 'Anna Woodson', 'Emily Robles', 'Regan Hill', 'Brooke Walker', 'Nidhi Pappu']
WatchingSports = ['Julia Lindstrom']
WatchingTVMovies = ['Julia Lindstrom']
Writing = ['Sarah Sims', 'Chloe Lim', 'Kate Neiman', 'Marley Page', 'Ellen Meltzer', 'Jessica Paine', 'Lola Daffin', 'Maya Abraham', 'Katelyn Quintanilla', 'Isabella Bartz', 'Kaitlin Black', 'Diyaa Dossani', 'Elyse Miller', 'Bella Wernli', 'Bella Anderson', 'Katie Walsh', 'Ellie Berman']
Karaoke = ['Morgan Baumel']
Plants = ['Morgan Baumel']
RollerCoasters = ['Morgan Baumel']

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
    "Religious Studies Minor": ReligiousStudiesMinor,
    "Stats And Data Science Minor": StatsandDataScienceMinor,
    "Creative Writing Minor": CreativeWritingMinor,
    "Korean Minor": KoreanMinor,
    "Chinese Minor": ChineseMinor,
    "Health Professions Minor": HealthProfessionsMinor,
    "Communicating Social Issues Minor": CommunicatingSocialIssuesMinor,
    "CommunicationStudiesMinor": CommunicationStudiesMinor,
    "ComputerScienceMinor": ComputerScienceMinor,
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
    "KinesiologyMinor": KinesiologyMinor,
    "Law Justice And Society Minor": LawJusticeAndSocietyMinor,
    "Media And Entertainment Industries Minor": MediaAndEntertainmentIndustriesMinor,
    "Physicians Assistant Minor": PhysiciansAssistantMinor,
    "PatientsPractitionersAndCareMinor": PatientsPractitionersAndCareMinor,
    "PreHealthMinor": PreHealthMinor,
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
    
# ===== Streamlit UI =====
st.title("Interest Finder")

def checkbox_columns(options, num_cols=2):
    """Creates a set of checkboxes split across columns and returns selected items."""
    cols = st.columns(num_cols)
    chunk_size = math.ceil(len(options) / num_cols)
    selected = []
    for i, option in enumerate(options):
        col = cols[i // chunk_size]
        if col.checkbox(option):
            selected.append(option)
    return selected

st.header("Majors"+'\U0001F4DA')
selected_majors = checkbox_columns(list(majors.keys()), num_cols=4)

st.header("Minors"+"\U0001F4DD")
selected_minors = checkbox_columns(list(minors.keys()), num_cols=4)

st.header("Hometowns"+"\U0001F3E0")
selected_hometowns = checkbox_columns(list(hometowns.keys()), num_cols=4)

st.header("High Schools"+"\U0001F3EB")
selected_schools = checkbox_columns(list(schools.keys()), num_cols=4)

st.header("HS Extracurriculars"+"\U0001F483")
selected_extras = checkbox_columns(list(extras.keys()), num_cols=4)

st.header("Activities/Interests for Fun"+"\U0001F3C3")
selected_activities = checkbox_columns(list(activities.keys()), num_cols=4)

selected_interests = selected_majors + selected_minors + selected_hometowns + selected_schools + selected_extras + selected_activities

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
        elif interest in hometowns:
            names = hometowns[interest]
        elif interest in schools:
            names = schools[interest]
        elif interest in extras:
            names = extras[interest]
        elif interest in activities:
            names = activities[interest]
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

    # Display
    st.subheader("✅ All Matches")
    if all_match:
        for name, matches in all_match:
            st.write(f"{name}: {', '.join(matches)}")
    else:
        st.write("(none)")

    st.subheader("🔹 Some Matches")
    if some_match:
        for name, matches in some_match:
            st.write(f"{name}: {', '.join(matches)}")
    else:
        st.write("(none)")

    st.subheader("⚪ One Match")
    if one_match:
        for name, matches in one_match:
            st.write(f"{name}: {', '.join(matches)}")
    else:
        st.write("(none)")