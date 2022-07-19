# Community-Project
python/django를 이용한 온라인 커뮤니티 제작

## 💡 Background

Python/Django를 이용하여 기본적인 CRUD기능을 가진 게시판을 구현해보기 위하여 진행한 프로젝트입니다.

# 🛠 Development

## Tech Stack

- HTML/CSS
- Bootstrap
- Python
- Django
- SQLite
- Git, Github

# Features & Screens

## Home

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/97ca5180-5a10-4de8-a5f6-9531fddb8d65/Untitled.png)

- 메인 페이지입니다.
- 위 화면은 로그인하지 않았을 경우에 보여주는 화면입니다. 로그인을 하고 나면 아래 화면처럼 환영합니다 문구를 보이도록 하였습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ca7acdd6-ad19-4829-aefb-981dec5cdb97/Untitled.png)

## 회원가입

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6e621890-f986-4117-bba8-169dfd4ea1a7/Untitled.png)

- 회원가입 페이지입니다.
- 이미 존재하고 있는 회원 정보라면 이미 아이디가 존재한다는 내용이 뜨도록 에러처리 해두었습니다.
- 비밀번호와 비밀번호 확인이 다르다면 회원가입할 수 없도록 하였습니다.

## 로그인

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/13e576b4-8880-435c-9fe5-079645192adb/Untitled.png)

- 로그인을 진행하는 페이지입니다.
- 존재하지 않는 회원 정보라면 아이디가 없다는 내용이 뜨도록 에러처리 해두었습니다.

## 게시판

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e4a29c04-1585-40b3-a1aa-103187c42672/Untitled.png)

- 회원들의 글들을 조회할 수 있는 게시판입니다.
- 모든 회원들의 글을 조회할 수 있도록 하였으며 회원이 아니더라도 볼 수 있도록 설정하였습니다.
- Pagination을 하여 한 페이지에 15개의 글이 보이도록 설정해두었습니다.

## 게시글 세부 보기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0dd19783-b0f0-4060-9ced-65fc70aaca17/Untitled.png)

- 회원들의 글을 세부하게 볼 수 있는 페이지입니다.
- 회원의 글에 대한 댓글을 달 수 있는 기능이 있습니다.
- 글의 세부 내용을 보기 위해서는 로그인을 해야만 하도록 권한 설정을 해두었습니다.
- 수정하기와 삭제하기는 글을 쓴 당사자일 경우에만 가능하도록 해두었으며 만약 다른 회원일 경우에는 밑의 화면처럼 버튼이 보이지 않도록 하였습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/618edbf1-f0dc-45be-93d3-4eebd7584925/Untitled.png)

## 마이 페이지

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/30b3f13f-0be1-4bce-9226-280c85311d51/Untitled.png)

- 마이 페이지입니다.
- 마이 페이지에서는 사용자가 지금까지 작성한 게시글을 볼 수 있습니다.
