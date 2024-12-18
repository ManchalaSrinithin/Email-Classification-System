---

# Email Classification System 

## Overview

The **Email Classification System** is a web-based application designed to classify emails into predefined categories using FastAPI and the Groq API. It supports both individual email classification and bulk processing of emails from a CSV file.

## Features

- **Email Classification**: Categorize individual emails into predefined categories.
- **Spam Detection**: Identify if an email is spam.
- **Relevance Assessment**: Determine the relevance of an email.
- **CSV File Upload**: Upload and classify multiple emails from a CSV file.
- **Category Filtering**: View emails based on their assigned categories.

## Technologies Used

- **FastAPI**: Web framework for building APIs with Python.
- **Groq API**: External API for email classification and relevance assessment.
- **HTML/CSS/JavaScript**: Frontend technologies for user interface.

## Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)
- Groq API key

### Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/genzverse-24/1222-Code-Conquerors.git
    cd genzverse-24/1222-Code-Conquerors
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Groq API Key**

   Open `app.py` and replace the placeholder with your actual Groq API key.

   ```python
   client = Groq(api_key="your_groq_api_key")
   ```

5. **Run the Application**

    ```bash
    uvicorn app:app --reload
    ```

    Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the application.

## Usage

1. **Classify an Email**

    - **Enter Email Details**: Use the form on the web interface to enter the email's details: address, subject, and body.
    - **Submit for Classification**: Click "Classify Email" to get the email's classification and category.

2. **Upload a CSV File**

    - **Upload CSV**: Click "Upload CSV File" to select and upload a CSV file containing multiple emails.
    - **Processing**: The application will read the CSV, classify each email, and display the results.

3. **View Categorized Emails**

    - **Filter by Category**: Use the sidebar menu to view emails categorized under different predefined categories.

## CSV File Guidelines

### Format

- **File Type**: CSV

### Columns

The CSV file should include the following columns:

- **email**: The email address of the sender.
- **subject**: The subject line of the email.
- **body**: The body content of the email.

### Example

Here’s an example of the required CSV format:

```csv
email                     subject                    body
example1@gmail.com    Meeting Request    Please schedule a meeting for next week.
example2@gmail.com    Job Application    Attached is my resume for the open position.
example3@gmail.com    HR Query           Can you provide more details about the company policies?
```

### Guidelines

- **Headers**: Ensure that the CSV file contains the headers `email`, `subject`, and `body` in the first row (case-sensitive).
- **Data Accuracy**: Make sure that the data in the columns is accurate and relevant.
- **File Size**: There might be limits on the file size. Ensure that the CSV file is within acceptable limits for upload.

## Contributing

To contribute to this project:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your branch to GitHub (`git push origin feature-branch`).
5. Submit a Pull Request with a clear description of your changes.

## Acknowledgments

- Special thanks to the **Genzeon Hackathon** team for the opportunity to develop this project.
- Thanks to **Groq API** for providing classification and relevance assessment capabilities.
- Inspired by modern email processing systems and tools.
  
---
