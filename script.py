import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://github.com/sdkjnksjfskn" # https:// 꼭 붙여야 연결됩니다!
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
colors = ["red", "007cb0"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "김에피")
write("description", "즐거운 학교생활")
write("button", "SURE?")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "자주하는거": "카톡",
  "하고싶은거": "일본가보기",
  "앞으로의 목표": "이학교에 합격하기",
  "진짜 해야하는거": "대회 합격하기"
}
information(informations)