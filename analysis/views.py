import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .forms import ExcelFileForm, FileUploadForm
from .models import ExcelFile
import os

# Home Page
def home(request):
    return render(request, 'analysiser/home.html')

# Upload File Functionality
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            file_path = os.path.join(settings.MEDIA_ROOT, str(file.file))

            try:
                # Process Excel File
                data = pd.read_excel(file_path)

                # Check for required columns
                required_columns = ['product name', 'quantity', 'profit']
                if not all(col in data.columns for col in required_columns):
                    return render(request, 'analysiser/error.html', {
                        'message': f"Uploaded file must contain columns: {', '.join(required_columns)}"
                    })

                # Convert data to HTML table
                table_html = data[['product name', 'quantity', 'profit']].to_html(index=False, classes='table table-bordered')

                # Find the product with the highest profit
                max_profit_row = data.loc[data['profit'].idxmax()]
                max_profit_product = max_profit_row['product name']
                max_profit_value = max_profit_row['profit']
                max_profit_quantity = max_profit_row['quantity']

                # Generate a graph for the product with the highest profit
                plt.figure(figsize=(8, 5))
                plt.bar(['Profit', 'Quantity'], [max_profit_value, max_profit_quantity], color=['green', 'blue'])
                plt.title(f"Profit and Quantity for {max_profit_product}")
                plt.ylabel("Value")
                graph_path = os.path.join(settings.MEDIA_ROOT, 'graph.png')
                plt.savefig(graph_path)
                plt.close()

                return render(request, 'analysiser/result.html', {
                    'table_html': table_html,
                    'max_profit_product': max_profit_product,
                    'max_profit_value': max_profit_value,
                    'graph_path': f'{settings.MEDIA_URL}graph.png'
                })

            except Exception as e:
                return render(request, 'analysiser/upload.html', {
                    'form': form,
                    'error': f"Error processing file: {str(e)}"
                })

    else:
        form = FileUploadForm()

    return render(request, 'analysiser/upload.html', {'form': form})

# Result Page View
def result(request, file_id):
    excel_file = get_object_or_404(ExcelFile, id=file_id)

    try:
        # Load the data from the uploaded Excel file
        df = pd.read_excel(excel_file.file.path)
        excel_file.file.close()  # Ensure the file is released after reading

        # Ensure the required columns exist
        required_columns = ['Product Name', 'Quantity', 'Profit']
        if not all(col in df.columns for col in required_columns):
            return render(request, 'analysiser/error.html', {
                'message': f"Uploaded file must contain columns: {', '.join(required_columns)}"
            })

        # Convert data to HTML table
        table_html = df[['product name', 'quantity', 'profit']].to_html(index=False, classes='table table-bordered')

        # Find the product with the highest profit
        max_profit_row = df.loc[df['Profit'].idxmax()]
        max_profit_product = max_profit_row['Product Name']
        max_profit_value = max_profit_row['Profit']
        max_profit_quantity = max_profit_row['Quantity']

        # Generate a graph for the product with the highest profit
        plt.figure(figsize=(8, 5))
        plt.bar(['Profit', 'Quantity'], [max_profit_value, max_profit_quantity], color=['green', 'blue'])
        plt.title(f"Profit and Quantity for {max_profit_product}")
        plt.ylabel("Value")
        graph_path = os.path.join(settings.MEDIA_ROOT, f'graph_{file_id}.png')
        plt.savefig(graph_path)
        plt.close()

        return render(request, 'analysiser/result.html', {
            'table_html': table_html,
            'max_profit_product': max_profit_product,
            'max_profit_value': max_profit_value,
            'graph_path': f'{settings.MEDIA_URL}graph_{file_id}.png'
        })

    except Exception as e:
        return render(request, 'analysiser/error.html', {'message': f"Error processing file: {str(e)}"})
