from key import *
import glob
import openai
from gpt import GPT
from gpt import Example


openai.api_key = key
gpt = GPT(engine="davinci",
          temperature=0.5,
          output_prefix="Output: \n\n",
          max_tokens=500)

# add some code examples
for file in glob.glob("examples/*"):
    title = file.replace("_", " ")
    with open(f"{file}", "r") as f:
        code = f.read()
    gpt.add_example(Example(title, code))


# add some report examples
gpt.add_example(Example("Write a report for A addressing the outcomes: trigonometry, financial maths. The student has been outstanding, committed, thorough", 
                        """A has achieved outstanding results this semester, demonstrating in depth knowledge of the course content. 
                        He has developed the capacity to evaluate his learning and manages his time effectively to ensure he is up to date with the concepts taught. 
                        A has demonstrated a thorough understanding of Trigonometry and financial mathematics. He is commended for his clear setting out in all topics which accurately conveys his thoughts. 
                        A must continue to review his work regularly in order to maintain his excellent results."""))
gpt.add_example(Example("Write a report for Daniel addressing the outcomes: trigonometry, financial maths. The student has been eager, curious, slightly careless", 
                        """Daniel has taken the initiative to ensure he understands the concepts taught in class and works cooperatively with his peers to achieve this. 
                        He consistently seeks thorough understanding of new content learnt and can apply new concepts in a variety of situations. 
                        Daniel has demonstrated a thorough understanding of Networks which was evident from his assignment. 
                        Attempting higher order problems related to the topics studied should equip Daniel with the ability to successfully answer difficult examination style questions. 
                        He should read the questions carefully, highlighting keywords to minimise misinterpretations. A continued positive approach is encouraged to improve these results further."""))
gpt.add_example(Example("Write a report for Zachary addressing the outcomes: trigonometry, financial maths. The student has been basic, unprepared, careless", 
                        """Zachary has demonstrated the capacity and knowledge to apply a variety of concepts to solve problems of varying difficulties. 
                        He is a capable student whose examination showed a lack of preparation and a need for him to extend his home study program before assessments as not all topics were revised fully. 
                        Zachary has demonstrated a basic understanding of Trigonometry. He needs to ensure that he carefully answers all questions, concentrating on the steps he writes in order to avoid errors. 
                        Zachary must use class time effectively and reinforce his concepts through regular revision and practice."""))
# Inferences
# prompt = "sort list in python"
# output = gpt.get_top_reply(prompt)
# print(prompt, ":", output)
# print("----------------------------------------")

# prompt = "Code weather api in python"
# output = gpt.get_top_reply(prompt)
# print(prompt, ":", output)
# print("----------------------------------------")

name = input("Welcome to the report maker!\nWhat is the students name? ")

outcome = input("Please list the outcomes that you would like the report to address: ")

mood = input("Please tell us how the student performed this term ")

prompt = f"Write a report for {name} addressing the outcomes: {outcome}. The student has been {mood} "
output = gpt.get_top_reply(prompt)
print(prompt, ":", output)
print("----------------------------------------")
