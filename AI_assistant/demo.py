import speech_recognition
from gtts import gTTS
import os
from datetime import date, datetime

while True:
    # khởi tạo
    ai_brain = " " # Ban đầu nó chưa được học gì cả nên cũng chưa có thông tin
    ai_ear = speech_recognition.Recognizer() # nghe người dùng nói

    with speech_recognition.Microphone() as mic:
        print("AI: Đang nghe |--___--|")
        audio = ai_ear.record(mic, duration = 5)
        # AI nghe trong vòng 5 giây rồi tắt mic
        print("\nAI: ... ")
    try:
        you = ai_ear.recognize_google(audio, language = 'vi-VN')
        # nghe và nối giọng việt nam
        print("\nNgười sử dụng:  " + you)
    except:
        ai_brain = "Tôi không hiểu bạn nói gì cả ! ..."
        print("\nAI:  " + ai_brain)

    if "Xin chào" in you:
        ai_brain = "Xin chào Bạn."    
    elif "thời tiết" in you:
        ai_brain = "Tôi là máy móc nên chưa biết thời tiết nha."   
    elif "ngày" in you:
        today = date.today()    
        ai_brain = today.strftime("%d/%m/%Y")
    elif "giờ" in you:
        now = datetime.now()
        ai_brain = now.strftime("%H:%M:%S")
    elif "Hẹn gặp lại" in you:
        ai_brain = "Chào tạm biệt và hẹn gặp lại."
        print("\nAI: " + ai_brain)    
        tts = gTTS(text = ai_brain, lang = 'vi')
        #C:\Users\blued\Desktop\AI_assistant
        tts.save("C:\\Users\\blued\\Desktop\\AI_assistant\\ai.mp3")
        os.system("C:\\Users\\blued\\Desktop\\AI_assistant\\ai.mp3")
        exit()
    else:
        ai_brain = "Cảm ơn bạn."     
        print("\nAI: " + ai_brain)   

    print("\nAI: " + ai_brain)

    tts = gTTS(text = ai_brain, lang = 'vi')
    tts.save("C:\\Users\\blued\\Desktop\\AI_assistant\\ai.mp3")
    os.system("C:\\Users\\blued\\Desktop\\AI_assistant\\ai.mp3")