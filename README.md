# Laon MVP Project - Phase 1

## 프로젝트 개요
Laon MVP 프로젝트는 감정 분석 및 사용자 맞춤형 수면 백색소음을 제공하는 서비스.  
프론트엔드는 **React Native**, 백엔드는 **FastAPI**를 기반으로 개발.

---

## 프로젝트 구조

```plaintext
backend/
├── app/
│   ├── main.py          # FastAPI 진입점
│   ├── routes/          # API 라우트
│   ├── models/          # 데이터베이스 모델
│   ├── core/            # 설정 및 DB 연결
│   └── __init__.py      # 패키지 인식 파일
└── requirements.txt     # Python 패키지 목록

frontend/
├── src/
│   ├── screens/         # React Native 화면 컴포넌트
│   ├── api/             # Axios API 설정
│   └── styles/          # 스타일 파일
└── App.js               # 진입점
