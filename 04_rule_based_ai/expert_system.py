# Mini Expert System: Diagnosing Common Problems

def diagnose(symptom):
    rules = {
        "fever": "You may have an infection.",
        "headache": "You might be dehydrated or stressed.",
        "stomachache": "Check your diet or see a doctor.",
        "cough": "You might have a cold or flu."
    }
    return rules.get(symptom.lower(), "Cannot diagnose. Please see a doctor.")

print("Expert System: Type 'quit' to exit.")
while True:
    symptom = input("Enter symptom: ")
    if symptom.lower() == "quit":
        break
    print("Diagnosis:", diagnose(symptom))
