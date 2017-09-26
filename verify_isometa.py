#Frank Donnelly, Geospatial Data Librarian, Baruch College CUNY
#Script in Python 3.x for verifying completeness of ISO geospatial metadata records
#Released under Creative Commons Attribution-Non Commercial-ShareAlike License 4.0 International
#http://creativecommons.org/licenses/by-nc-sa/4.0/
#Last updated Oct 26, 2015

#Create two reports that will contain errors and a list of checked values, named for the current
#time and date, in a directory immediately below the one where this script is stored. Two files will
#be generated that contain all the checked information for all metadata stored in the directory.

import os
from time import strftime
from xml.etree.ElementTree import ElementTree

#Change this value to the name of the directory where metadata files are stored;
#script should be stored and run from directory directly above the specified root
rootdir='processed/'

today=strftime('%Y_%m_%d_%H%M')

writeprob=open(rootdir + 'error_report' + today + '.txt','w')
writenoprob=open(rootdir + 'valcheck_report' + today + '.txt','w')

#Open all files that end with _export.xml and parse them. If this isn't desired, alter the string value
#and list index as appropriate.

for file in os.listdir(rootdir):
    if file[-11:]=='_export.xml':

        checkfile=file
        path=rootdir+checkfile
        tree = ElementTree()
        root = tree.parse(path)

#A dictionary of namespaces, so they can be referred to in shorthand.

        namespaces = {
        'gmd': 'http://www.isotc211.org/2005/gmd',
        'gco': 'http://www.isotc211.org/2005/gco',
        'gml': 'http://www.opengis.net/gml'
        }
        
#Lists of all the specific elements that must be checked, separated into logical groups.
#Namespaces of the elements are referred to using shorthand. Add or remove elements as
#appropriate.        

        header1=[
        'gmd:fileIdentifier/gco:CharacterString',
        'gmd:language/gmd:LanguageCode',
        'gmd:characterSet/gmd:MD_CharacterSetCode',
        'gmd:hierarchyLevel/gmd:MD_ScopeCode'
        ]

        contact=[
        'gmd:contact/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString',
        'gmd:contact/gmd:CI_ResponsibleParty/gmd:positionName/gco:CharacterString',
        'gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString',
        'gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString',
        'gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:administrativeArea/gco:CharacterString',
        'gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString',
        'gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gmd:Country',
        'gmd:contact/gmd:CI_ResponsibleParty/gmd:role/gmd:CI_RoleCode'
        ]

        header2=[
        'gmd:dateStamp/gco:Date',
        'gmd:metadataStandardName/gco:CharacterString',
        'gmd:metadataStandardVersion/gco:CharacterString',
        'gmd:dataSetURI/gco:CharacterString'
        ]

        spatial=[
        'gmd:spatialRepresentationInfo/gmd:MD_VectorSpatialRepresentation/gmd:topologyLevel/gmd:MD_TopologyLevelCode',
        'gmd:spatialRepresentationInfo/gmd:MD_VectorSpatialRepresentation/gmd:geometricObjects/gmd:MD_GeometricObjects/gmd:geometricObjectType/gmd:MD_GeometricObjectTypeCode',
        'gmd:spatialRepresentationInfo/gmd:MD_VectorSpatialRepresentation/gmd:geometricObjects/gmd:MD_GeometricObjects/gmd:geometricObjectCount/gco:Integer',
        'gmd:referenceSystemInfo/gmd:MD_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS_Identifier/gmd:code/gco:CharacterString',
        'gmd:referenceSystemInfo/gmd:MD_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS_Identifier/gmd:codeSpace/gco:CharacterString',
        'gmd:referenceSystemInfo/gmd:MD_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS_Identifier/gmd:version/gco:CharacterString'               
        ]

        idinfo=[
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:Date',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:edition/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:citedResponsibleParty/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:citedResponsibleParty/gmd:CI_ResponsibleParty/gmd:positionName/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:citedResponsibleParty/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:citedResponsibleParty/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:citedResponsibleParty/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:administrativeArea/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:citedResponsibleParty/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:citedResponsibleParty/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gmd:Country',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:citedResponsibleParty/gmd:CI_ResponsibleParty/gmd:role/gmd:CI_RoleCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:presentationForm/gmd:CI_PresentationFormCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:abstract/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:purpose/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:status/gmd:MD_ProgressCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact/gmd:CI_ResponsibleParty/gmd:positionName/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:administrativeArea/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gmd:Country',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:pointOfContact/gmd:CI_ResponsibleParty/gmd:role/gmd:CI_RoleCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceMaintenance/gmd:MD_MaintenanceInformation/gmd:maintenanceAndUpdateFrequency/gmd:MD_MaintenanceFrequencyCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:keyword/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:type/gmd:MD_KeywordTypeCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:thesaurusName/gmd:CI_Citation/gmd:title/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:thesaurusName/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:Date',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:thesaurusName/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_Constraints/gmd:useLimitation/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:accessConstraints/gmd:MD_RestrictionCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:resourceConstraints/gmd:MD_LegalConstraints/gmd:useConstraints/gmd:MD_RestrictionCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:spatialRepresentationType/gmd:MD_SpatialRepresentationTypeCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:language/gmd:LanguageCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:characterSet/gmd:MD_CharacterSetCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:topicCategory/gmd:MD_TopicCategoryCode',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:environmentDescription/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:description/gco:CharacterString',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:extentTypeCode/gco:Boolean',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:beginPosition',
        'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:endPosition'
        ]

        dist=[
        'gmd:distributionInfo/gmd:MD_Distribution/gmd:distributionFormat/gmd:MD_Format/gmd:name/gco:CharacterString',
##        'gmd:distributionInfo/gmd:MD_Distribution/gmd:distributionFormat/gmd:MD_Format/gmd:version/gco:CharacterString',
        'gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorContact/gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString',
        'gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorContact/gmd:CI_ResponsibleParty/gmd:positionName/gco:CharacterString',
        'gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorContact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString',
        'gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorContact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:city/gco:CharacterString',
        'gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorContact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:administrativeArea/gco:CharacterString',
        'gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorContact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:postalCode/gco:CharacterString',
        'gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorContact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:country/gmd:Country',
        'gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorContact/gmd:CI_ResponsibleParty/gmd:role/gmd:CI_RoleCode',
        'gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:transferSize/gco:Real'        
        ]


        dataq=[
        'gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:scope/gmd:DQ_Scope/gmd:level/gmd:MD_ScopeCode',
        'gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:statement/gco:CharacterString',
        'gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:source/gmd:LI_Source/gmd:description/gco:CharacterString',
        'gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:source/gmd:LI_Source/gmd:sourceCitation/gmd:CI_Citation/gmd:title/gco:CharacterString',
        'gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:source/gmd:LI_Source/gmd:sourceCitation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:Date',
        'gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:source/gmd:LI_Source/gmd:sourceCitation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode'
        ]

        meta=[
        'gmd:metadataConstraints/gmd:MD_Constraints/gmd:useLimitation/gco:CharacterString',
        'gmd:metadataConstraints/gmd:MD_LegalConstraints/gmd:accessConstraints/gmd:MD_RestrictionCode',
        'gmd:metadataConstraints/gmd:MD_LegalConstraints/gmd:useConstraints/gmd:MD_RestrictionCode',
        'gmd:metadataMaintenance/gmd:MD_MaintenanceInformation/gmd:maintenanceAndUpdateFrequency/gmd:MD_MaintenanceFrequencyCode',
        'gmd:metadataMaintenance/gmd:MD_MaintenanceInformation/gmd:maintenanceNote/gco:CharacterString'
        ]
        
##Two lists to hold errors and checked values respectively. Two functions, one to check for nodes
##that are missing, and one to check for nodes that are missing required text values.

        problems=[]
        noproblems=[]

        def elemcheck(nodelist):
            for node in nodelist:
                elem = root.find(node, namespaces)
                if elem is None:
                    problems.append('PROBLEM - THIS REQUIRED ELEMENT IS MISSING: %s.'%node)

        def valcheck(nodelist):
            for node in nodelist:
                for elem in root.findall(node, namespaces):      
                    for stuff in elem.iter():            
                        if stuff.text !=None:
                            noproblems.append('Tag %s in %s checked for value %s.' %(stuff.tag, node.split('/')[-2].strip('gmd'),stuff.text))
                        else:
                            problems.append('PROBLEM - A REQUIRED TEXT VALUE IS MISSING FOR: %s.' %node)
                                                   
##Read all the lists into one giant list and pass them to the functions

        all_lists=[header1,contact,header2,spatial,idinfo,dist,dataq,meta]

        for alist in all_lists:
            elemcheck(alist)
            valcheck(alist)

##Read through the results of the functions and generate the two reports

        if problems !=None:
            print('*** File %s has %s problems - see error report for details'%(checkfile,len(problems)))
            writeprob.writelines('*** Errors with %s: *** \n'%checkfile)     
            writeprob.writelines('\n')
            for errors in problems:            
                writeprob.writelines(errors+'\n')
                writeprob.writelines('\n')
            writeprob.writelines('\n')
        else:
            print('* No problems with %s'%checkfile)
            
##To write the values for no problems, we split the values based on the location of curly braces
##in order to avoid writing out the full address of the node - we just get the current tag
## and its parent.

        writenoprob.writelines('*** %s Values checked for %s: *** \n'%(len(noproblems),checkfile))
        writenoprob.writelines('\n')
        for values in noproblems:
            writenoprob.writelines((values.split('{')[0],values.split('}')[1].strip()))
            writenoprob.writelines('\n')
            writenoprob.writelines('\n') 
        writenoprob.writelines('\n')
        print('Checked values report created for %s'%checkfile)
            
writeprob.close()
writenoprob.close()



