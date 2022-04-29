import React,{ useState } from 'react';
 
function Data() {
  const [data,setData] = useState({});
  fetch('/data').then(response => {
    if(response.ok){
      return response.json()
    }
  }).then(data => console.log(data),[])
 
  return (
    <div>
      Hello
    </div>
  );
}
 
export default Data;