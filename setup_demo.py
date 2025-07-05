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

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run REST API demo:
   ```bash
   python demo_runner.py --rest
   ```

3. Run MCP server demo:
   ```bash
   python demo_runner.py --mcp
   ```

## Files

- `original_rest_client.py` - Original REST API implementation
- `mcp_server.py` - New MCP server implementation
- `demo_runner.py` - Demo script
- `setup_demo.py` - Setup script

## Demo Commands

Try these with the MCP server:
- "Get me the latest blog posts"
- "Create a new post about technology"
- "Show me user profiles"
- "Get comments for the first post"
"""
    }
    
    for filename, content in files_content.items():
        with open(os.path.join("mcp_demo", filename), "w") as f:
            f.write(content)
    
    print("✅ Project structure created!")

if __name__ == "__main__":
    install_requirements()
    create_project_structure()
    print("\n🎉 Demo setup complete!")
    print("📁 Check the 'mcp_demo' directory for all files")
    print("🚀 Run 'python demo_runner.py --rest' to start the REST demo")
    print("🚀 Run 'python demo_runner.py --mcp' to start the MCP server")

