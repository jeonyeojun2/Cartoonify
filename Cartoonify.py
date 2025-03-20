import cv2
import numpy as np

def cartoonify(image_path):
    # 이미지 로드
    img = cv2.imread(image_path)
    img = cv2.resize(img, (500, 500))  # 크기 조정

    # 양방향 필터 적용 (색을 부드럽게)
    color = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    # 그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 엣지 감지 (Canny 또는 Laplacian)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # 색상과 엣지 결합
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # 결과 출력
    cv2.imshow("Cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return cartoon

# 실행 예시
cartoonify("image_flower.png")