// signin a user
function signin_functions() {
    let formData = new FormData();
    formData.append('user_name', document.getElementById('signin_name').value);
    formData.append('password', document.getElementById('signin_password').value);
    formData.append("email", document.getElementById("signin_email").value);
    
    const options = {
        method: 'POST', 
        mode: 'cors',
        body: formData  
    };
    
    fetch("https://8000-mishalea-aback-sruuhfymol0.ws-eu62.gitpod.io/signup/", options)
    .then(res => res.json())
    .then(response => {
      console.log(response)
      if(response.result)
        window.location.href = '/login.html'
      else
        console.log("invalid")
    })
  }