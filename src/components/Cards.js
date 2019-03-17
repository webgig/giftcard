import React, { Component } from 'react';
import CardService from '../services/CardService';

class Cards extends Component {
    constructor(props) {
        super(props);
        this.state = {
            archived: false,
            cards: []
        }
    }

    
    showArchived(){
        let archived = false;

        if(this.state.archived)
            archived = false;
        else
            archived = true;

        this.setState({ archived:archived });
    }

    async archive(id,card){
        let cards = [...this.state.cards];
        let index = cards.findIndex(card => card.id == id);
        
        cards[index] = await CardService.archive(card.id,!card.archived);
        this.setState({ cards: cards });
    }
    componentWillReceiveProps(nextProps){
       this.setState({cards: nextProps.cards})
    }

    render() {
        const { cards } = this.state;

        const cardsNew = cards.filter((card) => {
            return card.archived == this.state.archived ;
        })

    
        return (
            <div className="container">
                <button type="button" className="btn btn-primary my-2" data-toggle="button" aria-pressed="false" onClick={this.showArchived.bind(this)}> View Archived Cards</button>
                

                {cardsNew.length > 0 &&
                    <div className="row">
                            {cardsNew.map((card, index) =>
                             
                                <div className="col-md-4" key={index}>
                                    <div className="card mb-4 shadow-sm">
                                        <svg className="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"> 
                                            <rect width="100%" height="100%" fill="#55595c"></rect>
                                            <text x="40%" y="50%" fill="#eceeef" dy=".3em">{card.title}</text>
                                        </svg>
                                        <div className="card-body">
                                            {this.state.archived && 
                                                <h6><span className="badge badge-secondary">Archived</span></h6>
                                            }
                                            <div className="card-text">
                                                <p>{card.description}</p>
                                                <small><strong>AUD  {card.value}</strong></small>
                                            </div>
                                            <div className="d-flex justify-content-between align-items-center">
                                                <div className="btn-group">
                                                    <button onClick={this.archive.bind(this,card.id,card)} type="button" className="btn btn-sm btn-outline-secondary">{this.state.archived? "Unarchive":"Archive"}</button>
                                                </div>
                                            
                                                <small className="text-muted"><strong>Voucher</strong> {card.voucher}</small>
                                                <small className="text-muted"><strong>Pin</strong>{card.voucher}</small>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                )}
                    </div>
                }
            </div>
        );
    }
}


export default Cards;