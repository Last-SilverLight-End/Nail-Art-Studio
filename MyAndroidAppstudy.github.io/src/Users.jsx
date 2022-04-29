import React,{ useState,Component } from 'react';
import "./App.css";
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
              <div className="row">
                  <div className="col-md-6 offset-md-3">
                      <br /><br />

                          <h3 className="text-white">React File Upload Example - Tutsmake.com</h3>
                          <br />
                          <div className="form-row">
                              <div className="form-group col-md-6">
                                  <label className="text-white">Select File :</label>
                                  <input type="file" className="form-control" name="upload_file" onChange={this.handleInputChange} />
                              </div>
                          </div>

                          <div className="form-row">
                              <div className="col-md-6">
                                  <button type="submit" className="btn btn-dark" onClick={()=>this.submit()}>Save</button>
                              </div>
                          </div>
                  </div>
              </div>
          </div>
      )  
  }
}

export default Main;
