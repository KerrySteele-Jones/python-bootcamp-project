from InquirerPy import inquirer
from generator.choose_license import licenseList


def ask_questions():
    project_title = inquirer.text(message="What is the title of the project").execute()
    description = inquirer.text(message="Give a short description of your project").execute()
    features = inquirer.text(message="What are the features").execute()
    install = inquirer.text(message="What are the installation instructions").execute()
    usage = inquirer.text(message="How should the project be use").execute()
    choose_license = inquirer.select(
        message="Choose a license",
        choices=["MIT License", "Apache License", "GPL License", "BSD-2-Clause", "BSD-3-Clause", "BSD-4-Clause"],
    ).execute()
    author = inquirer.text(message="Who is the Author").execute()
    contact_information = inquirer.text(message="What is the contact information for the Author of the project").execute()

    return {
        "project_title": project_title,
        "description": description,
        "features": features,
        "install": install,
        "usage": usage,
        "license": choose_license,
        "author": author,
        "contact_information": contact_information,

    }


