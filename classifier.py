from connector import alldata
import re

'''
classify_sentence -> Transform, divides
Load -> feedbackSummary
FeedbackReport -> Final report



'''

weakness_keywords = ["struggled", "missed", "needs", "improve", "confused", "slow", "absent", "difficult", "hard"]

strength_keywords = ["good", "very good", "impressive", "included", "correct", "easy", "strong"]

#classify_sentence and feedback reporter kept separate to allow future scalability.
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

#-- 3. Reporting Class --#

class FeedbackReport():
    def __init__(self,summary_data):
        self.summary_data = summary_data;

    def _format_text(self,text):
        '''Internal helper to lowercase the first letter safely'''
        return text[0].lower() + text[1:] if text else text
    
    def display(self):
        '''prints the final organised report'''

        for student, summary in self.summary_data.items():
            print(f"Student: {student}")

            print(" Strengths:")

            for s in summary["strengths"]:
                clean_f = self._format_text(s['feedback'])
                print(f"    - {s['subject']} | In {s['topic']}, {clean_f}")
            
            print (" Areas to improve:")
            
            for w in summary["weakness"]:
                clean_f = self._format_text(w['feedback'])
                print(f"    - {w['subject']} | In {w['topic']}, {clean_f}")
            print(f"Best,\n{summary['tutor']}")
            print("-" * 30)

        
def main():
#Loop over your google sheets dictionary output

    feedback_summary ={} # dictionary where key is student name & value will be dictionary w strengths + improvements

    #process 
    for row in alldata:
        # EVERYTHING BELOW IS NOW INSIDE THE LOOP
        studentName = row["StudentName"]
        subject = row["Subject"]
        topic = row["Topic"]
        feedback = row["RawFeedback"]
        tutorName = row['Tutor']


        strengths, weakness = classify_sentence(feedback) # returns two lists each


        if studentName not in feedback_summary:
            feedback_summary[studentName] = {"strengths": [], "weakness": [], "tutor": tutorName}

        #Save strength with context  #adds all items from strengths list (from classify_sentence) into student's strength's list
        for s in strengths:
            feedback_summary[studentName]["strengths"].append({
                "subject": subject,
                "topic": topic,
                "feedback": s
            })
        for w in weakness:
            feedback_summary[studentName]["weakness"].append({
                "subject": subject,
                "topic": topic,
                "feedback": w  
            })
    #Call reporter
    reporter = FeedbackReport(feedback_summary)
    reporter.display()

if __name__ == "__main__":
    main()
