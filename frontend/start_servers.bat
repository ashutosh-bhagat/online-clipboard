@echo off
echo Starting Clipy Clipboard servers...
echo.

echo Starting Backend Server (FastAPI)...
start "Backend Server" cmd /k "cd backend && python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000"

echo Waiting 3 seconds for backend to start...
timeout /t 3 /nobreak > nul

echo Starting Frontend Server...
start "Frontend Server" cmd /k "cd frontend && python server.py"

echo.
echo Servers are starting...
echo Backend: http://127.0.0.1:8000
echo Frontend: http://localhost:3000
echo.
echo Open http://localhost:3000 in your browser
echo.
pause 