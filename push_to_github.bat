@echo off
title Push Machine Manuals to GitHub
echo ====================================================
echo Syncing Machine Manuals to GitHub...
echo ====================================================
echo.

cd /d "%~dp0"

echo [1/3] Adding all updated and new files...
git add .

echo.
echo [2/3] Creating commit...
git commit -m "Auto-sync from company laptop: %date% %time%"

echo.
echo [3/3] Pushing to GitHub main branch...
git push origin main

echo.
echo ====================================================
echo Sync completed successfully!
echo ====================================================
echo.
pause
