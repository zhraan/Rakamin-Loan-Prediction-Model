import subprocess, os, sys, shutil

repo = r"d:\1Unand AAN\Data Unand, KHS & Kartu Ujian\Linkedin Data\Portfolio\Data Analyst Scientist\Rakamin - Virtual Interships\Data Scientist - Idx Partnert\Minggu 4\7. [Final Task] Prediction Model"
nb_original = os.path.join(repo, "Final_Task_Loan_Prediction_Model (1).ipynb")

work_dir = r"C:\nbconvert_temp"
os.makedirs(work_dir, exist_ok=True)
nb_temp = os.path.join(work_dir, "notebook.ipynb")
shutil.copy2(nb_original, nb_temp)

print("Converting to PDF...")
r = subprocess.run(
    [sys.executable, "-m", "jupyter", "nbconvert", "--to", "webpdf",
     "--allow-chromium-download", "notebook.ipynb"],
    cwd=work_dir, capture_output=True, text=True, timeout=600
)
print(f"Exit code: {r.returncode}")

pdf_temp = os.path.join(work_dir, "notebook.pdf")
if os.path.exists(pdf_temp):
    pdf_final = os.path.join(repo, "Final_Task_Loan_Prediction_Model(1).pdf")
    shutil.copy2(pdf_temp, pdf_final)
    size_mb = os.path.getsize(pdf_final) / (1024*1024)
    print(f"PDF berhasil! ({size_mb:.1f} MB) -> {pdf_final}")
else:
    print("PDF gagal.")
    if r.stderr:
        for line in r.stderr.strip().split('\n'):
            if 'error' in line.lower():
                print(f"  {line.strip()}")

shutil.rmtree(work_dir, ignore_errors=True)
print("Selesai!")
