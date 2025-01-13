
# Brain Hemorrhage Project

This project is a Django-based web application for Brain Hemorrhage detection.

## Prerequisites

- Python (>= 3.6)
- MySQL (or any other supported database)

## Installation

Follow these steps to set up and run the project:

### 1. Install Python

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### 2. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yajneshshetty/Intracranial-hemorrhage-detection-ICH-.git
cd Intracranial-hemorrhage-detection-ICH-/Brain_Hemorrhage
```

### 3. Create and Activate a Virtual Environment (Optional but Recommended)

- **On Windows**:

```bash
python -m venv venv
. venv\Scripts\activate
```

- **On macOS/Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install the Required Libraries

Install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Create the Database

Create a new database called `brain` using your preferred database management system.:

```bash
CREATE DATABASE brain;
```

### 6. Configure the Database Settings

In the `settings.py` file, update the `DATABASES` section with your database credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.your_db',
        'NAME': 'brain',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 7. Run Migrations

Apply the migrations to set up your database schema:

```bash
python manage.py migrate
```

### 8. Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

## Usage

After running the server, you can access the application in your web browser at:

```
http://127.0.0.1:8000/
```

## Contributing

Feel free to fork the repository and submit pull requests.
