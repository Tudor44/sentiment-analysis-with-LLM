# 🤖 Sentiment Analysis with LLM 🤖

The project demonstrates an example of how to use a supervised learning task using GPT-3.5 with JSON export, evaluating reviews in Italian Language.

## Overview

An experimental using Langchain with OpenAI APIs for demostrating a possibility to create a supervised learning task with GPT-3.5 model,
and the capability to export the information in JSON format.

## Requirements

- Python 3.x
- Langchain
- OpenAI API

## Installation

1. Clone the repository

2. Install the required packages using venv:
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. Set up your OPENAI_API_KEY, creating an .env file into main folder
```
OPENAI_API_KEY=<your_api_secret_key>
```

4. Execute it using streamlit
```
cd src
streamlit run main.py
```

## License
This project is licensed under the MIT License.

