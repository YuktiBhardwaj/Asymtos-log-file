from flask import Flask, render_template
from log_operations import FileProcessor

app = Flask(__name__)

# Define a route for serving static files
@app.route('/static/<path:path>')
def static_files(path):
    return app.send_static_file(path)

@app.route('/')
def index():
    # Initialize FileProcessor with the folder path and file name
    processor = FileProcessor(folder_path="C:/Users/DELL/Downloads/asym/tos/device/848665bf-8424-481d-ac8c-a3d047ca0fdf/logs", file_name="2023-09-27T15_10_12.999")

    # Process the file to extract timestamps, error count, source counts, and parsed data
    timestamps, error_count, source_counts, parsed_data = processor.process_file()

    # Pass the extracted data to the HTML template
    return render_template('index.html', timestamps=timestamps, error_count=error_count, source_counts=source_counts, parsed_data=parsed_data)

if __name__ == '__main__':
    app.run(debug=True)
