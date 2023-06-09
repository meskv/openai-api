
# Performing Tasks usig OpenAI 

![Home Page](https://github.com/meskv/openai-api/blob/master/screenshots/home_page.png?raw=true)

ChatGPT has been the talk of the social media world recently, and the buzz continues. The company behind ChatGPT is Open AI, a research lab dedicated to AI.

In this project I am basically using the OpenAI API endpoints of models to accomplish task which include

    * Instagram Description Generator
    * Text Summarizer

## Instagram Description Generator
Is generates description for an instagram post with relevant hastags

![Home Page](https://github.com/meskv/openai-api/blob/master/screenshots/Description_Generator_1.png?raw=true)

![Home Page](https://github.com/meskv/openai-api/blob/master/screenshots/Description_Generator.png?raw=true)


## Text Summarizer
It can generate summary of long text and summarize within the word limit given as input.

![Home Page](https://github.com/meskv/openai-api/blob/master/screenshots/Generated_Summary_1.png?raw=true)

![Home Page](https://github.com/meskv/openai-api/blob/master/screenshots/Generated_Summary.png?raw=true)


## File Structure
    - openai-api
      - static
        - style.css
      - templates
        - index.html
      - venv
      - .env
      - app.py
      - requirements.txt

## Installation

### clone this repository
```bash
git clone https://github.com/meskv/openai-api.git
```
### create virtual environment
```
python -m venv venv
```
*  Note: Include your *OPENAI_API_KEY* in .env file

### installing modules/requirements
```
pip install -r requirements.txt

```
### run flask app
```
flask run
```