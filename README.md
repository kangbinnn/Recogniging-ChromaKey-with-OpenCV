# recogniging-chroma-key--with-openCV

// 프로젝트 개요 //

오류를 없애기 위해서 웹캠 출력화면의 크기와, 배경 이미지의 크기를 똑같이 맞춤
웹캠의 영상을 읽어옴
스페이스바를 눌렀을 때 크로마키 색 인식을 시작함
cv2.cvtColor()를 사용해서 웹캠 이미지의 색 정보를 가져옴.
cv2.inRange()를 이용해서 특정색을 추출하여 마스크를 만듬.
cv2.copyTo()를 이용해서 배경,마스크,웹캠 이미지를 합침.
특정 키(q,w,e,r,z,x,c)를 눌러서 인식할 크로마키 색이나 배경을 변경함.
textOption() 함수를 만들어 웹캠 화면에 텍스트를 입력함.

// 이미지, 영상 //

1. 배경1 : https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/c9df6eec-1dd1-4a7f-a70f-9dea50e05ee7

2. 배경2 : https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/571100eb-6e62-4a27-a8b6-1d701d56d2a0

3. 배경3 (mp4) : https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/ea958eeb-63fa-48df-8180-209784336961

4. 검은색 크로마키 : https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/7a6b44ab-f71b-4950-8201-8f7b0ec948ce

5. 흰색 크로마키 : https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/4f02adab-6d0e-4885-81a3-854db8d9f4e4

6. 꺼진 상태 : https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/268b1cd8-46af-4211-b2f3-68425f58e6f7

7. 전체 기능(gif) : https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/85e0631f-ee8f-49d7-88e5-3a163a81eaaa

// 사용한 패키지 //

python 3.11.5 
openCV 4.8.1
 
// 실행방법 //

코드 실행 후 스페이스 바를 누르면 크로마키 색 인식 시작. 
q,w,e,r로 인식할 크로마키 색깔 변경.
z,x,c로 배경 이미지 변경.
esc 눌러서 종료.

// 한계 //

어두울 때는 색 인식을 잘 하지 못함.

// 참고자료 //

https://deep-learning-study.tistory.com/134
