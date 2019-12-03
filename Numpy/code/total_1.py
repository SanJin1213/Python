import cv2
import numpy as np


def video_demo():
    capture = cv2.VideoCapture(0)  # 打开摄像头
    while True:
        ret, frame = capture.read()  # 读取摄像头信息
        frame = cv2.flip(frame, 1)  # 镜像变换
        cv2.imshow("video", frame)  # 读取video
        c = cv2.waitKey(50)
        if c == 27:  # 判断结束条件
            break


def get_image_info(image):
    print(type(image))  # 读取到图片的类型
    print(image.shape)  # 读取图片的高，宽和通道数
    print(image.size)  # 大小
    print(image.dtype)  # 字节位数占多少
    pixel_data = np.array(image)
    print(pixel_data)


print("------------------Hello Python------------------------")
src = cv2.imread("D:/TOFU/github_new/Python/Numpy/images/lining.png")  # imread，是cv22库中读取图片的函数（）中填写所读去图片的位置，最好写绝对位置
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)  # 设置生成的窗口的名字和自动窗口调整大小
cv2.imshow("input image", src)  # imshow,用于显示读取到的图片，并命名读出来的窗口名字
get_image_info(src)
gray = cv2.cv2tColor(src, cv2.COLOR_BGR2GRAY)  # 生成灰度图
cv2.imwrite("D:/TOFU/github_new/Python/Numpy/images/lining_1.png", gray)
video_demo()  # 调用video 函数 使之显示
cv2.waitKey(0)

cv2.destroyAllWindows()
