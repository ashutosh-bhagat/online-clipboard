# 🔧 Troubleshooting Guide

## Frontend Not Working?

### Step 1: Check if Backend is Running

1. **Open terminal/command prompt**
2. **Navigate to backend folder:**
   ```bash
   cd backend
   ```
3. **Start the backend:**
   ```bash
   python -m uvicorn main:app --reload
   ```
4. **You should see:**
   ```
   INFO:     Uvicorn running on http://127.0.0.1:8000
   ```

### Step 2: Check if Frontend Server is Running

1. **Open a NEW terminal/command prompt**
2. **Navigate to frontend folder:**
   ```bash
   cd frontend
   ```
3. **Start the frontend server:**
   ```bash
   python server.py
   ```
4. **You should see:**
   ```
   Frontend server running at http://localhost:3000
   ```

### Step 3: Test Backend API

1. **Open browser and go to:** http://127.0.0.1:8000/docs
2. **You should see FastAPI documentation**
3. **If not, backend is not running properly**

### Step 4: Test Frontend

1. **Open browser and go to:** http://localhost:3000
2. **You should see the Clipy Clipboard interface**
3. **Open browser console (F12) to see any errors**

### Step 5: Common Issues

#### Issue: "Cannot connect to backend"
**Solution:**
- Make sure backend is running on port 8000
- Check if port 8000 is not used by another application
- Try: `netstat -an | findstr 8000` (Windows) or `lsof -i :8000` (Mac/Linux)

#### Issue: "Frontend page not loading"
**Solution:**
- Make sure frontend server is running on port 3000
- Check if port 3000 is not used by another application
- Try accessing: http://localhost:3000/index.html

#### Issue: "CORS errors in console"
**Solution:**
- Backend has CORS enabled, this shouldn't happen
- Make sure you're using the frontend server, not opening the file directly

#### Issue: "Upload not working"
**Solution:**
- Check browser console for errors
- Make sure both servers are running
- Try uploading a small text file first

### Step 6: Manual Testing

#### Test Text Upload:
1. **Go to:** http://127.0.0.1:8000/docs
2. **Click on POST /upload_text**
3. **Click "Try it out"**
4. **Enter some text**
5. **Click "Execute"**
6. **You should get a code back**

#### Test File Upload:
1. **Go to:** http://127.0.0.1:8000/docs
2. **Click on POST /upload**
3. **Click "Try it out"**
4. **Upload a file**
5. **Click "Execute"**
6. **You should get a code back**

### Step 7: Reset Everything

If nothing works:

1. **Stop all servers** (Ctrl+C in both terminals)
2. **Close all browser tabs**
3. **Restart backend:**
   ```bash
   cd backend
   python -m uvicorn main:app --reload
   ```
4. **Restart frontend (new terminal):**
   ```bash
   cd frontend
   python server.py
   ```
5. **Open:** http://localhost:3000

### Step 8: Check File Structure

Make sure your folders look like this:
```
online clipboard/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   └── server.py
└── uploads/
```

### Still Not Working?

1. **Check Python version:** `python --version` (should be 3.7+)
2. **Install dependencies:** `pip install -r backend/requirements.txt`
3. **Check for error messages** in both terminal windows
4. **Try a different browser** (Chrome, Firefox, Edge)
5. **Disable browser extensions** that might interfere

### Quick Fix Commands

```bash
# Kill processes on ports (if needed)
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -ti:8000 | xargs kill -9
lsof -ti:3000 | xargs kill -9

# Reinstall dependencies
pip install --upgrade fastapi uvicorn python-multipart
``` 