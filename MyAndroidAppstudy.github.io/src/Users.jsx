import React,{ useState } from 'react';
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
    e.preventDefault();
    const formData = new FormData();
    formData.append("img", content); 
    axios
      .post("/upload", formData)
      .then(res => {
        const { fileName } = res.data;
        console.log(fileName);
        setUploadedImg({ fileName, filePath: `${BASE_URL}/img/${fileName}` });
        alert("The file is successfully uploaded");
      })
      .catch(err => {
        console.error(err);
      });
  };

export default function App() {
  const [content, setContent] = useState("");

  const [uploadedImg, setUploadedImg] = useState({

    fileName: "",
    fillPath: ""
    }
  );

  return (
    <>
      <form onSubmit={onSubmit}>
        {uploadedImg ? (
          <>
            <img src={uploadedImg.filePath} alt="" />
            <h3>{uploadedImg.fileName}</h3>
          </>
        ) : (
          ""
        )}
        <input type="file" onChange={onChange} />
        <button type="submit">Upload</button>
      </form>
    </>
  );
}*/

