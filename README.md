# 🔗 Clipy Clipboard

A modern, secure online clipboard application that allows you to share files and text instantly with unique codes. Built with FastAPI, Tailwind CSS, and modern web technologies.

## ✨ Features

- **📤 Upload & Share** - Upload files or text and get a unique 6-character code
- **📥 Fetch Content** - Retrieve content using the generated code
- **🔄 Auto-Expiration** - Files automatically delete after 24 hours
- **📱 Responsive Design** - Works perfectly on desktop and mobile
- **🎨 Modern UI** - Beautiful Tailwind CSS interface with animations
- **🔒 Secure** - Unique codes with automatic cleanup
- **⚡ Fast** - Lightweight and optimized for speed

## 🏗️ Architecture

```
Clipy Clipboard/
├── backend/                 # FastAPI backend server
│   ├── main.py             # Main application with API endpoints
│   ├── requirements.txt    # Python dependencies
│   └── uploads/            # File storage directory
├── frontend/               # Static frontend files
│   ├── index.html         # Main application interface
│   └── server.py          # Simple HTTP server for development
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Local Development

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd clipy-clipboard
   ```

2. **Install backend dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Start the backend server**
   ```bash
   python -m uvicorn main:app --reload
   ```
   The backend will be available at: http://127.0.0.1:8000

4. **Start the frontend server** (in a new terminal)
   ```bash
   cd frontend
   python server.py
   ```
   The frontend will be available at: http://localhost:3000

5. **Open your browser**
   Navigate to http://localhost:3000 and start using Clipy Clipboard!

## 📖 How to Use

### Uploading Content

1. **Text Upload:**
   - Type your text in the "Text Content" area
   - Click "Upload & Get Code"
   - Copy the generated 6-character code

2. **File Upload:**
   - Click "Choose File" and select your file
   - Click "Upload & Get Code"
   - Copy the generated 6-character code

### Retrieving Content

1. **Enter the code** in the "Enter Code" field
2. **Click "Fetch Content"**
3. **For text:** Content will be displayed on screen
4. **For files:** File will be automatically downloaded

### Keyboard Shortcuts

- **Ctrl + Enter** in text area: Upload text
- **Enter** in code field: Fetch content

## 🔧 API Endpoints

### Backend API (FastAPI)

- `POST /upload` - Upload a file
- `POST /upload_text` - Upload text content
- `GET /get/{code}` - Retrieve content by code
- `GET /docs` - Interactive API documentation

### Example API Usage

```bash
# Upload text
curl -X POST "http://127.0.0.1:8000/upload_text" \
  -H "Content-Type: application/json" \
  -d '"Hello, this is my text!"'

# Upload file
curl -X POST "http://127.0.0.1:8000/upload" \
  -F "file=@yourfile.txt"

# Fetch content
curl "http://127.0.0.1:8000/get/ABC123"
```

## 🛠️ Development

### Project Structure

```
backend/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
└── uploads/            # File storage (auto-created)

frontend/
├── index.html          # Main application interface
└── server.py           # Development server
```

### Key Components

#### Backend (`backend/main.py`)
- **FastAPI Framework** - Modern, fast web framework
- **CORS Middleware** - Cross-origin resource sharing
- **File Storage** - Local file system storage
- **Code Generation** - Secure random code generation
- **Auto-Cleanup** - Automatic file deletion after 24 hours

#### Frontend (`frontend/index.html`)
- **Tailwind CSS** - Utility-first CSS framework
- **Vanilla JavaScript** - No framework dependencies
- **Responsive Design** - Mobile-first approach
- **Modern UI** - Beautiful gradients and animations

### Adding Features

#### New API Endpoints
Add to `backend/main.py`:
```python
@app.get("/new-endpoint")
async def new_endpoint():
    return {"message": "Hello World"}
```

#### Frontend Enhancements
Modify `frontend/index.html`:
```javascript
// Add new functionality
function newFeature() {
    // Your code here
}
```


### Environment Variables

For production deployment, set these environment variables:

```bash
# Backend
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key

# Frontend
BACKEND_URL=https://your-backend-url.com
```

## 🔒 Security Features

- **Unique Codes** - 6-character alphanumeric codes
- **Auto-Expiration** - Files delete after 24 hours
- **CORS Protection** - Configured for specific domains
- **Input Validation** - Server-side validation
- **Error Handling** - Graceful error responses

## 📊 Performance

- **Lightweight** - Minimal dependencies
- **Fast Response** - Optimized file handling
- **Efficient Storage** - Automatic cleanup
- **CDN Ready** - Static assets optimized

## 🐛 Troubleshooting

### Common Issues

1. **"Cannot connect to backend"**
   - Ensure backend is running on port 8000
   - Check CORS configuration
   - Verify network connectivity

2. **"Upload failed"**
   - Check file size limits
   - Verify uploads directory permissions
   - Review server logs

3. **"Invalid code"**
   - Code may have expired (24-hour limit)
   - Check for typos in the code
   - Verify code format (6 characters)

### Debug Commands

```bash
# Check if backend is running
curl http://127.0.0.1:8000/docs

# Check if frontend is accessible
curl http://localhost:3000

# View backend logs
tail -f backend/logs/app.log
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **FastAPI** - Modern web framework
- **Tailwind CSS** - Utility-first CSS framework
- **Vercel** - Frontend hosting
- **Railway** - Backend hosting

## 📞 Support

If you encounter any issues:

1. **Check the troubleshooting section**
2. **Review the API documentation** at `/docs`
3. **Open an issue** on GitHub
4. **Check the logs** for error details

---

**Made with ❤️ from Ashutosh** 
