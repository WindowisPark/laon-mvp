import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import apiClient from '../api/apiClient';

const HomeScreen = () => {
    const [status, setStatus] = useState('Loading...');

    useEffect(() => {
        // 백엔드 /health 엔드포인트 호출
        apiClient.get('/health')
            .then(response => setStatus(response.data.status))
            .catch(error => {
                console.error('API 호출 실패:', error);
                setStatus('Error connecting to backend');
            });
    }, []);

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Backend 연결 테스트</Text>
            <Text style={styles.status}>API 응답: {status}</Text>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#fff',
    },
    title: {
        fontSize: 20,
        fontWeight: 'bold',
    },
    status: {
        fontSize: 16,
        color: 'green',
        marginTop: 10,
    },
});

export default HomeScreen;
