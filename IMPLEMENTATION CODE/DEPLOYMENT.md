# 🚀 Netlify Deployment Guide

## 📋 Prerequisites

1. **Netlify Account**: Sign up at [netlify.com](https://www.netlify.com/)
2. **GitHub Account**: For repository integration
3. **Git**: Installed on your local machine

## 🗂️ Project Structure for Netlify

```
windsurf-project-2/
├── app.py                    # Main Flask app (for local development)
├── requirements.txt          # Python dependencies
├── netlify.toml             # Netlify configuration
├── README.md                # Project documentation
├── DEPLOYMENT.md            # This deployment guide
├── static/
│   └── style.css            # CSS styling
├── templates/
│   ├── index.html           # Home page
│   ├── dashboard.html       # Dashboard page
│   ├── story1.html          # Story 1
│   ├── story2.html          # Story 2
│   ├── story3.html          # Story 3
│   └── about.html           # About page
└── netlify/
    └── functions/
        ├── app.py           # Netlify function version
        └── requirements.txt # Function dependencies
```

## 📤 Step-by-Step Deployment

### Step 1: Initialize Git Repository

```bash
git init
git add .
git commit -m "Initial commit: Flask app with Tableau integration"
```

### Step 2: Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Create a new repository called `strategic-product-placement`
3. Push your local repository:

```bash
git remote add origin https://github.com/yourusername/strategic-product-placement.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy to Netlify

#### Option A: Using GitHub Integration (Recommended)

1. **Login to Netlify**
2. **Click "Add new site" → "Import an existing project"**
3. **Connect to GitHub**
4. **Select your repository**
5. **Build settings**:
   - **Build command**: Leave empty (Netlify will use netlify.toml)
   - **Publish directory**: Leave empty
6. **Click "Deploy site"**

#### Option B: Using Netlify CLI

1. **Install Netlify CLI**:
   ```bash
   npm install -g netlify-cli
   ```

2. **Login to Netlify**:
   ```bash
   netlify login
   ```

3. **Deploy**:
   ```bash
   netlify deploy --prod
   ```

### Step 4: Configure Environment Variables (if needed)

1. Go to your Netlify site dashboard
2. **Site settings → Build & deploy → Environment**
3. Add any required environment variables

## 🔧 Configuration Files Explained

### `netlify.toml`
```toml
[build]
  command = "pip install -r requirements.txt"
  functions = "netlify/functions"

[build.environment]
  PYTHON_VERSION = "3.9"

[[redirects]]
  from = "/*"
  to = "/.netlify/functions/app"
  status = 200
```

### `netlify/functions/app.py`
- Netlify function version of your Flask app
- Handles serverless deployment
- Includes proper handler for Netlify events

## 🌐 Access Your Deployed Site

After deployment, your site will be available at:
- **Netlify URL**: `https://your-site-name.netlify.app`
- **Custom domain**: Configure in Netlify settings if desired

## 🔄 Continuous Deployment

With GitHub integration, your site will automatically redeploy when:
- You push changes to the main branch
- You merge pull requests
- You update any configuration files

## 🐛 Troubleshooting

### Common Issues

1. **Function Not Found**
   - Check `netlify/functions/app.py` exists
   - Verify `netlify.toml` configuration

2. **Template Not Found**
   - Ensure `templates/` folder is in root
   - Check file paths in Flask routes

3. **Build Failures**
   - Check `requirements.txt` format
   - Verify Python version compatibility

### Debug Mode

Add debug logging to `netlify/functions/app.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📱 Testing Your Deployment

1. **Home Page**: `https://your-site.netlify.app/`
2. **Dashboard**: `https://your-site.netlify.app/dashboard`
3. **Stories**: `https://your-site.netlify.app/story1`
4. **About**: `https://your-site.netlify.app/about`

## 🎯 Next Steps

1. **Custom Domain**: Add your own domain in Netlify settings
2. **Analytics**: Enable Netlify Analytics
3. **Forms**: Add Netlify Forms for contact functionality
4. **Optimization**: Enable image optimization and caching

## 📞 Support

- **Netlify Docs**: [docs.netlify.com](https://docs.netlify.com/)
- **GitHub Issues**: Create issues in your repository
- **Netlify Community**: [community.netlify.com](https://community.netlify.com/)

---

**🎉 Your Strategic Product Placement Analysis is now live on Netlify!**
