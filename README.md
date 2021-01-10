# financial-news-data-sentiment-analyzer

This repo contains and EDA for financial data collected through [Webhose API](https://docs.webhose.io/), and Sentiment Analysis & Topic Modeling applied on this data.
Also an API for the sentiment analysis model.

You can view the notebook on Google Colab from here:
    https://colab.research.google.com/drive/1fB4lQUMc2nCrW30Ymiczr4QhZanOlC-6?usp=sharing

_It is better to view the notebook on Colab to get better experience and metigate the graphs not showing issue._


A walkthrough video for the notebook:
    https://www.loom.com/share/23c5bf01a49e40b1b3301fe5760ca8d0


## Install
_The following commands for running on your local machine._

#### Python Version
```
python-3.8.5
```

##### Note:
This project should be executed in a "Virtual Environment" with python
 version mentioned above

#### Install Requirements
```sh
pip install -r requirements.txt
```

### Add environment variables
Before running anything, make sure you added environment variables in `.env
` file, as shown in `.env-example` file.


## Run

Run using docker-compose:
```
docker-compose up -d
```

Alternatively, run this command to start the application
```
uvicorn api:app --host 0.0.0.0 --port 8081
``` 

## API Documentation
To view the API docs and try the endpoints, browse this url:
http://localhost:8081/docs

