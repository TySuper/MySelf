from MyQR import myqr
import os
import getpath

path = getpath.get_path()
myqr.run(
    # 扫描二维码后，显示的内容，或是跳转的链接
    words='https://github.com',
    # 设置容错率。
    version=5,
    # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    level='H',
    # 图片所在目录，可以是动图
    picture='../localImage/abc.png',
    # 黑白(False)还是彩色(True)
    colorized=True,
    # 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0。
    contrast=1.0,
    # 用来调节图片的亮度，用法同上。
    brightness=1.0,
    # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    save_name='3.png'
)
