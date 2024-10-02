from flask import Flask, render_template, request, jsonify
import base64
import vertexai
from vertexai.preview.generative_models import GenerativeModel, GenerationConfig, HarmCategory, HarmBlockThreshold
app = Flask(__name__)

# Initialize Vertex AI
vertexai.init(project="", location="")

prompt_template = """You are an AI assistant that helps people with financial advice. The answer should be descriptive.
I am of age: {age}
occupation: {occupation}
monthly income: {monthly_income}
monthly expenses: {monthly_expenses}
current saving: {current_saving}
investment goals: {investment_goals}
risk tolerance: {risk_tolerance}
item price is {item_price}
loan term: {loan_term}
What is the interest rate being offered on the loan? {interest_rate}
Do you have any other outstanding loans? {outstanding_loans}
What is your credit score? {credit_score}

Please provide me with loan advice."""

# Generation configuration
generation_config = GenerationConfig(
    max_output_tokens=2192,
    temperature=0.95,
    top_p=0.75,
)

# Safety settings
safety_settings = {
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

@app.route('/')
def index():
    return render_template('loan_advice.html')

@app.route('/get_advice', methods=['POST'])
def get_advice():
    user_data = request.form.to_dict()
    prompt = create_prompt(user_data)
    advice = generate(prompt)
    return jsonify({'advice': advice})

def create_prompt(user_data):
    return prompt_template.format(**user_data)

def generate(prompt):
    model = GenerativeModel("gemini-1.5-pro-001")
    responses = model.generate_content(
        [prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    full_response = ""
    for response in responses:
        full_response += response.text

    return full_response

if __name__ == '__main__':
    app.run(debug=True)
