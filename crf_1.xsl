<?xml version="1.0"?>
<xsl:stylesheet version="1.0" 
	 xmlns:odm="http://www.cdisc.org/ns/odm/v1.3"
	 xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	 xmlns:xlink="http://www.w3c.org/1999/xlink">

	<xsl:output method="html" version="4.0" encoding="UTF-8" indent="yes"/>

	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- File:         crf.xsl                                                                                  -->
	<!-- Date:         23-June-2006                                                                             -->
	<!-- Version:      1.0.0                                                                                    -->
	<!-- Author:       Dave Iberson-Hurst(Assero) with the kind assistance of Anthony Friebel (SAS)             -->
	<!-- Organization: Clinical Data Interchange Standards Consortium (CDISC)                                   -->
	<!-- Description:  This style sheet allows for the metadata held within an ODM file to be visualised. The   -->
	<!--               visualisation permits the CRF structures used to collect the data to be viewed along     -->
	<!--               with the associated SDTM annotations.                                                    -->
	<!--                                                                                                        -->
	<!-- Release Notes for version 1.0.0:                                                                       -->
	<!-- 1. Initial version.                                                                                    -->
    <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

	<xsl:variable name="FullWidth">1000</xsl:variable>
	<xsl:variable name="FillWidth">100%</xsl:variable>
	<xsl:variable name="Indent1">20</xsl:variable>
	<xsl:variable name="Indent2">40</xsl:variable>
	<xsl:variable name="Indent3">60</xsl:variable>
	<xsl:variable name="Indent4">80</xsl:variable>
	<xsl:variable name="FormClass">form</xsl:variable>
	<xsl:variable name="StudyClass">study</xsl:variable>
			
	<!--
		Template: The main template.
		Purpose:  Builds the entire HTML page.
	-->
	<xsl:template match="/">
	
		<html>
			<!-- Create the HTML Header, include any style information we need -->
			<head>
				<style type="text/css">
					p {text-align:left;font-size:8pt;font-family: verdana, arial, helvetica, sans-serif;}
					p.small {font-size:6pt;}
					p.annotation1 {text-align:center; font-size:8pt}
					p.annotation2 {text-align:left; font-size:8pt}
					p.audit {font-size:7pt; color:red}
					p.event {text-align:left; font-size:8pt}
					p.study {text-align:center; font-size:14pt}
					p.form {text-align:center; font-size:14pt}
					p.group {text-align:center; font-size:12pt}
					p.head {text-align:left; font-weight:bold; font-size:16pt;}
					p.infob {font-weight:bold; font-size:8pt;}
					p.info {font-size:8pt;}
					
					a.small {font-family: verdana, arial, helvetica, sans-serif; font-size: 8pt; font-style: normal; line-height: normal; font-weight: normal; text-align: left; color:5a5aef}
				</style>
				<title>Rendering of ODM Metadata. XSLT Stylesheet (R1.0.0)</title>
			</head>
			
			<!-- Now generate the CRFs within the ODM file. List the studies and then
			     detail each one. -->
			<body>
				<a name='top'/>
				<xsl:call-template name="ListStudies"/>
				<xsl:for-each select="/odm:ODM/odm:Study">
					<xsl:call-template name="Study">
						<xsl:with-param name="StudyTree" select="."/>	
					</xsl:call-template>	
				</xsl:for-each>
			</body>
		</html>
	</xsl:template>			

	<!--
		Template: ListStudies
		Purpose:  Lists all the studies within an ODM file.
	-->
	<xsl:template name="ListStudies">
		<table border='0' cellspacing='0' cellpadding='2'>
			<xsl:attribute name="width">
				<xsl:value-of select="$FullWidth"/>		
			</xsl:attribute>
			<tr>
				<td>
					<xsl:call-template name="ListHeading">
						<xsl:with-param name="Width" select="$FullWidth"/>
						<xsl:with-param name="Title">Studies</xsl:with-param>
					</xsl:call-template>
					<table width='100%' border='0' cellspacing='0' cellpadding='2'>
						<tr>
							<td width='150'><p class='infob'>Name</p></td>
							<td><p class='infob'>OID</p></td>
						</tr>
						<xsl:for-each select="/odm:ODM/odm:Study">
							<tr>
								<td valign='top'><p class='info'><xsl:value-of select="./odm:GlobalVariables/odm:StudyName"/></p></td>
							 	<td valign='top'>
									<p class='info'>
							  			<a>
											<xsl:attribute name="href">
												#<xsl:value-of select="@OID"/>
											</xsl:attribute>
											<xsl:value-of select="@OID"/>
										</a>
									</p>
						 		</td>
					 		</tr>
						</xsl:for-each>
					</table><br/> 
				</td>
			</tr>
		</table>
	</xsl:template>			
	
	<!--
		Template: Study
		Purpose:  Lists and displays all the metadata for a given study.
	-->
	<xsl:template name="Study">
		<xsl:param name="StudyTree"/>
		
		<!-- Display the study & protocol information.	-->
		<table border='0' cellspacing='0' cellpadding='2'>
			<xsl:attribute name="width">
				<xsl:value-of select="$FullWidth"/>		
			</xsl:attribute>
			<tr>
				<td> 
					<xsl:attribute name="width">
						<xsl:value-of select="$Indent1"/>		
					</xsl:attribute>
				</td>
				<td>
					<xsl:call-template name="InstanceHeading">
						<xsl:with-param name="AnchorName" select="@OID"/>
						<xsl:with-param name="Class" select="$StudyClass"/>
						<xsl:with-param name="Name" select="concat ('Study: ', $StudyTree/odm:GlobalVariables/odm:StudyName)"/>
						<xsl:with-param name="OID" select="@OID"/>
						<xsl:with-param name="Repeating" select="@Repeating"/>
						<xsl:with-param name="Width" select="$FillWidth"/>
						<xsl:with-param name="Link">Top</xsl:with-param>
						<xsl:with-param name="LinkText">Top</xsl:with-param>
					</xsl:call-template>
					<xsl:call-template name="StudyInfo">
						<xsl:with-param name="Width" select="$FillWidth"/>
						<xsl:with-param name="StudyTree" select="$StudyTree"/>
					</xsl:call-template>
				</td>
			</tr>					
		</table>
		<br/>
		
		<!-- 
		     Now list each of the MetaData Versions present in the ODM file. 
		     This just lists the name and OID for each MetaDataVersion present. 
		-->
		<xsl:call-template name="ListMetaData">
			<xsl:with-param name="StudyTree" select="$StudyTree"/>
		</xsl:call-template>
		
		<!-- 
		     Now display each of the MetaData Versions present. This loops for each 
		     MetaDataVersion and builds the tree of StudyEvents, Forms, ItemGroups and Items.
		-->
		<xsl:for-each select="$StudyTree/odm:MetaDataVersion">
			<table border='0' cellspacing='0' cellpadding='2'>
				<xsl:attribute name="width">
					<xsl:value-of select="$FullWidth"/>		
				</xsl:attribute>
				<tr>
					<td> 
						<xsl:attribute name="width">
							<xsl:value-of select="$Indent3"/>		
						</xsl:attribute>
					</td>
					<td>
						<xsl:call-template name="InstanceHeading">
							<xsl:with-param name="AnchorName" select="concat($StudyTree/@OID, '.', @OID)"/>
							<xsl:with-param name="Class" select="$FormClass"/>
							<xsl:with-param name="Name" select="concat ('MetaData: ', @Name)"/>
							<xsl:with-param name="OID" select="@OID"/>
							<xsl:with-param name="Repeating" select="@Repeating"/>
							<xsl:with-param name="Width" select="$FillWidth"/>
							<xsl:with-param name="Link" select="$StudyTree/@OID"/>
							<xsl:with-param name="LinkText">Study</xsl:with-param>
						</xsl:call-template>
					</td>
				</tr>
			</table>
			<table border='0' cellspacing='0' cellpadding='2'>
				<xsl:attribute name="width">
					<xsl:value-of select="$FullWidth"/>		
				</xsl:attribute>
				<tr>
					<td> 
						<xsl:attribute name="width">
							<xsl:value-of select="$Indent4"/>		
						</xsl:attribute>
					</td>
					<td>
						<xsl:call-template name="MetaDataVersion">
							<xsl:with-param name="MDV_Tree" select="."/>
							<xsl:with-param name="Key" select="concat($StudyTree/@OID, '.', @OID)"/>
						</xsl:call-template>
					</td>
				</tr>
			</table>
		</xsl:for-each>
	</xsl:template>			

	<!--
		Template: ListMetaData
		Purpose:  Lists all the metadata for a given study.
	-->
	<xsl:template name="ListMetaData">
		<xsl:param name="StudyTree"/>
		<table border='0' cellspacing='0' cellpadding='2'>
			<xsl:attribute name="width">
				<xsl:value-of select="$FullWidth"/>		
			</xsl:attribute>
			<tr>
				<td> 
					<xsl:attribute name="width">
						<xsl:value-of select="$Indent2"/>		
					</xsl:attribute>
				</td>
				<td>
					<xsl:call-template name="ListHeading">
						<xsl:with-param name="Width" select="$FillWidth"/>
						<xsl:with-param name="Title">MetaData</xsl:with-param>
					</xsl:call-template>
					<table width='100%' border='0' cellspacing='0' cellpadding='2'>
						<tr>
							<td width='150'><p class='infob'>Name</p></td>
							<td><p class='infob'>OID</p></td>
						</tr>
						<xsl:for-each select="$StudyTree/odm:MetaDataVersion">
							<tr>
							<td valign='top'><p class='info'><xsl:value-of select="@Name"/></p></td>
							 	<td valign='top'>
									<p class='info'>
							  			<a>
											<xsl:attribute name="href">
												#<xsl:value-of select="concat($StudyTree/@OID, '.', @OID)"/>
											</xsl:attribute>
											<xsl:value-of select="@OID"/>
										</a>
									</p>
						 		</td>
					 		</tr>
						</xsl:for-each>
					</table><br/> 
				</td>
			</tr>
		</table>
	</xsl:template>			
		
	<!--
		Template: StudyInfo
		Purpose:  Lists basic study information.
	-->
	<xsl:template name="StudyInfo">
		<xsl:param name="Width"/>
		<xsl:param name="StudyTree"/>
		<table border='0' cellspacing='0' cellpadding='2'>
			<xsl:attribute name="width">
				<xsl:value-of select="$Width"/>		
			</xsl:attribute>
			<tr>
				<td width='150'><p class='infob'><b>Name</b></p></td>
				<td><p class='info'><xsl:value-of select="$StudyTree/odm:GlobalVariables/odm:StudyName"/></p></td>
			</tr>
			<tr>
				<td><p class='infob'><b>Description</b></p></td>
				<td><p class='info'><xsl:value-of select="$StudyTree/odm:GlobalVariables/odm:StudyDescription"/></p></td>
			</tr>
			<tr>
				<td><p class='infob'><b>Protocol Name</b></p></td>
				<td><p class='info'><xsl:value-of select="$StudyTree/odm:GlobalVariables/odm:ProtocolName"/></p></td>
			</tr>					
		</table>
		<br/>
	</xsl:template>
				
	<!--
		Template: MetaDataVersion
		Purpose:  Displays each metadata version, the Events, the Forms, ItemGroups and Items
	-->
	<xsl:template name="MetaDataVersion">		 
		<xsl:param name="MDV_Tree"/>
		<xsl:param name="Key"/>
		<xsl:variable name="MDV_OID" select="@OID"/>
		
		<!-- Display each of the events in turn, listing the set of forms for each event. -->
		<xsl:call-template name="ListHeading">
			<xsl:with-param name="Width" select="$FillWidth"/>
			<xsl:with-param name="Title">Study Events and Forms</xsl:with-param>
		</xsl:call-template>
		<table width='100%' border='0' cellspacing='0' cellpadding='2'>
			<tr>
				<td><p class='infob'>Identifier</p></td>
				<td><p class='infob'>Mandatory</p></td>
				<td><p class='infob'>Forms</p></td>
			</tr>
			<xsl:for-each select="$MDV_Tree/odm:Protocol/odm:StudyEventRef">
				<xsl:variable name="SE_OID" select="@StudyEventOID"/>
			  	<xsl:variable name="SE_Man" select="@Mandatory"/>
				<tr>
				 	<td valign='top'><p class='info'><xsl:value-of select="$SE_OID"/></p></td>
				 	<td valign='top'><p class='info'><xsl:value-of select="$SE_Man"/></p></td>
				 	<td valign='top'>
						<p class='info'>
					  	<xsl:for-each select="$MDV_Tree/odm:StudyEventDef">
							<xsl:variable name="SED_OID" select="@OID"/>
						 	<xsl:if test="$SED_OID=$SE_OID">
								<xsl:for-each select="odm:FormRef">
							 		<xsl:variable name="F_OID" select="@FormOID"/>
							  		<xsl:variable name="FormKey" select="concat($Key, '.', $F_OID)"/>
							 		<a>
										<xsl:attribute name="href">
											#<xsl:value-of select="$FormKey"/>
										</xsl:attribute>
										<xsl:value-of select="$F_OID"/>
									</a>
									<br/>
								</xsl:for-each>
						 	</xsl:if>
					  	</xsl:for-each>
						</p>
				 	</td>
			  	</tr>
			</xsl:for-each>
		</table>  
		<br/>
	 
		<!-- Display the forms. Each form is composed of a set of groups. -->
		<xsl:for-each select="$MDV_Tree/odm:FormDef">
			<xsl:variable name="FD_Name" select="@Name"/>
			<xsl:variable name="FD_OID" select="@OID"/>
			<table width='100%' border='1' cellspacing='0' cellpadding='5'>
				<xsl:variable name="Class">form</xsl:variable>
	  			<xsl:variable name="FormKey" select="concat($Key, '.', $FD_OID)"/>
				<tr>
					<td>
						<xsl:call-template name="InstanceHeading">
							<xsl:with-param name="AnchorName" select="$FormKey"/>
							<xsl:with-param name="Class" select="$Class"/>
							<xsl:with-param name="Name" select="concat ('Form: ', $FD_Name)"/>
							<xsl:with-param name="OID" select="$FD_OID"/>
							<xsl:with-param name="Repeating" select="@Repeating"/>
							<xsl:with-param name="Width" select="$FillWidth"/>
							<xsl:with-param name="Link" select="$Key"/>
							<xsl:with-param name="LinkText">MetaData</xsl:with-param>
						</xsl:call-template>
					</td>
				</tr>
				<tr>
					<td>
						<xsl:for-each select="odm:ItemGroupRef">
							<xsl:variable name="IGR_OID" select="@ItemGroupOID"/>
							<table width='100%' border='0' cellspacing='0' cellpadding='2'>
								<tr>
									<td>
										<table width='100%' border='1' cellspacing='0' cellpadding='2'>
											<xsl:for-each select="$MDV_Tree/odm:ItemGroupDef">
												<xsl:variable name="IGD_OID" select="@OID"/>
												<xsl:variable name="IGD_Name" select="@Name"/>
												<xsl:if test="$IGR_OID=$IGD_OID">
													<xsl:call-template name="ItemGroup">
														<xsl:with-param name="MDV_Tree" select="$MDV_Tree"/>
													</xsl:call-template>	
												</xsl:if>
											</xsl:for-each>
										</table>
									</td>
								</tr>
							</table>
							<br/>
						</xsl:for-each>
					</td>
				</tr>
		 	</table>
		 	<br/>
		</xsl:for-each>
	</xsl:template>
	
	<!--
		Template: ItemGroup
		Purpose:  Displays an individual ItemGroup
	-->
	<xsl:template name="ItemGroup">
		<xsl:param name="MDV_Tree"/>
		<tr valign='top'>
			<td valign='top'>
				<p class='group'>
					<b>Group: <xsl:value-of select="@Name"/></b>
				</p>
				<p class='annotation1'>
					<i>OID=<xsl:value-of select="@OID"/>, Repeating=<xsl:value-of select="@Repeating"/></i>
				</p>
			</td>
		</tr>
		<tr valign='top'>
			<td valign='top'>
				<table border='0'>
				   <xsl:for-each select="odm:ItemRef">
						<xsl:variable name="IR_OID" select="@ItemOID"/>
						<xsl:for-each select="$MDV_Tree/odm:ItemDef">
							<xsl:variable name="ID_OID" select="@OID"/>
							<xsl:if test="$IR_OID=$ID_OID">
								<tr valign='top'>
					   				<td width='400' valign='top'>
					   					<p>
											<xsl:call-template name="QuestionText">
												<xsl:with-param name="OID" select="$ID_OID"/>
											</xsl:call-template>
											<br/>
											<font color='red'><xsl:call-template name="SDTMAnnotation"/></font>
										</p>
									</td>
									<td valign='top'> 
					   					<p>
											<xsl:call-template name="DataField">
												<xsl:with-param name="MDV_Tree" select="$MDV_Tree"/>
											</xsl:call-template><br/>
										</p>
									</td>
								</tr>
							</xsl:if>
						</xsl:for-each>
					</xsl:for-each>
				</table>
			</td>
		</tr>
	</xsl:template>
	
	<!--
		Template: QuestionText
		Purpose:  Displays the question text for a given Item.
	-->
	<xsl:template name="QuestionText">
		<xsl:choose>
		 	<xsl:when test="./odm:Question">
		 		<xsl:value-of select="./odm:Question/odm:TranslatedText"/>
	 		</xsl:when>
	 		<xsl:otherwise>
		 		<xsl:value-of select="@Name"/>
			</xsl:otherwise>
		</xsl:choose> 
	</xsl:template>
	
	<!--
		Template: SDTMAnnotation
		Purpose:  Determines if SDSVarName attribute exists and sets the annotated variable appropriately.
	-->
	<xsl:template name="SDTMAnnotation">
		<xsl:choose>
			<xsl:when test="./@SDSVarName">
				<xsl:value-of select="@SDSVarName"/>	
			</xsl:when>
	 		<xsl:otherwise>
		 		<b>@SDSVarName Not Set</b>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
	
	<!--
		Template: DataField
		Purpose:  Constructs a data field for an Item depending on the ItemDef
	-->
	<xsl:template name="DataField">
		<xsl:param name="OID"/>
		<xsl:param name="MDV_Tree"/>
		<xsl:variable name="ID_DT" select="@DataType"/>
		<xsl:choose>
		
			<!-- CodeList -->
			<xsl:when test="./odm:CodeListRef[@CodeListOID]">
			 	<xsl:variable name="ID_CLOID" select="./odm:CodeListRef/@CodeListOID"/>
		 		<xsl:for-each select="$MDV_Tree/odm:CodeList">
		 			<xsl:if test="@OID=$ID_CLOID">
						
						<!-- Drop Down List Version -->
						<!-- Radio button better in that very long TranslatedText content gets wrapped
						     whereas select ones do not. -->
						<!--<select>
			  				<xsl:attribute name="name">
					  			<xsl:value-of select="@OID"/>
			  				</xsl:attribute>
			  				<option>
					  			<xsl:attribute name="value">
							  		_blank			
					  			</xsl:attribute>
								Code List: <xsl:value-of select="@OID"/>
					 		</option>
					 		<xsl:for-each select="./odm:CodeListItem">
								<option>
						  			<xsl:attribute name="value">
								  			<xsl:value-of select="@CodedValue"/>
						  			</xsl:attribute>
									<xsl:value-of select="./odm:Decode/odm:TranslatedText"/>  
						 		</option>
							</xsl:for-each>
						</select>-->
						
						<!-- Radio Button Version -->
						<xsl:for-each select="./odm:CodeListItem">
							<xsl:call-template name="Radio">
								<xsl:with-param name="RadioName" select="@OID"/>
								<xsl:with-param name="RadioValue" select="@CodedValue"/>
								<xsl:with-param name="RadioText" select="./odm:Decode/odm:TranslatedText"/>
							</xsl:call-template>		
						</xsl:for-each>
					</xsl:if>
	 			</xsl:for-each>
	 		</xsl:when>
	 		
	 		<!-- Simple Text Field -->
			<xsl:when test="$ID_DT='text'">
		  		<xsl:choose>
			  		<xsl:when test="./@Length">
				  		<xsl:choose>
					  		<xsl:when test="@Length > 100">
							    <textarea>
							    	<xsl:attribute name="name">
								 		<xsl:value-of select="$OID"/>
					  				</xsl:attribute>
					  				<xsl:attribute name="rows">
										5
							  		</xsl:attribute>
							  		<xsl:attribute name="cols">
										40
							  		</xsl:attribute>
							  	</textarea>
					  		</xsl:when>
				  			<xsl:otherwise>
					  			<input>
						  			<xsl:attribute name="type">
										text
						  			</xsl:attribute>
					  				<xsl:attribute name="name">
								 			<xsl:value-of select="$OID"/>
					  				</xsl:attribute>
					  				<xsl:choose>
							  			<xsl:when test="@Length > 50">
									  		<xsl:attribute name="size">
												 		50
									  		</xsl:attribute>
							  			</xsl:when>
						  				<xsl:otherwise>
							  				<xsl:attribute name="size">
										 			<xsl:value-of select="@Length"/>
							  				</xsl:attribute>
						  				</xsl:otherwise>
						  			</xsl:choose>
					  				<xsl:attribute name="maxlength">
								 			<xsl:value-of select="@Length"/>
					  				</xsl:attribute>
			  					</input>
		  					</xsl:otherwise>
				  		</xsl:choose>
			  			</xsl:when>
		  			<xsl:otherwise>
			  			<i>Missing length attribute</i>	
		  			</xsl:otherwise>
	  			</xsl:choose>
			</xsl:when>
	
			<!-- Integer field -->
			<xsl:when test="$ID_DT='integer'">
			    <input>
					  <xsl:attribute name="type">
								 text
					  </xsl:attribute>
					  <xsl:attribute name="name">
								 <xsl:value-of select="$OID"/>
					  </xsl:attribute>
					  <xsl:attribute name="size">
								 <xsl:value-of select="@Length"/>
					  </xsl:attribute>
					  <xsl:attribute name="maxlength">
								 <xsl:value-of select="@Length"/>
					  </xsl:attribute>
				</input>
		
			</xsl:when>
			
			<!-- Float field -->
			<xsl:when test="$ID_DT='float'">
				<input>
					  <xsl:attribute name="type">
								 text
					  </xsl:attribute>
					  <xsl:attribute name="name">
								 <xsl:value-of select="$OID"/>A
					  </xsl:attribute>
					  <xsl:attribute name="size">
								 <xsl:value-of select="@Length"/>
					  </xsl:attribute>
					  <xsl:attribute name="maxlength">
								 <xsl:value-of select="@Length"/>
					  </xsl:attribute>
			  	</input>
				.
		  	  	<input>
					  <xsl:attribute name="type">
								 text
					  </xsl:attribute>
					  <xsl:attribute name="name">
								 <xsl:value-of select="$OID"/>B
					  </xsl:attribute>
					  <xsl:attribute name="size">
								 <xsl:value-of select="@SignificantDigits"/>
					  </xsl:attribute>
					  <xsl:attribute name="maxlength">
								 <xsl:value-of select="@SignificantDigits"/>
					  </xsl:attribute>
				</input>
			</xsl:when>
		
			<!-- Date field -->	
			<xsl:when test="$ID_DT='date'">
			  <xsl:call-template name="date"/>
			</xsl:when>
			
			<!-- Time field -->	
			<xsl:when test="$ID_DT='time'">
			  <xsl:call-template name="Time"/>
			</xsl:when>
			
			<!-- DateTime field -->	
			<xsl:when test="$ID_DT='datetime'">
			  <xsl:call-template name="date"/><b> + </b> 
			  <xsl:call-template name="Time"/>
			</xsl:when>
			
			<!-- Something we do not handle yet -->
			<xsl:otherwise>
			  <i>Not represented yet</i>
			</xsl:otherwise>
		</xsl:choose>
		
		<!-- If MeasurementUnitRef present, add the units -->
		<xsl:if test="./odm:MeasurementUnitRef[@MeasurementUnitOID]">
			<xsl:for-each select="./odm:MeasurementUnitRef">
			 	<!--
			 		The for-each is not strictly required, but processor fails to set $ID_MUOID
			 		<xsl:variable name="ID_MUOID" select="./odm:MeasurementUnitRef[@MeasurementUnitOID]"/>
			 	-->
			 	<xsl:variable name="ID_MUOID" select="@MeasurementUnitOID"/>  
				<xsl:for-each select="/odm:ODM/odm:Study/odm:BasicDefinitions/odm:MeasurementUnit">
			 		<xsl:if test="@OID=$ID_MUOID">
						( <xsl:value-of select="./odm:Symbol/odm:TranslatedText"/> )
					</xsl:if>
		 		</xsl:for-each>
	 		</xsl:for-each>
		</xsl:if>
		
	</xsl:template>

	<!--
		Template: Date
		Purpose:  Builds a date control.
	-->
	<xsl:template name="date">
		<xsl:call-template name="day"/>
		<xsl:call-template name="month"/>
		<xsl:call-template name="year"/>
	</xsl:template>
	
	<!--
		Template: Time
		Purpose:  Builds a time control.
	-->
	<xsl:template name="Time">
		<xsl:call-template name="Hour"/><b>:</b>
		<xsl:call-template name="Minute"/>
	</xsl:template>
	
	<!--
		Template: Day
		Purpose:  Builds a HTML select control for days as part of a date control
	-->
	<xsl:template name="day">
		<select>
			<xsl:attribute name="name">
				XXX
			</xsl:attribute>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="1"/>
				<xsl:with-param name="optiontext" select="1"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="2"/>
				<xsl:with-param name="optiontext" select="2"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="3"/>
				<xsl:with-param name="optiontext" select="3"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="4"/>
				<xsl:with-param name="optiontext" select="4"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="5"/>
				<xsl:with-param name="optiontext" select="5"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="6"/>
				<xsl:with-param name="optiontext" select="6"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="7"/>
				<xsl:with-param name="optiontext" select="7"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="8"/>
				<xsl:with-param name="optiontext" select="8"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="9"/>
				<xsl:with-param name="optiontext" select="9"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="10"/>
				<xsl:with-param name="optiontext" select="10"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="11"/>
				<xsl:with-param name="optiontext" select="11"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="12"/>
				<xsl:with-param name="optiontext" select="12"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="13"/>
				<xsl:with-param name="optiontext" select="13"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="14"/>
				<xsl:with-param name="optiontext" select="14"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="15"/>
				<xsl:with-param name="optiontext" select="15"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="16"/>
				<xsl:with-param name="optiontext" select="16"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="17"/>
				<xsl:with-param name="optiontext" select="17"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="18"/>
				<xsl:with-param name="optiontext" select="18"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="19"/>
				<xsl:with-param name="optiontext" select="19"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="20"/>
				<xsl:with-param name="optiontext" select="20"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="21"/>
				<xsl:with-param name="optiontext" select="21"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="22"/>
				<xsl:with-param name="optiontext" select="22"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="23"/>
				<xsl:with-param name="optiontext" select="23"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="24"/>
				<xsl:with-param name="optiontext" select="24"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="25"/>
				<xsl:with-param name="optiontext" select="25"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="26"/>
				<xsl:with-param name="optiontext" select="26"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="27"/>
				<xsl:with-param name="optiontext" select="27"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="28"/>
				<xsl:with-param name="optiontext" select="28"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="29"/>
				<xsl:with-param name="optiontext" select="29"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="30"/>
				<xsl:with-param name="optiontext" select="30"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="31"/>
				<xsl:with-param name="optiontext" select="31"/>
			</xsl:call-template>
		</select>
	</xsl:template>
	
	<!--
		Template: Month
		Purpose:  Builds a HTML select control for months as part of a date control
	-->
	<xsl:template name="month">
		<select>
			<xsl:attribute name="name">
				M123
			</xsl:attribute>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="1"/>
				<xsl:with-param name="optiontext" select="'Jan'"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="2"/>
				<xsl:with-param name="optiontext" select="'Feb'"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="3"/>
				<xsl:with-param name="optiontext" select="'Mar'"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="4"/>
				<xsl:with-param name="optiontext" select="'Apr'"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="5"/>
				<xsl:with-param name="optiontext" select="'May'"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="6"/>
				<xsl:with-param name="optiontext" select="'Jun'"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="7"/>
				<xsl:with-param name="optiontext" select="'Jul'"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="8"/>
				<xsl:with-param name="optiontext" select="'Aug'"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="9"/>
				<xsl:with-param name="optiontext" select="'Sep'"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="10"/>
				<xsl:with-param name="optiontext" select="'Oct'"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="11"/>
				<xsl:with-param name="optiontext" select="'Nov'"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="12"/>
				<xsl:with-param name="optiontext" select="'Dec'"/>
			</xsl:call-template>
		</select>
	</xsl:template>
	
	<!--
		Template: Year
		Purpose:  Builds a HTML text control for entering years as part of a date control.
	-->
	<xsl:template name="year">
		<input>
			<xsl:attribute name="type">
				text
			</xsl:attribute>
			<xsl:attribute name="name">
				YYYY
			</xsl:attribute>
			<xsl:attribute name="size">
				4
			</xsl:attribute>
			<xsl:attribute name="maxlength">
				4
			</xsl:attribute>
		</input>
	</xsl:template>
	
	<!--
		Template: Hour
		Purpose:  Builds a HTML select control for hours as part of a time control
	-->
	<xsl:template name="Hour">
		<select>
			<xsl:attribute name="name">
				XXX
			</xsl:attribute>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="0"/>
				<xsl:with-param name="optiontext">00</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="1"/>
				<xsl:with-param name="optiontext">01</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="2"/>
				<xsl:with-param name="optiontext">02</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="3"/>
				<xsl:with-param name="optiontext">03</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="4"/>
				<xsl:with-param name="optiontext">04</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="5"/>
				<xsl:with-param name="optiontext">05</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="6"/>
				<xsl:with-param name="optiontext">06</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="7"/>
				<xsl:with-param name="optiontext">07</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="8"/>
				<xsl:with-param name="optiontext">08</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="9"/>
				<xsl:with-param name="optiontext">09</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="10"/>
				<xsl:with-param name="optiontext" select="10"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="11"/>
				<xsl:with-param name="optiontext" select="11"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="12"/>
				<xsl:with-param name="optiontext" select="12"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="13"/>
				<xsl:with-param name="optiontext" select="13"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="14"/>
				<xsl:with-param name="optiontext" select="14"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="15"/>
				<xsl:with-param name="optiontext" select="15"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="16"/>
				<xsl:with-param name="optiontext" select="16"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="17"/>
				<xsl:with-param name="optiontext" select="17"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="18"/>
				<xsl:with-param name="optiontext" select="18"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="19"/>
				<xsl:with-param name="optiontext" select="19"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="20"/>
				<xsl:with-param name="optiontext" select="20"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="21"/>
				<xsl:with-param name="optiontext" select="21"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="22"/>
				<xsl:with-param name="optiontext" select="22"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="23"/>
				<xsl:with-param name="optiontext" select="23"/>
			</xsl:call-template>
		</select>
	</xsl:template>
	
	<!--
		Template: Hour
		Purpose:  Builds a HTML select control for hours as part of a time control
	-->
	<xsl:template name="Minute">
		<select>
			<xsl:attribute name="name">
				XXX
			</xsl:attribute>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="0"/>
				<xsl:with-param name="optiontext">00</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="1"/>
				<xsl:with-param name="optiontext">01</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="2"/>
				<xsl:with-param name="optiontext">02</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="3"/>
				<xsl:with-param name="optiontext">03</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="4"/>
				<xsl:with-param name="optiontext">04</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="5"/>
				<xsl:with-param name="optiontext">05</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="6"/>
				<xsl:with-param name="optiontext">06</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="7"/>
				<xsl:with-param name="optiontext">07</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="8"/>
				<xsl:with-param name="optiontext">08</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="9"/>
				<xsl:with-param name="optiontext">09</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="10"/>
				<xsl:with-param name="optiontext" select="10"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="11"/>
				<xsl:with-param name="optiontext" select="11"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="12"/>
				<xsl:with-param name="optiontext" select="12"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="13"/>
				<xsl:with-param name="optiontext" select="13"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="14"/>
				<xsl:with-param name="optiontext" select="14"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="15"/>
				<xsl:with-param name="optiontext" select="15"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="16"/>
				<xsl:with-param name="optiontext" select="16"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="17"/>
				<xsl:with-param name="optiontext" select="17"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="18"/>
				<xsl:with-param name="optiontext" select="18"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="19"/>
				<xsl:with-param name="optiontext" select="19"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="20"/>
				<xsl:with-param name="optiontext" select="20"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="21"/>
				<xsl:with-param name="optiontext" select="21"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="22"/>
				<xsl:with-param name="optiontext" select="22"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="23"/>
				<xsl:with-param name="optiontext" select="23"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="24"/>
				<xsl:with-param name="optiontext" select="24"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="25"/>
				<xsl:with-param name="optiontext" select="25"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="26"/>
				<xsl:with-param name="optiontext" select="26"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="27"/>
				<xsl:with-param name="optiontext" select="27"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="28"/>
				<xsl:with-param name="optiontext" select="28"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="29"/>
				<xsl:with-param name="optiontext" select="29"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="30"/>
				<xsl:with-param name="optiontext" select="30"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="31"/>
				<xsl:with-param name="optiontext" select="31"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="32"/>
				<xsl:with-param name="optiontext" select="32"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="33"/>
				<xsl:with-param name="optiontext" select="33"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="34"/>
				<xsl:with-param name="optiontext" select="34"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="35"/>
				<xsl:with-param name="optiontext" select="35"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="36"/>
				<xsl:with-param name="optiontext" select="36"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="37"/>
				<xsl:with-param name="optiontext" select="37"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="38"/>
				<xsl:with-param name="optiontext" select="38"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="39"/>
				<xsl:with-param name="optiontext" select="39"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="40"/>
				<xsl:with-param name="optiontext" select="40"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="41"/>
				<xsl:with-param name="optiontext" select="41"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="42"/>
				<xsl:with-param name="optiontext" select="42"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="43"/>
				<xsl:with-param name="optiontext" select="43"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="44"/>
				<xsl:with-param name="optiontext" select="44"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="45"/>
				<xsl:with-param name="optiontext" select="45"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="46"/>
				<xsl:with-param name="optiontext" select="46"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="47"/>
				<xsl:with-param name="optiontext" select="47"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="48"/>
				<xsl:with-param name="optiontext" select="48"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="49"/>
				<xsl:with-param name="optiontext" select="49"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="50"/>
				<xsl:with-param name="optiontext" select="50"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="51"/>
				<xsl:with-param name="optiontext" select="51"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="52"/>
				<xsl:with-param name="optiontext" select="52"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="53"/>
				<xsl:with-param name="optiontext" select="53"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="54"/>
				<xsl:with-param name="optiontext" select="54"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="55"/>
				<xsl:with-param name="optiontext" select="55"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="56"/>
				<xsl:with-param name="optiontext" select="56"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="57"/>
				<xsl:with-param name="optiontext" select="57"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="58"/>
				<xsl:with-param name="optiontext" select="58"/>
			</xsl:call-template>
			<xsl:call-template name="option">
				<xsl:with-param name="optionvalue" select="59"/>
				<xsl:with-param name="optiontext" select="59"/>
			</xsl:call-template>
		</select>
	</xsl:template>
	
	<!--
		Template: Option
		Purpose:  Builds an HTML option element for a select input.
	-->
	<xsl:template name="option">
		<xsl:param name="optionvalue"/>
		<xsl:param name="optiontext"/>
		<option>
			<xsl:attribute name="value">
				<xsl:value-of select="$optionvalue"/>
			</xsl:attribute>
			<xsl:value-of select="$optiontext"/>
		</option>
	</xsl:template>
	
	<!--
		Template: Radio
		Purpose:  Builds an HTML radio button element for a select input.
	-->
	<xsl:template name="Radio">
		<xsl:param name="RadioName"/>
		<xsl:param name="RadioValue"/>
		<xsl:param name="RadioText"/>
		<input type='radio'>
			<xsl:attribute name="name">
				<xsl:value-of select="$RadioName"/>
			</xsl:attribute>
			<xsl:attribute name="value">
				<xsl:value-of select="$RadioValue"/>
			</xsl:attribute>
			<xsl:value-of select="$RadioText"/><br/>
	 	</input>
		<label>
		 	<xsl:attribute name="for">
				<xsl:value-of select="$RadioName"/>
			</xsl:attribute>
			<xsl:value-of select="$RadioText"/>
		</label><br/>
	</xsl:template>

	<!--
		Template: TopLink
		Purpose:  Adds a link to the top of the page.
	-->
	<xsl:template name="TopLink">
		<xsl:param name="Link"/>
		<xsl:param name="LinkText"/>
		<td width='5%'>
			<a>
				<xsl:attribute name="href">#<xsl:value-of select="$Link"/></xsl:attribute>
				<p class='annotation'><xsl:value-of select="$LinkText"/></p>	
			</a>									
		</td>
	</xsl:template>

	<!--
		Template: ListHeading
		Purpose:  Builds a general heading.
	-->
	<xsl:template name="ListHeading">
		<xsl:param name="Width"/>
		<xsl:param name="Title"/>
		<table border='1' cellspacing='0' cellpadding='5'>
			<xsl:attribute name="width">
				<xsl:value-of select="$Width"/>		
			</xsl:attribute>
			<tr>
				<td><p class='head'><xsl:value-of select="$Title"/></p></td>
			</tr>
		</table><br/>
	</xsl:template>
	
	<!--
		Template: InstanceHeading
		Purpose:  Builds a title bar, consisting of a link to the top of the page, the item 
		          title text and a second link to the top. Also the OID is output plus the
		          repeating attribute.
	-->
	<xsl:template name="InstanceHeading">
		<xsl:param name="AnchorName"/>
		<xsl:param name="Class"/>
		<xsl:param name="Name"/>
		<xsl:param name="OID"/>
		<xsl:param name="Repeating"/>
		<xsl:param name="Width"/>
		<xsl:param name="Link"/>
		<xsl:param name="LinkText"/>
		<table border='1' cellspacing='0' cellpadding='5'>
			<xsl:attribute name="width">
				<xsl:value-of select="$Width"/>		
			</xsl:attribute>
			<tr><td>
				<a>
					<xsl:attribute name="name">
						<xsl:value-of select="$AnchorName"/>
					</xsl:attribute>
					<table width='100%' border='0' cellspacing='0' cellpadding='2'>
						<tr>
							<xsl:call-template name="TopLink">
								<xsl:with-param name="Link" select="$Link"/>
								<xsl:with-param name="LinkText" select="$LinkText"/>
							</xsl:call-template>
							<td width='90%'>
								<p>
									<xsl:attribute name="class">
										<xsl:value-of select="$Class"/>
									</xsl:attribute>
									<b><xsl:value-of select="$Name"/></b>
								</p>
								<p class='annotation1'>
									<i>OID=<xsl:value-of select="$OID"/>	
									<xsl:choose>
										<xsl:when test="$Repeating=Yes">
											Repeating=<xsl:value-of select="$Repeating"/>
										</xsl:when>
								 		<xsl:when test="$Repeating=No">
											Repeating=<xsl:value-of select="$Repeating"/>
										</xsl:when>
									</xsl:choose>
									</i>
								</p>
							</td>
							<xsl:call-template name="TopLink">
								<xsl:with-param name="Link" select="$Link"/>
								<xsl:with-param name="LinkText" select="$LinkText"/>
							</xsl:call-template>
						</tr>
					</table>
				</a>
			</td></tr>
		</table><br/>
	</xsl:template>
	
</xsl:stylesheet>