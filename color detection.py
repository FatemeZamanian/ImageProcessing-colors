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

    val,frame=video.read()
    if not val:
        break

    row, col, ch = frame.shape
    mask = frame[row // 10:row // 2, col // 10:col // 2]
    frame=cv2.medianBlur(frame,25)
    frame[row // 10:row // 2, col // 10:col // 2] = mask
    rm, cm ,ch= mask.shape
    for i in range(rm):
        for j in range(rm):
            [b,g,r]=mask[i,j]
            if b==g and g==r and (g >50 and g<220):
                gray+=1
            elif b>70 and g>50 and r<50 :
                cyan+=1
            elif b>220 and g>220 and r>220 and b==r==g:
                white+=1
            elif b<50 and g<50 and r<50 and b==r==g:
                black+=1
            elif b>50 and g<10 and r>250 :
                magenta+=1
            elif b>150 and g<100 and r<50:
                blue+=1
            elif b<30 and g<10 and r>200:
                red+=1
            elif b<30 and g>100 and r>100:
                yellow+=1
            elif b<150 and g>240 and r<30:
                green+=1
    if cyan>300:
        color='Cyan'
    elif white>300:
        color='white'
    elif gray>300:
        color='gray'
    elif black>300:
        color='black'
    elif magenta>300:
        color='magenta'
    elif blue>300:
        color='blue'
    elif red>300:
        color='red'
    elif yellow>300:
        color='yellow'
    elif green>300:
        color='green'

    cv2.putText(frame, color, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (110, 110, 50), 2)
    cv2.imshow('', frame)
    cv2.waitKey(1)
