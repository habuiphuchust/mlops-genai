from django.shortcuts import render
from .forms import ExpenseForm
from .utils import predict_expenses

def predict_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # Lấy dữ liệu từ form
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            bmi = form.cleaned_data['bmi']
            children = form.cleaned_data['children']
            smoker = form.cleaned_data['smoker']

            # Dự đoán chi phí y tế
            predicted_expense = predict_expenses(age, sex, bmi, children, smoker)

            # Trả kết quả về template
            return render(request, 'predictor/result.html', {'predicted_expense': predicted_expense})

    else:
        form = ExpenseForm()

    return render(request, 'predictor/form.html', {'form': form})
