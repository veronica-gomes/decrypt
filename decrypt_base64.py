import base64

def base64_decode(encoded_string):
    try:
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
    except:
        return None

def base32_decode(encoded_string):
    try:
        decoded_bytes = base64.b32decode(encoded_string)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
    except:
        return None
    
exit = "0"
while (exit == "0"):
    option = input("Digite 1 para decodificar para base64 ou digite 2 para decodificar para base32: ")
    
    if option == "1":
        flag = input("Digite a flag em base64: ")
        decoded_flag_base64 = base64_decode(flag)
        if decoded_flag_base64 is not None:
            print("Flag decodificada (Base64):", decoded_flag_base64)
        else:
            print("Erro ao decodificar a flag em Base64.")
    elif option == "2":
        flag = input("Digite a flag em base32: ")
        decoded_flag_base32 = base32_decode(flag)
        if decoded_flag_base32 is not None:
            print("Flag decodificada (Base32):", decoded_flag_base32)
        else:
            print("Erro ao decodificar a flag em Base32.")
    else:
        print("Opção inválida.")

    exit = input("Digite 0 para continuar, ou qualquer valor para parar: ")