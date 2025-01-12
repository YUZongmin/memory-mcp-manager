import json
import os
import sys

CONFIG_FILE = "config.json"
CONFIG_TEMPLATE_FILE = "config.template.json"

def expand_path(path):
    """Expand ~ to user's home directory and resolve any relative paths."""
    return os.path.expanduser(os.path.expandvars(path))

def init_config():
    """Initialize configuration if it doesn't exist."""
    if not os.path.exists(CONFIG_FILE):
        if os.path.exists(CONFIG_TEMPLATE_FILE):
            with open(CONFIG_TEMPLATE_FILE, 'r') as f:
                config = json.load(f)
        else:
            config = {
                "clients": [],
                "memory_paths": {}
            }
        save_config(config)
        print("Initialized new configuration file")
    return load_config()

def load_config():
    """Load configuration, initializing if necessary."""
    if not os.path.exists(CONFIG_FILE):
        return init_config()
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def update_client_configs(memory_path):
    """Update memory path in all client configurations."""
    config = load_config()
    success = True
    
    for client in config["clients"]:
        try:
            config_path = expand_path(client["config_path"])
            with open(config_path, 'r') as f:
                client_config = json.load(f)
            
            if 'mcpServers' in client_config and 'memory' in client_config['mcpServers']:
                client_config['mcpServers']['memory']['args'][3] = memory_path
                
                with open(config_path, 'w') as f:
                    json.dump(client_config, f, indent=2)
                print(f"Updated {client['name']} config memory path to: {memory_path}")
        except Exception as e:
            print(f"Error updating {client['name']} config: {e}")
            success = False
    
    return success

def add_memory_path(name, path):
    config = load_config()
    config["memory_paths"][name] = expand_path(path)
    save_config(config)
    print(f"Added memory path '{name}' => '{path}'")

def remove_memory_path(name):
    config = load_config()
    if name in config["memory_paths"]:
        del config["memory_paths"][name]
        save_config(config)
        print(f"Removed memory path '{name}'")
    else:
        print(f"Memory path '{name}' not found")

def list_memory_paths():
    config = load_config()
    if not config["memory_paths"]:
        print("No memory paths configured")
        return
    
    print("\nConfigured memory paths:")
    for name, path in config["memory_paths"].items():
        print(f"  {name}: {path}")

def switch_memory(name):
    config = load_config()
    if name not in config["memory_paths"]:
        print(f"Error: Memory path '{name}' not found")
        return False
    
    path = config["memory_paths"][name]
    return update_client_configs(path)

def add_client(name, config_path):
    config = load_config()
    for client in config["clients"]:
        if client["name"] == name:
            print(f"Client '{name}' already exists")
            return False
    
    config["clients"].append({
        "name": name,
        "config_path": expand_path(config_path)
    })
    save_config(config)
    print(f"Added client '{name}' with config path: {config_path}")
    return True

def list_clients():
    config = load_config()
    print("\nConfigured clients:")
    for client in config["clients"]:
        print(f"  {client['name']}: {client['config_path']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Initialize config:  python memory_manager.py init")
        print("  Add memory path:    python memory_manager.py add <name> <path>")
        print("  Remove memory path: python memory_manager.py remove <name>")
        print("  List memory paths:  python memory_manager.py list")
        print("  Switch memory:      python memory_manager.py switch <name>")
        print("  Add client:         python memory_manager.py add-client <name> <config_path>")
        print("  List clients:       python memory_manager.py list-clients")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "init":
        init_config()
    elif command == "add" and len(sys.argv) == 4:
        add_memory_path(sys.argv[2], sys.argv[3])
    elif command == "remove" and len(sys.argv) == 3:
        remove_memory_path(sys.argv[2])
    elif command == "list":
        list_memory_paths()
    elif command == "switch" and len(sys.argv) == 3:
        switch_memory(sys.argv[2])
    elif command == "add-client" and len(sys.argv) == 4:
        add_client(sys.argv[2], sys.argv[3])
    elif command == "list-clients":
        list_clients()
    else:
        print("Invalid command or arguments") 