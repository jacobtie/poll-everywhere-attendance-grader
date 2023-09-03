# PollEverywhere Attendance Grader

In my software engineering course at UNC Charlotte, I take attendance using PollEverywhere. Afterwards, I download the results as a CSV, but need a way to get the students absent from class from this CSV. Additionally, I also use PollEverywhere to take attendance for extra credit sessions, for which I need the list of students who attended. This script makes getting to this information easy.

Note that this is set up for my course, which meets twice a week and has extra credit sessions after class and may not work for an arbitrary course.

## Setup

### Python

To run this script, you need Python 3.10+ installed. Then, create a virtual environment with `python -m venv venv` and install the dependencies with `pip install -r requirements.txt`. The script itself does not require any third party dependencies, however testing is achieved with the third party `pytest` module.

### Student Names

Add the students names as an array of strings in a JSON file called `student_names.json`.

### PollEverywhere Results

After conducting an attendance poll with PollEverywhere, save it in the `attendance` folder in its respective module folder. The module name should be of the pattern `module-XX` where the module number is two digits (eg. 01 and 10). The CSV file should follow the naming format `class-X.csv` where the class number is 1 or 2. There is no need to modify the contents of the CSV from PollEverywhere.

## Running

To run the script, run `python main.py <module-number> <class-number>` for general attendance to print out the list of students who did not attend class, sorted alphabetically by last name. When taking attendance for an extra credit session, run `python main.py <module-number> <class-number> -e` which will print the present students alphabetically by their last names.

## Testing

To run the tests, run `pytest` or `python -m test`.
