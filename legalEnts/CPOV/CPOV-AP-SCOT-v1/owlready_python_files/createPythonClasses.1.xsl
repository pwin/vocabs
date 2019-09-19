<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
    xml:base="https://entities.gov.scot/def/gov/cpov-ap-scot/"
    xmlns:core="http://www.w3.org/2004/02/skos/core#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns="https://entities.gov.scot/def/gov/cpov-ap-scot/"
    version="2.0">
    
    <xsl:template match="/">
        <html>
            <body>
                <h1><xsl:value-of select="rdf:RDF/owl:Ontology/rdfs:comment"/></h1>
                <h2>OWL ontology</h2>
                <dl>
                    <dt>Ontology IRI</dt>
                    <dd><xsl:value-of select="rdf:RDF/owl:Ontology/@rdf:about"/></dd>
                    
                    <dt>Version IRI</dt>
                    <dd><xsl:value-of select="rdf:RDF/owl:Ontology/owl:versionIRI/@rdf:resource"/></dd>

                </dl>
                
                <h3>Defined object properties</h3>
                <dl>
                    <xsl:for-each select="//owl:ObjectProperty">
                        <dt>
                            <em><xsl:value-of select="rdfs:label" /></em>
                            &#xa0;
                            <code><xsl:value-of select="@rdf:about" /></code>
                        </dt>
                        <dd><small><xsl:value-of select="rdfs:comment" /></small></dd>
                    </xsl:for-each>
                </dl>
                
                
                <h3>Defined data type properties</h3>
                <dl>
                    <xsl:for-each select="//owl:DatatypeProperty">
                        <dt><code><xsl:value-of select="@rdf:about" /></code> 
                            &#xa0;
                            <em><xsl:value-of select="rdfs:label" /></em></dt>
                        <dd><small><xsl:value-of select="rdfs:comment" /></small></dd>
                    </xsl:for-each>
                </dl>
                <h3>Defined classes</h3>
                <dl>
                    <xsl:for-each select="//owl:Class">
                        <dt><code><xsl:value-of select="@rdf:about" /></code> 
                            &#xa0;
                            <em><xsl:value-of select="rdfs:label" /></em></dt>
                        <dd><small><xsl:value-of select="rdfs:comment" /></small></dd>
                    </xsl:for-each>
                </dl>               
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>