# Flask Todo App - Deployment Guide 🚀

## 📋 Prerequisites Complete ✅

Your project is now ready for production deployment on Vercel with Supabase PostgreSQL!

## 🔧 Local Development

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Locally
```bash
python run.py
```

The app will run at: `http://127.0.0.1:5000`

## 🌐 Deploy to Vercel

### Option A: Deploy via Vercel Dashboard (Easiest)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for production deployment"
   git push origin main
   ```

2. **Import to Vercel**
   - Go to https://vercel.com/new
   - Import your GitHub repository
   - Vercel will auto-detect the configuration

3. **Add Environment Variables**
   Before deploying, add these in Vercel:
   
   | Variable | Value |
   |----------|-------|
   | `SECRET_KEY` | Generate: `python -c "import secrets; print(secrets.token_hex(32))"` |
   | `DATABASE_URL` | Your Supabase PostgreSQL connection string |
   | `FLASK_ENV` | `production` |

4. **Deploy!**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your app will be live!

### Option B: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
vercel

# Add environment variables
vercel env add SECRET_KEY
vercel env add DATABASE_URL
vercel env add FLASK_ENV

# Deploy to production
vercel --prod
```

## 🗄️ Supabase Database Setup

### Get Your Database URL

1. Go to your Supabase project dashboard
2. Click **Settings** → **Database**
3. Find **Connection string** → **URI** tab
4. Copy the URL (format: `postgresql://postgres:[YOUR-PASSWORD]@db.xxxxx.supabase.co:5432/postgres`)
5. Replace `[YOUR-PASSWORD]` with your actual password

### Verify Tables

After first deployment:
1. Go to Supabase → **Table Editor**
2. You should see:
   - `user` table (id, username, email, password_hash)
   - `task` table (id, title, status, user_id)

## 🎯 Testing Your Deployment

1. Visit your Vercel URL: `https://your-app.vercel.app`
2. Register a new user
3. Login
4. Create some tasks
5. Verify data persists in Supabase

## 📁 Project Structure

```
ToDo-Flask/
├── api/
│   └── index.py          # Vercel entry point
├── app/
│   ├── __init__.py       # App factory with smart DB config
│   ├── models.py         # User & Task models
│   ├── forms.py          # WTForms
│   ├── routes/
│   │   ├── auth.py       # Registration, login, logout
│   │   └── tasks.py      # Task management
│   ├── templates/        # Jinja2 templates
│   └── static/           # CSS files
├── .env                  # Local environment (not committed)
├── .env.example          # Environment template
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel configuration
├── run.py                # Local development server
└── README.md            # This file
```

## 🔒 Security Notes

- ✅ `.env` is in `.gitignore` (never commit secrets!)
- ✅ Passwords are hashed with bcrypt
- ✅ CSRF protection enabled
- ✅ SECRET_KEY should be random in production

## 🐛 Troubleshooting

### Local Development Issues

**Import errors:**
```bash
pip install -r requirements.txt
```

**Database errors:**
```bash
# Delete old database and recreate
del instance\todo.db
python run.py
```

### Vercel Deployment Issues

**Check logs:**
1. Vercel Dashboard → Your Project → Deployment
2. Click "Functions" tab → View logs

**Common fixes:**
- Verify all environment variables are set
- Check DATABASE_URL format is correct
- Ensure `api/index.py` exists at root level

## 📊 Environment Variables

### Local (.env)
```env
SECRET_KEY=dev-key
FLASK_ENV=development
DATABASE_URL=sqlite:///todo.db
```

### Production (Vercel Dashboard)
```env
SECRET_KEY=<random-32-char-hex>
FLASK_ENV=production
DATABASE_URL=postgresql://postgres:PASSWORD@db.xxx.supabase.co:5432/postgres
```

## 🎉 Success!

Your Flask Todo app is now production-ready with:
- ✅ Persistent PostgreSQL database
- ✅ User authentication
- ✅ Serverless deployment
- ✅ Free hosting
- ✅ Auto-deploys from Git

---

**Live App:** https://your-app.vercel.app (after deployment)

**Tech Stack:**
- Backend: Flask + SQLAlchemy
- Database: PostgreSQL (Supabase)
- Hosting: Vercel (Serverless)
- Authentication: Flask-Login
