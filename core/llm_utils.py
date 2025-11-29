# core/llm_utils.py
from openai import OpenAI
from google import genai 
from google.genai import types
import json
from core.config import *

client = OpenAI(
    api_key=DEEPSEEK_API, 
    base_url=DEEPSEEK_BASE_URL
    )


# ================================   LLM based on DeepSeek   ================================
# def analyze_with_deepseek(text: str) -> str:
def analyze_with_deepseek(text):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": """
                 You are a receipt analysis expert. Your tasks:
                    1. Identify the store/date/total purchase
                    2. Extract the address (if applicable)
                    3. Format the output as:
                        Store: [store name]  
                        Date: [date]  
                        Address: [address]  
                        Total: [total payment]  
                """},
                {"role": "user", 
                 "content": f"Analyze the following receipt text and then please write the output as 4 formats (Store, Date, Address, Total) only! No explanation, no extra notes! \n\n{text}"}
            ],
            temperature=0.2,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[DeepSeek ERROR] {e}"



# ==================================================================================
# ==================================================================================
# core/llm_utils.py (Versi Sederhana)

# ================================   LLM based on Gemini   ================================

# try:
#     client = genai.Client(
#         api_key=GEMINI_API
#     )
# except Exception as e:
#     # Handling error jika API Key tidak ditemukan
#     print(f"Error initializing Gemini client: {e}")
#     client = None

# def analyze_with_gemini_simple(text: str) -> str:
#     if not client:
#         return "[GEMINI CLIENT ERROR]"

#     MODEL = "gemini-2.5-flash"
    
#     # 1. System Instruction (Mirip dengan yang Anda pakai)
#     # Tambahkan instruksi untuk format output JSON yang ketat.
#     system_content = """
#     Anda adalah receipt analysis expert. Tugas Anda:
#     1. Identify the store, date, and total purchase.
#     2. Extract the address (if applicable).
#     3. Format the ENTIRE output as a STRICT JSON object with no explanation, 
#     no commentary, and no extra text outside the JSON block.
    
#     FORMAT JSON:
#     {
#         "store": "[store name]",
#         "date": "[Date in YYYY-MM-DD]",
#         "total": "[total payment amount]",
#         "address": "[address or 'N/A']"
#     }
#     """

#     # 2. User Prompt
#     user_content = f"Analyze the following receipt text:\n\n{text}"

#     try:
#         response = client.models.generate_content(
#             model=MODEL,
#             # contents=[types.Content(role="system", parts= [types.Part.from_text(system_content)]),
#             #           types.Content(role="user", parts= [types.Part.from_text(user_content)])],
#             content= [
#                 {'role': 'system', 'parts': [{'text': system_content}]},
#                 {'role': 'user', 'parts': [{'text': user_content}]},
#             ],
#             config=types.GenerateContentConfig(
#                 temperature=0.3,
#                 max_output_tokens=300
#             )
#         )
        
#         # Mengembalikan teks hasil respons (berupa string JSON)
#         return response.text.strip()

#     except Exception as e:
#         # Handling exception
#         return f"[GEMINI ERROR] {e}"

# --- Contoh Penggunaan ---
# text_from_ocr = "..."
# result = analyze_with_gemini_simple(text_from_ocr)
# print(result)

# ==================================================================================
# ==================================================================================

# try:
#     client = genai.Client()
# except Exception as e:
#     print(f"Error initializing Gemini client: {e}")
#     print("Pastikan variabel lingkungan 'GEMINI_API_KEY' sudah disetel.")
#     exit()

# def extract_receipt_data_with_gemini(text):
#     """
#     Mengirim teks mentah hasil OCR ke Gemini untuk diekstraksi menjadi data terstruktur.
    
#     Args:
#         ocr_text: Teks mentah dari struk belanja.

#     Returns:
#         dict: Data terstruktur yang diekstrak (misalnya, total, tanggal, item).
#     """

#     # 1. Tentukan Schema Output JSON yang Anda inginkan
#     # Ini memastikan Gemini menghasilkan format data yang bisa diproses
#     output_schema = types.Schema(
#         type=types.Type.OBJECT,
#         properties={
#             "nama_toko": types.Schema(type=types.Type.STRING, description="Nama lengkap merchant/toko."),
#             "tanggal_transaksi": types.Schema(type=types.Type.STRING, description="Tanggal transaksi dalam format YYYY-MM-DD."),
#             "waktu_transaksi": types.Schema(type=types.Type.STRING, description="Waktu transaksi dalam format HH:MM."),
#             "total_pembayaran": types.Schema(type=types.Type.NUMBER, description="Jumlah total pembayaran (hanya angka)."),
#             "kategori_pengeluaran": types.Schema(type=types.Type.STRING, description="Klasifikasi kategori pengeluaran (misalnya: 'Makanan', 'Transportasi', 'Belanja Rumah')."),
#             "items": types.Schema(
#                 type=types.Type.ARRAY,
#                 description="Daftar item yang dibeli.",
#                 items=types.Schema(
#                     type=types.Type.OBJECT,
#                     properties={
#                         "nama_item": types.Schema(type=types.Type.STRING),
#                         "jumlah": types.Schema(type=types.Type.NUMBER),
#                         "harga_satuan": types.Schema(type=types.Type.NUMBER)
#                     }
#                 )
#             )
#         },
#         required=["nama_toko", "tanggal_transaksi", "total_pembayaran"]
#     )
    
#     # 2. Instruksi Sistem (Peran untuk Gemini)
#     system_instruction = (
#         "Anda adalah AI Engineer spesialis dalam Ekstraksi Data dari Teks Struk Belanja. "
#         "Tugas Anda adalah membaca teks OCR yang diberikan dan mengonversinya menjadi objek JSON. "
#         "Pastikan tanggal menggunakan format YYYY-MM-DD. Kategori pengeluaran harus jelas."
#     )
    
#     # 3. Prompt User (Input teks dari OCR Anda)
#     user_prompt = f"Ekstrak data dari struk belanja berikut: \n\n{text}"

#     try:
#         response = client.models.generate_content(
#             model='gemini-2.5-flash', # Model yang cepat dan efisien
#             contents=user_prompt,
#             config=types.GenerateContentConfig(
#                 system_instruction=system_instruction,
#                 response_mime_type="application/json", # Minta output JSON
#                 response_schema=output_schema # Terapkan skema yang sudah dibuat
#             )
#         )
        
#         # Output dari Gemini adalah string JSON
#         json_string = response.text.strip()
        
#         # Konversi string JSON menjadi Python Dictionary
#         extracted_data = json.loads(json_string)
#         return extracted_data

#     except Exception as e:
#         print(f"Terjadi kesalahan saat memanggil Gemini API: {e}")
#         return None