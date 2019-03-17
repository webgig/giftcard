import {apiUrl,authHeader,handleResponse} from "../helpers/ApiHelper"

// Handles user auth & token rertrieval
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

// Handles logout
const logout = () => {
    localStorage.removeItem('user');
}

// Retrieves current user's profile
const getMe = async() => {
    let user = JSON.parse(localStorage.getItem('user'));

    if (user && user.user_id) {
        const requestOptions = {
            method: 'GET',
            headers: authHeader()
        };

        let response = await fetch(`${apiUrl}/me/`, requestOptions);
        let user =  handleResponse(response);
        return user;
    }
}

const UserService = {
    login,
    logout,
    getMe
}


export default UserService;