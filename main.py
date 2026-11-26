from hr_assistant.pipeline import ask, build_hr_assistant


def main():
    print("Building the HR policy assistant ...")
    agent = build_hr_assistant()
    print("Assistant ready! \n")

    demo_ques = [
        "How many paid annual leave days do I get?",
        "Can i work from home every day?"
    ]

    for qu in demo_ques:
        print("==" * 30)
        print("QUESTION:", qu)
        answer = ask(agent, qu)
        print("ANSWER: ", answer)
        print("- " * 30)



if __name__ == "__main__":
    main()
