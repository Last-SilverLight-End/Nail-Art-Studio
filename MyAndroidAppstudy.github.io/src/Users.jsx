import React,{ useState,Component } from 'react';
import "./App.css";
import Camera from "react-camera-pro";
import axios from 'axios';


// 일단은 전송은 되나 나중에 사진 찍고 저장하여 파일 업로드는 구현 해야 한다.
class Main extends React.Component{

    
  constructor(){

      super();
      this.state = {
          selectedFile:'',
      }

      this.handleInputChange = this.handleInputChange.bind(this);
  }
  
  handleInputChange(event) {
      this.setState({
          selectedFile: event.target.files[0],
        })
  }

  submit(){
      const data = new FormData() 
      data.append('file', this.state.selectedFile);
      console.warn(this.state.selectedFile);

      let url = "/uploader";

      axios.post(url, data, {
         // 주소와 formdata를 posting 한다
      })
      .then(res => { 
        //상태 출력
          console.warn(res);
      })
  }

  render(){
      return(
    <div>
        <div >
            <br /><br />
                <h3>React File Upload Example - Tutsmake.com</h3>
                <br />
                <div>
                    <div >
                        <label >Select File :</label>
                        <input type="file" 
                        name="upload_file" 
                        onChange={this.handleInputChange} />
                    </div>
                </div>
                <div >
                    <div>
                        <button 
                        type="submit"
                        onClick={()=>this.submit()}>
                            Save
                            </button>
                    </div>
            </div>
        </div>

    </div>
      )  
  }
}

export default Main;
