import http from 'k6/http';

export let options = {
    vus: 10000,
    duration: '1m'
};

export default () => http.patch(`http://localhost:8000/api/v1/messages/push`);
