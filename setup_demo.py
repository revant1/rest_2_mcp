"""
Setup script for the demo
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    subprocess.run([sys.executable, "-m", "pip", "install", "mcp", "httpx"])
    print("✅ Requirements installed!")

def create_project_structure():
    """Create the demo project structure"""
    print("📁 Creating project structure...")
    
    # Create main directory
    os.makedirs("mcp_demo", exist_ok=True)
    
    # Create files with content
    files_content = {
        "requirements.txt": "mcp>=1.0.0\nhttpx>=0.25.0\nasyncio>=3.4.3",
        "README.md": """# MCP Demo Project
