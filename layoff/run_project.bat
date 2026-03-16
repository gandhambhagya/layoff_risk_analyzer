@echo off
echo Starting installation...
call npm install --no-audit --no-fund > npm_install_log.txt 2>&1
echo npm install finished.
start /B python -m uvicorn backend.main:app --port 8000 > backend_log.txt 2>&1
echo Backend started.
npm run dev > frontend_log.txt 2>&1
