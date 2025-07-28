from generator.prompt_questions import ask_questions

def main():
    answers =ask_questions()

    read_me = f"""
    ## Project Title 
    {answers["project_title"]}

    ## Description \n
    {answers["description"]} 

    """
    print(read_me)
    
if __name__ == "__main__":
    main()