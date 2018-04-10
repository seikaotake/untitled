import os
import cv2

path_list = ["/Users/seika/Desktop/picture_0",
             "/Users/seika/Desktop/picture_1"]

for path_name in path_list:
    if not os.path.exists(path_name):
        os.mkdir(path_name)

def movie_to_image(num_cut):

    for x in os.listdir('/Users/seika/Desktop/video_0'):
        name = "picture_{}".format(x)
        print(name)
        path1 = os.path.join("/Users/seika/Desktop/picture_0/", name)
        path2 = os.path.join("/Users/seika/Desktop/video_0/", x)

        print(type(path1))   # path2 = キャプチャ動画のパス（ファイル名含む）
        output_path = "/Users/seika/Desktop/picture_0/"  # 出力するフォルダパス

        # キャプチャ動画読み込み（キャプチャ構造体生成）
        capture = cv2.VideoCapture(path2)

        img_count = 0  # 保存した候補画像数
        frame_count = 0  # 読み込んだフレーム画像数

        if not os.path.exists(os.path.join(output_path,x)):
            os.mkdir(os.path.join(output_path,x))

        # フレーム画像がある限りループ
        while(capture.isOpened()):
        # フレーム画像一枚取得
            ret, frame = capture.read()
            if ret == False:
                break

            # 指定した数だけフレーム画像を間引いて保存
            if frame_count % num_cut == 0:
                img_file_name = str(img_count) + ".jpg"
                cv2.imwrite(os.path.join(output_path,x,img_file_name), frame)
                img_count += 1

            frame_count += 1

        # キャプチャ構造体開放
        capture.release()


if __name__ == '__main__':

    # 間引き数を10にしてフレーム画像抽出
    movie_to_image(int(10))


def movie_to_image(num_cut):

    for x in os.listdir('/Users/seika/Desktop/video_1'):
        name = "picture_{}".format(x)
        print(name)
        path3 = os.path.join("/Users/seika/Desktop/picture_1/", name)
        path4 = os.path.join("/Users/seika/Desktop/video_1/", x)

        print(type(path3))
        video_path = path4   # キャプチャ動画のパス（ファイル名含む）
        output_path = "/Users/seika/Desktop/picture_1/"  # 出力するフォルダパス

        # キャプチャ動画読み込み（キャプチャ構造体生成）
        capture = cv2.VideoCapture(video_path)

        img_count = 0  # 保存した候補画像数
        frame_count = 0  # 読み込んだフレーム画像数

        if not os.path.exists(os.path.join(output_path,x)):
            os.mkdir(os.path.join(output_path,x))

        # フレーム画像がある限りループ
        while(capture.isOpened()):
        # フレーム画像一枚取得
            ret, frame = capture.read()
            if ret == False:
                break

            # 指定した数だけフレーム画像を間引いて保存
            if frame_count % num_cut == 0:
                img_file_name = str(img_count) + ".jpg"
                cv2.imwrite(os.path.join(output_path,x,img_file_name), frame)
                img_count += 1

            frame_count += 1

        # キャプチャ構造体開放
        capture.release()


if __name__ == '__main__':

    # 間引き数を10にしてフレーム画像抽出
    movie_to_image(int(10))


