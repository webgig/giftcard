import {apiUrl,authHeader,handleResponse} from "../helpers/ApiHelper"

// Retrieves current user's card
const getMyCards = async() => {

    let user = JSON.parse(localStorage.getItem('user'));
    
    if (user && user.user_id) {
        const requestOptions = {
            method: 'GET',
            headers: authHeader(),
        };
        return fetch(`${apiUrl}/me/cards/`, requestOptions).then(handleResponse);
    }
}

// Archives/Unarchives card
const archive = async(card_id,archive) =>{

    if (card_id){
        const requestOptions = {
            method: 'PATCH',
            headers: authHeader(),
            body:JSON.stringify({archived:archive})

        };

       return await fetch(`${apiUrl}/cards/`+ card_id + '/', requestOptions).then(handleResponse);
    }

}

const CardService = {
    getMyCards,
    archive
}

export default CardService;