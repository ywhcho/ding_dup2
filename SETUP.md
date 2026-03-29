# Django + MySQL Setup Instructions

## Requirements

- Python 3.x
- Django
- MySQL

## Steps

1. **Install Dependencies**
   ```bash
   pip install django mysqlclient python-dotenv
   ```

2. **Setup Environment Variables**
   Create a `.env` file at the root of your project with the following content:
   ```plaintext
   NAME=mydatabase
   USER=myusername
   PASSWORD=
   HOST=localhost
   PORT=3306
   ```
   > **Note:** Do not commit your `.env` file. Add it to `.gitignore`.  

3. **Create Django Project**
   ```bash
   django-admin startproject config .
   ```

4. **Create Django App**
   ```bash
   python manage.py startapp min_dup
   ```

5. **Update `settings.py`**
   - Configure DATABASES to use environment variables.
   - Set up authentication using Django's built-in views.
   - Add your app to `INSTALLED_APPS`.

6. **Add Models and Admin Interface**
   - Create a model for Medicine in `min_dup/models.py`.
   - Register the model in `min_dup/admin.py`.

7. **Implement Views and Templates**
   - Create necessary views for your app.
   - Design `templates/base.html` with a navbar.

8. **Sample Data and Management Command**
   - Create a fixture or management command to load sample data into your database.

9. **Migrations**
   - Run migrations to create the necessary database tables.
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
10. **Update `requirements.txt`**
    > Add necessary packages to your `requirements.txt`.

11. **Create `.gitignore`**
    Add the following entries:
    ```plaintext
    .env
    venv/
    __pycache__/
    *.pyc
    ```
    
12. **Run Your Application**
    ```bash
    python manage.py runserver
    ```  

That’s it! Your Django + MySQL environment is ready.  
Make sure to follow best practices for security, especially with database credentials.