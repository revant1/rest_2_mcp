"""
Original REST API Client - Before MCP conversion
This demonstrates the traditional way of calling APIs
"""

import httpx
import asyncio
import json

class JSONPlaceholderClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
    
    async def get_posts(self, post_id=None):
        """Get posts from the API"""
        async with httpx.AsyncClient() as client:
            if post_id:
                response = await client.get(f"{self.base_url}/posts/{post_id}")
            else:
                response = await client.get(f"{self.base_url}/posts")
            return response.json()
    
    async def create_post(self, title, body, user_id):
        """Create a new post"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/posts",
                json={"title": title, "body": body, "userId": user_id}
            )
            return response.json()
    
    async def get_users(self, user_id=None):
        """Get users from the API"""
        async with httpx.AsyncClient() as client:
            if user_id:
                response = await client.get(f"{self.base_url}/users/{user_id}")
            else:
                response = await client.get(f"{self.base_url}/users")
            return response.json()

# Demo function for original REST client
async def demo_original_api():
    print("=== Original REST API Demo ===")
    client = JSONPlaceholderClient()
    
    # Get first post
    print("\n1. Getting first post...")
    post = await client.get_posts(1)
    print(f"Title: {post['title']}")
    print(f"Body: {post['body'][:50]}...")
    
    # Create new post
    print("\n2. Creating new post...")
    new_post = await client.create_post(
        title="Demo Post",
        body="This is a demo post created via REST API",
        user_id=1
    )
    print(f"Created post with ID: {new_post['id']}")
    
    # Get user info
    print("\n3. Getting user info...")
    user = await client.get_users(1)
    print(f"User: {user['name']} ({user['email']})")
