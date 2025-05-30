import os
from dotenv import load_dotenv
from openai_handler import generate_text
import sys
from utils import (
    load_prompt,
    fill_prompt,
    save_cv_to_docx,
    save_cover_letter_to_docx,
    collect_user_data_interactive  # bunu ekle
)

load_dotenv()
import os
from pathlib import Path

def get_output_dir():
    # Kullanıcının Masaüstü
    desktop = Path.home() / "Desktop"
    output_dir = desktop / "GeneratedCV"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def resource_path(relative_path):
    """PyInstaller içinden çalışırken gerçek yolu çözer"""
    try:
        # PyInstaller ile paketlenmişse geçici dizine bak
        base_path = sys._MEIPASS
    except Exception:
        # Normal Python ortamıysa çalıştırma dizinini al
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def main():
    user_data = collect_user_data_interactive()
    output_dir = get_output_dir()
  



    about_prompt = f"""You are a professional resume writer with expertise in AI-enhanced career branding. Based on the following keywords, write a compelling, 4–5 sentence 'About Me' section for a CV:\n\n{user_data['about_keywords']}\n\nThe tone should match the candidate's tone preference: {user_data['tone_preference']}. Keep it clear, confident, and concise."""
    user_data["about_me"] = generate_text(about_prompt)

    cv_template = load_prompt("prompts/cv_prompt.txt")
    cv_prompt = fill_prompt(cv_template, user_data)
    cv_output = generate_text(cv_prompt)
    save_cv_to_docx(cv_output, output_dir / "generated_cv.docx", user_data)

    cl_template = load_prompt("prompts/cover_letter_prompt.txt")
    cl_prompt = fill_prompt(cl_template, user_data)
    cl_output = generate_text(cl_prompt)
    save_cover_letter_to_docx(cl_output, output_dir / "generated_cover_letter.docx", user_data)

    print(f"\n✅ All done! Your CV and Cover Letter are saved in: {output_dir}")

if __name__ == "__main__":
    main()
