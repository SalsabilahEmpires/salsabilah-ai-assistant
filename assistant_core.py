# ==========================================================
# OWNER: MD. AL AMIN SOHAG
# ENTITY: Salsabilah Amin Empires Ltd.
# RESEARCH: The SOHAG Filter & The Digit Theory
# STATUS: READY FOR MANUAL EXECUTION
# ==========================================================

import google.generativeai as genai
from datetime import datetime

# রানটাইমে এনভায়রনমেন্ট থেকে এপিআই কী নেওয়া হবে
# আপনি চাইলে সরাসরি কী এখানেও বসাতে পারেন
api_key = "" 
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')

class SalsabilahAssistant:
    def __init__(self):
        self.owner = "MD. AL AMIN SOHAG"
        self.identity = "Global Strategic Researcher & Founder of Salsabilah Amin Empires"
        self.research = ["The SOHAG Filter", "The Digit Theory", "19-Nation Grid Resilience"]
        self.credentials = "55+ International Certifications from Google, IBM, Cisco, and Microsoft"

    def get_auto_bio(self):
        """আপনার প্রোফাইলের জন্য একটি শক্তিশালী বায়ো জেনারেট করবে"""
        prompt = f"Write a world-class professional bio for {self.owner}, {self.identity}. Mention his research: {', '.join(self.research)} and his {self.credentials}."
        response = model.generate_content(prompt)
        return response.text

    def display_status(self):
        print("-" * 50)
        print(f"Salsabilah AI Core - Active for {self.owner}")
        print(f"Status: Monitoring Research Archives")
        print(f"Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)

if __name__ == "__main__":
    assistant = SalsabilahAssistant()
    assistant.display_status()
    
    # একটি স্যাম্পল বায়ো প্রিন্ট করে দেখাচ্ছি আপনার কাজের জন্য
    print("\n[AI Generated Profile Insight]:")
    print(assistant.get_auto_bio())
