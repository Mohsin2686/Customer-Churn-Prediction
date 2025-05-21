
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from uvicorn import run as app_run

from typing import Optional

from customer_churn_prediction.constants import APP_HOST, APP_PORT
from customer_churn_prediction.pipline.prediction_pipeline import ChurnData, ChurnClassifier
from customer_churn_prediction.pipline.training_pipeline import TrainPipeline

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='templates')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.gender: Optional[str] = None
        self.SeniorCitizen: Optional[str] = None
        self.Partner: Optional[str] = None
        self.Dependents: Optional[str] = None
        self.tenure: Optional[str] = None
        self.InternetService: Optional[str] = None
        self.OnlineSecurity: Optional[str] = None
        self.OnlineBackup: Optional[str] = None
        self.DeviceProtection: Optional[str] = None
        self.TechSupport: Optional[str] = None
        self.StreamingTV: Optional[str] = None
        self.StreamingMovies: Optional[str] = None
        self.Contract: Optional[str] = None
        self.PaperlessBilling: Optional[str] = None
        self.PaymentMethod: Optional[str] = None
        self.MonthlyCharges: Optional[str] = None
        self.TotalCharges: Optional[str] = None


    async def get_churn_data(self):
        form = await self.request.form()
        self.gender = form.get("gender")
        self.SeniorCitizen = form.get("SeniorCitizen")
        self.Partner = form.get("Partner")
        self.Dependents = form.get("Dependents")
        self.tenure = form.get("tenure")
        self.InternetService = form.get("InternetService")
        self.OnlineSecurity = form.get("OnlineSecurity")
        self.OnlineBackup = form.get("OnlineBackup")
        self.DeviceProtection = form.get("DeviceProtection")
        self.TechSupport = form.get("TechSupport")
        self.StreamingTV = form.get("StreamingTV")
        self.StreamingMovies = form.get("StreamingMovies")
        self.Contract = form.get("Contract")
        self.PaperlessBilling = form.get("PaperlessBilling")
        self.PaymentMethod = form.get("PaymentMethod")
        self.MonthlyCharges = form.get("MonthlyCharges")
        self.TotalCharges = form.get("TotalCharges")
        

@app.get("/", tags=["authentication"])
async def index(request: Request):

    return templates.TemplateResponse(
            "customerchurn.html",{"request": request, "context": "Rendering"})


@app.get("/train")
async def trainRouteClient():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/predict")
async def predictRouteClient(request: Request):
    try:
        form = DataForm(request)
        await form.get_churn_data()
        
        churn_data = ChurnData(
                                gender= form.gender,
                                SeniorCitizen= form.SeniorCitizen,
                                Partner= form.Partner,
                                Dependents= form.Dependents,
                                tenure= form.tenure,
                                InternetService= form.InternetService,
                                OnlineSecurity= form.OnlineSecurity,
                                OnlineBackup= form.OnlineBackup,
                                DeviceProtection= form.DeviceProtection,
                                TechSupport= form.TechSupport,
                                StreamingTV= form.StreamingTV,
                                StreamingMovies= form.StreamingMovies,
                                Contract= form.Contract,
                                PaperlessBilling= form.PaperlessBilling,
                                PaymentMethod= form.PaymentMethod,
                                MonthlyCharges= form.MonthlyCharges,
                                TotalCharges= form.TotalCharges,
                                )
        
        churn_df = churn_data.get_churn_input_data_frame()

        model_predictor = ChurnClassifier()

        value = model_predictor.predict(dataframe=churn_df)[0]

        status = None
        if value == 1:
            status = "Customer Likely to Churn"
        else:
            status = "Customer Not Likely to Churn"

        return templates.TemplateResponse(
            "customerchurn.html",
            {"request": request, "context": status},
        )
        
    except Exception as e:
        return {"status": False, "error": f"{e}"}


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)