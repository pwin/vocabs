<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:foo="http://whatever"
    version="2.0">
    
    <xsl:output encoding="UTF-8" indent="yes" method="xml" omit-xml-declaration="yes"/>
    
    
    
    <xsl:param name="test1">
        <xsl:value-of select="concat('http:','//this.is.the/id/url1')"/>
    </xsl:param>
    
    <xsl:param name="test2">
        <xsl:value-of select="concat('http:','//this.is.the/id#url2')"/>
    </xsl:param>


    <xsl:function name="foo:getURL">
        <xsl:param name="path" />
        <xsl:choose>
            <xsl:when test="contains($path,'#')">
                <xsl:value-of select="substring-before($path,tokenize($path,'#')[last()])" />
            </xsl:when>
            <xsl:when test="contains($path,'/')">
                <xsl:value-of select="substring-before($path,tokenize($path,'/')[last()])" />
            </xsl:when>
            <xsl:otherwise />
        </xsl:choose>
    </xsl:function>


    <xsl:function name="foo:getClass">
        <xsl:param name="path" />
        <xsl:choose>
            <xsl:when test="contains($path,'#')">
                <xsl:value-of select="tokenize($path,'#')[last()]" />
            </xsl:when>
            <xsl:when test="contains($path,'/')">
                <xsl:value-of select="tokenize($path,'/')[last()]" />
            </xsl:when>
            <xsl:otherwise />
        </xsl:choose>
    </xsl:function>
    

    <xsl:template match="/">
        <e><xsl:value-of select="foo:getURL($test1)"/></e>
        <e><xsl:value-of select="foo:getURL($test2)"/></e>
        <e><xsl:value-of select="foo:getClass($test1)"/></e>
        <e><xsl:value-of select="foo:getClass($test2)"/></e>
    </xsl:template>
</xsl:stylesheet>