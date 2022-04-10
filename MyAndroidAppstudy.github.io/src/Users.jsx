import React,{ useState } from 'react';
<<<<<<< HEAD
import PropTypes from 'prop-types';
import Data from './Data';
import Data2 from './Data2';

class Users extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
        imageURL: "",
    };
    this.UploadImage = this.UploadImage.bind(this);
}

  UploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);
    data.append('filename', this.fileName.value);

    fetch('http://localhost:5000/uploader', { method: 'POST', body: data })
    .then((response) => { response.json().then((body) => { 
        this.setState({ imageURL: `http://localhost:5000/${body.file}` });
      });
    });
  }

  render() {
    return (
      <form onSubmit={this.UploadImage}>
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
        </div>
        <div>
          <input ref={(ref) => { this.fileName = ref; }} type="text" placeholder="Enter the desired name of file" />
        </div>
        <br />
        <div>
          <button>Upload</button>
        </div>
        <img src={this.state.imageURL} alt="img" />
      </form>
    );
  }
}
 
export default Users;

/*import React, { useState } from "react";
import axios from "axios";
const BASE_URL = "http://localhost:4000";

function Data2() {
    const [img, setImage] = useState(null);

    const onChange = (e) => {
        setImage(e.target.files[0]);
      }
    
      const onClick = async () => {
        const formData = new FormData();
        formData.append('file', img);
        // 서버의 upload API 호출
        const res = await axios.post("/api/upload", formData);
        console.log(res);
      }
      
  return (
    <div className="App">
      <input type="img" multiple onChange={onChange}/>
      <button onClick={onClick}>제출</button>
    </div>
  );
  
  
}

export default Data2;*/


/*const onChange = e => {
    setContent(e.target.files[0]);
  };
  const onSubmit = e => {
=======
import axios from 'axios';

class Main extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageURL: '',
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }
  handleUploadImage(ev){
    ev.preventDefault();

    const data = new FormData();
    data.append('file',this.uploadInput.files[0]);
    data.append('filename',this.fileName.value);

    fetch('http://localhost:5000/uploads',{
      method : 'POST',
      body:data,
    }).then((response) => {
      response.json().then((body) => {
        this.setState({ imageURL : `http://localhost:5000/${body.file}`});
      });
    });
  }
  uploadFile(e) {
>>>>>>> a2a11575f37f134cb824b2931e5209e8e7c44450
    e.preventDefault();
    let file = this.state.fileToBeSent;
    let file_name = this.state.fileToBeSent.name;
    console.log(file_name);
    const formData = new FormData();

    formData.append("file", file);

    axios
      .post("/uploads", formData)
      .then(res => console.log(res))
      .catch(err => console.warn(err));
    }
    
  render(){
    return (
      <div>
      <input type="file" name="file" onChange={this.onChangeFile}/>
      <button onClick={this.uploadFile}>
          Upload 
      </button>
      </div>
    );
  }
}

export default Main;
