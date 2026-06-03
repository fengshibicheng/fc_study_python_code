# from PIL import Image, ImageDraw
#
# # 创建空白画布
# width, height = 800, 600
# image = Image.new("RGB", (width, height), color="white")
# draw = ImageDraw.Draw(image)
#
# # 绘制线条
# draw.line([(100, 100), (700, 500)], fill="black", width=5)
#
# # 绘制矩形
# # draw.rectangle([(200, 200), (600, 400)], outline="red", width=3, fill="yellow")
# draw.rectangle([(200, 200), (600, 400)], outline="red", width=3)
#
# # 绘制椭圆
# draw.ellipse([(300, 150), (500, 350)], outline="blue", width=3, fill="lightblue")
#
# # 绘制圆形
# draw.ellipse([(550, 50), (650, 150)], outline="green", width=2, fill="lightgreen")
#
# # 绘制多边形
# draw.polygon([(100, 500), (300, 450), (500, 550), (250, 600)],
#              outline="purple", fill="lavender")
#
# # 绘制圆弧
# draw.arc([(400, 400), (600, 500)], start=0, end=180, fill="orange", width=3)
#
# # 绘制点
# for i in range(50):
#     import random
#     x = random.randint(0, width)
#     y = random.randint(0, height)
#     draw.point((x, y), fill="black")
#
# image.save("drawings.png")

# ****************************************************************************************************
# ****************************************************************************************************
# ****************************************************************************************************
# ****************************************************************************************************
# ****************************************************************************************************
from PIL import Image, ImageDraw
import math

# 创建空白画布
width, height = 800, 800
image = Image.new("RGB", (width, height), color="white")
draw = ImageDraw.Draw(image)


# 绘制星形
def draw_star(draw, center, points=5, outer_radius=100, inner_radius=50, rotation=0, **kwargs):
    """绘制星形

    参数:
        center: 中心点坐标元组 (x, y)
        points: 星星的角数
        outer_radius: 外圆半径
        inner_radius: 内圆半径
        rotation: 旋转角度（度）
        **kwargs: 传递给 polygon() 的参数
    """
    cx, cy = center
    angle = math.pi / points
    rotation_rad = math.radians(rotation)

    vertices = []
    for i in range(2 * points):
        radius = outer_radius if i % 2 == 0 else inner_radius
        theta = i * angle + rotation_rad
        x = cx + radius * math.sin(theta)
        y = cy - radius * math.cos(theta)
        vertices.append((x, y))

    draw.polygon(vertices, **kwargs)


# 绘制星星
draw_star(draw, center=(200, 200), fill="gold", outline="orange", width=2)
draw_star(draw, center=(500, 200), points=8, rotation=22.5,
          outer_radius=120, inner_radius=40, fill="blue", outline="navy", width=2)


# 绘制心形
def draw_heart(draw, center, size=100, **kwargs):
    """绘制心形

    参数:
        center: 中心点坐标元组 (x, y)
        size: 心形大小
        **kwargs: 传递给 polygon() 的参数
    """
    cx, cy = center
    vertices = []
    for t in range(100):
        angle = t / 100 * 2 * math.pi
        x = 16 * math.sin(angle) ** 3
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
        # 缩放和平移
        vertices.append((cx + x * size / 16, cy - y * size / 16))

    draw.polygon(vertices, **kwargs)


draw_heart(draw, center=(200, 500), size=150, fill="red", outline="darkred", width=3)


# 绘制螺旋
def draw_spiral(draw, center, loops=3, radius_start=5, radius_end=100, points=500, **kwargs):
    """绘制螺旋

    参数:
        center: 中心点坐标元组 (x, y)
        loops: 螺旋的圈数
        radius_start: 起始半径
        radius_end: 结束半径
        points: 点的数量
        **kwargs: 传递给 line() 的参数
    """
    cx, cy = center
    vertices = []

    for i in range(points + 1):
        # 计算当前角度和半径
        angle = i / points * loops * 2 * math.pi
        radius = radius_start + (radius_end - radius_start) * i / points

        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        vertices.append((x, y))

    # 绘制折线
    for i in range(len(vertices) - 1):
        draw.line([vertices[i], vertices[i + 1]], **kwargs)


draw_spiral(draw, center=(500, 500), loops=5, fill="purple", width=2)

image.save("complex_shapes.png")