from . import api, types, exceptions, asyncapi

METHODS = {
    "Authorities": [
        "/v2.0/users/me/organizations",
        "/v2.0/users/me/organizations/{organizationId}"],
    "Authorizations": ["/v2.0/authorizations"],
    "AverageMarks": [
        "/v2.0/persons/{person}/reporting-periods/{period}/avg-mark",
        "/v2.0/persons/{person}/reporting-periods/{period}/subjects/{subject}/avg-mark",
        "/v2.0/edu-groups/{group}/reporting-periods/{period}/avg-marks/{date}",
        "/v2.0/edu-groups/{group}/avg-marks/{from}/{to}"],
    "Children": [
        "/v2.0/user/{userID}/children",
        "/v2.0/person/{personID}/children"],
    "Classmates": ["/v2.0/users/me/classmates"],
    "Context": [
        "/v2.0/users/me/context",
        "/v2.0/users/{userId}/context"],
    "CriteriaJournalMarks": [""],
    "": [""], # TODO: дополнить всё с https://api.school.mosreg.ru/partners/swagger/ui/index#/
}
