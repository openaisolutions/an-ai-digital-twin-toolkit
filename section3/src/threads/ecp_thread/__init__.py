"""
ECP Thread Module

This module provides functionality for handling various Engineering Change Proposal (ECP) related tasks
in the digital twin framework, including ECP processing, Bill of Materials (BOM) management, and integration
with various systems like JIRA, Teamcenter, and SAP.

Available submodules:
- ecp: Engineering Change Proposal processing and management
- bom: Bill of Materials management
- jira: Integration with JIRA for issue tracking
- teamcenter: Integration with Teamcenter for PLM
- sap: Integration with SAP for ERP

"""

from .ecp import ECPProcessor
from .bom import BOMManager
from .jira import JiraIntegration
from .teamcenter import TeamcenterIntegration
from .sap import SAPIntegration

__all__ = [
    'ECPProcessor',
    'BOMManager',
    'JiraIntegration',
    'TeamcenterIntegration',
    'SAPIntegration',
]
