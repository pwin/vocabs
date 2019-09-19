#!/usr/bin/env python


"""
Comment: DCAT is an RDF vocabulary designed to facilitate interoperability between data catalogs published on the Web.
          By using DCAT to describe datasets in data catalogs, publishers increase discoverability and enable
          applications easily to consume metadata from multiple catalogs. It further enables decentralized
          publishing of catalogs and facilitates federated dataset search across sites. Aggregated DCAT metadata can
          serve as a manifest file to facilitate digital preservation.
          DCAT is defined at http://www.w3.org/TR/vocab-dcat/. Any variance between that normative
          document and this schema is an error in this schema.
About: 
Version Info: This is an updated copy of v1.0 of the DCAT vocabulary, taken from https://www.w3.org/ns/dcat.ttl and will replace that file when DCAT2 is published
Temporarily added imports for DCTerms, SKOS, FOAF to assist in development of v1.* or v2.0 by W3C Data Exchange Working Group
Version IRI: 
"""


from owlready2 import *

default_world.set_backend(filename = "./onto.file.sqlite3")

owlready2.JAVA_EXE = r"C:\Java\bin\java.exe"
inferencer = False

onto = get_ontology("http://www.w3.org/ns/dcat#")

class Concept(Thing):
    pass


class Class(Thing):
    namespace = onto.get_namespace("http://www.w3.org/2002/07/owl#")

class Resource(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "Catalogued resource"
    comment = """Resource published or curated by a single agent."""
    
class Dataset(Resource):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "Dataset"
    comment = """A collection of data, published or curated by a single source, and available for access or download in one or more represenations"""
    


class relation(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")

class contributor(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")

class contributor(contributor):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")

class description(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")

class creator(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")
    
class creator(creator):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")



class title(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")

    
class description(description):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class title(title):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class accessService(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")


class endpointURL(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")


class Relationship(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")


class Attribution(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/prov#")


class alternateOf(relation):
    namespace = onto.get_namespace("http://www.w3.org/ns/prov#")


class hadPrimarySource(relation):
    namespace = onto.get_namespace("http://www.w3.org/ns/prov#")


class specializationOf(relation):
    namespace = onto.get_namespace("http://www.w3.org/ns/prov#")


class wasAttributedTo(relation):
    namespace = onto.get_namespace("http://www.w3.org/ns/prov#")


class wasDerivedFrom(relation):
    namespace = onto.get_namespace("http://www.w3.org/ns/prov#")


class wasGeneratedBy(relation):
    namespace = onto.get_namespace("http://www.w3.org/ns/prov#")


class wasInfluencedBy(relation):
    namespace = onto.get_namespace("http://www.w3.org/ns/prov#")


class wasQuotedFrom(relation):
    namespace = onto.get_namespace("http://www.w3.org/ns/prov#")


class wasRevisionOf(relation):
    namespace = onto.get_namespace("http://www.w3.org/ns/prov#")


class Agent(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Agent"
    comment = """A resource that acts or has the power to act."""


class AgentClass(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Agent Class"
    comment = """A group of agents."""


class BibliographicResource(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Bibliographic Resource"
    comment = """A book, article, or other documentary resource."""


class Box(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "DCMI Box"
    comment = """The set of regions in space defined by their geographic coordinates according to the DCMI Box Encoding Scheme."""


class FileFormat(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "File Format"
    comment = """A digital resource format."""


class Frequency(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Frequency"
    comment = """A rate at which something recurs."""


class ISO3166(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "ISO 3166"
    comment = """The set of codes listed in ISO 3166-1 for the representation of names of countries."""


class ISO639_2(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "ISO 639-2"
    comment = """The three-letter alphabetic codes listed in ISO639-2 for the representation of names of languages."""


class ISO639_3(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "ISO 639-3"
    comment = """The set of three-letter codes listed in ISO 639-3 for the representation of names of languages."""


class Jurisdiction(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Jurisdiction"
    comment = """The extent or range of judicial, law enforcement, or other authority."""


class LicenseDocument(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "License Document"
    comment = """A legal document giving official permission to do something with a Resource."""


class LinguisticSystem(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Linguistic System"
    comment = """A system of signs, symbols, sounds, gestures, or rules used in communication."""


class Location(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Location"
    comment = """A spatial region or named place."""


class LocationPeriodOrJurisdiction(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Location, Period, or Jurisdiction"
    comment = """A location, period of time, or jurisdiction."""


class MediaType(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Media Type"
    comment = """A file format or physical medium."""


class MediaTypeOrExtent(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Media Type or Extent"
    comment = """A media type or extent."""


class MethodOfAccrual(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Method of Accrual"
    comment = """A method by which resources are added to a collection."""


class MethodOfInstruction(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Method of Instruction"
    comment = """A process that is used to engender knowledge, attitudes, and skills."""


class Period(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "DCMI Period"
    comment = """The set of time intervals defined by their limits according to the DCMI Period Encoding Scheme."""


class PeriodOfTime(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Period of Time"
    comment = """An interval of time that is named or defined by its start and end dates."""


class PhysicalMedium(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Physical Medium"
    comment = """A physical material or carrier."""


class PhysicalResource(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Physical Resource"
    comment = """A material thing."""


class Point(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "DCMI Point"
    comment = """The set of points in space defined by their geographic coordinates according to the DCMI Point Encoding Scheme."""


class Policy(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Policy"
    comment = """A plan or course of action by an authority, intended to influence and determine decisions, actions, and other matters."""


class ProvenanceStatement(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Provenance Statement"
    comment = """A statement of any changes in ownership and custody of a resource since its creation that are significant for its authenticity, integrity, and interpretation."""


class RFC1766(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "RFC 1766"
    comment = """The set of tags, constructed according to RFC 1766, for the identification of languages."""


class RFC3066(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "RFC 3066"
    comment = """The set of tags constructed according to RFC 3066 for the identification of languages."""


class RFC4646(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "RFC 4646"
    comment = """The set of tags constructed according to RFC 4646 for the identification of languages."""


class RFC5646(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "RFC 5646"
    comment = """The set of tags constructed according to RFC 5646 for the identification of languages."""


class RightsStatement(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Rights Statement"
    comment = """A statement about the intellectual property rights (IPR) held in or over a Resource, a legal document giving official permission to do something with a resource, or a statement about access rights."""


class SizeOrDuration(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Size or Duration"
    comment = """A dimension or extent, or a time taken to play or execute."""


class Standard(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Standard"
    comment = """A basis for comparison; a reference point against which other things can be evaluated."""


class URI(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "URI"
    comment = """The set of identifiers constructed according to the generic syntax for Uniform Resource Identifiers as specified by the Internet Engineering Task Force."""


class W3CDTF(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "W3C-DTF"
    comment = """The set of dates and times constructed according to the W3C Date and Time Formats Specification."""


class abstract(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Abstract"
    comment = """A summary of the resource."""


class accessRights(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Access Rights"
    comment = """Information about who can access the resource or an indication of its security status."""


class accrualMethod(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Accrual Method"
    comment = """The method by which items are added to a collection."""


class accrualPeriodicity(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Accrual Periodicity"
    comment = """The frequency with which items are added to a collection."""


class accrualPolicy(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Accrual Policy"
    comment = """The policy governing the addition of items to a collection."""


class alternative(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Alternative Title"
    comment = """An alternative name for the resource."""


class audience(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Audience"
    comment = """A class of entity for whom the resource is intended or useful."""


class available(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Date Available"
    comment = """Date (often a range) that the resource became or will become available."""


class bibliographicCitation(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Bibliographic Citation"
    comment = """A bibliographic reference for the resource."""


class conformsTo(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Conforms To"
    comment = """An established standard to which the described resource conforms."""


class contributor(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Contributor"
    comment = """An entity responsible for making contributions to the resource."""


class coverage(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Coverage"
    comment = """The spatial or temporal topic of the resource, the spatial applicability of the resource, or the jurisdiction under which the resource is relevant."""


class created(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Date Created"
    comment = """Date of creation of the resource."""


class creator(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Creator"
    comment = """An entity primarily responsible for making the resource."""


class date(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Date"
    comment = """A point or period of time associated with an event in the lifecycle of the resource."""


class dateAccepted(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Date Accepted"
    comment = """Date of acceptance of the resource."""


class dateCopyrighted(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Date Copyrighted"
    comment = """Date of copyright."""


class dateSubmitted(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Date Submitted"
    comment = """Date of submission of the resource."""


class description(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Description"
    comment = """An account of the resource."""


class educationLevel(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Audience Education Level"
    comment = """A class of entity, defined in terms of progression through an educational or training context, for which the described resource is intended."""


class extent(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Extent"
    comment = """The size or duration of the resource."""


class format(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Format"
    comment = """The file format, physical medium, or dimensions of the resource."""


class hasFormat(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Has Format"
    comment = """A related resource that is substantially the same as the pre-existing described resource, but in another format."""


class hasPart(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Has Part"
    comment = """A related resource that is included either physically or logically in the described resource."""


class identifier(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Identifier"
    comment = """An unambiguous reference to the resource within a given context."""


class instructionalMethod(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Instructional Method"
    comment = """A process, used to engender knowledge, attitudes and skills, that the described resource is designed to support."""


class isFormatOf(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Is Format Of"
    comment = """A related resource that is substantially the same as the described resource, but in another format."""


class isPartOf(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Is Part Of"
    comment = """A related resource in which the described resource is physically or logically included."""


class isReferencedBy(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Is Referenced By"
    comment = """A related resource that references, cites, or otherwise points to the described resource."""


class isReplacedBy(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Is Replaced By"
    comment = """A related resource that supplants, displaces, or supersedes the described resource."""


class isRequiredBy(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Is Required By"
    comment = """A related resource that requires the described resource to support its function, delivery, or coherence."""


class isVersionOf(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Is Version Of"
    comment = """A related resource of which the described resource is a version, edition, or adaptation."""


class issued(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Date Issued"
    comment = """Date of formal issuance (e.g., publication) of the resource."""


class language(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Language"
    comment = """A language of the resource."""


class license(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "License"
    comment = """A legal document giving official permission to do something with the resource."""


class mediator(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Mediator"
    comment = """An entity that mediates access to the resource and for whom the resource is intended or useful."""


class medium(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Medium"
    comment = """The material or physical carrier of the resource."""


class modified(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Date Modified"
    comment = """Date on which the resource was changed."""


class provenance(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Provenance"
    comment = """A statement of any changes in ownership and custody of the resource since its creation that are significant for its authenticity, integrity, and interpretation."""


class publisher(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Publisher"
    comment = """An entity responsible for making the resource available."""


class references(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "References"
    comment = """A related resource that is referenced, cited, or otherwise pointed to by the described resource."""


class relation(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Relation"
    comment = """A related resource."""


class replaces(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Replaces"
    comment = """A related resource that is supplanted, displaced, or superseded by the described resource."""


class requires(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Requires"
    comment = """A related resource that is required by the described resource to support its function, delivery, or coherence."""


class rights(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Rights"
    comment = """Information about rights held in and over the resource."""


class rightsHolder(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Rights Holder"
    comment = """A person or organization owning or managing rights over the resource."""


class source(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Source"
    comment = """A related resource from which the described resource is derived."""


class spatial(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Spatial Coverage"
    comment = """Spatial characteristics of the resource."""


class subject(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Subject"
    comment = """The topic of the resource."""


class tableOfContents(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Table Of Contents"
    comment = """A list of subunits of the resource."""


class temporal(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Temporal Coverage"
    comment = """Temporal characteristics of the resource."""


class title(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Title"
    comment = """A name given to the resource."""


class type(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Type"
    comment = """The nature or genre of the resource."""


class valid(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Date Valid"
    comment = """Date (often a range) of validity of a resource."""


class hasBeginning(Thing):
    namespace = onto.get_namespace("http://www.w3.org/2006/time#")


class hasEnd(Thing):
    namespace = onto.get_namespace("http://www.w3.org/2006/time#")


class theme(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "theme"
    comment = """A main category of the resource. A resource can have multiple themes."""


class hasPolicy(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/odrl/2/")


class qualifiedAttribution(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/prov#")


class VocabularyEncodingScheme(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/dcam/")
    

class Collection(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/dcmitype/")
    

class Service(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/dcmitype/")
    

class Agent(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class AgentClass(Class):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class BibliographicResource(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class FileFormat(MediaType):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class Frequency(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class Jurisdiction(LocationPeriodOrJurisdiction):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class LicenseDocument(RightsStatement):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class LinguisticSystem(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class Location(LocationPeriodOrJurisdiction):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class LocationPeriodOrJurisdiction(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class MediaType(MediaTypeOrExtent):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class MediaTypeOrExtent(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class MethodOfAccrual(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class MethodOfInstruction(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class PeriodOfTime(LocationPeriodOrJurisdiction):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class PhysicalMedium(MediaType):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class PhysicalResource(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class Policy(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class ProvenanceStatement(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class RightsStatement(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class SizeOrDuration(MediaTypeOrExtent):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class Standard(Thing):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class Class(Thing):
    namespace = onto.get_namespace("http://www.w3.org/2000/01/rdf-schema#")
    

class Resource(Thing):
    namespace = onto.get_namespace("http://www.w3.org/2000/01/rdf-schema#")
    

class Kind(Thing):
    namespace = onto.get_namespace("http://www.w3.org/2006/vcard/ns#")
    

class Catalog(Dataset):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "Catalog"
    comment = """A curated collection of metadata about datasets and data services"""
    

class CatalogRecord():
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "Catalog Record"
    comment = """A record in a data catalog, describing the registration of a single dataset or data service."""
    

class DataService(Service, Resource):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "Data service"
    comment = """A site or end-point providing operations related to the discovery of, access to, or processing functions on, data or related resources."""
    


class Distribution(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "Distribution"
    comment = """A specific representation of a dataset. A dataset might be available in multiple serializations that may differ in various ways,
                  including natural language, media-type or format, schematic organization, temporal and spatial resolution, level of detail or
                  profiles (which might specify any or all of the above)."""
    

class Relationship(Thing):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "Relationship"
    comment = """An association class for attaching additional information to a relationship between DCAT Resources."""
    

    

class Role(Concept):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "Role"
    comment = """A role is the function of a resource or agent with respect to another resource, in the context of resource attribution or resource relationships. Role je funkce zdroje či agenta ve vztahu k jinému zdroji, v kontextu přiřazení zdrojů či vztahů mezi zdroji."""
    

class Document(Thing):
    namespace = onto.get_namespace("http://xmlns.com/foaf/0.1/")
    

class Person(Thing):
    namespace = onto.get_namespace("http://xmlns.com/foaf/0.1/")
    

class accessRights(rights):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class accrualMethod(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class accrualPeriodicity(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class accrualPolicy(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class audience(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class conformsTo(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class contributor(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class coverage(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class creator(contributor):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class educationLevel(audience):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class extent(format):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class format(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class instructionalMethod(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class language(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class license(rights):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class mediator(audience):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class medium(format):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class provenance(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class publisher(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class rights(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class rightsHolder(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class spatial(coverage):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class temporal(coverage):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class type(ObjectProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    

class member(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/2000/01/rdf-schema#")
    

class accessService(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "data access service"
    comment = """A site or end-point that gives access to the distribution of the dataset."""
    

class accessURL(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "access address"
    comment = """A URL of a resource that gives access to a distribution of the dataset. E.g. landing page, feed, SPARQL endpoint.
          Use for all cases except a simple download link, in which case downloadURL is preferred."""
    

class catalog(hasPart, member):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "catalog"
    comment = """A catalog whose contents are of interest in the context of this catalog."""
    

class compressFormat(format):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "compression format"
    comment = """The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file."""
    

class contactPoint(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "contact point"
    comment = """Relevant contact information for the catalogued resource. Use of vCard is recommended."""
    

class dataset(hasPartmember):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "dataset"
    comment = """A collection of data that is listed in the catalog."""
    

class distribution(relation):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "distribution"
    comment = """An available distribution of the dataset."""
    

class downloadURL(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "download URL"
    comment = """The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The
            format is indicated by the distribution's dct:format and/or dcat:mediaType"""
    

class endpointDescription(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "description of service end-point"
    comment = """A description of the service end-point, including its operations, parameters etc."""
    

class endpointURL(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "service end-point"
    comment = """The root location or primary endpoint of the service (a web-resolvable IRI)"""
    

class hadRole(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "hadRole"
    comment = """The function of an entity or agent with respect to another entity or resource."""
    

class landingPage(page):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "landing page"
    comment = """A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information."""
    

class mediaType(format):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "media type"
    comment = """The media type of the distribution as defined by IANA"""
    

class packageFormat(format):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "packaging format"
    comment = """The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together."""
    

class qualifiedRelation(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "qualified relation"
    comment = """Link to a description of a relationship with another resource."""
    

class record(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "record"
    comment = """A record describing the registration of a single dataset or data service that is part of the catalog."""
    

class servesDataset(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "serves dataset"
    comment = """A collection of data that this DataService can distribute"""
    

class service(hasPartmember):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "service"
    comment = """A site or endpoint that is listed in the catalog."""
    

class theme(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    

class themeTaxonomy(ObjectProperty):
    namespace = onto.get_namespace("http://www.w3.org/ns/dcat#")
    label = "theme taxonomy"
    comment = """The knowledge organization system (KOS) used to classify catalog's datasets."""
    

class homepage(ObjectProperty):
    namespace = onto.get_namespace("http://xmlns.com/foaf/0.1/")
    

class page(ObjectProperty):
    namespace = onto.get_namespace("http://xmlns.com/foaf/0.1/")
    

class primaryTopic(ObjectProperty):
    namespace = onto.get_namespace("http://xmlns.com/foaf/0.1/")
    




class coverage(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")


class date(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")





class format(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")


class identifier(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")


class language(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")


class publisher(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")


class rights(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")


class source(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")


class subject(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")





class type(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/elements/1.1/")


class abstract(description):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class accessRights(rights):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class alternative(title):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class available(date):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class bibliographicCitation(identifier):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class conformsTo(relationrelation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class coverage(coverage):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class created(date):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class date(date):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class dateAccepted(date):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class dateCopyrighted(date):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class dateSubmitted(date):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class extent(format):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class format(format):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class hasFormat(relationrelation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class hasPart(relationrelation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class hasVersion(relationrelation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class identifier(identifier):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class isFormatOf(relationrelation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class isPartOf(relationrelation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class isReferencedBy(relation, relation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class isReplacedBy(relation, relation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class isRequiredBy(relation, relation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class isVersionOf(relation, relation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class issued(date):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class language(language):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class license(rights):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class medium(format):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class modified(date):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class publisher(publisher):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class references(relation, relation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class relation(relation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class replaces(relation, relation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class requires(relation, relation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class rights(rights):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class source(source, relation):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class spatial(coverage):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class subject(subject):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class tableOfContents(description):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class temporal(coverage):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class type(type):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class valid(date):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")


class affiliation(AnnotationProperty):
    namespace = onto.get_namespace("http://schema.org/")


class rangeIncludes(AnnotationProperty):
    namespace = onto.get_namespace("http://schema.org/")


class maker(AnnotationProperty):
    namespace = onto.get_namespace("http://xmlns.com/foaf/0.1/")


class name(AnnotationProperty):
    namespace = onto.get_namespace("http://xmlns.com/foaf/0.1/")


class workInfoHomepage(AnnotationProperty):
    namespace = onto.get_namespace("http://xmlns.com/foaf/0.1/")


class hasVersion(AnnotationProperty):
    namespace = onto.get_namespace("http://purl.org/dc/terms/")
    label = "Has Version"
    comment = """A related resource that is a version, edition, or adaptation of the described resource."""


default_world.save()


onto.save(file = r".\2019-09-15T19_19_21.833+01_00_ontology.owlready2.rdf", format = "rdfxml")
onto.save(file = r".\2019-09-15T19_19_21.833+01_00_ontology.owlready2.n3", format = "ntriples")

Query = '''SELECT * WHERE {?a ?b ?c.} limit 10'''
results = default_world.as_rdflib_graph().query_owlready(Query)
results = list(results) 
print(results)


