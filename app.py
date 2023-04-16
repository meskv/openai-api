import openai
import flask

from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

# Set up the OpenAI API client
openai.api_key = config["OPENAI_API_KEY"]   # Your API KEY

# Set up the Flask app
app = flask.Flask(__name__)

# Home Route
@app.route("/")
def index():
    return flask.render_template("index.html")

#  Get Instagram Description Page
@app.route("/insta_description")
def insta_description():
    return flask.render_template("insta_description.html")

# generate description for Instagram post
@app.route("/generate_description", methods=["GET", "POST"])
def generate_description():
    # Get the user's input text
    input_text = flask.request.form.get("input_text")
    
    # Use GPT-3 to generate a description for the Instagram post
    prompt = (f"generate 2 line Quotes and 10 relevant Hashtags for an Instagram post for the following text in not more than 100 characters\n{input_text}\n\n"
    )
    
    response = openai.Completion.create(
        engine="text-davinci-002", #text-davinci-002 #gpt2-small
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
        )
    description = response["choices"][0]["text"]
    
    # Render the generated description in the HTML template
    return flask.render_template("insta_description.html", input_text=input_text, description=description)

# Get Text Summarization Page
@app.route("/summarizer")
def summarizer():
    return flask.render_template("summarizer.html")

# text summarization
@app.route("/generated_summary", methods=["GET", "POST"])
def generated_summary():
    # Get the user's input text
    input_text = flask.request.form.get("input_text")
    words_count = flask.request.form.get("words_count")
    
    # Use GPT-3 to generate a description for the Instagram post
    prompt = (f"Summarize the following text in not more than {words_count} words\n{input_text}\n\n"
    )
    
    response = openai.Completion.create(
        engine="text-davinci-003", #text-davinci-002 #gpt2-small
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=1
        )
    summary = response["choices"][0]["text"]
    
    # Render the generated description in the HTML template
    return flask.render_template("summarizer.html", input_text=input_text, summary=summary)


if __name__ == "__main__":
 app.run()
