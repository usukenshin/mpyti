def mbti_test():

    import matplotlib.pyplot as plt
    import random
    import time
    import webbrowser

    num_questions = int(input(" How many questions do you want to answer? ( Max. 40 / Min. 10 ) "))
    if num_questions in range(10,40):
        print("The number is within the range.")
    else:
        print("Invalid input.")

    trait_map = {
        "E": ["I prefer to be in group settings", "I enjoy meeting new people", "I am energized by social interaction", "I am comfortable being the center of attention", "I find it easy to approach strangers"],
        "I": ["I prefer to spend time alone", "I enjoy working independently", "I am drained by too much social interaction", "I am comfortable working behind the scenes", "I find it difficult to approach strangers"],
        "S": ["I am good at remembering details", "I pay attention to facts and data", "I prefer routine and predictability", "I am practical and down-to-earth", "I am not easily distracted"],
        "N": ["I am good at seeing the big picture", "I pay attention to patterns and possibilities", "I prefer variety and change", "I am open-minded and curious", "I am easily distracted"],
        "T": ["I am good at analyzing and solving problems", "I make decisions based on reason and logic", "I am not easily swayed by emotions", "I am critical and objective", "I prefer to discuss solutions in times of hardship"],
        "F": ["I am good at understanding and empathizing with others", "I make decisions based on values and feelings", "I am easily swayed by emotions", "I am supportive and empathetic", "I prefer comfort and solace in times of hardship"],
        "J": ["I like to plan and organize", "I am reliable and consistent", "I am committed to achieving my goals", "I am orderly and structured", "I am not spontaneous"],
        "P": ["I like to go with the flow", "I am adaptable and flexible", "I am open to new possibilities", "I am spontaneous and unstructured", "I am not reliable"]
            }

    questions = []

    traits = []

    for trait in trait_map:
        questions.extend(trait_map[trait])
        traits.append(trait)

    sub_questions=random.sample(questions, num_questions)

    #print(traits)
    #print(sub_questions)

    results = {
        "E": 0,
        "I": 0,
        "S": 0,
        "N": 0,
        "T": 0,
        "F": 0,
        "J": 0,
        "P": 0,
            }

    rem_questions=num_questions

    for question in sub_questions:
        for key, value in trait_map.items():
            if question in value:
                trait = key
                opposite_trait = trait == "E" and "I" or trait == "I" and "E" or trait == "S" and "N" or trait == "N" and "S" or trait == "T" and "F" or trait == "F" and "T" or trait == "J" and "P" or trait == "P" and "J"
        while rem_questions > 0:
            print(rem_questions)
            answer = input(question + " [y/=/n]? ").lower()
            if answer.lower() in ["yes", "y"]:
                results[trait] += 1
                rem_questions -= 1
                break
            elif answer.lower() in ["no", "n"]:
                results[opposite_trait] += 1
                rem_questions -= 1
                break
            elif answer.lower() in ["="]:
                results[trait] += 1
                results[opposite_trait] += 1    
                rem_questions -= 1
                break
            elif answer.lower() in ["r"]:
                eliminate_n = num_questions - rem_questions
                del sub_questions[:eliminate_n]
                rand_answers = ["y", "=", "n"]
                for question in sub_questions:
                    #print(results)
                    print(question)
                    for key, value in trait_map.items():
                        if question in value:
                            trait = key
                            opposite_trait = trait == "E" and "I" or trait == "I" and "E" or trait == "S" and "N" or trait == "N" and "S" or trait == "T" and "F" or trait == "F" and "T" or trait == "J" and "P" or trait == "P" and "J"
                            #print(trait)
                    while rem_questions > 0:
                        #time.sleep(0.5)
                        rand_answer = random.choice(rand_answers)
                        #print(rem_questions)
                        #print(rand_answer)
                        if rand_answer in ["yes", "y"]:
                            results[trait] += 1
                            rem_questions -= 1
                            print("YEEP :D")
                            break
                        elif rand_answer in ["no", "n"]:
                            results[opposite_trait] += 1
                            rem_questions -= 1
                            print("NEEP :/")
                            break
                        elif rand_answer in ["="]:
                            results[trait] += 1 
                            results[opposite_trait] += 1
                            rem_questions -= 1
                            print("BEEHP I_I")
                            break
                break
            else:
                print("Invalid answer. Please enter 'yes', 'no' or 'r'.")

    # for question in sub_questions:
    #     for key, value in trait_map.items():
    #         if question in value:
    #             trait = key
    #             opposite_trait = trait == "E" and "I" or trait == "I" and "E" or trait == "S" and "N" or trait == "N" and "S" or trait == "T" and "F" or trait == "F" and "T" or trait == "J" and "P" or trait == "P" and "J"
    #     while True:
    #         answer = input(question + " [y/=/n]? ").lower()
    #         if answer.lower() in ["yes", "y"]:
    #             results[trait] += 1
    #             break
    #         elif answer.lower() in ["no", "n"]:
    #             results[opposite_trait] += 1
    #             break
    #         elif answer.lower() in ["="]:
    #             results[trait] and results[opposite_trait] +- 1
    #             break
    #     else:
    #         print("Invalid answer. Please enter 'yes' or 'no'.")

    #print(results)

    mbti = ""
    ei_added = False
    sn_added = False
    tf_added = False
    jp_added = False

    for trait in ["E", "I", "S", "N", "T", "F", "J", "P"]:
        if trait in ["E", "I"] and not ei_added:
            if results["E"] > results["I"]:
                mbti += "E"
                ei_added = True
            elif results["E"] == results["I"]:
                mbti += "X"
                ei_added = True
            elif not ei_added:
                mbti += "I"
                ei_added = True
        if trait in ["S", "N"] and not sn_added:
            if results["S"] > results["N"]:
                mbti += "S"
                sn_added = True
            elif results["S"] == results["N"]:
                mbti += "X"
                sn_added = True
            elif not sn_added:
                mbti += "N"
                sn_added = True
        if trait in ["T", "F"] and not tf_added:
            if results["T"] > results["F"]:
                mbti += "T"
                tf_added = True
            elif results["T"] == results["F"]:
                mbti += "X"
                tf_added = True
            elif not tf_added:
                mbti += "F"
                tf_added = True
        if trait in ["J", "P"] and not jp_added:
            if results["J"] > results["P"]:
                mbti += "J"
                jp_added = True
            elif results["J"] == results["P"]:
                mbti += "X"
                jp_added = True
            elif not jp_added:
                mbti += "P"
                jp_added = True

    print("Your MBTI type is:", mbti)

    percentages = [
        results["E"]/(results["E"]+results["I"])*100,
        results["I"]/(results["E"]+results["I"])*100,
        results["S"]/(results["S"]+results["N"])*100,
        results["N"]/(results["S"]+results["N"])*100, 
        results["T"]/(results["T"]+results["F"])*100,
        results["F"]/(results["T"]+results["F"])*100, 
        results["J"]/(results["J"]+results["P"])*100,
        results["P"]/(results["J"]+results["P"])*100
        ]

    #print(percentages)

    trait_perc = dict(zip(traits, percentages))

    #for key, value in trait_perc.values():
            #key = value

    for key, value in trait_perc.items():
        globals()[key] = value

    print(trait_perc)

    dichotomies_a = ["E/I", "S/N", "T/F", "J/P"]

    dichotomies = [(E, I), (S, N), (T, F), (J, P)]

    # Create a bar chart    
    fig, ax = plt.subplots()
    x = range(len(dichotomies))
    ax.bar(x, [d[0] for d in dichotomies], label='First variable')
    ax.bar(x, [d[1] for d in dichotomies], label='Second variable', bottom=[d[0] for d in dichotomies])

    # Add labels and legend
    ax.set_ylabel('Percentage')
    ax.set_xticks(x)
    ax.set_xticklabels(['E/I', 'S/N', 'T/F', 'J/P'])
    ax.legend()

    # Show the chart
    plt.show()

    # fig, ax = plt.subplots()
    # ax.bar(traits, percentages)
    # ax.set_title("MBTI Spectrum")
    # ax.set_xlabel("Traits")
    # ax.set_ylabel("Percentage")

    # plt.bar(traits, percentages)
    # plt.xlabel("Trait")
    # plt.ylabel("Percentage")
    # plt.title("MBTI Trait Percentage")

    link = "https://www.truity.com/personality-type/" + mbti
    webbrowser.open(link)

mbti_test()
