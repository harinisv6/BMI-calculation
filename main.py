from fastapi import FastAPI

app = FastAPI()


@app.post("/bmi")
def bmi(weight: int, height: int):
    height_m = height / 100  # convert cm to meters
    bmi_value = weight / (height_m ** 2)

    if bmi_value < 18.5:
        category = "Underweight"
    elif bmi_value < 25:
        category = "Normal weight"
    elif bmi_value < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return {"BMI": round(bmi_value, 2), "Category": category}
