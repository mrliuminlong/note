import pygame  # pip install pygame
import time

# 貌似只能播放单声道音乐，可能是pygame模块限制
def playMusic(filename, loops=1, start=0.0, value=0.8):
    """
    :param filename: 文件名
    :param loops: 循环次数
    :param start: 从多少秒开始播放
    :param value: 设置播放的音量，音量value的范围为0.0到1.0
    :return:
    以流的形式因此用while循环
    """
    flag = False  # 是否播放过
    pygame.mixer.init()  # 音乐模块初始化
    while 1:
        if flag == 0:
            pygame.mixer.music.load(filename)
            # pygame.mixer.music.play(loops=1, start=0.0) loops和start分别代表重复的次数和开始播放的位置。
            pygame.mixer.music.play(loops=loops, start=start)
            pygame.mixer.music.set_volume(value)  # 来设置播放的音量，音量value的范围为0.0到1.0。
        if pygame.mixer.music.get_busy() == True:
            flag = True
        else:
            if flag:
                pygame.mixer.music.stop()  # 停止播放
                break

filename = '/home/tarena/aid1811/python_net/practise/music/蓝莲花 - 许巍.mp3'                
playMusic(filename)



# pygame.mixer.init()
# print("播放音乐")
# track = pygame.mixer.music.load(filename)
# pygame.mixer.music.load(filename)
# time.sleep(50)
# pygame.mixer.music.stop()


