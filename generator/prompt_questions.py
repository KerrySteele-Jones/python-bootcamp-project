from PyInquirer import prompt
from generator.choose_license import licenseList

questions = [
{
'type': 'input',
'name': 'project_title',
'message': 'What is the title of the project',
},
{
'type': 'input',
'name': 'description',
'message': 'Give a short description of your project',
},
{
'type': 'input',
'name': 'features',
'message': 'What are the features',
},
{
'type': 'input',
'name': 'installation_instructions',
'message': 'What are the installation instructions',
},
{
'type': 'input',
'name': 'usage',
'message': 'How should the project be used',
},
{
'type': 'list',
'name': 'license',
'message': 'Choose a license',
"choices": licenseList
},
{
'type': 'input',
'name': 'author',
'message': 'Who is the Author',
},
{
'type': 'input',
'name': 'contact_information',
'message': 'What is the contact information for the Author of the project',
},
]

def ask_questions():
    return prompt(questions)