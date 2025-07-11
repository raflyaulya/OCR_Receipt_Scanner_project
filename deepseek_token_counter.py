import tiktoken
from datetime import datetime

# 1. Hitung Token dari Teks
def count_tokens(text: str, model: str = "deepseek-chat") -> int:
    try:
        enc = tiktoken.encoding_for_model(model)
        return len(enc.encode(text))
    except:
        # Fallback untuk model yang tidak dikenali
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))

# 2. Estimasi Biaya
def calculate_cost(
    input_tokens: int, 
    output_tokens: int, 
    model: str = "deepseek-reasoner",
    use_discount: bool = False
) -> float:
    # Harga per 1K token (USD)
    pricing = {
        "deepseek-chat": {"input": 0.0005, "output": 0.0015},
        "deepseek-reasoner": {"input": 0.0001, "output": 0.0003},
    }
    
    if model not in pricing:
        raise ValueError(f"Model {model} tidak ditemukan")
    
    # Apply diskon 75% jika di jam off-peak (23:30-07:30 WIB)
    if use_discount:
        discount = 0.75 if model == "deepseek-reasoner" else 0.50
        input_cost = (pricing[model]["input"] * (1 - discount)) * input_tokens / 1000
        output_cost = (pricing[model]["output"] * (1 - discount)) * output_tokens / 1000
    else:
        input_cost = pricing[model]["input"] * input_tokens / 1000
        output_cost = pricing[model]["output"] * output_tokens / 1000
    
    return input_cost + output_cost

# 3. Contoh Pemakaian
if __name__ == "__main__":
    # Contoh teks dari OCR receipt
    ocr_text = """
    Total: Rp35.000
    """
    prompt = "Ekstrak total belanja, tanggal, dan nama merchant dalam format JSON."

    # Hitung token input (teks + prompt)
    input_tokens = count_tokens(ocr_text + prompt, model="deepseek-reasoner")
    
    # Simulasi output (200 token)
    output_tokens = 200  

    # Cek apakah sedang diskon (23:30-07:30 WIB)
    current_hour = datetime.now().hour
    is_discount_time = 23 <= current_hour or current_hour <= 7

    # Hitung biaya
    cost = calculate_cost(
        input_tokens,
        output_tokens,
        model="deepseek-reasoner",
        use_discount=is_discount_time
    )

    print(f"Input Tokens: {input_tokens}")
    print(f"Output Tokens: {output_tokens}")
    print(f"Model: deepseek-reasoner")
    print(f"Diskon 75%: {'YA' if is_discount_time else 'TIDAK'}")
    print(f"Biaya/Request: ${cost:.6f}")
    print(f"Estimasi Request dengan $2: {int(2 / cost)}")