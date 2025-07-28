import React, { useState } from "react";
import "./Register.css";

const Register = () => {
  // State variables for form inputs
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setlastName] = useState("");

  // Redirect to home
  const gohome = ()=> {
    window.location.href = window.location.origin;
  }

  // Handle form submission
  const register = async (e) => {
    e.preventDefault();
    let register_url = window.location.origin+"/djangoapp/register";
    
    // Send POST request to register endpoint
    const res = await fetch(register_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        "userName": userName,
        "password": password,
        "firstName":firstName,
        "lastName":lastName,
        "email":email
      }),
    });
    
    const json = await res.json();
    if (json.status) {
      // Save username in session and reload home
      sessionStorage.setItem('username', json.userName);
      window.location.href = window.location.origin;
    }
    else if (json.error === "Already Registered") {
      alert("The user with same username is already registered");
      window.location.href = window.location.origin;
    }
  };

  return(
    <div className="register_container" style={{width: "50%"}}>
      <div className="header" style={{display: "flex",flexDirection: "row", justifyContent: "space-between"}}>
        <span className="text" style={{flexGrow:"1"}}>SignUp</span>
        <div style={{display: "flex",flexDirection: "row", justifySelf: "end", alignSelf: "start" }}>
          <button onClick={gohome} style={{background: "none", border: "none", fontSize: "20px", cursor: "pointer"}}>
            ✕
          </button>
        </div>
      </div>
      <hr/>
      <form onSubmit={register}>
        <div className="inputs">
          <div className="input">
            <span>👤</span>
            <input type="text" name="username" placeholder="Username" className="input_field" onChange={(e) => setUserName(e.target.value)}/>
          </div>
          <div className="input">
            <span>👤</span>
            <input type="text" name="first_name" placeholder="First Name" className="input_field" onChange={(e) => setFirstName(e.target.value)}/>
          </div>
          <div className="input">
            <span>👤</span>
            <input type="text" name="last_name" placeholder="Last Name" className="input_field" onChange={(e) => setlastName(e.target.value)}/>
          </div>
          <div className="input">
            <span>📧</span>
            <input type="email" name="email" placeholder="Email" className="input_field" onChange={(e) => setEmail(e.target.value)}/>
          </div>
          <div className="input">
            <span>🔒</span>
            <input name="psw" type="password" placeholder="Password" className="input_field" onChange={(e) => setPassword(e.target.value)}/>
          </div>
        </div>
        <div className="submit_panel">
          <input className="submit" type="submit" value="Register"/>
        </div>
      </form>
    </div>
  )
}

export default Register;