from flask import Flask, render_template, request, send_file
from flask_cors import CORS
from google import genai
import os
import gc
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# PDF Libraries
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # 1. INITIALIZE CLIENT INSIDE THE ROUTE
            # This guarantees Render has loaded the environment variables first.
            API_KEY = os.environ.get("GEMINI_API_KEY")
            if not API_KEY:
                raise ValueError("API Key is missing in Render environment variables!")
            
            client = genai.Client(api_key=API_KEY)

            leaf_file = request.files.get('leaf_image')
            grape_file = request.files.get('grape_image')
            sugar = request.form.get('sugar', '15.0')

            if not leaf_file or leaf_file.filename == '':
                raise ValueError("Leaf image is required (upload or capture).")
            if not grape_file or grape_file.filename == '':
                raise ValueError("Grape image is required (upload or capture).")

            # We will resize the images to save memory and processing time
            def process_image(file_storage):
                file_storage.seek(0)
                img = Image.open(file_storage)
                img.thumbnail((800, 800))
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                return img

            leaf_img = process_image(leaf_file)
            grape_img = process_image(grape_file)

           prompt = f"""
                तुम्ही एक ज्येष्ठ द्राक्ष शेती तज्ज्ञ (Viticulturist) आणि वनस्पती रोगनिदान शास्त्रज्ञ आहात. शेतकरी बांधवांनी पाठवलेल्या द्राक्षाच्या पानाच्या आणि फळाच्या फोटोंचे बारकाईने निरीक्षण करा.
                माहिती: रिफ्रॅक्टोमीटरवर साखरेचे प्रमाण (Sugar Reading) {sugar} Brix आहे.

                गावातील सामान्य शेतकऱ्यांना सहज समजेल अशा सोप्या, स्पष्ट आणि शुद्ध मराठी भाषेत "विटीसेन्स द्राक्ष रोगनिदान अहवाल" तयार करा. प्रत्येक मुद्द्याचे उत्तर २ ते ३ सोप्या वाक्यांत असावे:

            - 🌿 रोगाचे नाव / निदान: द्राक्ष वेलीला नेमका कोणता रोग झाला आहे किंवा ती निरोगी आहे का, ते स्पष्ट सांगा. फोटोंवरून तुम्हाला हे कसे समजले, ते अगदी सोप्या भाषेत समजावून सांगा.
            - 🔍 रोगाची लक्षणे: पानावरील किंवा फळावरील डाग, चट्टे किंवा बदललेला रंग याबद्दल सांगा. या लक्षणांमुळे पानांच्या अन्न तयार करण्याच्या क्षमतेवर (प्रकाशसंश्लेषण) किंवा फळांच्या वाढीवर कसा वाईट परिणाम होतोय, ते सांगा.
            - 🧪 औषधोपचार / उपाय: बाजारात मिळणाऱ्या बुरशीनाशकांची किंवा कीटकनाशकांची नावे सुचवा (उदा. मॅन्कोझेब - Mancozeb, मायक्लोब्युटानिल - Myclobutanil, किंवा कॉपर हायड्रॉक्साईड - Copper Hydroxide). हे औषध रोगाचा नाश करण्यासाठी कसे काम करते, ते मराठीत सांगा.
            - 📅 औषध फवारणीचे वेळापत्रक: औषध किती दिवसांच्या अंतराने आणि एकूण किती वेळा फवारणी करायची, त्याचे अचूक वेळापत्रक द्या. रोगाचा प्रादुर्भाव पूर्णपणे थांबवण्यासाठी हे वेळापत्रक पाळणे का गरजेचे आहे, ते सांगा.
            - 🍇 द्राक्ष पिकण्याची स्थिती: साखरेचे प्रमाण ({sugar} Brix) आणि द्राक्षाचा दिसणारा रंग यांची तुलना करून द्राक्ष काढणीस तयार आहेत का ते सांगा. बाजारातील चांगल्या गोडीसाठी साखर आणि आंबटपणाचे प्रमाण कसे असावे, यावर सल्ला द्या.
            - 📊 बाजारपेठ आणि काढणीचा सल्ला: द्राक्षाचा दर्जा आणि गोडी बघून ती कुठे विकली जाऊ शकतात ते ठरवा. द्राक्षे लगेच तोडावीत, काही दिवस वाट पाहावी, की आधी औषधोपचार करून मगच निर्णय घ्यावा, याबद्दल अंतिम सल्ला द्या.

            नियम:
            १. माहितीसाठी बुलेट पॉइंट्स (मुद्देसूद रचना) वापरा.
            २. भाषा पूर्णपणे मराठी असावी (केवळ औषधांची नावे इंग्रजीत कंसात लिहिता येतील).
            ३. प्रत्येक मुद्द्यामध्ये २ ते ३ सोपी आणि स्पष्ट वाक्ये असावीत, जेणेकरून शेतकरी ती सहज वाचू शकतील.
                """

            # Use Gemini API
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=[prompt, leaf_img, grape_img]
            )
            
            report = response.text

            # 2. FREE UP MEMORY
            # This prevents Render from killing the app when processing multiple images
            del leaf_img
            del grape_img
            gc.collect()

            return render_template('index.html', result=True, report=report)

        except Exception as e:
            print(f"Server Error: {e}")
            return render_template('index.html', result=False, error=str(e))

    return render_template('index.html', result=False)

@app.route('/download-report', methods=['POST'])
def download_report():
    report_text = request.form.get('report_content')
    if not report_text:
        return "No report content found", 400
        
    buffer = BytesIO()
    
    # PDF Setup
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=18, spaceAfter=20, textColor=colors.HexColor("#a29bfe"))
    body_style = styles['Normal']
    body_style.fontSize = 11
    body_style.leading = 14 
    
    story = []
    story.append(Paragraph("VITISENSE PRO - OFFICIAL AGRONOMIST REPORT", title_style))
    story.append(Spacer(1, 12))
    
    # Process text for PDF
    clean_text = report_text.replace("**", "").replace("#", "").replace("*", "")
    lines = clean_text.split('\n')
    for line in lines:
        if line.strip():
            story.append(Paragraph(line, body_style))
            story.append(Spacer(1, 10))

    doc.build(story)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="VitiSense_Report.pdf")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
