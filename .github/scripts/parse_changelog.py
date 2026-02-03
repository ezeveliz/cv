import re
import json
import os
import sys

def main():
    file_path = "./RELEASES.md"
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("::error::RELEASES.md file not found.")
        sys.exit(1)
        
    version_pattern = r'<!-- Version start @@ ({.*?}) -->'
    match = re.search(version_pattern, content)
    
    if not match:
        print("::error::No version start tag found.")
        sys.exit(1)
        
    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError as e:
        print(f"::error::Error decoding JSON: {e}")
        sys.exit(1)
        
    start_index = match.end()
    rest_of_file = content[start_index:]
    
    # Find delimiters to determine end of current version block
    delimiter_pattern = re.compile(r'(<!-- Version start|<!-- Version end|\n-\s###\s)')
    matches = list(delimiter_pattern.finditer(rest_of_file))
    
    end_pos = len(rest_of_file)
    if matches:
        first_match = matches[0]
        prefix = rest_of_file[:first_match.start()].strip()
        # If first match is a header strictly at the start (current version header), skip it
        if not prefix and first_match.group().strip().startswith('- ###'):
            if len(matches) > 1:
                end_pos = matches[1].start()
            else:
                end_pos = len(rest_of_file)
        else:
            end_pos = first_match.start()
            
    changelog_body = rest_of_file[:end_pos].strip()
    
    # Write outputs to GITHUB_OUTPUT if available
    if 'GITHUB_OUTPUT' in os.environ:
        with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
            print(f"shouldCreateRelease={data.get('shouldCreateRelease', 'false')}", file=fh)
            print(f"shouldCreatePDF={data.get('shouldCreatePDF', '')}", file=fh)
            print(f"version={data.get('version', '')}", file=fh)
            print(f"release={data.get('release', '')}", file=fh)
            
            # Multiline string for changelog
            delimiter = "EOF"
            print(f"changelog<<{delimiter}", file=fh)
            print(changelog_body, file=fh)
            print(delimiter, file=fh)
    else:
        # Fallback for local testing
        print("GITHUB_OUTPUT not detected. Parsed values:")
        print(f"shouldCreateRelease: {data.get('shouldCreateRelease', 'false')}")
        print(f"version: {data.get('version', '')}")
        print(f"release: {data.get('release', '')}")
        print(f"Changelog length: {len(changelog_body)} chars")

if __name__ == "__main__":
    main()
