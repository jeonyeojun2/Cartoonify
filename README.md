# 🎨 Cartoonify: 이미지를 만화 스타일로 변환하기

## 📌 소개

- Cartoonify는 OpenCV를 활용하여 이미지를 만화 스타일로 변환하는 간단한 이미지 처리 프로젝트입니다.  
- 이 알고리즘은 양방향 필터링, 엣지 검출, 적응형 임계값 처리(adaptive thresholding)를 적용하여 만화 같은 효과를 구현합니다.

## ✨ 기능

✅ 이미지를 만화 스타일로 변환  
✅ 양방향 필터링을 사용하여 색상을 부드럽게 하면서도 엣지를 유지  
✅ 적응형 임계값 처리를 통해 엣지를 감지하고 윤곽을 강조 

## 📷 데모

### ✅ 만화 스타일 변환이 잘 된 이미지:

- 엣지가 뚜렷하고 색상이 선명한 이미지가 가장 좋은 결과를 보입니다.

- 예제🌸
<img src="https://github.com/user-attachments/assets/160c2f39-e66e-4a7a-afdd-3b393e5c0a63" width="400" height="400"/>
  &rarr;
<img src="https://github.com/user-attachments/assets/2684912b-0073-4cc3-afae-7353356febe8" width="400" height="400"/>

### ❌ 만화 스타일 변환이 잘 안 된 이미지:

- 너무 어둡거나 밝은 이미지는 효과가 잘 적용되지 않을 수 있습니다.

- 흐릿한 이미지는 엣지 디테일이 부족하여 효과가 떨어집니다.

- 예제🌳 🧑‍🔬  
<img src="https://github.com/user-attachments/assets/5853038d-5f68-4c36-b797-6f224366bb64" width="400" height="400"/>  
<img src="https://github.com/user-attachments/assets/f44b6995-6af0-43f1-8dee-4b82a3d78385" width="400" height="400"/>

### ⚠️ 한계점

- 너무 어둡거나 밝은 이미지에서는 변환 효과가 잘 나타나지 않을 수 있습니다.

- 저해상도 이미지는 디테일이 손실될 가능성이 있습니다.

- 일부 이미지에서는 엣지가 뚜렷하지 않아 만화 효과가 부족할 수 있습니다.
