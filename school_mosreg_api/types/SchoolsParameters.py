from pydantic import BaseModel

class HobbyGroup(BaseModel):
    schoolId: int
    schoolId_str: str
    hobbyGroupName: str
    hobbyGroupDescription: str
    hobbyGroupSchedule: str
    hobbyGroupPayment: str = None
    hobbyGroupEnrollment: str


class LearningResult(BaseModel):
    schoolId: int
    schoolId_str: str
    studyYear: int
    prizesAtAllRussiaOlympiadPercentage: int = None
    basicCertificatesReceivedPercentage: int = None
    certificatesReceivedPercentage: int = None
    egeMathBaseLevelAverageScore: int = None
    egeMathProfileLevelAverageScore: int = None
    egeRussianAverageScore: int = None
    giaMathPassedPercentage: int = None
    giaMathPassedPerfectlyPercentage: int = None
    giaRussianPassedPercentage: int = None
    giaRussianPassedPerfectlyPercentage: int = None
    medalistsCount: int = None
    medalistsPercentage: int = None
    enrolledPercentage: int = None
    rankedInTheTop100: bool = None


class SchoolParameters(BaseModel):
    """[GET] /v2.0/schools/{school}/parameters\n~~~\nПараметры общеобразовательных организаций\n~~~"""
    
    schoolId: int
    schoolId_str: str
    municipality: str
    fullName: str
    shortName: str
    status: str
    foundationYear: int
    hasspecialty: bool
    specialty: str
    address: list[str]
    website: str
    email: str
    schoolPhone: str
    schoolDaysCount: int
    workHours: str
    shiftsCount: int
    eduOrgForm: str
    directorFullName: str
    directorPhone: str
    directorQualification: str
    directorPhoto: str
    licence: str
    accreditation: str
    charter: str
    cooperationName: str
    cooperationWebsite: str
    prescriptions: str
    activeJournalUrl: str
    inn: str
    facadePhoto: str
    cantinaPhoto: str
    gymPhoto: str
    classroomPhoto: str
    physicsroomPhoto: str
    chemicsryroomPhoto: str
    biologyroomPhoto: str
    mathroomPhoto: str
    russianroomPhoto: str
    musicroomPhoto: str
    educationalLevels: list[str]
    generalEducationalProgrammsLicense: str
    furtherEducationalProgramsLicense: str
    primarySchoolEducationalPrograms: list[str]
    hasAdaptedEducationalPrograms: bool = None
    hasOwnEducationalPrograms: bool = None
    ownEducationalPrograms: str
    hasDistEduTech: bool = None
    teachingForeignLanguages: list[str]
    studyPlan: str
    actualOccupancy: int = None
    designCapacity: int = None
    enrollmentIsOpen: bool = None
    vacantPlacesCount: int = None
    disabledChildrenCount: int = None
    firstStageGroupsCount: int = None
    secondStageGroupsCount: int = None
    thirdStageGroupsCount: int = None
    firstStageStudentsCount: int = None
    secondStageStudentsCount: int = None
    thirdStageStudentsCount: int = None
    teachersCount: int = None
    teachersWithHigherEducationCount: int = None
    highestCategoryTeachersCount: int = None
    publications: str
    laureatesOfContestsCount: str
    laureatesOfContestsInfo: str
    hasEducationalPsychologists: bool = None
    hasDefectologists: bool = None
    hasSpeechTherapists: bool = None
    hasSocialWorkers: bool = None
    hasMedicalWorkers: bool = None
    studentsPerComputer: int = None
    hasCompensatingClasses: bool = None
    hasBarrierFreeEnvironment: bool = None
    hasSwimmingPool: bool = None
    hasMedicalOffice: bool = None
    hasDiningRoom: bool = None
    hasGym: bool = None
    gymCount: int = None
    hasAssemblyHall: bool = None
    hasWinterGarden: bool = None
    hasCctv: bool = None
    hasGpd: bool = None
    schoolSiteArea: int = None
    hasEstheticZone: bool = None
    trainingExperimentalPlotArea: int = None
    hasSportArea: bool = None
    hasRecreationArea: bool = None
    hasZonesForTrainingInPreventionOfChildRoadTrafficInjuries: bool = None
    hasAreasOfEconomicPurpose: bool = None
    hobbyGroups: list[HobbyGroup]
    learningResults: list[LearningResult]
