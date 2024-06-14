import cv2 #opencv
import mediapipe as mp

# inicializando o opencv e o mediapipe
webcam = cv2.VideoCapture(1)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    #ler as informações da webcam
    verificador, frame = webcam.read()

    if not verificador:   # se nao conseguir ler a informação da webcam: break
        break

    # reconhecer os rostos dentro dela
    lista_rostos = reconhecedor_rostos.process(frame)

     #desenhar os rostos na imagem
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            desenho.draw_detection(frame, rosto)
    
    cv2.imshow("Rostos", frame)
           
    # quando apertar ESC, o loop para
    if cv2.waitKey(5) == 27:   # 27 == código da tecla ESC
        break

webcam.release()
cv2.destroyAllWindows()