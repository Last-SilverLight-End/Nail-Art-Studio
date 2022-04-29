import React,{ useState,Component } from 'react';
import "./App.css";
import axios from 'axios';

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
      data.append('file', this.state.selectedFile)
      console.warn(this.state.selectedFile);
      let url = "/uploader";

      axios.post(url, data, { // receive two parameter endpoint url ,form data 
      })
      .then(res => { // then print response status
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
