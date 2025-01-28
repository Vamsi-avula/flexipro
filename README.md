# Flexipro

Flexipro is a powerful and flexible application designed to leverage **OpenAI's API** for performing advanced natural language processing tasks. It uses **LangChain** for building language models and provides a modular and extensible solution for integrating AI capabilities into various workflows.

## Features

- **OpenAI Integration**: Seamless integration with OpenAI's language models using the API key.
- **LangChain Framework**: Utilizes LangChain to enable efficient and scalable workflows.
- **Dynamic Inputs**: Allows users to input data and interact dynamically.
- **Extensibility**: Easily extend the functionality to support additional use cases.
- **Streamlit Deployment**: Deployed on Streamlit Cloud for easy accessibility.

## Prerequisites

Before you can run this project, ensure you have the following installed:

- **Python 3.8 or later**
- **Streamlit**
- **OpenAI Python SDK**
- **LangChain**

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Vamsi-avula/flexipro.git
   cd flexipro
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API key for OpenAI:
   - Create a folder named `.streamlit` at the root of your project.
   - Add a `secrets.toml` file with the following content:

     ```toml
     [openai]
     api_key = "your-openai-api-key-here"
     ```

## Usage

To run the application locally:

1. Start the Streamlit server:

   ```bash
   streamlit run flexipro.py
   ```

2. Open the URL displayed in the terminal (e.g., `http://localhost:8501`) in your browser.

## Deployment on Streamlit Cloud

1. Push your project to GitHub.
2. Add a `secrets.toml` file on Streamlit Cloud:
   - Go to your app's settings on Streamlit Cloud.
   - Add your OpenAI API key in the **Secrets** section:
     ```json
     {
       "openai": {
         "api_key": "your-openai-api-key-here"
       }
     }
     ```
3. Deploy your app directly using the Streamlit Cloud interface.

## Directory Structure

```
flexipro/
├── flexipro.py           # Main application file
├── requirements.txt      # Dependencies
├── .streamlit/
│   └── secrets.toml      # Contains API key (not included in version control)
├── README.md             # Documentation
```

## Troubleshooting

- **KeyError: 'st.secrets has no key "openai"'**:
  - Ensure the `secrets.toml` file is correctly formatted and in the `.streamlit` folder.
  - If deploying on Streamlit Cloud, make sure the secrets are set in the app settings.

- **API Key Error**:
  - Verify your OpenAI API key is valid and has sufficient usage limits.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.
