import axios from 'axios';

async function getUser() {
    try {
        const response = await axios.get('http://localhost:8000/api/auth/users/me/');
        console.log(response);
    } catch (e) {
        console.error(e);
    }
}

export { getUser };
