import UserService from "../services/UserService"

export const apiUrl = "http://localhost:8000/api";

export const authHeader = () => {
    let user = JSON.parse(localStorage.getItem('user'));

    if (user && user.token) {
        return { 'Authorization': 'Token ' + user.token, 'Content-Type': 'application/json' };
    } else {
        return {};
    }
}


export const handleResponse = async(response) => {
    const text = await response.text()
    const data = text && JSON.parse(text);

    if (!response.ok) {
        if (response.status === 401) {
            UserService.logout();
            window.location.reload(true);
        }
        const error = (data && data.non_field_errors)  || response.statusText;

        return Promise.reject(error);
    }
    
    return data;
}

