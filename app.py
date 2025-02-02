import os
import datetime
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Set up the upload folder
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'xls', 'xlsx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# To store uploaded report information (this can be stored in a database in production)
reports_info = []

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the upload page and processing
@app.route('/', methods=['GET', 'POST'])
def index():
    global reports_info

    metrics = {
        'Total Assets': 0,
        'Assets Nearing End-of-Life': 0,
        'Unused Software Licenses': 0
    }

    if request.method == 'POST':
        file = request.files['file']

        if file and allowed_file(file.filename):
            # Secure the filename and save the file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Process the file using pandas (you can customize this based on your needs)
            df = pd.read_excel(filepath)

            # Generate a report file name
            report_name = filename.split('.')[0] + '_report.xlsx'
            report_filepath = os.path.join(app.config['UPLOAD_FOLDER'], report_name)

            # Calculate metrics for this specific report
            report_metrics = {
                'Total Assets': len(df),
                'Assets Nearing End-of-Life': df[df['Status'] == 'Nearing End-of-Life'].shape[0],
                'Unused Software Licenses': df[df['Status'] == 'Unused'].shape[0]
            }

            # Add the report details and metrics to the list (to keep track of uploads and metrics)
            report_details = {
                'file_name': filename,
                'upload_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'report_path': report_filepath,
                'metrics': report_metrics  # Store metrics with each report
            }
            # Insert the latest report at the top of the list (index 0)
            reports_info.insert(0, report_details)

            # Save a summary report as an Excel file (example)
            df_summary = df.describe()  # You can customize the summary calculation
            df_summary.to_excel(report_filepath)

            # Update cumulative metrics
            for key in metrics:
                metrics[key] = sum(report['metrics'][key] for report in reports_info)

            # Redirect to the report page after processing the file
            return render_template('report.html', success=True, reports=reports_info, metrics=metrics)

    # Always pass metrics (even if it's empty)
    return render_template('index.html', success=False, reports=reports_info, metrics=metrics)

# Route to download a specific report
@app.route('/download_report/<report_filename>')
def download_report(report_filename):
    return redirect(url_for('static', filename='uploads/' + report_filename))

# Route for displaying uploaded reports and cumulative metrics
@app.route('/reports')
def view_reports():
    metrics = {
        'Total Assets': 0,
        'Assets Nearing End-of-Life': 0,
        'Unused Software Licenses': 0
    }

    # Sum up metrics from all uploaded reports
    for report in reports_info:
        metrics['Total Assets'] += report['metrics']['Total Assets']
        metrics['Assets Nearing End-of-Life'] += report['metrics']['Assets Nearing End-of-Life']
        metrics['Unused Software Licenses'] += report['metrics']['Unused Software Licenses']

    return render_template('report.html', reports=reports_info, metrics=metrics)

if __name__ == '__main__':
    # Create upload folder if not exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.run(debug=True)
