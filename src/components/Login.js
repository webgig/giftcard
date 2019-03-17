import React, { Component } from 'react';
import UserService from '../services/UserService';

class LoginPage extends Component {
    constructor(props) {
        super(props);

        UserService.logout();

        this.state = {
            username: '',
            password: '',
            submitted: false,
            loading: false,
            error: ''
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleLogin = this.handleLogin.bind(this);
    }

    handleChange(e) {
        const { name, value } = e.target;
        this.setState({ [name]: value });
    }

    async handleLogin(e){
        e.preventDefault();

        this.setState({ submitted: true });
        const { username, password, returnUrl } = this.state;
        // stop here if form is invalid
        if (!(username && password)) {
            return;
        }

        this.setState({ loading: true });
        UserService.login(username,password)
        .then(
            user => {
                console.log(user);
                const { from } = this.props.location.state || { from: { pathname: "/" } };
                this.props.history.push(from);
            },
            error => this.setState({ error, loading: false })
        );
     
    }

    render() {
       const { username, password, submitted, loading, error } = this.state;

      return (
            
            <form className="form-signin text-center" onSubmit={this.handleLogin}>
              <h2>Prezzee</h2>

              {error && <div className={'alert alert-danger'}>{error}</div> }

              <h1 className="h3 mb-3 font-weight-normal">Please sign in</h1>
              <label htmlFor="inputEmail" className="sr-only">Email address</label>
              <input name="username"  type="text" id="inputEmail" className="form-control" placeholder="Email address" required autoFocus onChange={this.handleChange}/>
              
              <label htmlFor="inputPassword" value="sagar123" className="sr-only">Password</label>
              <input name="password"   type="password" id="inputPassword" className="form-control" placeholder="Password" required onChange={this.handleChange}/>
              
              <button className="btn btn-lg btn-primary btn-block" type="submit"  >Sign in</button>

            </form>
      );
    }
  }
  
  export default LoginPage;