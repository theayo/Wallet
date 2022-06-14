
import axios from "axios";
const token = ""

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

    }).then(resp => resp.json())
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

    }).then(resp => token=resp.json().token
    )

  }

  static GetMoney(){
    fetch('http://127.0.0.1:8000/api/v1/wallet/get_user_wallet/', {
            'method': 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
            }
        })
            .then(resp => resp.json())
            .catch(error => console.log(error))
  }
}