from src.predict import predict_email

print("===================================")
print(" Phishing Email Detection System ")
print("===================================")

while True:
    email = input("\nEnter email text (type 'exit' to quit): ")

    if email.lower() == "exit":
        break

    result = predict_email(email)

    if result == 1:
        print("⚠ Phishing Email Detected!")
    else:
        print("✅ Safe Email")