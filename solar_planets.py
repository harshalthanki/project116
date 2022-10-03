import cv2

img = cv2.imread("solar-system.jpg")

# cv2.imshow("output",img)

# cv2.waitKey(0)

cv2.putText(
    img,
    "Sun",
    (1,220),
    cv2.FONT_HERSHEY_TRIPLEX,
    1,
    (20,20,20)
    )
cv2.putText(
    img,
    "Mercury",
    (100,260),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (0,0,255)
    )
cv2.putText(
    img,
    "Venus",
    (190,260),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (0,0,255)
    )
cv2.putText(
    img,
    "Earth",
    (280,260),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (0,0,255)
    )
cv2.putText(
    img,
    "Mars",
    (380,260),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (0,0,255)
    )
cv2.putText(
    img,
    "Jupiter",
    (550,380),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (0,0,255)
    )
cv2.putText(
    img,
    "Saturn",
    (750,320),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (0,0,255)
    )
cv2.putText(
    img,
    "Uranus",
    (970,300),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (0,0,255)
    )
cv2.putText(
    img,
    "Neptune",
    (1110,300),
    cv2.FONT_HERSHEY_TRIPLEX,
    0.5,
    (0,0,255)
    )

cv2.imshow("output",img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)