
---

# IT Asset Management System

This project is a simple IT Asset Management System built using Python, Flask, Pandas, and Openpyxl. It allows users to upload and manage IT asset data through Excel files, visualize asset details, and generate reports. The application tracks asset details such as asset name, type, purchase date, and status, and provides key metrics for asset management.

## Features

- Upload and process Excel files containing IT asset data.
- Display assets in a tabular format with asset details such as name, type, purchase date, and status.
- Automatically generate key metrics like total assets, assets nearing end-of-life, and unused software licenses.
- View a list of all previously uploaded reports and their respective metrics.
- Responsive and styled UI using CSS.

## Technologies Used

- **Flask**: Web framework for Python to build the web application.
- **Pandas**: For data manipulation and analysis.
- **Openpyxl**: To read and write Excel files.
- **HTML/CSS**: For frontend layout and styling.
- **Jinja2**: Templating engine for rendering dynamic content in HTML files.

## Setup and Installation

### Prerequisites

- Python 3.x
- Pip (Python package manager)

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/it-asset-management.git
   ```

2. Navigate into the project directory:
   ```bash
   cd it-asset-management
   ```

3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Flask application by running:
   ```bash
   python app.py
   ```

2. Open a web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. You can upload an Excel file, and the app will display the asset details and key metrics for the uploaded data.

## File Structure

```
IT-Asset-Management/
│
├── uploads/                    # Directory for storing uploaded files & reports
├── templates/                   # HTML templates for rendering pages
│   ├── index.html               # Home page
│   ├── login.html               # Login page
│   ├── signup.html              # Signup page
│   ├── data_form.html           # Form for uploading data files
│   ├── report.html              # Page for displaying report metrics
├── static/                      # Static files like CSS and images
│   └── styles.css               # CSS styles for the frontend
├── app.py                        # Main Flask application
├── requirements.txt              # Python dependencies
├── IT_Assets.xlsx                # Sample dataset (generated dynamically)
├── README.md                     # Project documentation
```

## Uploading and Viewing Reports

1. **Upload a Report**: On the home page (`index.html`), you can upload an Excel file containing IT asset data. After uploading, the application will parse the file, extract relevant information, and display the asset details.
   
2. **View Reports**: After successfully uploading a file, you will see the metrics related to the contents of the Excel file, including:
   - Total number of assets
   - Number of assets nearing end-of-life
   - Number of unused software licenses
   
3. **List of All Reports**: All previously uploaded reports are listed on the page with their associated metrics.

## Sample Excel Dataset

Here is a sample dataset to get started with testing the application:

```plaintext
| Asset Name        | Asset Type | Purchase Date | Status             |
|-------------------|------------|---------------|--------------------|
| Dell XPS 13       | Laptop     | 2021-02-20    | Active             |
| Microsoft Office  | Software   | 2020-08-15    | Unused             |
| MacBook Pro       | Laptop     | 2020-11-10    | Active             |
| Adobe Photoshop   | Software   | 2019-05-05    | Nearing End-of-Life|
| Samsung Galaxy    | Mobile     | 2022-01-12    | Active             |
| Windows 10        | Software   | 2020-06-23    | Active             |
| Slack             | Software   | 2021-03-30    | Active             |
| HP Printer        | Hardware   | 2018-09-05    | Nearing End-of-Life|
| Microsoft Word    | Software   | 2020-08-15    | Active             |
| iPhone 12         | Mobile     | 2021-05-10    | Active             |
```

You can upload this dataset through the app interface.

## Metrics

After uploading a report, the application will display the following metrics:

- **Total Number of Assets**: Count of all assets in the uploaded report.
- **Assets Nearing End-of-Life**: Count of assets marked as "Nearing End-of-Life".
- **Unused Software Licenses**: Count of software assets marked as "Unused".

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are welcome!

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
