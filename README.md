
This project implements a robust client-server architecture from scratch, designed to operate within a local network. A designated computer running the server program acts as the central server, while clients connect using the server's IP address. The server efficiently handles multiple clients and features a versatile large language model (LLM) running in two modes:

1. **Online Model**: Utilizes the Google Gemini API, which can be switched to other online models such as OpenAI GPT, requiring an API key.
2. **Local Model**: Hosts a local LLM using Ollama, supporting various models like Llama3, Mixtral, Gemma, etc.

Clients interact with the server through a command-line interface (CLI), sending prompts that the server processes to generate AI responses. These responses can handle a wide range of inputs, from basic English queries to complex mathematical problems and computer programs. The server can be configured to run either the online-based API script or the locally hosted LLM script before starting.

---
# Installation ⬇️

### Cloning the Repository

First, clone the repository to your local machine using the following command:

```sh
git clone https://github.com/your-username/your-repo-name.git
```

### Model setup:

#### LLM local setup:
Download [Ollama](https://github.com/MrTechyWorker/chartokenizer) and follow the instructions in the website to get the model locally.

#### API_KEY setup:

Log on to [Google_Gemini](https://ai.google.dev/gemini-api/docs/api-key) and follow instruction to get the API key.

### Installing Dependencies

You can install the required dependencies using `pip`. There are two methods to do this: using a `requirements.txt` file or installing directly with a single `pip` command.

#### Method 1:
Using ```requirements.txt```

Run the following command to install the dependencies:
```sh
pip install -r requirements.txt
```

#### Method 2: 
Direct Installation with `pip`

Run the following command to install all the required libraries directly:
```sh
pip install google-api-core google-generativeai ollama
```

This will install all the necessary packages for your project.

Make sure to update the ```server_local.py``` with the model name installed qith ollama,

```python
def response(msg):  
  messages = [
    {
      'role': 'user',
      'content': msg,
    },
  ]
  response = ollama.chat('model_name', messages=messages) # update model name here
  return response['message']['content']
```
and also update your api key here
```python
genai.configure(api_key="API-KEY")
model = genai.GenerativeModel('gemini-pro')
```
---

# Quick Start 🏁

After installing all dependencies, first run the Ollama server by
```bash
ollama run <model_name>
```
then, navigate to the directory cloned and,
```python server_local.py``` for locally hosted LLM or ```python server_online.py``` for API based LLM.

Upon running the code, the Server Port will be prompted which is as per the user wish **usually 4444** and the server ip will be displayed in the output.
  <p align="left">
    <picture>
    <img alt="logo" src="/docs/server_out.png" height="170">
    </picture>
  </p>

In the client side, both the IP and PORT will be prompted and credentials of server must be given.

> ENJOY PROMPTING 😇

---

# Key Features ✅

- **Dual LLM Modes**: Flexibly switch between using an online API-based LLM and a locally hosted LLM.

- **Multi-client Support**: Efficiently handles multiple client connections simultaneously.
- **Extensive Customization**: Provides full access to server connection settings, client handling mechanisms, IP address validation, and more.
- **Comprehensive Logging and Security**: Logs every incoming prompt along with the source IP address for enhanced security and monitoring.
- **Private Network Operations**: Restricts access to IPs within the local network, with an additional layer of IP verification for future authentication.
- **Custom AI Responses**: Allows for the integration of customized LLMs trained on user-specific datasets, supporting unique data requirements.
- **Security Measures**: Implements additional layers to prevent misuse, ensuring the AI provides appropriate responses, making it suitable for controlled environments like schools and restricted areas.
- **RAG Model Implementation**: Facilitates the creation of a Retrieval-Augmented Generation (RAG) model, where the AI accesses a custom database of files to generate responses relevant to the data.

---

# Impact of the Project 🦾

This project has significant implications across various fields and applications, particularly in enhancing security, customization, and information retrieval.

> ### Security Features

- **IP Validation**: Ensures that only authorized devices within the local network can connect to the server by implementing strict IP validation protocols.
- **Prompt and IP Logging**: Every prompt sent by the clients and their respective IP addresses are logged. This enhances security by providing an audit trail for all interactions, which can be reviewed and analyzed to prevent and investigate any misuse.
- **Preventing Jailbreaking**: The system includes security layers designed to prevent users from bypassing restrictions and attempting to jailbreak the AI, ensuring safe and intended use.

> ### Retrieval-Augmented Generation (RAG) Implementation
- **Custom Database Access**: Supports the creation of a RAG model, enabling the AI to access and retrieve information from a custom database of files. This is particularly useful in environments where specific data needs to be referenced, such as in corporate settings or specialized research fields.

> ### Age Restriction Implementation
- **Controlled Environments**: The project can be deployed in schools and other age-restricted areas where the AI must provide appropriate and safe responses. By integrating security layers and monitoring, the system prevents the dissemination of unintended or harmful information.

> ### Custom AI Models

- **User-Customized Models**: Users can host their own AI models, either fine-tuned or trained from scratch on specific datasets. This allows for highly customized AI responses tailored to the unique needs of different organizations or individuals.
- **Support for Various LLMs**: The system is compatible with a range of LLMs, both online and local, providing flexibility in choosing the right model for the application.

---

# Technologies Used 👨🏻‍💻

- **Programming Language**: Python
- **Online LLM**: Google Gemini API (or any compatible online LLM API)
- **Local LLM**: Ollama (supporting models like Llama3, Mixtral, Gemma)
- **Client Interface**: Command Line Interface (CLI)
- **Logging and Monitoring**: Built-in logging for prompt and IP tracking

---

# ‼️NOTE‼️

- Make sure **Ollama model is running** or else the code will note run stating ```Ollama not running```.
- For API based server, **ACCESS TO INTERNET IS COMPULSORY**.
- For Local AI server, **NETWORK IS REQUIED BUT NOT THE INTERNET ACCESS**. Visit this [link](https://www.psychz.net/client/question/en/what-is-a-difference-between-ip-transit-and-dedicated-internet-access.html) or more info on this point.
- ‼️For local AI hosting, system specification plays a major role‼️ The Hardware specs of machine used to run and test :
  <p align="left">
    <picture>
    <img alt="logo" src="/docs/hardware.png" height="170">
    </picture>
  </p>

---

# Contributing

We welcome contributions from the community! To contribute, please fork the repository, create a feature branch, and submit a pull request with your changes. Ensure your code adheres to the project's coding standards and includes appropriate tests.

---

# License

Released under [MIT License](/LICENSE) by [@MrTechyWorker](https://github.com/MrTechyWorker).

---

# Acknowledgments

Special thanks to the developers and researchers who created the LLM models and APIs utilized in this project. Their work has been instrumental in making this project possible.

---
> Learn, Build, Develop !! 😉
