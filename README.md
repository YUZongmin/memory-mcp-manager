# Memory MCP Manager

A tool to manage and switch between different memory paths for Claude clients using the [mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) server.

## Prerequisites

- Python 3.x
- A Claude client with MCP memory server
- [mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) installed

## Quick Start

```bash
# Install
git clone https://github.com/yourusername/memory-mcp-manager.git
cd memory-mcp-manager
chmod +x memory.sh

# Setup
./memory.sh init
./memory.sh add-client my-claude "/path/to/claude/config.json"
./memory.sh add project1 "~/projects/project1/memory.jsonl"
./memory.sh switch project1
```

## Commands

```bash
# Client Management
./memory.sh add-client <name> <config_path>  # Add a Claude client
./memory.sh list-clients                     # List configured clients

# Memory Management
./memory.sh add <name> <path>     # Add a memory path
./memory.sh remove <name>         # Remove a memory path
./memory.sh switch <name>         # Switch to a memory path
./memory.sh list                  # List all memory paths
```

## Configuration

Your settings are stored in `config.json` (git-ignored):

```json
{
  "clients": [
    {
      "name": "my-claude",
      "config_path": "/path/to/claude/config.json"
    }
  ],
  "memory_paths": {
    "project1": "/path/to/project1/memory.jsonl"
  }
}
```

## How It Works

When switching memory paths, the tool updates all registered Claude clients to use the new memory path, allowing you to maintain separate memory contexts for different projects.
