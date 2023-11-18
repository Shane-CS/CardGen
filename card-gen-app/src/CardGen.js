import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import APIService from './APIService.js'

function CardGen(props) {
    const [name, setName] = useState("");
    const [full_name, setFullName] = useState("");
    const [email_personal, setEmailPersonal] = useState("");
    const [email_work, setEmailWork] = useState("");
    const [email_other, setEmailOther] = useState("");
    const [bday, setBday] = useState("");
    const [address_home, setAddressHome] = useState("");
    const [address_work, setAddressWork] = useState("");
    const [address_other, setAddressOther] = useState("");
    const [notes, setNotes] = useState("");
    const [org, setOrg] = useState("");
    const [photo, setPhoto] = useState("");
    const [role, setRole] = useState("");
    const [tel_home, setTelHome] = useState("");
    const [tel_work, setTelWork] = useState("");
    const [tel_mobile, setTelMobile] = useState("");
    const [title, setTitle] = useState("");

    const insertArticle = () =>{
        APIService.InsertArticle({name, full_name, email_personal, email_work, email_other, bday, address_home, address_work, address_other, notes, org, photo, role, tel_home, tel_work, tel_mobile, title})
        .then((response) => props.insertedArticle(response))
        .catch(error => console.log('error',error))
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        insertArticle();
        alert('A name was submitted: ' + name);
    }
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label for="name">Name:
                    <input type="text" value={name} onChange={(e) => setName(e.target.value)}></input>
                </label>
                <label for="email_personal">Personal Email:
                    <input type="text" value={email_personal} onChange={(e) => setEmailPersonal(e.target.value)}></input>
                </label>
                <label for="email_work">Work Email:
                    <input type="text" value={email_work} onChange={(e) => setEmailWork(e.target.value)}></input>
                </label>
                <label for="email_other">Other Email:
                    <input type="text" value={email_other} onChange={(e) => setEmailOther(e.target.value)}></input>
                </label>
                <label for="bday">Birthday:
                    <input type="text" value={bday} onChange={(e) => setBday(e.target.value)}></input>
                </label>
                <label for="address_home">Home Address:
                    <input type="text" value={address_home} onChange={(e) => setAddressHome(e.target.value)}></input>
                </label>
                <label for="address_work">Work Address:
                    <input type="text" value={address_work} onChange={(e) => setAddressWork(e.target.value)}></input>
                </label>
                <label for="address_other">Other Address:
                    <input type="text" value={address_other} onChange={(e) => setAddressOther(e.target.value)}></input>
                </label>
                <label for="notes">Notes:
                    <input type="text" value={notes} onChange={(e) => setNotes(e.target.value)}></input>
                </label>
                <label for="org">Organization:
                    <input type="text" value={org} onChange={(e) => setOrg(e.target.value)}></input>
                </label>
                <label for="photo">Photo:
                    <input type="text" value={photo} onChange={(e) => setPhoto(e.target.value)}></input>
                </label>
                <label for="role">Role:
                    <input type="text" value={role} onChange={(e) => setRole(e.target.value)}></input>
                </label>
                <label for="tel_home">Home Phone:
                    <input type="text" value={tel_home} onChange={(e) => setTelHome(e.target.value)}></input>
                </label>
                <label for="tel_work">Work Phone:
                    <input type="text" value={tel_work} onChange={(e) => setTelWork(e.target.value)}></input>
                </label>
                <label for="tel_mobile">Mobile Phone:
                    <input type="text" value={tel_mobile} onChange={(e) => setTelMobile(e.target.value)}></input>
                </label>
                <label for="title">Title:
                    <input type="text" value={title} onChange={(e) => setTitle(e.target.value)}></input>
                </label>
                <input type="submit" value="Submit"></input>
            </form>
        </div>
    );
}

export default CardGen;