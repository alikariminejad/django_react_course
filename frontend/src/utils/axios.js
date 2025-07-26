import axios from 'axios'


const apiInstance = axios.create({
    baseURL: '127.0.0.1:8000/api/v1/',
    timeout: 20000,
    headers: {
        'Content-Type': "application/json",
        Accept: "application/json",
    },
});

export default apiInstance;