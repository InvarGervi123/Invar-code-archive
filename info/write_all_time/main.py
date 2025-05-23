import speech_recognition as sr

def main():
    r = sr.Recognizer()
    mic = sr.Microphone()

    # כיול לרעשי רקע
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("מוכן להאזין. דבר...")

    while True:
        try:
            with mic as source:
                print("מאזין...")
                audio = r.listen(source)
                print("מזהה את הדיבור...")
            
            # זיהוי הדיבור (Google) והגדרה לשפה עברית
            text = r.recognize_google(audio, language='he-IL')
            
            # כותבים את הטקסט החדש לסוף הקובץ (append) עם ירידת שורה
            with open("pankas.txt", "a", encoding="utf-8") as f:
                f.write(text + "\n")

            print(f"הטקסט שהתקבל: {text}")

        except sr.UnknownValueError:
            print("לא זוהה דיבור ברור, נסה שוב...")
        except sr.RequestError as e:
            print(f"שגיאה בבקשה לשירות הזיהוי: {e}")

if __name__ == "__main__":
    main()
