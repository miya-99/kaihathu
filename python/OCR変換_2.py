from PIL import Image, ImageOps
import pyocr
import pyocr.builders
import sys

file_path = 'C:/Users/29004/Desktop/キャプチャ.png'
# ツール読み込み
tools = pyocr.get_available_tools()
# ツールが見付からない場合
if len(tools) == 0:
    print('pyocrが見付かりません。pyocrをインストールして下さい。')
    sys.exit(1)
tool = tools[0]
# 画像読み込み
img_org = Image.open(file_path)
# 背景色と文字色を反転（白文字→黒文字へ変換）
max_medals_img = ImageOps.invert(img_org.convert('RGB'))
# OCR
max_medals = tool.image_to_string(max_medals_img, lang='eng', builder=pyocr.builders.DigitBuilder(tesseract_layout=6))
print(f'max_medals:{max_medals}')