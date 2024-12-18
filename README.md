
---

#### **3. 코드 리팩토링 및 정리**
1. **불필요한 파일 제거**:
   - `__init__.py` 파일들이 잘못된 인코딩으로 생성되었던 문제를 정리했으니, 불필요한 내용이 남아있지 않은지 확인.

2. **코드 포매팅**:
   - **프론트엔드**: Prettier 적용.
     ```bash
     npm install --save-dev prettier
     npx prettier --write .
     ```
   - **백엔드**: Black 적용.
     ```bash
     pip install black
     black app/
     ```

3. **주석 추가**:
   - 주요 함수와 라우트에 간단한 설명 주석을 추가하세요.

---

### **마무리 점검**
1. **백엔드와 프론트엔드 연결 테스트 확인** ✅
2. **GitHub에 커밋 및 푸시**:
   ```bash
   git add .
   git commit -m "Day 1: Backend-Frontend setup and API connection test"
   git push
