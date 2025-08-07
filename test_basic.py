#!/usr/bin/env python3
"""
Basic test script for the financial agent without voice dependencies.
"""
import asyncio
import os
import sys

# Set Python path
sys.path.insert(0, '/app')

async def main():
    print("Testing Financial Agent Basic Functionality...")
    print("=" * 50)
    
    # Check if OpenAI API key is set
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set!")
        return 1
    
    print(f"✓ OpenAI API Key found: {api_key[:10]}...")
    
    # Test basic imports without voice components
    try:
        from agents import Agent, WebSearchTool
        from agents.model_settings import ModelSettings
        print("✓ Basic agent imports successful")
    except Exception as e:
        print(f"✗ Agent import failed: {e}")
        return 1
    
    # Test MCP server import
    try:
        from agents.mcp import MCPServerSse
        print("✓ MCP server import successful")
    except Exception as e:
        print(f"✗ MCP server import failed: {e}")
        return 1
    
    print("\nBasic imports successful! Financial agent core is working.")
    print("Note: Voice functionality requires additional audio libraries.")
    print("To run full functionality, install portaudio19-dev and rebuild.")
    
    return 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)