import cv2
video=cv2.VideoCapture(0)
b=0
g=0
r=0
while True:
    cyan=0
    magenta=0
    white=0
    gray=0
    black=0
    blue=0
    red=0
    green=0
    yellow=0
    color=''
    val,frame=video.read()
    if not val:
        break

    row, col, ch = frame.shape
    mask = frame[row //2-100:row // 2+100, col // 2-100:col // 2+100]
    frame=cv2.medianBlur(frame,25)
    frame[row // 2-100:row // 2+100, col // 2-100:col // 2+100] = mask
    rm, cm ,ch= mask.shape
    for i in range(rm):
        for j in range(rm):
            [b,g,r]=mask[i,j]
            if b==g and g==r and (g >50 and g<220):
                gray+=1
            elif b>100 and g>200 and r<20 :
                cyan+=1
            elif b>220 and g>220 and r>220 and b==r==g:
                white+=1
            elif b<50 and g<50 and r<50 and b==r==g:
                black+=1
            elif b>100 and g<60 and r>100 :
                magenta+=1
            elif b>50 and g<50 and r<50:
                blue+=1
            elif b<40 and g<40 and r>100:
                red+=1
            elif b<30 and g>100 and r>100:
                yellow+=1
            elif b<150 and g>240 and r<30:
                green+=1
    if cyan>500:
        color='Cyan'
        font_c=(110, 110, 50)
    elif white>500:
        color='white'
        font_c = (255, 255, 255)
    elif gray>500:
        color='gray'
        font_c = (150, 150,150)
    elif black>500:
        color='black'
        font_c = (0, 0, 0)
    elif magenta>500:
        color='magenta'
        font_c = (100, 0, 100)
    elif blue>500:
        color='blue'
        font_c = (200, 0, 0)
    elif red>500:
        color='red'
        font_c = (0, 0, 200)
    elif yellow>500:
        color='yellow'
        font_c = (0, 200, 200)
    elif green>500:
        color='green'
        font_c = (0, 200, 0)

    cv2.putText(frame, color, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, font_c, 2)
    cv2.imshow('', frame)
    cv2.waitKey(1)
