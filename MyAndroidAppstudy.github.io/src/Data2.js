import React, { useState } from "react";
import axios from "axios";
const BASE_URL = "http://localhost:4000";

class Data2 extends React.Component {
    state = { selectedFiles: null };

    // 저장 하는 부분
    onClick = async() => {
        
    }

    onClickHandler = event => {
      const formData = new FormData();
      formData.append(
        "uploadImages",
        this.state.selectedFiles,
        this.state.selectedFiles.name
      );
      const config = {
        headers: {
          "content-type": "multipart/form-data"
        }
      };
      axios.post("/api/upload", formData);
    }; 
    

    fileChangedHandler = event => {
      const files = event.target.files;
      this.setState({
        selectedFiles: files
      });
    };

    render() {
      return (
        <div className="App" style={{ marginTop: "100px" }}>
          <input type="file" multiple onChange={this.fileChangedHandler} />
          <button onClick={this.onClickHandler}>저장하기</button>
        </div>
      );
    }
  }
  
  export default Data2;


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

