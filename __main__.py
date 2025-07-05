"""
Main entry point for the demo
"""

import sys
import asyncio
from demo_runner import DemoRunner

async def main():
    runner = DemoRunner()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--rest":
            await runner.run_rest_demo()
        elif sys.argv[1] == "--mcp":
            runner.run_mcp_demo()
        else:
            print("Usage: python demo_runner.py [--rest|--mcp]")
    else:
        # Run both demos
        await runner.run_rest_demo()
        input("\nPress Enter to start MCP server demo...")
        runner.run_mcp_demo()

if __name__ == "__main__":
    asyncio.run(main())
