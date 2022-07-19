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

![1](https://user-images.githubusercontent.com/68835451/179648467-5a0b67a9-a960-4340-9c89-c44db85a291c.jpg)

- 메인 페이지입니다.
- 위 화면은 로그인하지 않았을 경우에 보여주는 화면입니다. 로그인을 하고 나면 아래 화면처럼 환영합니다 문구를 보이도록 하였습니다.

![2](https://user-images.githubusercontent.com/68835451/179648469-6157c642-02ba-4d72-b5d7-1441c0bcf05e.jpg)

## 회원가입

![3](https://user-images.githubusercontent.com/68835451/179648470-ddd150aa-8948-419d-ba72-739a518b7944.jpg)

- 회원가입 페이지입니다.
- 이미 존재하고 있는 회원 정보라면 이미 아이디가 존재한다는 내용이 뜨도록 에러처리 해두었습니다.
- 비밀번호와 비밀번호 확인이 다르다면 회원가입할 수 없도록 하였습니다.

## 로그인

![4](https://user-images.githubusercontent.com/68835451/179648472-cffab59b-0d81-4b22-ae34-5ba5d55cd1de.jpg)

- 로그인을 진행하는 페이지입니다.
- 존재하지 않는 회원 정보라면 아이디가 없다는 내용이 뜨도록 에러처리 해두었습니다.

## 게시판

![5](https://user-images.githubusercontent.com/68835451/179648474-eb605cc4-4019-4364-bd91-b4eac8217387.jpg)

- 회원들의 글들을 조회할 수 있는 게시판입니다.
- 모든 회원들의 글을 조회할 수 있도록 하였으며 회원이 아니더라도 볼 수 있도록 설정하였습니다.
- Pagination을 하여 한 페이지에 15개의 글이 보이도록 설정해두었습니다.

## 게시글 세부 보기

![6](https://user-images.githubusercontent.com/68835451/179648463-261a8871-ce46-4c91-bd4f-0308f29cca30.jpg)

- 회원들의 글을 세부하게 볼 수 있는 페이지입니다.
- 회원의 글에 대한 댓글을 달 수 있는 기능이 있습니다.
- 글의 세부 내용을 보기 위해서는 로그인을 해야만 하도록 권한 설정을 해두었습니다.
- 수정하기와 삭제하기는 글을 쓴 당사자일 경우에만 가능하도록 해두었으며 만약 다른 회원일 경우에는 밑의 화면처럼 버튼이 보이지 않도록 하였습니다.

![7](https://user-images.githubusercontent.com/68835451/179648465-f8c148f0-1d48-40f5-a786-d0b32d8127d4.jpg)

## 마이 페이지

![8](https://user-images.githubusercontent.com/68835451/179648466-ecddb6c7-a892-4aad-bd36-1d642a6f09ba.jpg)

- 마이 페이지입니다.
- 마이 페이지에서는 사용자가 지금까지 작성한 게시글을 볼 수 있습니다.
