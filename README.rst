Project setup
=============

Django Rest API Boilerplate
---------------------------

Welcome to the Django Rest API Boilerplate! This repository provides a comprehensive template for setting up a backend API service using Django and Django Rest Framework, ready to be hosted on AWS S3. Designed to give developers a head start, this boilerplate includes essential configurations and dependencies to build robust and scalable web applications.

Features
--------

- **Django 4.2**: Leverage the latest features of Django to build powerful web applications.
- **Django Rest Framework 3.14.0**: Create RESTful APIs with ease using a powerful, flexible toolkit.
- **PostgreSQL Support**: Integrated with `psycopg2` for PostgreSQL database connectivity.
- **Django Filter and Split Settings**: Simplify complex queries and organize Django settings into multiple files for better environment management.
- **Boto3 for AWS S3**: Ready-to-use AWS S3 setup for hosting static and media files.
- **Channels 4.0.0**: Utilize Django Channels for handling WebSockets, chat protocols, and more.
- **CORS Headers Configuration**: Included `django-cors-headers` for handling Cross-Origin Resource Sharing (CORS).
- **Additional Libraries**: Support for image operations with Pillow, YAML configurations with PyYAML, and more.

Prerequisites
-------------

- Python 3.12: Ensure Python 3.12 or newer is installed on your system.
- Poetry: This project uses Poetry for dependency management. Install Poetry before proceeding with the setup.

Setup
-----

1. **Clone the Repository**: Start by cloning this repository to your local machine.**

.. code-block:: bash


    git clone <repository-url>
    cd <repository-name>
    

2. **Install Dependencies**: Use Poetry to install the required dependencies.**

.. code-block:: bash


    poetry install
    

3. **Configure Settings**: Split settings are used for better configuration management. Adjust the settings in the `settings/` directory as per your environment.**

4. **Run Migrations**: Setup your database schema.**

.. code-block:: bash


    poetry run python manage.py migrate
    

5. **Run the Development Server**: Start the Django development server.**

.. code-block:: bash


    poetry run python manage.py runserver
    

6. **Deploy to AWS S3**: Follow the appropriate AWS documentation to configure your AWS S3 bucket for hosting.**

Development Tools
-----------------

- **Code Linting**: Flake8 for code linting.
- **Pre-commit Hooks**: Ensure code quality with pre-commit hooks.
- **Colorlog**: Enhanced logging with color support for better debugging.

License
-------

MIT License

Contribution
------------

Contributions are welcome! Please feel free to submit a pull request.

---

mkdir -p local
cp core/project/settings/templates/settings.dev.py ./local/settings.dev.py
