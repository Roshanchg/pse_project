# Website Setup Instructions

Follow these steps to get the website up and running.

Make sure you have the following installed:
- **Python 3.13.1**: The version used during development.
- **Django**: Install using the following command:
    ```bash
    pip install django
    ```
## Steps to Run the Website

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Roshanchg/pse_project.git
    cd pse_project
    ```

2. **Navigate to the Project Directory**
    ```bash
    cd tourism
    ```

3. **Make Migrations**
    Generate migration files for the database:
    ```bash
    py manage.py makemigrations
    ```

4. **Apply Migrations**
    Apply the migrations to set up the database:
    ```bash
    py manage.py migrate
    ```

5. **Create/Set the Superuser Password**
    To set or change the superuser password, use the following command to create a superuser:
    ```bash
    py manage.py createsuperuser
    ```

    This will prompt you to enter a username, email, and password for the superuser. If you want to change the password for an existing superuser, use:
    ```bash
    py manage.py changepassword <superuser-username>
    ```

6. **Run the Server**
    Start the development server:
    ```bash
    py manage.py runserver
    ```

    The website should now be accessible at `http://127.0.0.1:8000/` by default.

## Project Structure

- **Templates Folder**: Templates are stored in the `templates` folder/directory.
- **Static Folder**: CSS, JavaScript, and images are stored inside the `static` directory in their respective folders.

### Key Templates:
- **`account.html`**: Page where the user views their account details (non-sensitive).
- **`accountedit.html`**: Page that lets users change their details such as name, email, etc.
- **`booking.html`**: Page where users select the package they want to book, including seeing the total billing.
- **`destinations_sections.html`** & **`package_section.html`**: Pages displayed in `index.html` (the homepage) using loops from a query in the database.
- **`loginform.html`**: Login page for the user to authenticate.
- **`regform.html`**: Registration page for new users to sign up.
- **`payment.html`**: The final stage of booking where the user confirms their payment by entering card details (no form validation is done).

### File Naming and Structure:
- Styles and scripts for each page are named the same as the HTML file, with different extensions.
    - For example:
        - `index.html` has `index.css` and `index.js`.
        - `booking.html` has `booking.css` and `booking.js`, and so on.

## Additional Information

- Ensure that your database is correctly configured in the `settings.py` file if you're using a different database other than SQLite.
- If you encounter any issues during setup, make sure Django is installed and try running the migrations again.
