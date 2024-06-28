# Upload_Merge_File_to_AWS_S3


This Python script automates the process of merging CSV files from two different S3 buckets and uploading the merged file to another S3 bucket.

## Prerequisites

Before running the script, ensure you have:

- Python 3.x installed. If not installed, download it from [python.org](https://www.python.org/downloads/).
- `pip` package manager installed with Python. This usually comes with Python installation.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Upload_Merge_File_to_AWS_S3
   cd Upload_Merge_File_to_AWS_S3

2. **Install dependencies:**
   
   `bash`
    pip install boto3
   
   `bash`
    pip install boto3 pandas python-dotenv


3. **Configure AWS credentials:**

Ensure your AWS credentials are set up either through environment variables or AWS configuration files (`~/.aws/credentials`).


4. **Update configuration:**

Modify `config.py` file with your S3 bucket name, region, and other necessary configurations.


## Features

- **Upload:** Uploads a file to a specified S3 bucket.
- **Merge:** Merges multiple uploaded files into a single file in S3.


