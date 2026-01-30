# Healthcare Backend API (FastAPI)
의료 서비스 환경을 가정하여 환자 관리 기능을 제공하는 백엔드 API를 FastAPI와 PostgreSQL로 구현한 프로젝트다.
단순 CRUD 구현이 아닌, Layered Architecture(Controller-Service-Repository) 구조를 적용하여 확장성과 유지보수를 고려한 설계를 목표로 한다.



# 프로젝트 목적
- 헬스케어/의료 서비스 백엔드의 기본 구조 이해
- Rest API 요청-응답 흐름 이해
- MSO(병의원 통합 운영 플랫폼) 형태의 서비스 확장을 위한 설계

# 아키텍처
```
Client
  ↓
Router (Controller)
  ↓
Service (Business Logic)
  ↓
Repository (DB Access)
  ↓
PostgreSQL
```

| 레이어     | 역할            |
| ---------- | ------------- |
| Router     | HTTP 요청/응답 처리 |
| Service    | 비즈니스 로직 관리    |
| Repository | 데이터베이스 접근     |
| Schema     | 요청/응답 데이터 검증  |

# 기술 스택
- __Language__: Python 3.13.1
- __Framework__: FastAPI
- __ORM__: SQLAlchemy
- __Database__: PostgreSQL
- __Validation__: Pydantic
- __Server__: Uvicorn

# 구현 기능
## 환자 관리 API
| Method | Endpoint    | Description |
| ------ | ----------- | ----------- |
| GET    | `/patients` | 환자 목록 조회    |
| POST   | `/patients` | 환자 등록       |

# 프로젝트 구조
```
app/
 ┣ routers/
 ┃ ┗ patient.py
 ┣ services/
 ┃ ┗ patient_service.py
 ┣ repositories/
 ┃ ┗ patient_repository.py
 ┣ models/
 ┃ ┗ patient.py
 ┣ schemas/
 ┃ ┗ patient.py
 ┣ database.py
 ┗ main.py
```

# 실행 방법
```
# 가상환경 생성
python -m venv venv
source venv/Scripts/activate

# 패키지 설치
pip install -r requirements.txt

# 서버 실행
uvicorn app.main:app --reload
```

# 향후 개선 예정
- 환자 목록 페이지네이션
- 병원 엔티티 추가 (MSO 구조)
- 인증/인가(JWT) 적용
- 테스트 코드(Pytest) 작성
- Docker 기반 배포 환경 구성
