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
// 이 부분 수정
    fetch('http://localhost:5000/uploader',{
      method : 'POST',
      body:data,
    }).then((response) => {s
      response.json().then((body) => {
        this.setState({ imageURL : `http://localhost:5000/${body.file}`});
      })
      
    }) .then(data => console.log(data));
  }

  render(){
    return (
      <form onSubmit={this.handleUploadImage}>
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

export default Main;
