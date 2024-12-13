# Market Analysis Application

## Overview

The **Market Analysis Application** is a Django-based web application designed to analyze market data from uploaded Excel files. The application processes the data, identifies key insights, and displays them in a user-friendly interface, including tables and graphs.

---

## Features

1. **Home Page:**

   - Provides an overview and navigation to the upload functionality.

2. **File Upload:**

   - Accepts Excel files containing market data.
   - Validates the presence of required columns: `product name`, `quantity`, and `profit`.

3. **Data Display:**

   - Displays the uploaded data in a well-formatted HTML table.

4. **Insights and Visualization:**

   - Identifies the product with the highest profit.
   - Generates a bar chart visualizing the profit and quantity of the most profitable product.

5. **Error Handling:**

   - Provides meaningful error messages for missing columns or invalid file formats.

---

## Technologies Used

- **Backend:** Django Framework
- **Frontend:** HTML, CSS, Bootstrap 5, JavaScript
- **Data Processing:** Pandas
- **Visualization:** Matplotlib

---

## Prerequisites

1. Python (version 3.8 or higher)
2. Django (version 4.x)
3. Required Python libraries:
   - Pandas
   - Matplotlib

---

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/market_analysis.git
   ```

2. Navigate to the project directory:

   ```bash
   cd market_analysis
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## How to Use

### Uploading Data

1. Navigate to the upload page.
2. Select an Excel file with the required columns (`product name`, `quantity`, `profit`).
3. Click **Upload**.

### Viewing Results

1. View the uploaded data in an HTML table.
2. Check the identified product with the highest profit.
3. Analyze the bar graph visualizing the profit and quantity of the most profitable product.
4. Use the "Back to Home" button to return to the home page.

---

## Key Functionalities in Code

1. **File Upload Handling** (`views.py`):

   - Saves the uploaded file and processes it using Pandas.
   - Validates column presence.

2. **Data Analysis**:

   - Identifies the product with the highest profit using Pandas.
   - Generates visualizations with Matplotlib.

3. **Dynamic Template Rendering**:

   - Utilizes Django template tags to dynamically render data and graphs.

---

## Example

### Input

A sample Excel file with the following columns:

```
| product name | quantity | profit |
|--------------|----------|--------|
| Product A    | 50       | 200    |
| Product B    | 30       | 300    |
| Product C    | 70       | 250    |
```

### Output

- **HTML Table:** Displays the above data.
- **Insights:** Identifies "Product B" as the most profitable product.
- **Graph:** Displays a bar chart comparing the profit and quantity of "Product B".

---

## Troubleshooting

- **Error:** "Uploaded file must contain columns: product name, quantity, profit"

  - Ensure the uploaded file has the required columns with correct names.

- **Graph not displayed:**

  - Verify Matplotlib and file permissions in the media directory.

---

## Future Enhancements

1. Add support for other file formats (e.g., CSV).
2. Implement advanced visualizations.
3. Enable multi-user access and file history tracking.

hope you will like it
