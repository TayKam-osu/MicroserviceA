import os
import time

REQUEST_FILE = "key_request.txt"
RESPONSE_FILE = "key_response.txt"

def validate_key(key):
    key = key.strip().upper()
    if len(key) != 4:
        return False, "Key must be exactly 4 characters long."
    if any(ch not in "ATCG" for ch in key):
        return False, "Key contains invalid characters. Only A, T, C, G allowed."
    if len(set(key)) != 4:
        return False, "Key must contain 4 unique DNA bases."
    mapping = {
        "00": key[0],
        "01": key[1],
        "10": key[2],
        "11": key[3]
    }
    return True, mapping

def process_key_file():
    if os.path.exists(REQUEST_FILE):
        with open(REQUEST_FILE, "r") as f:
            content = f.read().strip()
        if content:
            valid, result = validate_key(content)
            if valid:
                mapping = result
                mapping_str = f"00 -> {mapping['00']}, 01 -> {mapping['01']}, 10 -> {mapping['10']}, 11 -> {mapping['11']}"
                response = f"VALID: {mapping_str}"
            else:
                response = f"INVALID: {result}"
            with open(RESPONSE_FILE, "w") as f:
                f.write(response)
                f.flush()
            print(f"[Microservice] Wrote to '{RESPONSE_FILE}': {response}")

        os.remove(REQUEST_FILE)

def main():
    print("Key Validator Microservice started. Monitoring for key requests...")
    try:
        while True:
            process_key_file()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Microservice terminated.")

if __name__ == "__main__":
    main()

