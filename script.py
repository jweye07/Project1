import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.google.com/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["black", "white"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "문진위")
write("description", "한울안중학교 3기")
write("button", "구글")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "생일": "10/8",
  "나이": "16",
  "좋아하는 것": "게임",
  "싫어하는 것": "버섯"
}
information(informations)
