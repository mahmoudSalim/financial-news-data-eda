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


## Start the Tensorflow server

Make sure you installed [Sensorflow Serving](https://www.tensorflow.org/tfx/guide/serving) depencies first, if not run the following commands:

```
echo "deb http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | sudo tee /etc/apt/sources.list.d/tensorflow-serving.list && \
curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | sudo apt-key add -
```

```
sudo apt update
```
```
sudo apt-get install tensorflow-model-server
```

### Start the server

```
nohup tensorflow_model_server --rest_api_port=8501  --model_name=sentiment --model_base_path="/Full/Path/for/thr/Model" >server.log 2>&1
```

_change the `/Full/Path/for/thr/Model` with the actual model directory._


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

