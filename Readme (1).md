# Science Equipment Catalogue

## Overview

This project is a catalogue of various science tools and equipment designed for the LASA science wing. The primary goal is to help science teachers keep track of items, including their location, quantity, description, and last updated time. Teachers can also edit or add items.

### Product Goals
- Display all equipment in the database
- Show item's location, quantity, description, and last update
- Allow teachers to edit or add items

### Tools and Technologies Used
- HTML
- CSS
- Python
- Flask
- SQLAlchemy
- Figma (for prototyping)
- Miro (for collaboration)

## Installation

### Prerequisites
- Python 3.x
- Virtual environment (optional but recommended)

### Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/science-equipment-catalogue.git
    cd science-equipment-catalogue
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Flask and SQLAlchemy:**
    ```sh
    pip install flask sqlalchemy
    ```

4. **Set up the database:**
    - Edit the `database.py` file to suit your needs.
    - Initialize the database (ensure you have SQLite or your preferred database installed).

5. **Run the Flask application:**
    ```sh
    flask run
    ```

6. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000`

## File Structure

- `app.py`: The main Flask application.
- `database.py`: Database setup and models.
- `templates/`: HTML templates for the application.
- `static/`: Static files like CSS and JavaScript.
- `design_process/`: Contains design board, Miro files and presentation.

## Design Process

The design process included prototyping using Figma for UX/UI design and Miro for online collaboration.

### Figma
- Used for creating graphic designs and user interface prototypes.
- Helped visualize the flow and layout of the website.

### Miro
- Used for brainstorming and feature planning.
- Aided in collaborative online sessions to gather ideas and finalize features.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

- Khush Lalchandani
- Austin Buckley
- Tate Smith

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgments

Thank you to Dr. Chin, Mr. Shockey, and my groupmates for helping us create and execute this project.

---