# API
자가진단 앱의 HTTP Request, Response 입니다.<br/>
매크로 만들고 싶은 사람은 쓰삼.<br/>
__대덕소프트웨어마이스터고기준임. 알아서 바꿔서 하셈__
## 유저 찾기
- URI : https://djehcs.eduro.go.kr/v2/findUser
- METHOD : POST
 ```json
{
    "orgCode":"G100000170", // 대마고
    "name":"", // RSA 공개키로 암호화된 이름
    "birthday":"", // RSA 공개키로 암호화된 생일 (yymmdd)
    "stdntPNo":null,
    "loginType":"school"
}
```