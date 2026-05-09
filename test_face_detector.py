import cv2
from face_detector import detect_face

img = cv2.imread("test.jpeg")

if img is None:
    print("Image not found")
    exit()

print("Image loaded successfully")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

face = detect_face(img_rgb)

if face is None:
    print("No face detected")
else:

    print("Face detected")

    cv2.imshow(
        "Detected Face",
        cv2.cvtColor(face, cv2.COLOR_RGB2BGR)
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()