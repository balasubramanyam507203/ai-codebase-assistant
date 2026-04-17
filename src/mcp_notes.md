# MCP Layer for AI Codebase Assistant

## What is MCP?
MCP (Model Context Protocol) is a standard for connecting AI applications to external tools, resources, and prompts.

## How MCP fits this project
This project currently uses local Python tools for:
- explaining pasted code
- searching the indexed codebase
- finding possible bugs

In a future MCP-enabled version, these capabilities could be backed by MCP servers instead of local-only logic.

## MCP concept mapping
- Resources: repository files, documentation pages, configuration files
- Tools: search repository, fetch file contents, run code analysis
- Prompts: reusable code review and debugging templates

## Future MCP integrations
- GitHub MCP server
- Filesystem MCP server
- Documentation MCP server
- External API or engineering metadata server

## Why this matters
MCP would make the assistant more modular, reusable, and easier to connect with real engineering systems.