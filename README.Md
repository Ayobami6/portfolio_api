# Backend Engineer Rest API Portfolio App Template

## Overview
This project is a template for backend engineers to showcase their skills and projects through a REST API. Built with best practices, and Django Rest Framework, and integrated with PostgreSQL/Sqlite for robust data management.


## Getting Started
1. **Clone the repository**:
   ```
   git clone https://github.com/Ayobami6/portfolio_api.git
   ```
2. **Navigate to the project directory**:
   ```
   cd portfolio_api
   ```
3. **Create a virtual nnvironment**:
   ```
   python -m venv venv
   ```

4. **Activate the environment**
   ```
   source ./venv/bin/activate
   ```

5. **Connect your postgresql database or use default sqlite**
   ```bash
   # .env
   DB_NAME=""
   DB_USER=""
   DB_HOST=""
   DB_PASSWORD=""
   REDIS_URL=""
   MACHINE="local" # optional to use for postgres or not for sqlite
   ```

6. **Make migration**
   ```bash
   # use make 
   make migrate
   # or
   python manage.py migrate
   ```

7. **Start the app**
   ```bash
   make run
   # or 
   python manage.py runserver
   ```

Visit the admin page to update your portfolio details

## Customization
You can customize to your liking by adding other creative features, and if you want to make the features available to others, you can submit a pull request.

## Contributing
Contributions are welcome! feel free to submit a pull request or create an issue.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

