import os
import json
from collections import defaultdict

class FileProcessor:
    def __init__(self, folder_path, file_name, delimiter=','):
        self.folder_path = folder_path
        self.file_name = file_name
        self.file_path = os.path.join(folder_path, file_name)
        self.delimiter = delimiter

    def process_file(self):
        timestamps = []
        error_count = 0
        source_counts = defaultdict(int)
        parsed_data = []

        with open(self.file_path, "r") as file:
            for line in file:
                try:
                    data = json.loads(line.strip())
                    parsed_data.append({
                        "severity": data.get('severity', ''),
                        "source": data.get('source', ''),
                        "content": data.get('content', ''),
                        "timestamp": data.get('timestamp', ''),
                        "filename": data.get('filename', ''),
                        "function": data.get('function', '')
                    })

                    timestamps.append(data.get('timestamp', ''))
                    if data.get('severity', '') == 'error':
                        error_count += 1
                    source_counts[data.get('source', '')] += 1
                except json.JSONDecodeError:
                    
                    continue

        return timestamps, error_count, dict(source_counts), parsed_data
