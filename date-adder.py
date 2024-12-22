import os
import re
import argparse
from datetime import datetime
from typing import List, Optional
import platform
from pathlib import Path

def get_creation_time(filepath: str) -> datetime:
    """Get file creation time cross-platform."""
    if platform.system() == 'Windows':
        return datetime.fromtimestamp(os.path.getctime(filepath))
    else:
        # On Unix, use stat to get creation time
        stat = os.stat(filepath)
        # Try birth time first (not available on all Unix systems)
        try:
            return datetime.fromtimestamp(stat.st_birthtime)
        except AttributeError:
            # Fallback to earliest of modification or metadata change time
            return datetime.fromtimestamp(min(stat.st_mtime, stat.st_ctime))

def get_markdown_files(directory: str) -> List[str]:
    """Recursively find all .md files in the given directory."""
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def extract_yaml_frontmatter(content: str) -> tuple[str, str, str]:
    """Extract YAML frontmatter from the content.
    Returns: (pre_yaml, yaml_content, post_yaml)"""
    yaml_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
    match = yaml_pattern.match(content)
    
    if match:
        yaml_content = match.group(1)
        post_yaml = content[match.end():]
        return ('---\n', yaml_content, '\n---\n' + post_yaml)
    return ('---\n', '', '\n---\n' + content)

def get_existing_created_date(yaml_content: str) -> Optional[str]:
    """Check if created date exists in YAML content."""
    created_pattern = re.compile(r'created:\s*([^\n]+)')
    match = created_pattern.search(yaml_content)
    return match.group(1).strip() if match else None

def add_created_date(yaml_content: str, date: datetime) -> str:
    """Add creation date to YAML frontmatter if it doesn't exist."""
    if get_existing_created_date(yaml_content):
        return yaml_content
    
    date_str = date.strftime('%Y-%m-%d')
    created_str = f"created: {date_str}\n"
    
    if yaml_content.strip():
        return yaml_content.strip() + '\n' + created_str
    return created_str

def process_file(filepath: str, dry_run: bool = False) -> None:
    """Process a single markdown file to add creation date."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        pre_yaml, yaml_content, post_yaml = extract_yaml_frontmatter(content)
        
        # Skip if created date already exists
        if get_existing_created_date(yaml_content):
            print(f"Skipping {filepath} - created date already exists")
            return
        
        # Get file creation time
        creation_date = get_creation_time(filepath)
        new_yaml = add_created_date(yaml_content, creation_date)
        new_content = pre_yaml + new_yaml + post_yaml
        
        if dry_run:
            print(f"Would modify {filepath}:")
            print(new_content[:200] + '...' if len(new_content) > 200 else new_content)
            return
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Successfully added created date to {filepath}")
        
    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(
        description='Add creation date to markdown files that don\'t have one')
    parser.add_argument('--directory', '-d', default='.', 
                       help='Directory to process (default: current directory)')
    parser.add_argument('--dry-run', '-n', action='store_true',
                       help='Show what would be done without making changes')
    
    args = parser.parse_args()
    
    # Get all markdown files
    markdown_files = get_markdown_files(args.directory)
    if not markdown_files:
        print(f"No markdown files found in {args.directory}")
        return
    
    print(f"Found {len(markdown_files)} markdown files")
    
    # Process each file
    for filepath in markdown_files:
        process_file(filepath, args.dry_run)

if __name__ == '__main__':
    main()