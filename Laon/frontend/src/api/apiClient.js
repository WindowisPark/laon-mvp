import axios from 'axios';

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:8000', // 백엔드 FastAPI 서버 URL
    headers: {
        'Content-Type': 'application/json',
    },
});

export default apiClient;
