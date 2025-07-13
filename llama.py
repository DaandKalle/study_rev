from huggingface_hub import InferenceClient



client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",  # The official LLaMA 3 model
    token=HF_API_KEY
)
from typing import List
import re

def gen_ques(notes: str, quiz_type: str) -> List[str]:
    prompt = f"Create 3 {quiz_type} quiz questions based only on the following notes:\n\n{notes}\n\nJust return the 3 questions. No explanations, no answers."

    response = client.chat_completion(
        messages=[
            {"role": "system", "content": "You generate only questions from study notes."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=512,
        temperature=0.7
    )

    raw_output = response.choices[0].message["content"]
    
    # Clean the output: remove explanations or anything after the question
    lines = raw_output.strip().split("\n")
    questions = [re.sub(r"^\d+[\).\s]*", "", line).strip() for line in lines if "?" in line]

    return questions[:3]  # Return only first 3 questions

from typing import Dict, Any
import re

def eval_ans(question: str, answer: str) -> Dict[str, Any]:
    prompt = f"""You are an evaluator. Score the student's answer from 0 to 10 and provide concise feedback.

Question: {question}
Answer: {answer}

Respond in the format:
Score: <number>/10
Feedback: <short feedback and tips to improve>"""

    response = client.chat_completion(
        messages=[
            {"role": "system", "content": "You are a strict but fair evaluator."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=256,
        temperature=0.7
    )

    output = response.choices[0].message["content"]

    # Parse score and feedback
    score_match = re.search(r"Score:\s*(\d+)/10", output)
    feedback_match = re.search(r"Feedback:\s*(.*)", output, re.DOTALL)

    score = int(score_match.group(1)) if score_match else None
    feedback = feedback_match.group(1).strip() if feedback_match else output.strip()

    return {
        "score": score,
        "feedback": feedback
    }
notes = """
Photosynthesis is the process by which green plants use sunlight to make food from carbon dioxide and water.
It involves the green pigment chlorophyll and generates oxygen as a by-product.
"""

questions = gen_ques(notes, "short answer")
print("Questions:", questions)

result = eval_ans(questions[0], "It makes oxygen using sunlight.")
print("Result:", result)

