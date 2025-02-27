# Tourist Attractions

This is a Django-based web application for showcasing tourist attractions. Users can view details about various attractions, like them, and leave comments.

## Features

- View a list of tourist attractions
- View detailed information about each attraction
- Like attractions
- Leave comments on attractions
- Real-time search functionality

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/tourist-attractions.git
    cd tourist-attractions
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Install and configure `django-tailwind`:

    ```bash
    python manage.py tailwind init
    ```

    make sure to remove theme from settings before doing thi

    Follow the prompts to set up Tailwind CSS. Make sure to select the correct app name.

7. Run the Tailwind CSS build process:

    ```bash
    python manage.py tailwind start
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

9. Open your browser and go to `http://127.0.0.1:8000/` to see the application.

## Usage

- Navigate to the home page to see a list of tourist attractions.
- Click on an attraction to view its details.
- If logged in, you can like attractions and leave comments.
- Use the search bar to filter attractions in real-time.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.