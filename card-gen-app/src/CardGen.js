import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import APIService from './APIService.js'
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css'


function CardGen() {
    const [name, setName] = useState("");
    const [first_name, setFirstName] = useState("");
    const [last_name, setLastName] = useState("");
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
    const [vcf, setVcf] = useState("");

    const makeVcfDownload = (response) => {
        console.log("Making vcf download");
        console.log(response);
        const element = document.createElement("a");
        const file = new Blob([response], {type: 'text/plain'});
        element.href = URL.createObjectURL(file);
        element.download = "contact.vcf";
        document.body.appendChild(element); // Required for this to work in FireFox
        element.click();
    }

    const insertArticle = (newName, newFullName) =>{
        let name = newName;
        let full_name = newFullName;
        APIService.InsertArticle({name, full_name, email_personal, email_work, email_other, bday, address_home, address_work, address_other, notes, org, photo, role, tel_home, tel_work, tel_mobile, title})
        .then((response) => makeVcfDownload(response))
        .catch(error => console.log('error',error))
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        let newName = (last_name + ';' + first_name);
        let newFullName = (first_name + ' ' + last_name);
        setName(newName);
        setFullName(newFullName);
        insertArticle(newName, newFullName);
        alert('A name was submitted: ' + name);
    }

    const setTestValues = () => {
        console.log("Setting test values");
        console.log(process.env.REACT_APP_FIRST_NAME);
        setFirstName(process.env.REACT_APP_FIRST_NAME);
        setLastName(process.env.REACT_APP_LAST_NAME);
        setEmailPersonal(process.env.REACT_APP_EMAIL_PERSONAL);
        setEmailWork(process.env.REACT_APP_EMAIL_WORK);
        setEmailOther(process.env.REACT_APP_EMAIL_OTHER);
        setBday(process.env.REACT_APP_BDAY);
        setAddressHome(process.env.REACT_APP_ADDRESS_HOME);
        setAddressWork(process.env.REACT_APP_ADDRESS_WORK);
        setAddressOther(process.env.REACT_APP_ADDRESS_OTHER);
        setNotes(process.env.REACT_APP_NOTES);
        setOrg(process.env.REACT_APP_ORG);
        setPhoto(process.env.REACT_APP_PHOTO);
        setRole(process.env.REACT_APP_ROLE);
        setTelHome(process.env.REACT_APP_TEL_HOME);
        setTelWork(process.env.REACT_APP_TEL_WORK);
        setTelMobile(process.env.REACT_APP_TEL_MOBILE);
        setTitle(process.env.REACT_APP_TITLE);
    }


    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label for="name">First Name:
                    <input type="text" value={first_name} onChange={(e) => setFirstName(e.target.value)}></input>
                </label>
                <label for="name">Last Name:
                    <input type="text" value={last_name} onChange={(e) => setLastName(e.target.value)}></input>
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
                    <DatePicker selected={bday} onChange={bday => setBday(bday)} dateFormat='yyyy-MM-dd'></DatePicker>
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
            <button onClick={setTestValues}>Click to set test values</button>
        </div>
    );
}

export default CardGen;