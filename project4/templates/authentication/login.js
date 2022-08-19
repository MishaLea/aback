// login a user
function login_functions() {
    let formData = new FormData();
    formData.append('user_name', document.getElementById('loginEmailInput').value);
    formData.append('password', document.getElementById('loginpasswordInput').value);
    
    const options = {
        method: 'POST', 
        mode: 'cors',
        body: formData  
    };
    
    fetch("https://mishalea-aback-vyy3649uck1.ws-eu62.gitpod.io/login/", options)
    .then(res => res.json())
    .then(response => {
      console.log(response)
      if(response.result)
        window.location.href = '/index.html'
      else
        console.log("invalid")
    })
  }
  