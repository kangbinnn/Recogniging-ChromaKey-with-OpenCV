import cv2

# 웹캠에서 영상 불러오기
cap1 = cv2.VideoCapture(0)

# 바꿀 배경 사진, 배경 영상 불러오기
back1 = cv2.imread('./image/room.png')

# 프레임 간 시간 간격 설정
fps = round(cap1.get(cv2.CAP_PROP_FPS))
delay = int(1000 / fps)

# 합성 여부 플래그
do_composit = False # False 면 합성을 안함. True면 크로마키 합성

# 웹캠 영상과 배경 크기 같게 조정
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 689)
back1 = cv2.resize(back1, dsize=(800, 600), interpolation=cv2.INTER_LINEAR)

# 전체 동영상 재생
while True: # 무한 루프
    ret1, frame1 = cap1.read() # 웹캠 영상 읽어오기
    ret2, frame2 = cap1.read() # 원본 영상도 띄우기 위해

    # do_composit 플래그가 True일 때에만 합성
    if do_composit:
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (45, 50, 0), (75, 255, 255))
        cv2.copyTo(back1, mask, frame1)

    cv2.imshow('frame1', frame1)
    cv2.imshow('frame2', frame2)

    # Key 인식
    key = cv2.waitKey(delay)
    # 스페이스바를 누르면 do_composit을 True로 변경
    if key == ord(' '): 
        do_composit = not do_composit
    elif key == 27: # esc 누르면 종료
        break
        
cap1.release()
cv2.destroyAllWindows()