import React,{ useState } from 'react';
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
