# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model, BaseModel, Field


# 定义输入模型
class InsurancePredictionModelInput(BaseModel):
    age: int = Field(default=18, ge=0, le=120)  # 年龄，使用证书，限制在0到120之间
    sex: str = Field(default='female', regrex="^(male|female)$")  # 性别，只接受 nale 或 female
    bmi: float = Field(default=21.66)  # 体质指数，使用浮点数，默认值为21.66
    children: int = Field(default=0, ge=0)  # 子女数量，使用整数，不小于0
    smoker: str = Field(default='yes', regrex="^(yes|no)$")  # 吸烟者，只接受 yes 或 no
    region: str = Field(default='northeast')  # 区域


class InsurancePredictionModelOutput(BaseModel):
    prediction: float  # 预测值，使用浮点数


# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("insurance_prediction_model")

# # Create input/output pydantic models
# input_model = create_model("insurance_prediction_model_input", **{'age': 18, 'sex': 'female', 'bmi': 21.65999984741211, 'children': 0, 'smoker': 'yes', 'region': 'northeast'})
# output_model = create_model("insurance_prediction_model_output", prediction=14283.459)

# 使用新定义的模型类替换原有的动态创建方式
input_model = InsurancePredictionModelInput
output_model = InsurancePredictionModelOutput


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
