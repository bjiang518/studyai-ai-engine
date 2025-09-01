# StudyAI AI Engine - Deployment Guide

## 🚀 Railway.app Deployment (Recommended)

### Step 1: Prepare Your Repository
```bash
cd /Users/bojiang/StudyAI_Workspace/03_ai_engine
git init
git add .
git commit -m "Initial AI Engine setup with improved LaTeX prompting"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### Step 2: Deploy to Railway
1. Go to [Railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "Deploy from GitHub repo"
4. Select your `03_ai_engine` repository
5. Railway will auto-detect Python and deploy

### Step 3: Set Environment Variables
In Railway dashboard, add these environment variables:
```
OPENAI_API_KEY=your_openai_api_key_here
DEFAULT_MODEL=gpt-4o-mini
ENVIRONMENT=production
PORT=8000
```

### Step 4: Get Your Deployed URL
Railway will provide a URL like: `https://studyai-ai-engine-production.up.railway.app`

### Step 5: Update iOS App
Update `NetworkService.swift`:
```swift
// Replace localhost with Railway URL
private let localAIEngineURL = "https://studyai-ai-engine-production.up.railway.app"
```

## 🔄 Alternative: Render.com Deployment

### Step 1: Create Web Service
1. Go to [Render.com](https://render.com)
2. Connect GitHub repository
3. Create new "Web Service"

### Step 2: Configure Build
- **Build Command**: `pip install -r requirements-railway.txt`
- **Start Command**: `uvicorn src.main:app --host 0.0.0.0 --port $PORT`
- **Environment**: Python 3.11

### Step 3: Environment Variables
```
OPENAI_API_KEY=your_api_key
DEFAULT_MODEL=gpt-4o-mini
```

## 🧪 Testing Your Deployment

### Test Health Endpoint
```bash
curl https://your-railway-url.up.railway.app/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "StudyAI AI Engine", 
  "version": "2.0.0",
  "features": ["advanced_prompting", "educational_optimization", "practice_generation"]
}
```

### Test Question Processing
```bash
curl -X POST https://your-railway-url.up.railway.app/api/v1/process-question \
  -H "Content-Type: application/json" \
  -d '{
    "student_id": "test_student_001",
    "question": "Solve 2x + 3 = 7",
    "subject": "mathematics",
    "include_followups": true
  }'
```

## 📱 iOS Integration

Your iOS app will now:
1. **Try AI Engine first** (Railway URL) - Gets improved LaTeX formatting
2. **Fallback to Vercel** - If AI Engine is down

## 🎯 Expected Results

With the AI Engine deployed, you'll get responses like:
```
To solve the equation $2x + 3 = 7$, we need to isolate the variable $x$.

First, subtract 3 from both sides:
$$2x + 3 - 3 = 7 - 3$$
$$2x = 4$$

Next, divide both sides by 2:
$$x = 2$$

Therefore, the solution is $x = 2$.
```

**No more:**
- ❌ `### Step 1:` headers
- ❌ `- bullet points`  
- ❌ `---` separators
- ❌ Unrendered `\sqrt{3}`

## 💰 Cost Estimation

### Railway.app:
- **Free tier**: $5 credit (good for testing)
- **Paid**: ~$5-10/month for basic usage
- **Scaling**: Automatic based on traffic

### Render.com:
- **Free tier**: 750 hours/month
- **Paid**: $7/month for always-on service

### OpenAI Costs:
- **GPT-4o-mini**: ~$0.15 per 1M input tokens
- **Estimated**: $10-50/month depending on usage