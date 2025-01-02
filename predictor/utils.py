import joblib
import numpy as np

# Tải mô hình và scaler, encoder đã huấn luyện
model = joblib.load('predictor/model.pkl')
poly_features = joblib.load('predictor/poly_features.pkl')
scaler_age = joblib.load('predictor/scaler_age.pkl')
scaler_bmi = joblib.load('predictor/scaler_bmi.pkl')
scaler_children = joblib.load('predictor/scaler_children.pkl')
label_encoder_sex = joblib.load('predictor/label_encoder_sex.pkl')
label_encoder_smoker = joblib.load('predictor/label_encoder_smoker.pkl')


def predict_expenses(age, sex, bmi, children, smoker):
    # Chuyển đổi giá trị đầu vào theo các scaler và encoder
    age_scaled = scaler_age.transform(np.array([[float(age)]]))[0, 0]
    bmi_scaled = scaler_bmi.transform(np.array([[float(bmi)]]))[0, 0]
    children_scaled = scaler_children.transform(np.array([[float(children)]]))[0, 0]
    sex_encoded = label_encoder_sex.transform([sex])[0]
    smoker_encoded = label_encoder_smoker.transform([smoker])[0]

    # Tạo mảng đầu vào sau khi xử lý
    input_data = np.array([[age_scaled, sex_encoded, bmi_scaled, children_scaled, smoker_encoded]])
    input_poly = poly_features.transform(input_data)

    # Dự đoán
    predicted_expense = model.predict(input_poly)
    return predicted_expense[0]