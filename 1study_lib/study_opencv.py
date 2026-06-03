import os.path

output_dir = "./output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# import cv2
# import numpy as np
#
# # 读取图像
# image = cv2.imread('study.jpg', cv2.IMREAD_GRAYSCALE)
#
# # 计算 x 方向的梯度
# sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
#
# # 计算 y 方向的梯度
# sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
#
# # 计算梯度幅值
# sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)
#
# # 应用 Laplacian 算子
# canny = cv2.Canny(image, 100, 200)
#
# # 应用 Laplacian 算子
# laplacian = cv2.Laplacian(image, cv2.CV_64F)
#
# # 显示结果
# cv2.imshow('Canny', canny)
# cv2.imshow('Laplacian', laplacian)
#
# # 显示结果
# cv2.imshow('Sobel X', sobel_x)
# cv2.imshow('Sobel Y', sobel_y)
# cv2.imshow('Sobel Combined', sobel_combined)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
#
# # 轮廓检测
# image = cv2.imread('study.jpg')
#
# # 转换为灰度图
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # 二值化处理
# ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#
# # 查找轮廓
# contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
# # 绘制轮廓
# cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
#
# # 显示结果
# cv2.imshow("Contours", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



import cv2

# # 加载 Haar 特征分类器
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 创建 VideoCapture 对象，读取摄像头视频
import numpy as np

cap = cv2.VideoCapture(0)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# 读取视频帧
while True:
    ret, frame = cap.read()

    # 如果读取到最后一帧，退出循环
    if not ret:
        break

    # # 显示当前帧
    # cv2.imshow('Camera', frame)

    # 分离 BGR 通道
    b, g, r = cv2.split(frame)

    # 调整通道强度
    r = np.clip(r * 0.393 + g * 0.769 + b * 0.189, 0, 255).astype(np.uint8)
    g = np.clip(r * 0.349 + g * 0.686 + b * 0.168, 0, 255).astype(np.uint8)
    b = np.clip(r * 0.272 + g * 0.534 + b * 0.131, 0, 255).astype(np.uint8)

    # 合并通道
    vintage_image = cv2.merge((b, g, r))

    # 显示灰度帧
    cv2.imshow('Gray Video', vintage_image)

    # # 进行人脸检测
    # faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    #
    # # 绘制检测结果
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #
    # # 显示结果
    # cv2.imshow('Detected Faces', frame)

    # 按下 'q' 键退出
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()

