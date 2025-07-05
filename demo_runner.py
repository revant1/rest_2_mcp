"""
Demo script to showcase both REST and MCP approaches
"""

import asyncio
import subprocess
import sys
import os

class DemoRunner:
    def __init__(self):
        self.rest_client = None
    
    async def run_rest_demo(self):
        """Run the original REST API demo"""
        print("🚀 Starting REST API Demo...")
        print("=" * 50)
        
        # Import and run original REST client
        from original_rest_client import JSONPlaceholderClient, demo_original_api
        await demo_original_api()
        
        print("\n" + "=" * 50)
        print("✅ REST API Demo Complete!")
    
    def run_mcp_demo(self):
        """Run the MCP server demo"""
        print("\n🚀 Starting MCP Server Demo...")
        print("=" * 50)
        print("MCP Server is now running!")
        print("You can connect to it using any MCP-compatible client.")
        print("\nTo test with Claude Desktop, add this to your config:")
        print(json.dumps({
            "mcpServers": {
                "jsonplaceholder": {
                    "command": "python",
                    "args": ["mcp_server.py"],
                    "env": {}
                }
            }
        }, indent=2))
        
        print("\n🔧 Available MCP Tools:")
        print("- get_posts(post_id?: int) - Get blog posts")
        print("- create_post(title: str, body: str, user_id: int) - Create new post")
        print("- get_users(user_id?: int) - Get user information")
        print("- get_post_comments(post_id: int) - Get comments for a post")
        
        print("\n🎯 Try these example calls:")
        print("- 'Get me the first blog post'")
        print("- 'Create a new post about AI with title \"AI Revolution\"'")
        print("- 'Show me user information for user 1'")
        print("- 'Get comments for post 1'")
        
        # Run the actual MCP server
        print("\n⚡ Starting MCP Server...")
        try:
            import mcp_server
            asyncio.run(mcp_server.main())
        except KeyboardInterrupt:
            print("\n✅ MCP Server Demo Complete!")
