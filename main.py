# pip install -U git+https://github.com/PrithivirajDamodaran/Gramformer.git
# pip install dill
# pip install spacy
# pip install flask
# pip install torch

from flask import Flask, request, jsonify
from gramformer import Gramformer
import torch
import dill
import spacy.cli

app = Flask(__name__)

spacy.cli.download('en')
spacy.load('en_core_web_sm')

def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)



gf = Gramformer(models = 1, use_gpu=False) # 1=corrector, 2=detector

PATH = "/content/sample_data/gf.pth"

# save file
with open(PATH, 'wb') as f:
    dill.dump(gf, f)

# open file
with open(PATH, 'rb') as f:
    gf_inference = dill.load(f)

influent_sentences = [
    "Hello, I am a goof person",
    "eat you're vegetables",
    "it's your's"
]

for influent_sentence in influent_sentences:
    corrected_sentences = gf_inference.correct(influent_sentence)
    print("[Input] ", influent_sentence)
    for corrected_sentence in corrected_sentences:
      print("[Correction] ",corrected_sentence)
    print("-" *100)

# @app.route("/api/{sentence}")
# def translate(sentence):
#   corrected_sentences = gf_inference.correct(sentence)
#   toreturn = {
#      "original" : sentence,
#   }
#   return jsonify()









# # -----------------------------------------
# from flask import Flask, request, jsonify

# app = Flask(__name__)

@app.route("/")
def home():
  return jsonify("Hello World")

# @app.route("/translate/<data>")
# def translate(data):
#   return jsonify("translatedString"+data)

if __name__ == "__main__":
  app.run(debug=True)