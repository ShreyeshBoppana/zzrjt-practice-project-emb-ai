from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    return "Bye"

@app.route("/")
def render_index_page():
    return "Hi"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
