"""
MCP Server Implementation - After conversion
This is the new MCP-compatible server
"""

import asyncio
import json
import httpx
from mcp.server import Server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
from mcp.server.stdio import stdio_server

class JSONPlaceholderMCPServer:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.server = Server("jsonplaceholder-mcp")
        self.setup_tools()
    
    def setup_tools(self):
        @self.server.tool()
        async def get_posts(post_id: int = None) -> list[TextContent]:
            """
            Get blog posts from JSONPlaceholder API
            
            Args:
                post_id: Optional post ID to get specific post
            
            Returns:
                List of posts or single post details
            """
            async with httpx.AsyncClient() as client:
                try:
                    if post_id:
                        response = await client.get(f"{self.base_url}/posts/{post_id}")
                        post = response.json()
                        return [TextContent(
                            type="text",
                            text=f"**Post #{post['id']}**\n\n**Title:** {post['title']}\n\n**Content:** {post['body']}\n\n**Author ID:** {post['userId']}"
                        )]
                    else:
                        response = await client.get(f"{self.base_url}/posts")
                        posts = response.json()[:5]  # Limit to first 5 for demo
                        posts_text = "\n\n".join([
                            f"**Post #{post['id']}:** {post['title']}"
                            for post in posts
                        ])
                        return [TextContent(
                            type="text",
                            text=f"**Recent Posts:**\n\n{posts_text}"
                        )]
                except Exception as e:
                    return [TextContent(
                        type="text",
                        text=f"Error fetching posts: {str(e)}"
                    )]
        
        @self.server.tool()
        async def create_post(title: str, body: str, user_id: int) -> list[TextContent]:
            """
            Create a new blog post
            
            Args:
                title: Post title
                body: Post content
                user_id: Author's user ID
            
            Returns:
                Confirmation of post creation
            """
            async with httpx.AsyncClient() as client:
                try:
                    response = await client.post(
                        f"{self.base_url}/posts",
                        json={"title": title, "body": body, "userId": user_id}
                    )
                    post = response.json()
                    return [TextContent(
                        type="text",
                        text=f"✅ **Post Created Successfully!**\n\n**ID:** {post['id']}\n**Title:** {post['title']}\n**Content:** {post['body']}\n**Author ID:** {post['userId']}"
                    )]
                except Exception as e:
                    return [TextContent(
                        type="text",
                        text=f"❌ Error creating post: {str(e)}"
                    )]
        
        @self.server.tool()
        async def get_users(user_id: int = None) -> list[TextContent]:
            """
            Get user information from JSONPlaceholder API
            
            Args:
                user_id: Optional user ID to get specific user
            
            Returns:
                User information
            """
            async with httpx.AsyncClient() as client:
                try:
                    if user_id:
                        response = await client.get(f"{self.base_url}/users/{user_id}")
                        user = response.json()
                        return [TextContent(
                            type="text",
                            text=f"**User Profile:**\n\n**Name:** {user['name']}\n**Username:** {user['username']}\n**Email:** {user['email']}\n**Phone:** {user['phone']}\n**Website:** {user['website']}\n**Company:** {user['company']['name']}"
                        )]
                    else:
                        response = await client.get(f"{self.base_url}/users")
                        users = response.json()[:3]  # Limit to first 3 for demo
                        users_text = "\n\n".join([
                            f"**{user['name']}** (@{user['username']}) - {user['email']}"
                            for user in users
                        ])
                        return [TextContent(
                            type="text",
                            text=f"**Users:**\n\n{users_text}"
                        )]
                except Exception as e:
                    return [TextContent(
                        type="text",
                        text=f"Error fetching users: {str(e)}"
                    )]
        
        @self.server.tool()
        async def get_post_comments(post_id: int) -> list[TextContent]:
            """
            Get comments for a specific post
            
            Args:
                post_id: Post ID to get comments for
            
            Returns:
                List of comments for the post
            """
            async with httpx.AsyncClient() as client:
                try:
                    response = await client.get(f"{self.base_url}/posts/{post_id}/comments")
                    comments = response.json()[:3]  # Limit to first 3 for demo
                    comments_text = "\n\n".join([
                        f"**{comment['name']}** ({comment['email']})\n{comment['body']}"
                        for comment in comments
                    ])
                    return [TextContent(
                        type="text",
                        text=f"**Comments for Post #{post_id}:**\n\n{comments_text}"
                    )]
                except Exception as e:
                    return [TextContent(
                        type="text",
                        text=f"Error fetching comments: {str(e)}"
                    )]
