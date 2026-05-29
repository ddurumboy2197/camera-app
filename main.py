import cv2

def suratga_olish():
    # Kamera orqali suratga olish uchun kamera yaratamiz
    kamera = cv2.VideoCapture(0)

    # Kamera faol bo'lsa, True qaytaradi, aks holda False
    if kamera.isOpened():
        while True:
            # Kameradan frame olinadi
            frame, frame_matn = kamera.read()

            # Frame ni ekranga chiqarish uchun window yaratamiz
            cv2.imshow('Suratga olish', frame_matn)

            # 'q' tugmasini bosganda dastur tugatiladi
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Kamera yopiladi
        kamera.release()

        # Ekranda chiqarilgan barcha windowlar yopiladi
        cv2.destroyAllWindows()

    else:
        print("Kamera faol emas.")

suratga_olish()
