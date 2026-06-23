# Task 2: FAQ Chatbot
# CodeAlpha AI Internship - June 2026

print("=== CodeAlpha FAQ Bot ===")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()
    
    if user == "bye":
        print("Bot: Goodbye! All the best for internship")
        break
    elif "internship" in user:
        print("Bot: CodeAlpha AI Internship duration is 1 month")
    elif "certificate" in user:
        print("Bot: Yes, you get certificate after completing 3 tasks")
    elif "task" in user:
        print("Bot: Complete 3 tasks and submit GitHub repo link")
    elif "hello" in user or "hi" in user:
        print("Bot: Hello! Ask me about CodeAlpha internship")
    else:
        print("Bot: Sorry, I can answer about internship, tasks, certificate")