from .model import Type

class HobbyGroup(Type):
    schoolId: int
    schoolId_str: str
    hobbyGroupName: str
    hobbyGroupDescription: str
    hobbyGroupSchedule: str
    hobbyGroupPayment: str | None | None = None
    hobbyGroupEnrollment: str


class LearningResult(Type):
    schoolId: int
    schoolId_str: str
    studyYear: int
    prizesAtAllRussiaOlympiadPercentage: int | None = None
    basicCertificatesReceivedPercentage: int | None = None
    certificatesReceivedPercentage: int | None = None
    egeMathBaseLevelAverageScore: int | None = None
    egeMathProfileLevelAverageScore: int | None = None
    egeRussianAverageScore: int | None = None
    giaMathPassedPercentage: int | None = None
    giaMathPassedPerfectlyPercentage: int | None = None
    giaRussianPassedPercentage: int | None = None
    giaRussianPassedPerfectlyPercentage: int | None = None
    medalistsCount: int | None = None
    medalistsPercentage: int | None = None
    enrolledPercentage: int | None = None
    rankedInTheTop100: bool | None = None


class SchoolParameters(Type):
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
    hasAdaptedEducationalPrograms: bool | None = None
    hasOwnEducationalPrograms: bool | None = None
    ownEducationalPrograms: str
    hasDistEduTech: bool | None = None
    teachingForeignLanguages: list[str]
    studyPlan: str
    actualOccupancy: int | None = None
    designCapacity: int | None = None
    enrollmentIsOpen: bool | None = None
    vacantPlacesCount: int | None = None
    disabledChildrenCount: int | None = None
    firstStageGroupsCount: int | None = None
    secondStageGroupsCount: int | None = None
    thirdStageGroupsCount: int | None = None
    firstStageStudentsCount: int | None = None
    secondStageStudentsCount: int | None = None
    thirdStageStudentsCount: int | None = None
    teachersCount: int | None = None
    teachersWithHigherEducationCount: int | None = None
    highestCategoryTeachersCount: int | None = None
    publications: str
    laureatesOfContestsCount: str
    laureatesOfContestsInfo: str
    hasEducationalPsychologists: bool | None = None
    hasDefectologists: bool | None = None
    hasSpeechTherapists: bool | None = None
    hasSocialWorkers: bool | None = None
    hasMedicalWorkers: bool | None = None
    studentsPerComputer: int | None = None
    hasCompensatingClasses: bool | None = None
    hasBarrierFreeEnvironment: bool | None = None
    hasSwimmingPool: bool | None = None
    hasMedicalOffice: bool | None = None
    hasDiningRoom: bool | None = None
    hasGym: bool | None = None
    gymCount: int | None = None
    hasAssemblyHall: bool | None = None
    hasWinterGarden: bool | None = None
    hasCctv: bool | None = None
    hasGpd: bool | None = None
    schoolSiteArea: int | None = None
    hasEstheticZone: bool | None = None
    trainingExperimentalPlotArea: int | None = None
    hasSportArea: bool | None = None
    hasRecreationArea: bool | None = None
    hasZonesForTrainingInPreventionOfChildRoadTrafficInjuries: bool | None = None
    hasAreasOfEconomicPurpose: bool | None = None
    hobbyGroups: list[HobbyGroup]
    learningResults: list[LearningResult]
