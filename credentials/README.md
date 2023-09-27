
## Credentials Folder

The "credentials" folder is a dedicated directory within this project where sensitive information, such as database credentials and API keys, is stored. Storing sensitive credentials in a separate folder helps keep them secure and prevents accidental exposure through version control.

### Folder Structure
project/
├── ...
├── credentials/
│ ├── database_credentials.ini
│ └── api_keys.json
└── ...

### Files

1. `database_credentials.ini`: This file contains database connection details, including hostname, port, username, and database name.

2. `api_keys.json`: This file stores API keys for external services or APIs used in the project.

**Important**: Never commit sensitive credentials or API keys to version control. These files should be kept private and should not be shared in public repositories.

## Usage

To use the credentials stored in the "credentials" folder, follow these steps:

1. In your code, use a secure method to load and access these credentials. For example, you can use libraries like `configparser` for INI files and `json` for JSON files to read the credentials into your application.

Example for loading database credentials from `database_credentials.ini` in Python using `configparser`:

```python
import configparser

config = configparser.ConfigParser()
config.read('credentials/database_credentials.ini')

db_host = config['database']['hostname']
db_port = config['database']['port']
db_username = config['database']['username']
db_password = config['database']['password']
db_name = config['database']['database_name']
```

Example for loading API keys from api_keys.json in Python:

```
import json

with open('credentials/api_keys.json', 'r') as key_file:
    api_keys = json.load(key_file)

api_key = api_keys.get('api_key_name')  # Replace 'api_key_name' with the actual key name.
```
By following these steps, you can securely manage and use sensitive credentials in your project while keeping them separate from your codebase.


This README provides an overview of the "credentials" folder and guidelines on how to use it to store and access sensitive information in your project. Customize it to suit your specific project needs and provide clear instructions for your team members or collaborators.
