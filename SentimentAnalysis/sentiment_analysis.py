import requests,json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header)
    f=json.loads(response.text)
    label = f['documentSentiment']['label']
    score = f['documentSentiment']['score']
    d={}
    d['label']=label
    d['score']=score
    return d