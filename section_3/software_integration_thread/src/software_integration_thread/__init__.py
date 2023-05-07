"""
The software_integration_thread package contains modules that implement functionality
for software integration thread.

Modules
-------
code.py: This module contains the class Code which represents code that can be integrated 
         into the digital twin.
test.py: This module contains the class Test which represents a test that can be run on 
         the digital twin.
simulink.py: This module contains the class Simulink which represents a Simulink model 
             that can be integrated into the digital twin.
jira.py: This module contains the class Jira which represents a Jira issue that is associated 
         with the software integration thread.
teamcenter.py: This module contains the class Teamcenter which represents a Teamcenter 
               item that is associated with the software integration thread.
"""

from .code import Code
from .test import Test
from .simulink import Simulink
from .jira import Jira
from .teamcenter import Teamcenter
