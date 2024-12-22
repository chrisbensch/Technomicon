import os

# Define the directory of your Obsidian vault
vault_path = "/Users/chrisbensch/zTemp/Technomicon"

# Define the YAML frontmatter to add
default_yaml = """---
category: Uncategorized
tags: []
---
"""

for root, _, files in os.walk(vault_path):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, "r+", encoding="utf-8") as f:
                content = f.read()
                if not content.startswith("---"):
                    f.seek(0)
                    f.write(default_yaml + content)

