#!/usr/bin/env python


"""
Comment: Scottish extension of Organisation ontology / application profile based on  EC Core Public Organisation Vocabulary and W3C Organization Vocabulary This is the ontology of the Scottish application profile of Organisations (Public)
About: 
Version Info: Version 1 - Modified 11 July 2019 - An initial draft.
Version IRI: https://entities.gov.scot/def/gov/cpov-ap-scot/1/
"""


from owlready2 import *

default_world.set_backend(filename = "./onto.file.sqlite3")

owlready2.JAVA_EXE = r"C:\Java\bin\java.exe"
inferencer = False

onto = get_ontology("http://entities.gov.scot/def/gov/cpov-ap-scot/")


class Class(Thing):
    namespace = onto.get_namespace("http://www.w3.org/2002/07/owl#")


class NDPB(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")

class BFO_0000027(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/http://purl.obolibrary.org/obo/")
    label = "BFO_0000027"

class Function(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Function"
    
class CentralGovernmentOrganisation(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class CentralGovernmentOrganisation(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class ArmsLengthBody(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class NDPB(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class LocalGovernmentOrganisation(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class LocalGovernmentOrganisation(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class LocalGovernmentOrganisation(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class Organization(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")


class NHSBoard(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class NHSBoard(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class RegisteredOrganization(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/regorg#")


class ExecutiveNDPB(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class RegisteredOrganization(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/regorg#")


class ExecutiveNDPB(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class spatial(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "spatial"


class contactPoint(Thing):
    namespace = onto.get_namespace("http://schema.org/")
    label = "contact point"


class email(Thing):
    namespace = onto.get_namespace("http://schema.org/")
    label = "has email"


class hoursAvailable(Thing):
    namespace = onto.get_namespace("http://schema.org/")
    label = "availability restriction"


class logo(Thing):
    namespace = onto.get_namespace("http://schema.org/")
    label = "logo"


class openingHours(Thing):
    namespace = onto.get_namespace("http://schema.org/")
    label = "opening hours"


class telephone(Thing):
    namespace = onto.get_namespace("http://schema.org/")
    label = "has telephone"


class prefLabel(Thing):
    namespace = onto.get_namespace("http://www.w3.org/2004/02/skos/core#")
    label = "preferred label"


class identifier(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    label = "identifier"


class HighCourt(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class JPCourt(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class SheriffAppealCourt(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class SheriffCourt(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class SupremeCourt(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")


class FoundationEvent(Thing):
    namespace = onto.get_namespace("http://data.europa.eu/m8g/")
    

class PublicOrganisation(Organization):
    namespace = onto.get_namespace("http://data.europa.eu/m8g/")
    label = "Public Organisation"
    comment = """The Public Organization class represents the organization. One organization may comprise several sub-organizations and any organization may have one or more organizational units. Each of these is described using the same properties and relationships."""
    
class NonClassifiedEntity(PublicOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Non-Classified Entity"
    

class NonClassifiedGovernmentEntity(NonClassifiedEntity):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Non-Classified Government Entity"
    
class FormalFramework(Thing):
    namespace = onto.get_namespace("http://purl.org/vocab/cpsv#")
    

class ContactPoint(Thing):
    namespace = onto.get_namespace("http://schema.org/")
    

class OpeningHoursSpecification(Thing):
    namespace = onto.get_namespace("http://schema.org/")
    
class FormalOrganization(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    
class LegalEntity(FormalOrganization):
    namespace = onto.get_namespace("http://www.w3.org/ns/legal#")
    label = "Legal Entity"
    comment = """This is the key class for the Business Core Vocabulary and represents a 
    business that is legally registered. In many countries there is a single registry although in others, 
    such as Spain and Germany, multiple registries exist. A Legal Entity is able to trade, is 
    legally liable for its actions, accounts, tax affairs etc. It is a sub class of org:FormalOrganization
    which covers a wider range of entities, such as charities."""
    

class ChangeEvent(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    


    

class Organization(BFO_0000027):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    label = "Organization"
    comment = """from Organization ontology"""
    

class RegisteredOrganization(FormalOrganization):
    namespace = onto.get_namespace("http://www.w3.org/ns/regorg#")
    label = "Registered Organization"
    

class Advisory(Function):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Advisory"
    

class AdvisoryNDPB(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Advisory Non-Departmental Public Body"
    

class ArmsLengthBody(CentralGovernmentOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Arms Length Body"
    

class CentralBank(PublicOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Central Bank"
    

class CentralGovPC(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Central Government Public Corporation"
    

class CentralGovernmentOrganisation(PublicOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Central Government Organisation"
    

class Committee(Organization):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Committee"
    

class CommunityCouncil(LocalGovernmentOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Community Council"
    

class ConservationBoardAONB(PublicOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Conservation Board for Area of Outstanding Natural Beauty"
    

class Council(LocalGovernmentOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Unitary Authority"
    

class Court(PublicOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Court"
    

class CrownEstate(PublicOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Crown Estate"
    

class DepartmentSpecificEntityType(NonClassifiedGovernmentEntity):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Department-specific Class of Entity"
    

class DevolvedAdministration(CentralGovernmentOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Devolved Administration"
    

class EducationalEstablishment(Organization):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Educational Establishment"
    

class Executive(Function):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Executive"
    

class ExecutiveAgency(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Executive Agency"
    

class ExecutiveNDPB(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Executive Non-Departmental Public Body"
    

class ExpertCommittee(NonClassifiedGovernmentEntity):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Expert Committee"
    
   

class HealthBody(ArmsLengthBody):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Health Body"
    

class HighCourt(Court):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "High Court"
    

class IntegrationAuthority(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Integration Authority"
    

class JPCourt(Court):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "JP Court"
    

class Jurisdiction(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Jurisdiction"
    

class LegalStatus(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Legal Status"
    

class LocalGovPC(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Local Government Public Corporation"
    

class LocalGovernmentCentralPurchasingBody(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Local Government Central Purchasing Body"
    

class LocalGovernmentOrganisation(PublicOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Local Government Organisation"
    

class LocalHarbourTrust(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Local Harbour Trust"
    

class LocalJurisdiction(Jurisdiction):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Local Jurisdiction"
    

class MarketBody(Organization):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Market Body"
    

class NDPB(ArmsLengthBody):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Non-Departmental Public Body"
    

class NHSBoard(HealthBody):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "NHSBoard"
    

class NationalJurisdiction(Jurisdiction):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "National Jurisdiction"
    

class NationalParkAuthority(PublicOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "National Park Authority"
    


    

class NonMarketBody(Organization):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Non-Market Body"
    

class NonMinisterialDept(ArmsLengthBody):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Non-Ministerial Department"
    

class OfficeOrTaskforce(NonClassifiedGovernmentEntity):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Office Or Taskforce"
    

class OtherSigBody(ArmsLengthBody):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Other Significant Body"
    

class ParlBody(PublicOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Parliamentary Body"
    

class ParlCommOrOmbuds(ArmsLengthBody):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Parliamentary Commissioner or Ombudsman"
    

class PublicBroadcastingAuthority(PublicOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Public Broadcasting Authority"
    

class Purchasing(Function):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Purchasing"
    

class RegionalTransportPartnership(LocalGovernmentOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Regional Transport Partnership"
    

class RegulatedInspectedServiceProvider(Organization):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Regulated and Inspected Service Provider"
    

class Regulator(PublicOrganisation):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Regulator"
    

class SheriffAppealCourt(Court):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Sheriff Appeal Court"
    

class SheriffCourt(Court):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Sheriff Court"
    

class SpecialNHSBoard(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Special NHS Board"
    

class SpecialPurposeVehicle(Organization):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Special Purpose Vehicle"
    

class StatutoryOfficeHolder(NonClassifiedGovernmentEntity):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Statutory Office Holder"
    

class SupremeCourt(Court):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Supreme Court"
    

class TerritorialNHSBoard(Thing):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Territorial NHS Board"
    

class Tribunal(ArmsLengthBody):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Tribunal"
    

class UtilityRegulator(Regulator):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Utility Regulator"
    

class WorkingGroup(NonClassifiedGovernmentEntity):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "Working Group"
    

    

class hasFormalFramework(ObjectProperty):
    namespace = onto.get_namespace("http://data.europa.eu/m8g/")
    

class implements(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/vocab/cpsv#")
    

class next(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/1999/xhtml/vocab#")
    

class prev(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/1999/xhtml/vocab#")
    

class changedBy(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    

class hasMember(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    

class hasSubOrganization(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    

class hasUnit(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    

class memberOf(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    

class originalOrganization(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    

class resultedFrom(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    label = "resulted from"
    

class resultingOrganization(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    

class subOrganizationOf(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    

class unitOf(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/org#")
    

class address(ObjectProperty):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "address"
    

class administeredBy(ObjectProperty):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "administered by"
    

class administers(ObjectProperty):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "administers"
    

class hasFunction(ObjectProperty):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "has function"
    

class hasJurisdiction(ObjectProperty):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "has jurisdiction"
    

class hasLegalStatus(ObjectProperty):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
    label = "has legal status"
    

class hasFunction(ObjectProperty):
    namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-scot/")
    

class language(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/")


class search(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/")


class site_featured(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/")
    label = "site-featured"


class site_pinned(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/")
    label = "site-pinned"


class workflow_status(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/is/")


class default(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/language/")


class translation_author(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/language/")


class translation_source(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/language/")


class translation_status(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/language/")


class uid(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/owner/")


class elibrary_creation(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/solution/")


class moderation(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/solution/")


class related_by_type(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/solution/")


class webdav_creation(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/solution/")


class policy_domain(AnnotationProperty):
    namespace = onto.get_namespace("http://joinup.eu/voc/")
    label = "policy-domain"


class StillImage(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/dcmitype/")


class accrualPeriodicity(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class creator(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class description(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class hasVersion(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class identifier(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class issued(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class language(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class licence(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class modified(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class publisher(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class rightsHolder(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class title(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class type(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class preferredNamespacePrefix(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/vocab/vann/")


class usageNote(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/vocab/vann/")


class altLabel(AnnotationProperty):
    namespace = onto.get_namespace("http://www.w3.org/2004/02/skos/core#")
    label = "alternative label"


class note(AnnotationProperty):
    namespace = onto.get_namespace("http://www.w3.org/2004/02/skos/core#")


#class status(AnnotationProperty):
#    namespace = onto.get_namespace("http://www.w3.org/ns/adms#")


class contactPoint(AnnotationProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")


class keyword(AnnotationProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")


#class purpose(AnnotationProperty):
#    namespace = onto.get_namespace("http://www.w3.org/ns/org#")


class Image(AnnotationProperty):
    namespace = onto.get_namespace("http://xmlns.com/foaf/0.1/")


default_world.save()


onto.save(file = r".\2019-09-20T09_25_34.786+01_00_ontology.owlready2.rdf", format = "rdfxml")
onto.save(file = r".\2019-09-20T09_25_34.786+01_00_ontology.owlready2.n3", format = "ntriples")

Query = '''SELECT * WHERE {?a ?b ?c.} limit 10'''
results = default_world.as_rdflib_graph().query_owlready(Query)
results = list(results) 
print(results)


