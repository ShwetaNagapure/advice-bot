#  Advice Bot Using Vertex AI
This is a Flask-based web application that provides personalized financial advice. The application uses Google's Vertex AI to generate advice based on user input, such as age, occupation, income, expenses, and loan details.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Application Structure](#application-structure)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [License](#license)

## Installation

### Prerequisites

- Python 3.7 or later
- Flask
- Vertex AI Python SDK

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/financial-advice-bot.git
    cd financial-advice-bot
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up Vertex AI:

   Ensure that your Google Cloud project is correctly set up and has access to Vertex AI. You must also authenticate using Google Cloud SDK or a service account with the necessary permissions.

4. Initialize Vertex AI in your code:
    ```python
    import vertexai
    vertexai.init(project="your-project-id", location="us-central1")
    ```

5. Run the Flask application:
    ```bash
    python app.py
    ```

6. Open your browser and navigate to `http://127.0.0.1:5000` to access the application.

## Configuration

- **Vertex AI Initialization**: 
  Ensure you replace `"your-project-id"` with your Google Cloud project ID in the `vertexai.init()` method.

- **Generation Configuration**: 
  The `GenerationConfig` object allows customization of the AI's response, such as the maximum output tokens, temperature, and top_p. Adjust these settings based on your needs.

- **Safety Settings**: 
  The `safety_settings` dictionary blocks specific categories of harmful content. Modify these thresholds if necessary.

## Usage

1. Open the web application in your browser.
2. Fill out the form with the required financial information, including age, occupation, income, expenses, etc.
3. Submit the form to receive personalized financial advice based on your inputs.

## Application Structure

- **app.py**: The main Flask application that handles routing and integrates with Vertex AI.
- **templates/loan_advice.html**: The HTML template for the input form.
- **static/**: Directory for static files such as CSS and JavaScript.

## API Endpoints

- **`/`**: The home page displaying the loan advice form.
- **`/get_advice`**: A POST endpoint that receives user data, generates a prompt, and returns financial advice as JSON.

## Technologies Used

- **Flask**: A lightweight web framework for Python.
- **Vertex AI**: Google's AI platform for training and deploying machine learning models.
- **HTML/CSS**: For the frontend user interface.
- **JavaScript**: For client-side interactions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
