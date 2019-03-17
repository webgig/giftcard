import React from 'react';
import { Link } from 'react-router-dom';

import UserService from '../services/UserService';
import CardService from '../services/CardService';

import Cards from '../components/Cards'

class HomePage extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            user: {},
            cards: []
        };
    }

    // Load User and Card
    async componentDidMount() {
        this.setState({ 
            user: JSON.parse(localStorage.getItem('user'))
        });

        let user = await UserService.getMe();
            user = user[0];
        let cards = await CardService.getMyCards();
        
        this.setState({ user,cards });
    }

    render() {
        const { user,cards } = this.state;
        return (
            <div>
                <header className="navbar navbar-dark bg-dark shadow-sm">
                    <div className="container d-flex justify-content-between">
                        <a href="#" className="navbar-brand d-flex align-items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" aria-hidden="true" className="mr-2" viewBox="0 0 24 24" focusable="false"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
                            <strong>Prezzee</strong>
                        </a>
                        {user.username && <strong className="text-right text-white">hi {user.username}</strong>}<Link to="/login">Logout</Link>
                    </div>
                </header>
                <div className="album py-5 bg-light">
                
                    <Cards param="test" cards={cards}></Cards>
                </div>
            </div>
        );
    }
}

export { HomePage };