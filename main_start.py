from generator.prompt_questions import ask_questions

def main():
    answers =ask_questions()

    read_me = f"""
    ## Project Title 
    {answers["project_title"]}

    ## Description 
    {answers["description"]} 

    ## Features
    {answers["features"]} 

    ## Installation Instructions
    {answers["install"]} 

    ## Usage
    {answers["usage"]} 

    ## License
    {answers["license"]} 

    ## Author
    {answers["author"]}

    ## Contact Information
    {answers["contact_information"]}

    """
    print(read_me)
    
if __name__ == "__main__":
    main()