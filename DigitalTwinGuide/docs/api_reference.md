API Reference for the Digital Twin Guide
This document provides an overview of the Application Programming Interface (API) for the Digital Twin Guide. The API allows you to interact with the various threads and sub-threads in the guide programmatically, using Python scripts.

Requirements Thread API
The Requirements Thread API provides functions for working with the System Requirements, DOORS, Cameo, and SysML sub-threads. The following functions are available:

get_system_requirements(): Returns a list of system requirements for the project.
get_doors_requirements(): Returns a list of requirements from DOORS.
get_cameo_requirements(): Returns a list of requirements from Cameo.
get_sysml_requirements(): Returns a list of requirements modeled in SysML.
Design Thread API
The Design Thread API provides functions for working with the 3D Models, Design Documents, Siemens NX, PLM, and CAM sub-threads. The following functions are available:

get_3d_models(): Returns a list of 3D models for the project.
get_design_documents(): Returns a list of design documents for the project.
get_siemens_nx_models(): Returns a list of models created in Siemens NX.
get_plm_documents(): Returns a list of documents managed in the PLM system.
get_cam_programs(): Returns a list of programs created in the CAM software.
ECP Thread API
The ECP Thread API provides functions for working with the ECP Documents, BOM, Jira, Siemens Teamcenter, and SAP sub-threads. The following functions are available:

get_ecp_documents(): Returns a list of ECP documents for the project.
get_bom(): Returns a Bill of Materials (BOM) for the project.
get_jira_tickets(): Returns a list of Jira tickets related to the project.
get_teamcenter_documents(): Returns a list of documents managed in the Siemens Teamcenter system.
get_sap_documents(): Returns a list of documents managed in the SAP system.
Materials Management Thread API
The Materials Management Thread API provides functions for working with the BOM, Inventory Data, Jira, Siemens Teamcenter, and SAP sub-threads. The following functions are available:

get_bom(): Returns a Bill of Materials (BOM) for the project.
get_inventory_data(): Returns inventory data for the project.
get_jira_tickets(): Returns a list of Jira tickets related to the project.
get_teamcenter_documents(): Returns a list of documents managed in the Siemens Teamcenter system.
get_sap_documents(): Returns a list of documents managed in the SAP system.
Software Integration Thread API
The Software Integration Thread API provides functions for working with the Code, Test Results, Simulink, Jira, and Siemens Teamcenter sub-threads. The following functions are available:

get_code(): Returns the code for the project.
get_test_results(): Returns the results of tests run on the project.
get_simulink_models(): Returns a list of Simulink models for the project.
get_jira_tickets(): Returns a list of Jira tickets related to the project.
get_teamcenter_documents(): Returns a list of documents managed in the Siemens Teamcenter system.
Test Thread API
The Test Thread API provides functions for working with the Test Cases, Test Results, Selenium, Cucumber, Jira, Python, and Java sub-threads.