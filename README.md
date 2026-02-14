# Strategic Product Placement Analysis

A professional Flask web application that analyzes retail product placement effectiveness using Tableau visualizations and interactive dashboards.

## 📊 Project Overview

This project demonstrates how product category and placement influence sales performance through comprehensive data visualization. The application integrates Tableau dashboards with Flask to provide insights into optimal product positioning strategies.

## 🚀 Features

- **Interactive Dashboard**: Real-time sales performance visualization
- **Story Analysis**: Three comprehensive stories covering different aspects of product placement
- **Professional UI**: Modern, responsive design with gradient navigation
- **Tableau Integration**: Seamless embedding of Tableau Public visualizations
- **Mobile Responsive**: Optimized for all device sizes

## 📁 Project Structure

```
windsurf-project-2/
├── app.py                 # Flask application with routes
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── static/
│   └── style.css         # Professional CSS styling
└── templates/
    ├── index.html        # Home page with project overview
    ├── dashboard.html    # Interactive dashboard page
    ├── story.html        # Legacy story page (redirects)
    ├── story1.html       # Story 1: Category Performance
    ├── story2.html       # Story 2: Placement Impact
    ├── story3.html       # Story 3: Combined Impact
    └── about.html        # About page with project details
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd windsurf-project-2
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

## 🌐 Deployment Options

### Option 1: PythonAnywhere (Recommended for Beginners)

1. **Sign up** at [PythonAnywhere](https://www.pythonanywhere.com/)
2. **Create a new Web App** using Flask template
3. **Upload your files** to the PythonAnywhere file system
4. **Install requirements** in the virtual environment
5. **Configure the web app** to point to `app.py`

### Option 2: Heroku

1. **Install Heroku CLI**
2. **Create requirements.txt** (already included)
3. **Create Procfile:**
   ```
   web: python app.py
   ```
4. **Deploy:**
   ```bash
   heroku create
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

### Option 3: Vercel (Recommended for Flask)

1. **Install Vercel CLI**
2. **Create vercel.json configuration**
3. **Deploy:**
   ```bash
   vercel
   ```

## 📱 Application Pages

- **Home** (`/`): Project overview and navigation
- **Dashboard** (`/dashboard`): Interactive Tableau dashboard
- **Story 1** (`/story1`): Category performance analysis
- **Story 2** (`/story2`): Placement impact analysis
- **Story 3** (`/story3`): Combined impact analysis
- **About** (`/about`): Project information and details

## 🎨 Design Features

- **Modern Navigation**: Dropdown menu for story navigation
- **Card-Based Layout**: Professional About page with card sections
- **Responsive Design**: Optimized for mobile, tablet, and desktop
- **Smooth Animations**: Hover effects and transitions
- **Professional Typography**: Clean, readable fonts
- **Gradient Styling**: Modern color schemes

## 📊 Dataset Information

The application analyzes retail product placement data including:
- Product categories and classifications
- Physical placement locations
- Pricing and competitor pricing
- Sales volume metrics
- Promotional activities
- Customer demographics

## 🔧 Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualization**: Tableau Public API
- **Styling**: Custom CSS with responsive design
- **Icons**: Emoji icons for visual appeal

## 📝 Flask Routes

```python
@app.route('/')           # Home page
@app.route('/dashboard')  # Interactive dashboard
@app.route('/story')      # Redirects to story1
@app.route('/about')      # About page
@app.route('/story1')     # Story 1: Category Performance
@app.route('/story2')     # Story 2: Placement Impact
@app.route('/story3')     # Story 3: Combined Impact
```

## 🌍 Live Demo

Access the live application at: `https://your-app-url.com`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 📞 Contact

For questions or suggestions, please open an issue in the repository.

---

**Built with ❤️ using Flask and Tableau Public**
