# recogniging-chroma-key--with-openCV

// 프로젝트 //  
크로마키 색을 인식해서 다양한 배경으로 바꾸는 openCV 프로젝트이다. 특정 키를 눌러서 인식할 크로마키 색깔을 변경할 수 있고, 어떤 배경으로 바꿀지도 변경할 수 있다.

// 프로젝트 개요 //

오류를 없애기 위해서 웹캠 출력화면의 크기와, 배경 이미지의 크기를 똑같이 맞춤  

웹캠의 영상을 읽어옴  

스페이스바를 눌렀을 때 크로마키 색 인식을 시작함.  

cv2.cvtColor()를 사용해서 웹캠 이미지의 색 정보를 가져옴.  

cv2.inRange()를 이용해서 특정색을 추출하여 마스크를 만듬.  

cv2.copyTo()를 이용해서 배경,마스크,웹캠 이미지를 합침.  

특정 키(q,w,e,r,z,x,c)를 눌러서 인식할 크로마키 색이나 배경을 변경함.  

textOption() 함수를 만들어 웹캠 화면에 텍스트를 입력함.  

// 이미지, 영상 //

1. 배경1 : ![배경1](https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/e1d0a38c-a30d-4aa2-9033-86a3f969dd26)

2. 배경2 : ![배경2](https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/af4b838c-7632-4ebd-9e77-95d89c2e8ac8)

3. 배경3 (.gif) :


![배경 3](https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/cf9e867b-27fa-4f31-b0ff-c2d6cbd39337)

4. 검은색 크로마키 : ![검은색크로마키](https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/435628dc-bdbb-4abd-ac14-b4919e42fed7)

5. 흰색 크로마키 : ![흰색크로마키](https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/c3e7ee42-309d-480c-b0e1-f0299e66b8e1)

6. 꺼진 상태 : ![꺼진상태](https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/268b1cd8-46af-4211-b2f3-68425f58e6f7)

7. 전체 기능(.gif) :


![전체기능](https://github.com/kangbinnn/Recogniging-ChromaKey-with-OpenCV/assets/143775863/85e0631f-ee8f-49d7-88e5-3a163a81eaaa)  

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
