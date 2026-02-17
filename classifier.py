
from connector import alldata
import re

weakness_keywords = ["struggled", "missed", "needs", "improve", "confused", "slow", "absent", "difficult", "hard"]

strength_keywords = ["good", "very good", "impressive", "included", "correct", "Easy", "strong"]

def classify_sentence (sentence):

    parts = re.split(r"\s*(?:,|;|otherwise|but|and)\s+", sentence, flags = re.IGNORECASE) #(?:) used since text is not required separately #s+ consume after delimiter only
    parts = [p.strip() for p in parts] #remove extra spaces

    strengths = []
    weakness = []

    for part in parts:
        part_lower = part.lower() #lowercase just for checking keywords and then append original text -> no slicing erros occur - best practice
        if any (word in part_lower for word in strength_keywords): 
            strengths.append(part)
        
        if any(word in part_lower for word in weakness_keywords):
            weakness.append(part)
    
    return strengths, weakness

#Loop over your google sheets dictionary output

feedback_summary ={} # dictionary where key is student name & value will be dictionary w strengths + improvements

for row in alldata:
    name = row["StudentName"]
    subject = row["Subject"]
    module = row["Module"]
    topic = row["Topic"]
    feedback = row["RawFeedback"]


    strengths, weakness = classify_sentence(feedback) # returns two lists each


    if name not in feedback_summary:
        feedback_summary[name] = {"strengths": [], "weakness": []}

    #Save strength with context                                 #adds all items from strengths list (from classify_sentence) into student's strength's list
    for s in strengths:
        feedback_summary[name]["strengths"].append({
            "subject": subject,
            "topic": topic,
            "feedback": s
        })
    for w in feedback_summary[name]["weakness"].append({
        feedback_summary[name]["weakness"].append({
            "subject": subject,
            "topic": topic,
            "feedback": w   
        })
    }):

#Print Feedback Summary

for student, summary in feedback_summary.items():
    print(f"Student: {student}")
    print(" Strengths:")

    for s in summary["strengths"]:
        print(f"    - {s['subject']} | {s['topic']}] {s['feedback']}")
    print (" Areas to improve:")
    for w in summary["weakness"]:
        print(f"    - {w['subject']}| {w['topic']} {w{'feedback'}}")
    print()

'''def main():

    test_sentences = [
        "Good format and very strong arguements.",
        "Missed subheadings and struggled with PEEl.",
        "Missed subheadings but overall good understanding.",
        "Good format, strong argument but missed conclusion depth"
    ]

    for s in test_sentences:
        print(s, "->", classify_sentence(s))


if __name__ == "__main__":
    main()
'''




