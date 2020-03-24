echo "Compiling GUI files (PyQt5 format)"
echo "Resource file"
pyrcc5 ui/images.qrc -o images_rc.py
echo "[+] Converting .ui files to .py files"
echo " |-> ui/main_form.ui to main_form.py"
pyuic5 ui/main.ui -o main_form.py
echo " |-> ui/frm_preview.ui to preview_form.py"
pyuic5 ui/frm_preview.ui -o preview_form.py
echo "[*] Done"
