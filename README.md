# Card Gen

This project is a personal project – A vCard generator built with a ReactJS frontend and a Python Flask App backend.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

1. Clone the repository: `git clone [repository URL]`
2. Install the node dependencies:
    - `cd card-gen-app`
    - `npm install`
3. Install the python dependencies:
    - `cd card-gen-backend`
    - `python3 -m venv venv`
    - `source venv/bin/activate`
    - `pip install -r requirements.txt`

## Usage - Local Use

1. cd into the backend folder: `cd card-gen-backend`
2. Activate the virtual environment: `source venv/bin/activate`
3. Start the Flask server: `flask --app gen --debug run`
4. cd into the app folder: `cd ../card-gen-app`
5. Start the React server: `npm start`
6. Open your browser and navigate to `http://localhost:3000`

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
