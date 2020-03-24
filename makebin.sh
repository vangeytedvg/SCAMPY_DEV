echo "*** Create Executable ***"
echo "Creating tango executable"
pyinstaller -w -i app.ico scampy.py --hidden-import=img2pdf --hidden-import=yagmail
echo "Copying ressources and icon to target"
cp app.ico ./dist/scampy
cp ./ui/images.qrc ./dist/scampy
echo "[*] Done"
