import connector

#accept rawFeedback from connector py
#Gemini parses over it  and provides key strengths, improvement areas and recommendations 1-2 lines




def classify_sentence (sentence)
    sentence_lower = sentence.lower()

    #checks for existence
    has_strength = any(word in sentence_lower for word in strength_keywords)
    has_improve = any(word in sentence_lower for word in improve_keywords)

    if has_strength and not has_improve :
        return "strength" # still sees the line as only strength when the line can have multiple keywords
    
    if not has_strength and has_improve:
        return "improvements"
    
    else:
        return "neutral" 
    

#Step 3 is setting up line splitting
 '''
    1. Split sentences by commas or 'but'
    2. Classify each fragment separately
    3. Store strengths separately from improvements
 
 '''


Version #1:

import re

improve_keywords = ["struggled", "missed", "needs", "improve", "confused", "slow", "absent", "difficult", "hard"]

strength_keywords = ["good", "very good", "impressive", "followed", "included", "correct", "Easy"]

def classify_sentence (sentence):
    sentence_lower = sentence.lower()

    import re
    parts = re.split(r", | but | and", sentence_lower).strip()

    #sentence contains strength word -> returns label as strength
    for word in strength_keywords:
        if word in sentence_lower:
            return "strength"
    
    #sentence contains weakness word -> returns label as improvement
    for word in improve_keywords:
        if word in sentence_lower:
            return "weakness"
    
    return "neutral"
    
'''
Good format and very strong arguements. -> strength
Missed subheadings and struggled with PEEl. -> weakness
Missed subheadings but overall good understanding. -> strength
Good format, strong argument but missed conclusion depth -> strength

'''
'''

Version #2
1. Split by , , but, and
2. Put them all inside a dictionary
3. Classify each part 
4. Append to either - strenght list or weakness list

'''