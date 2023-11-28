import cv2

###################################################################################

#배경 변경 함수
def changeBackground(mask, frame): 
    if back1_check:   # 배경을 이미지1로 변경
        cv2.copyTo(back1, mask, frame)
        textOption(frame, "Background: 1", 3)

    elif back2_check: # 배경을 이미지2로 변경
        cv2.copyTo(back2, mask, frame)
        textOption(frame, "Background: 2", 3)

    elif back3_check: # 배경을 이미지3로 변경
        ret2, back3Frame = back3.read() # 이미지3(영상) 불러오기
        back3Frame = cv2.resize(back3Frame, dsize=(800, 600), interpolation=cv2.INTER_LINEAR) # 영상과 배경 크기 같게 조정
        
        # 영상 끝나면 처음으로 돌아감
        if(back3.get(cv2.CAP_PROP_POS_FRAMES) == back3.get(cv2.CAP_PROP_FRAME_COUNT)):
            back3.open(videoFile1)
    
        cv2.copyTo(back3Frame, mask, frame)  # 영상을 배경으로 출력
        textOption(frame, "Background: 3", 3)

# 크로마키 배경 인식 함수
def sensingBack(frame): 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # HSV로 크로마키 색 인식 할 때 쓸 변수

    if func1_check:   # 인식할 크로마키 색: 초록색
        mask = cv2.inRange(hsv, (45, 50, 0), (75, 255, 255))  # 영상, 최솟값, 최댓값
        textOption(frame, "Chromakey: Green", 2)

    elif func2_check: # 인식할 크로마키 색: 검은색
        mask = cv2.inRange(frame, (0, 0, 0), (60, 60, 60))   # 영상, 최솟값, 최댓값
        textOption(frame, "Chromakey: Black", 2)

    elif func3_check: # 인식할 크로마키 색: 파란색
        mask = cv2.inRange(hsv, (90, 130, 0), (120, 255, 255)) # 영상, 최솟값, 최댓값
        textOption(frame, "Chromakey: Blue", 2)
    
    elif func4_check: # 인식할 크로마키 색: 흰색
        mask = cv2.inRange(hsv, (0, 0, 190), (255, 60, 255)) # 영상, 최솟값, 최댓값
        textOption(frame, "Chromakey: White", 2)

    return mask

# 텍스트 입력 함수 // 위치: 1 or 2 or 3 // 1:ON/OFF 2:크로마키색 3:배경
def textOption(frame, string, pos):
    frame = cv2.putText(frame,string, (10,pos*20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

############################################################################################

# 웹캠에서 영상 불러오기
cap1 = cv2.VideoCapture(0)

# 바꿀 배경 사진, 배경 영상 불러오기
back1 = cv2.imread('./image/back1.jpg')
back2 = cv2.imread('./image/back2.jpg')
videoFile1 = './video/back3.mov'
back3 = cv2.VideoCapture(videoFile1)

# 프레임 간 시간 간격 설정
fps = round(cap1.get(cv2.CAP_PROP_FPS))
delay = int(1000 / fps)

# 합성 여부 플래그
do_composit = False # False 면 합성을 안함. True면 크로마키 합성
func1_check = True  # 기본값
func2_check = False
func3_check = False
func4_check = False
back1_check = True  # 기본값
back2_check = False
back3_check = False

# 웹캠 영상과 배경 크기 같게 조정
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 689)
back1 = cv2.resize(back1, dsize=(800, 600), interpolation=cv2.INTER_LINEAR)
back2 = cv2.resize(back2, dsize=(800, 600), interpolation=cv2.INTER_LINEAR)

# 전체 동영상 재생
while True: # 무한 루프
    ret1, frame1 = cap1.read() # 웹캠 영상 읽어오기
    ret2, frame2 = cap1.read() # 원본 영상도 띄우기 위해

    textOption(frame1, "[SPACE]: on/off", 27)
    textOption(frame1, "[Q/W/E/R]: chromakey color", 28)
    textOption(frame1, "[Z/X/C]: background type", 29)

    # do_composit 플래그가 True일 때에만 합성
    if do_composit:
        changeBackground(sensingBack(frame1), frame1)
        textOption(frame1, "[ON]", 1)
    else:
        textOption(frame1, "[OFF]", 1)

    cv2.imshow('frame1', frame1)
    cv2.imshow('frame2', frame2)

    # Key 인식
    key = cv2.waitKey(delay)
    # 스페이스바를 누르면 do_composit을 True로 변경
    if key == ord(' '): 
        do_composit = not do_composit
    elif key == 27: # esc 누르면 종료
        break

    if do_composit: # do_composit가 True일 때
        # 인식할 크로마키 색깔 플래그 설정
        if key == ord('q'):
            func1_check = True
            func2_check = func3_check = func4_check = False
        elif key == ord('w'):
            func2_check = True
            func1_check = func3_check = func4_check = False
        elif key == ord('e'):
            func3_check = True
            func1_check = func2_check = func4_check = False
        elif key == ord('r'):
            func4_check = True
            func1_check = func2_check = func3_check = False
        # 배경 색깔 플래그 설정
        if key == ord('z'):
            back1_check = True
            back2_check = back3_check = False
        elif key == ord('x'):
            back2_check = True
            back1_check = back3_check = False
        elif key == ord('c'):
            back3_check = True
            back1_check = back2_check = False
        
cap1.release()
cv2.destroyAllWindows()
