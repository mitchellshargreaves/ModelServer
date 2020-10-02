# DIPSModelServer

A docker image for a fastapi web server to run a pytorch model based on [this image](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) by tiangolo.

The app is stored in the `app` folder.

`app/torchmodels/models.py` Stores the models to run
`app/torchmodels/evaluator.py` Evaluator class to run the models
`app/main.py` Main app - defines the endpoints


### Usage

**GET /**
Root call
{
  "status": "ready"
}

**GET /docs**
Generated swagger documentation

**GET /predict?input="ModelInput"**
Run input through model
{
  "prediction": value
}