"""
Design Thread Module

This module provides functionality for handling various design-related tasks
in the digital twin framework, including network analysis, product lifecycle
management (PLM), and computer-aided manufacturing (CAM).

Available submodules:
- nx: Network analysis using the NetworkX library
- plm: Product lifecycle management integration and processing
- cam: Computer-aided manufacturing integration and processing
"""

from .nx import NetworkAnalysis
from .plm import PLMIntegration
from .cam import CAMIntegration

__all__ = [
    'NetworkAnalysis',
    'PLMIntegration',
    'CAMIntegration',
]
