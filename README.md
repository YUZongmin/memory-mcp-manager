# Memory MCP Manager

A tool to manage and switch between different memory paths for Claude clients using the Model Context Protocol (MCP) memory server.

This project helps manage memory configurations for Claude clients that use the [mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) server for persistent memory storage.

## Features

- Manage multiple memory paths with easy-to-remember names
- Quick switching between different memory configurations
- Support for multiple Claude clients (Claude Desktop, Cline, etc.)
- Persistent storage of memory paths and client configurations
- Automatic initialization with default settings

## Prerequisites

- Python 3.x
- A Claude client that uses the MCP memory server (e.g., Claude Desktop, Cline)
- [mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) server installed and configured

## Installation

1. Clone the repository
2. Make the script executable: `chmod +x memory.sh`
3. The first time you run `./memory.sh`, it will automatically create a configuration file based on the template

## Usage

### Basic Commands

1. Initialize or reset configuration:

```bash
./memory.sh init
```

2. List all configured memory paths:

```bash
./memory.sh list
```

3. Switch to a specific memory configuration:

```bash
./memory.sh switch <name>
```

4. Add a new memory path:

```bash
./memory.sh add <name> <path>
```

5. Remove a memory path:

```bash
./memory.sh remove <name>
```

### Client Management

1. List configured clients:

```bash
./memory.sh list-clients
```

2. Add a new client:

```bash
./memory.sh add-client <name> <config_path>
```

## Configuration

The configuration is stored in two files:

- `config.template.json`: Version-controlled template with default settings
- `config.json`: Your personal configuration file (git-ignored)

### Example Client Paths

For macOS:

```
~/Library/Application Support/Claude/claude_desktop_config.json
~/Library/Application Support/Cursor/User/globalStorage/rooveterinaryinc.roo-cline/settings/cline_mcp_settings.json
```

### Example Memory Path Structure

Memory paths typically follow a structure like:

```
~/path/to/project/memory.jsonl
```

## How It Works

This tool manages the memory path configuration for Claude clients that use the [mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) server. The server enables persistent memory through a local knowledge graph, allowing Claude to maintain context and information across sessions.

When you switch memory paths, the tool updates the configuration files of all registered Claude clients to use the new memory path. This allows you to maintain separate memory contexts for different projects or purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
