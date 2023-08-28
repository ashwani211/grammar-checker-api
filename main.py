from flask import Flask, request, jsonify
from gramformer import Gramformer
import torch
import dill
import spacy.cli
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

spacy.cli.download('en')
nlp = spacy.load('en_core_web_sm')

def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)



gf = Gramformer(models = 1, use_gpu=False) # 1=corrector, 2=detector

PATH = "/content/sample_data/gf.pth"

influent_sentences = [
    "Hello, I am a goof person",
    "eat you're vegetables",
    "it's your's"
]

@app.route("/api/<sentence>")
def translate(sentence):
  corrected_sentences = gf.correct(sentence)
  toreturn = {
     "original" : sentence,
     "corrected" : list(corrected_sentences)[0],
  }
  return jsonify(toreturn)


@app.route("/")
def home():
  return jsonify("Hello World")

if __name__ == "__main__":
  app.run(debug=True)