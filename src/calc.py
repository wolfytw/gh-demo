"""範例 B 用的小程式：BMI 計算。現場示範時把 bmi() 改壞，看 9 個測試一起變紅。"""


def bmi(weight_kg: float, height_cm: float) -> float:
    if height_cm <= 0:
        raise ValueError("身高必須大於 0")
    h = height_cm / 100
    return round(weight_kg / (h * h), 1)


def level(value: float) -> str:
    if value < 18.5:
        return "過輕"
    if value < 24:
        return "正常"
    if value < 27:
        return "過重"
    return "肥胖"
