#!/usr/bin/env python


"""
Comment: Scottish extension of Organisation ontology / application profile based on  EC Core Public Organisation Vocabulary and W3C Organization Vocabulary This is the ontology of the Scottish application profile of Organisations (Public)
About: 
Version Info: Version 1 - Modified 11 July 2019 - An initial draft.
Version IRI: https://entities.gov.scot/def/gov/cpov-ap-scot/1/
"""


from owlready2 import *

##default_world.set_backend(filename = "./onto.file.sqlite3")

owlready2.JAVA_EXE = r"C:\Java\bin\java.exe"
inferencer = False

onto = get_ontology("http://entities.gov.scot/def/gov/cpov-ap-scot/")
owl = onto.get_namespace("http://www.w3.org/2002/07/owl#")
obo = onto.get_namespace("http://purl.obolibrary.org/obo/")
org = onto.get_namespace("http://www.w3.org/ns/org#")
regorg = onto.get_namespace("http://www.w3.org/ns/regorg#")
dct = onto.get_namespace("http://purl.org/dc/terms/")
schema = onto.get_namespace("http://schema.org/")
skos = onto.get_namespace("http://www.w3.org/2004/02/skos/core#")
m8g = onto.get_namespace("http://data.europa.eu/m8g/")
cpsv = onto.get_namespace("http://purl.org/vocab/cpsv#")
legal = onto.get_namespace("http://www.w3.org/ns/legal#")
xhtml = onto.get_namespace("http://www.w3.org/1999/xhtml/vocab#")
dcat = onto.get_namespace("http://www.w3.org/ns/dcat#")
joinup = onto.get_namespace("http://joinup.eu")
vann = onto.get_namespace("http://purl.org/vocab/vann/")
adms = onto.get_namespace("http://www.w3.org/ns/adms#")


# Annotation Properties
with onto:
    class prefLabel(AnnotationProperty):
        namespace = skos
        label = "preferred label"

    class altLabel(AnnotationProperty):
        namespace = skos
        label = "alternative label"

    class contactPoint(AnnotationProperty):
        namespace = dcat
        label = "contact point"

    class keyword(AnnotationProperty):
        namespace = dcat
        label = "keyword"

    class accrualPeriodicity(AnnotationProperty):
        namespace = dct
        label = "accrual periodicity"

    class creator(AnnotationProperty):
        namespace = dct
        label = "creator"

    class description(AnnotationProperty):
        namespace = dct
        label = "description"

    class hasVersion(AnnotationProperty):
        namespace = dct
        label = "has version"

    class identifier(AnnotationProperty):
        namespace = dct
        label = "identifier"

    class issued(AnnotationProperty):
        namespace = dct
        label = "issued"

    class language(AnnotationProperty):
        namespace = dct
        label = "language"

    class licence(AnnotationProperty):
        namespace = dct
        label = "licence"

    class modified(AnnotationProperty):
        namespace = dct
        label = "modified"

    class publisher(AnnotationProperty):
        namespace = dct
        label = "publisher"

    class rightsHolder(AnnotationProperty):
        namespace = dct
        label = "rights holder"

    class title(AnnotationProperty):
        namespace = dct
        label = "title"

    class type(AnnotationProperty):
        namespace = dct
        label = "type"

    class default(AnnotationProperty):
        namespace = joinup
        label = "default"

    class elibrary_creation(AnnotationProperty):
        namespace = onto.get_namespace("http://joinup.eu/solution/")
        label = "elibrary creation"

    class language(AnnotationProperty):
        namespace = onto.get_namespace("http://joinup.eu/")

    class preferredNamespacePrefix(AnnotationProperty):
        namespace = vann
        label = "preferred namespace prefix"

    class usageNote(AnnotationProperty):
        namespace = vann
        label = "usage note"

    class note(AnnotationProperty):
        namespace = skos
        label = "note"

    class status(AnnotationProperty):
        namespace = adms
        label = "status"

    class purpose(AnnotationProperty):
        namespace = org
        label = "purpose"




# Data Properties
with onto:
    class notation(DataProperty):
        namespace = skos
        label = "notation"    


# Object Properties
with onto:
    class address(ObjectProperty):
        label = "address"
        
    class administeredBy(ObjectProperty):
        label = "administered by"
        
    class administers(ObjectProperty):
        label = "administers"
        
    class hasFunction(ObjectProperty):
        label = "has function"
        
    class hasJurisdiction(ObjectProperty):
        label = "has jurisdiction"
        
    class hasLegalStatus(ObjectProperty):
        label = "has legal status"

    class hasFormalFramework(ObjectProperty):
        namespace = m8g
        label = "has formal framework"

    class hasFunction(ObjectProperty):
        label = "has function"

    class implements(ObjectProperty):
        namespace = cpsv
        label = "implements"
        
    class changedBy(ObjectProperty):
        namespace = org
        label = "changed by"

    class hasMember(ObjectProperty):
        namespace = org
        label = "has member"
        
    class hasSubOrganization(ObjectProperty):
        namespace = org
        label = "has sub-organization"

    class hasUnit(ObjectProperty):
        namespace = org
        label = "has unit"

    class memberOf(ObjectProperty):
        namespace = org
        label = "member of"
        
    class originalOrganization(ObjectProperty):
        namespace = org
        label = "original organization"

    class resultingOrganization(ObjectProperty):
        namespace = org
        label = "resulting organization"
        
    class subOrganizationOf(ObjectProperty):
        namespace = org
        label = "sub-organization of"

    class unitOf(ObjectProperty):
        namespace = org
        label = "unit of"
        
    class resultedFrom(ObjectProperty):
        namespace = org
        label = "resulted from"
 
    class next(ObjectProperty):
        namespace = xhtml
        label = "next"
        
    class prev(ObjectProperty):
        namespace = xhtml
        label = "previous"
        

# Classes
with onto:
#    class Class(Thing):
#        namespace = owl

    class BFO_0000027(Thing):
        namespace = obo
        label = "BFO_0000027"

    class FormalFramework(Thing):
        namespace = cpsv
        label = "Formal Framework"

    class FoundationEvent(Thing):
        namespace = m8g
        label = "Foundation Event"

    class Image(Thing):
        namespace = onto.get_namespace("http://xmlns.com/foaf/0.1/")
        label = "Image"        
        
    class Function(Thing):
        label = "Function"

    class Advisory(Function):
        label = "Advisory"

    class Executive(Function):
        label = "Executive"
        
    class Purchasing(Function):
        label = "Purchasing"
        
    class Jurisdiction(Thing):
        label = "Jurisdiction"
        
    class LocalJurisdiction(Jurisdiction):
        label = "Local Jurisdiction"
        
    class NationalJurisdiction(Jurisdiction):
        label = "National Jurisdiction"
        
    class LegalStatus(Thing):
        label = "Legal Status"
        
    class ChangeEvent(Thing):
        namespace = org
        label = "Change Event"

    class FormalOrganization(Thing):
        namespace = org
        label = "Formal Organisation"
        
    class LegalEntity(FormalOrganization):
        namespace = legal
        label = "Legal Entity"
        comment = """This is the key class for the Business Core Vocabulary and represents a 
        business that is legally registered. In many countries there is a single registry although in others, 
        such as Spain and Germany, multiple registries exist. A Legal Entity is able to trade, is 
        legally liable for its actions, accounts, tax affairs etc. It is a sub class of org:FormalOrganization
        which covers a wider range of entities, such as charities."""

    class RegisteredOrganization(FormalOrganization):
        namespace = regorg
        label = "Registered Organization"
        
    class ContactPoint(Thing):
        namespace = schema
        label = "Contact Point"

    class OpeningHoursSpecification(Thing):
        namespace = schema
        label = "Opening Hours Specification"






#----  BFO_0000027  class things
        
    class Organization(BFO_0000027):
        namespace = org
        label = "Organization"
        comment = """from Organization ontology"""       

    class Committee(Organization):
        label = "Committee"

    class EducationalEstablishment(Organization):
        label = "Educational Establishment"
        
    class LocalHarbourTrust(Organization):
        label = "Local Harbour Trust"
        equivalent_to = [Organization & hasJurisdiction.some(LocalJurisdiction)]
        
    class MarketBody(Organization):
        label = "Market Body"
        
    class NonMarketBody(Organization):
        namespace = onto.get_namespace("https://entities.gov.scot/def/gov/cpov-ap-scot/")
        label = "Non-Market Body"
        
    class PublicOrganisation(Organization):
        namespace = m8g
        label = "Public Organisation"
        comment = """The Public Organization class represents the organization. One organization may comprise several sub-organizations and any organization may have one or more organizational units. Each of these is described using the same properties and relationships."""

    class CentralBank(PublicOrganisation):
        label = "Central Bank"

    class CentralGovernmentOrganisation(PublicOrganisation):
        label = "Central Government Organisation"

    class ArmsLengthBody(CentralGovernmentOrganisation):
        label = "Arms Length Body"

    class ExecutiveAgency(ArmsLengthBody):
        label = "Executive Agency"
        equivalent_to = [ArmsLengthBody & hasFunction.some(Executive)]

    class HealthBody(ArmsLengthBody):
        label = "Health Body"
        
    class NHSBoard(HealthBody):
        label = "NHS Board"

    class SpecialNHSBoard(NHSBoard):
        label = "Special NHS Board"
        equivalent_to = [NHSBoard & hasJurisdiction.some(NationalJurisdiction)]
        
    class TerritorialNHSBoard(NHSBoard):
        label = "Territorial NHS Board"
        equivalent_to = [NHSBoard & hasJurisdiction.some(LocalJurisdiction)]
        
    class NDPB(ArmsLengthBody):
        label = "Non-Departmental Public Body"

    class AdvisoryNDPB(NDPB):
        label = "Advisory Non-Departmental Public Body"
        equivalent_to = [NDPB & hasFunction.some(Advisory)]
        
    class ExecutiveNDPB(NDPB):
        label = "Executive Non-Departmental Public Body"
        equivalent_to = [NDPB & hasFunction.some(Executive)]

    class NonMinisterialDept(ArmsLengthBody):
        label = "Non-Ministerial Department"
        
    class OtherSigBody(ArmsLengthBody):
        label = "Other Significant Body"
        
    class ParlCommOrOmbuds(ArmsLengthBody):
        label = "Parliamentary Commissioner or Ombudsman"
        
    class Tribunal(ArmsLengthBody):
        label = "Tribunal"
        
    class CentralGovPC(CentralGovernmentOrganisation):
        label = "Central Government Public Corporation"
        equivalent_to = [CentralGovernmentOrganisation & hasLegalStatus.some(RegisteredOrganization),
                         CentralGovernmentOrganisation & hasFunction.some(MarketBody)]
        
    class DevolvedAdministration(CentralGovernmentOrganisation):
        label = "Devolved Administration"
        
    class ConservationBoardAONB(PublicOrganisation):
        label = "Conservation Board for Area of Outstanding Natural Beauty"
        
    class Court(PublicOrganisation):
        label = "Court"

    class HighCourt(Court):
        label = "High Court"

    class JPCourt(Court):
        label = "JP Court"

    class SheriffAppealCourt(Court):
        label = "Sheriff Appeal Court"

    class SheriffCourt(Court):
        label = "Sheriff Court"

    class SupremeCourt(Court):
        label = "Supreme Court"

    class CrownEstate(PublicOrganisation):
        label = "Crown Estate"
        
    class LocalGovernmentOrganisation(PublicOrganisation):
        label = "Local Government Organisation"

    class CommunityCouncil(LocalGovernmentOrganisation):
        label = "Community Council"
        
    class IntegrationAuthority(LocalGovernmentOrganisation):
        label = "Integration Authority"
        equivalent_to = [LocalGovernmentOrganisation & hasFunction.some(HealthBody)]
        
    class LocalGovernmentCentralPurchasingBody(LocalGovernmentOrganisation):
        label = "Local Government Central Purchasing Body"
        equivalent_to = [LocalGovernmentOrganisation & hasFunction.some(Committee) & hasFunction.some(Purchasing) & hasMember.min(2, Thing)]
        
    class LocalGovPC(LocalGovernmentOrganisation):
        label = "Local Government Public Corporation"
        equivalent_to = [LocalGovernmentOrganisation & hasFunction.some(MarketBody)]
        
    class RegionalTransportPartnership(LocalGovernmentOrganisation):
        label = "Regional Transport Partnership"
        
    class Council(LocalGovernmentOrganisation):
        label = "Unitary Authority"
        
    class NationalParkAuthority(PublicOrganisation):
        label = "National Park Authority"
        
    class NonClassifiedEntity(PublicOrganisation):
        label = "Non-Classified Entity"
        
    class NonClassifiedGovernmentEntity(NonClassifiedEntity):
        label = "Non-Classified Government Entity"

    class DepartmentSpecificEntityType(NonClassifiedGovernmentEntity):
        label = "Department-specific Class of Entity"
        
    class ExpertCommittee(NonClassifiedGovernmentEntity):
        label = "Expert Committee"
        
    class OfficeOrTaskforce(NonClassifiedGovernmentEntity):
        label = "Office Or Taskforce"
        
    class StatutoryOfficeHolder(NonClassifiedGovernmentEntity):
        label = "Statutory Office Holder"
        
    class WorkingGroup(NonClassifiedGovernmentEntity):
        label = "Working Group"
        
    class ParlBody(PublicOrganisation):
        label = "Parliamentary Body"

    class PublicBroadcastingAuthority(PublicOrganisation):
        label = "Public Broadcasting Authority"
        
    class Regulator(PublicOrganisation):
        label = "Regulator"
        
    class UtilityRegulator(Regulator):
        label = "Utility Regulator"
        
    class RegulatedInspectedServiceProvider(Organization):
        label = "Regulated and Inspected Service Provider"
        
    class SpecialPurposeVehicle(Organization):
        label = "Special Purpose Vehicle"

    AllDisjoint([Organization, Jurisdiction])
    #AllDisjoint([MarketBody, NonMarketBody, LocalJurisdiction, NationalJurisdiction, ExecutiveAgency, NDPB, HealthBody, NonMinisterialDept, OtherSigBody, ParlCommOrOmbuds, Tribunal ]) 
        
        






#-----------------------



default_world.save()


onto.save(file = r".\2019-09-20_v3_ontology.owlready2.rdf", format = "rdfxml")
onto.save(file = r".\2019-09-20_v3_ontology.owlready2.n3", format = "ntriples")

Query = '''SELECT * WHERE {?a ?b ?c.} limit 10'''
results = default_world.as_rdflib_graph().query_owlready(Query)
results = list(results) 
print(results)


