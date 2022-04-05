import React,{ useState } from 'react';
 
function Data() {
  const [data,setData] = useState({});
  fetch('/data')
  .then(res => res.json())
  .then(data => setData(data),()=>{
  console.log('data read : ' , data);
  })
 
  return (
    <div>
      {data.lastname} {data.firstname}
    </div>
  );
}
 
export default Data;