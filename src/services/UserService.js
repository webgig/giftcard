import {apiUrl,authHeader,handleResponse} from "../helpers/ApiHelper"


const login = async(username, password) => {

    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    };

    let response = await fetch(`${apiUrl}/auth/`, requestOptions);
    let user = await handleResponse(response);

    if (user) {
        localStorage.setItem('user', JSON.stringify(user));
    }
    return user;
}   

const logout = () => {
    localStorage.removeItem('user');
}



const getMe = async() => {
    let user = JSON.parse(localStorage.getItem('user'));
    
    if (user && user.user_id) {
        const requestOptions = {
            method: 'GET',
            headers: authHeader()
        };
        return fetch(`${apiUrl}/me/`, requestOptions).then(handleResponse);
    }
}

const UserService = {
    login,
    logout,
    getMe
}


export default UserService;