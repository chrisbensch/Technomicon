import os
import re
import argparse
from typing import List

def get_markdown_files(directory: str) -> List[str]:
    """Recursively find all .md files in the given directory."""
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def has_last_modified_line(content: str) -> bool:
    """Check if the file already has a Last Modified line."""
    patterns = [
        r"Last updated: `\$= dv\.current\(\)\.file\.mtime",
        r"Last modified: `\$= dv\.current\(\)\.file\.mtime"
    ]
    return any(re.search(pattern, content) for pattern in patterns)

def add_last_modified_line(content: str) -> str:
    """Add Last Modified line to the content with proper spacing."""
    # Remove trailing whitespace and newlines
    content = content.rstrip()
    
    # Add newlines and the Last Modified line
    return (f"{content}\n\n\n"
            f"Last updated: `$= dv.current().file.mtime.toFormat(\"MMMM dd, yyyy 'at' HH:mm\")`\n")

def process_file(filepath: str, dry_run: bool = False) -> None:
    """Process a single markdown file to add Last Modified line."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Skip if Last Modified line already exists
        if has_last_modified_line(content):
            print(f"Skipping {filepath} - Last Modified line already exists")
            return
        
        new_content = add_last_modified_line(content)
        
        if dry_run:
            print(f"Would modify {filepath}:")
            print("..." + new_content[-200:] if len(new_content) > 200 else new_content)
            return
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Successfully added Last Modified line to {filepath}")
        
    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(
        description='Add Last Modified line to markdown files that don\'t have one')
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
