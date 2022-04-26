# Back-end
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-360/)

**Back-end**는 REST API 서버를 구현한 프로젝트입니다.

## Tables

* [Prerequisites](#prerequisites)
* [API service](#api-service)

## Prerequisites
프로젝트를 실행시키기 위해 필요한 소프트웨어.

### Install:
- [Docker](https://docs.docker.com/get-docker/)
- [Python 3.9+ (pip)](https://www.python.org/)
- [docker-compose](https://docs.docker.com/compose/install/)

## API service
### Example:
- User 로그인
```
[POST] http://localhost/auth/login
```

- User 회원가입
```
[POST] http://localhost/auth/register
```

- User JWT decode
```
[GET] http://localhost/auth
```

- Workspace Create
```
[POST] http://localhost/workspace
```

- Workspace Read
```
[GET] http://localhost/workspace/<int:workspaceid>
```

- Workspace Update
```
[PUT] http://localhost/workspace/<int:workspaceid>
```

- Workspace Delete
```
[DELETE] http://localhost/workspace/<int:workspaceid>
```
