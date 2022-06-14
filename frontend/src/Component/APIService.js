
import axios from "axios";

export default class APIService {

  static UpdateArticle(article_id, body, token) {

    return fetch(`http://127.0.0.1:8000/api/articles/${article_id}/`, {
      'method': 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`
      },
      body: JSON.stringify(body)

    }).then(resp => resp.json())


  }

  static InsertArticle(body, token) {

    return fetch('http://127.0.0.1:8000/api/articles/', {
      'method': 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`
      },
      body: JSON.stringify(body)

    }).then(resp => resp.json())

  }

  static DeleteArticle(article_id, token) {

    return fetch(`http://127.0.0.1:8000/api/articles/${article_id}/`, {
      'method': 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`
      }

    })

  }

  static LoginUser(body) {
    console.log(body)
    return fetch('http://127.0.0.1:8000/auth/token/login/', {
      'method': 'POST',
      headers: {
        'Content-Type': 'application/json',

      },
      body: JSON.stringify(body)

    }).then(resp => {
      const token = resp.json().data.auth_token;
      const expirationDate = new Date(new Date().getTime() + 3600 * 1000);

      localStorage.setItem('token', token);
      localStorage.setItem('expirationDate', expirationDate);
    })

  }


  static RegisterUser(body) {
    console.log(body)
    return fetch('http://127.0.0.1:8000/auth/users/', {
      'method': 'POST',
      headers: {
        'Content-Type': 'application/json',

      },
      body: JSON.stringify(body)

    }).then(resp => resp.json())

  }

  static GetLoginUser(body) {
    console.log(body)
    return fetch('http://127.0.0.1:8000/auth/token/login/', {
      'method': 'POST',
      headers: {
        'Content-Type': 'application/json',

      },
      body: JSON.stringify(body)

    }).then(resp => resp.json())

  }

  static authLogin = (username, password) => {
    return dispatch => {
        dispatch();
    
        axios.post('http://127.0.0.1:8000/auth/token/login/', {
            username: username,
            password: password
        })
        .then(res => {
            const token = res.data.auth_token;

            localStorage.setItem('token', token);
        })
    }
}
}