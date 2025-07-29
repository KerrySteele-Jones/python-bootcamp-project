## Python Week 6 README.md file

## Description
The project is a python-powered README file generator,created as part of a bootcamp assignment.  It uses terminal prompts to collect project information and then outputs a README.md ready to upload to GitHub.

View walkthrough on YouTube here 👉 https://youtu.be/E41n5RPQpDg

## Message to teacher ✏️✏️✏️
The app saves a file called "READTask.md" just so it does not overwrite the README.md file created for this assignment.  If used again it would save as READ.md. 

## Features
📋 Interactive command-line prompts using InquirerPy
💾 Automatically creates or overwrites a README.md file based on user input

## Installation Instructions
In the terminal run python3 main_start.py

## Notes to remember what I did for this assignment

- Created a virtual environment using "python3 -m venv venv where I can install everything I need, keeping everything clean and organised
- Used terminal to esnure I am working in my python environment - source venv/bin/activate & installed PyInquirer [pip install PyInquirer]
- Created a requirments.txt file.  This lists all of the packages used within my python enviroment and their versions. Uselful if collaborating with others ensuring that we are all working with the same dependecies within a python project (packages & versions).
- Created files and named them in a way that hopefully makes sense to me later 🤔.
- Created a list for Licences (following W3C)
- Planned and implemented prompt questions: define a **define a list of questions** and hand them to **prompt** [prompt returns a list of **answers**] (pypi.org)
    💻 using dictionaries in W3C to test
- Testing questions showed up an error that my version of Python would not work with PyInquirer, moved to InquirePy - change my queston syntax to name = inquirer.text(message="What's your name:").execute() (https://inquirerpy.readthedocs.io/en/latest/)
- used a fstring to pull in and write all the headings and titles for the readme file.
- created a function that uses file write.
- imported the file write function into main_start.py and added write.file at the end to make it! 

I DID A THING 🎉🤪

## Useful links that helped with assignment
https://pypi.org/project/PyInquirer/
https://pip.pypa.io/en/stable/user_guide/#requirements-files 
https://github.com/RichardLitt/standard-readme 
https://github.com/davidbgk/open-source-template/ 
https://realpython.com/readme-python-project/
https://docs.python.org/3/library/venv.html 
https://medium.com/@sim30217/pip-freeze-requirements-txt-993eb433ab0b
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository 
https://gist.github.com/nicolasdao/a7adda51f2f185e8d2700e1573d8a633
https://www.w3schools.com/python/python_lists.asp
https://docs.python.org/3/library/venv.html
https://inquirerpy.readthedocs.io/en/latest/
https://www.w3schools.com/python/python_file_write.asp 


## Author
Kerry Steele-Jones

## Contact 
kerry@createxr.co.uk | www.createxr.co.uk