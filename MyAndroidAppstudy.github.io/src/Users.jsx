import React,{ useState } from 'react';
import "./App.css";
import Axios from 'axios';

function Main(){

  const [imageSelected, setImageSelected] = useState("");
  const uploadImage = () => {
    const formData = new FormData()
    formData.append("file",imageSelected)
    formData.append("upload_preset");

    Axios.post(
        "/uploader",formData)
        .then((response) => {
          console.log(response);
        });
  };

    return (
      <div className = "App">
        <h1>THE FORM</h1>
        <form>
          <div className=''>
            <label>SelectFile</label>
            <input type="file"
             name ="file" 
             onChange = {(e) =>
              setImageSelected(e.target.files)}/>
          </div>
          <br/>
          <button onClick={uploadImage}>Upload</button>
        </form>
      </div>
    );
  }


export default Main;
