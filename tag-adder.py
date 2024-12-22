import os
import re
import argparse
from typing import List, Set

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

def parse_yaml_tags(yaml_content: str) -> Set[str]:
    """Parse tags from YAML content."""
    tags = set()
    tag_pattern = re.compile(r'tags:\s*\[(.*?)\]|tags:\s*\n-\s*(.*?)(?:\n|$)', re.DOTALL)
    match = tag_pattern.search(yaml_content)
    
    if match:
        # Handle inline array format: tags: [tag1, tag2]
        if match.group(1):
            tags.update(tag.strip() for tag in match.group(1).split(','))
        # Handle list format: tags:\n- tag1\n- tag2
        elif match.group(2):
            tags.add(match.group(2).strip())
            list_pattern = re.compile(r'-\s*(.*?)(?:\n|$)')
            tags.update(m.group(1).strip() for m in list_pattern.finditer(yaml_content))
    
    return {tag for tag in tags if tag}  # Remove empty tags

def add_tag_to_yaml(yaml_content: str, new_tag: str) -> str:
    """Add a new tag to the YAML frontmatter."""
    existing_tags = parse_yaml_tags(yaml_content)
    existing_tags.add(new_tag)
    
    # Remove old tags section if it exists
    yaml_content = re.sub(r'tags:\s*\[.*?\]|tags:\s*\n(?:-\s*.*?\n)*', '', yaml_content)
    
    # Add new tags section
    tags_str = f"tags: [{', '.join(sorted(existing_tags))}]\n"
    if yaml_content.strip():
        return yaml_content.strip() + '\n' + tags_str
    return tags_str

def process_file(filepath: str, tag: str, dry_run: bool = False) -> None:
    """Process a single markdown file to add the specified tag."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        pre_yaml, yaml_content, post_yaml = extract_yaml_frontmatter(content)
        new_yaml = add_tag_to_yaml(yaml_content, tag)
        new_content = pre_yaml + new_yaml + post_yaml
        
        if dry_run:
            print(f"Would modify {filepath}:")
            print(new_content[:200] + '...' if len(new_content) > 200 else new_content)
            return
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Successfully updated {filepath}")
        
    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Add a tag to all markdown files in a directory')
    parser.add_argument('tag', help='Tag to add to files')
    parser.add_argument('--directory', '-d', default='.', 
                        help='Directory to process (default: current directory)')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help='Show what would be done without making changes')
    
    args = parser.parse_args()
    
    # Validate tag format
    if not re.match(r'^[a-zA-Z0-9_/-]+$', args.tag):
        print("Error: Tag should only contain letters, numbers, underscores, forward slashes, or hyphens")
        return
    
    # Get all markdown files
    markdown_files = get_markdown_files(args.directory)
    if not markdown_files:
        print(f"No markdown files found in {args.directory}")
        return
    
    print(f"Found {len(markdown_files)} markdown files")
    
    # Process each file
    for filepath in markdown_files:
        process_file(filepath, args.tag, args.dry_run)

if __name__ == '__main__':
    main()
