import React, { useState } from 'react';
import './App.css';

interface IStudent {
  student_nr: string;
  name: string;
  birthday: string;
  year: number;
  email: string;
}

const App: React.FC = () => {
  const [students, setStudents] = useState<IStudent[]>([]);

  React.useEffect(() => {
    getStudents();
  }, []);

  return (
    <div className="App">
      {students.map((x, key) => (
        <div key={key}>{x.name}</div>
      ))}
    </div>
  );

  async function getStudents() {
    const r = await getAllStuds();
    console.log(r);
    setStudents(r);
  }
};

export async function getAllStuds() {
  const BASE_URL = 'http://127.0.0.1:5000';
  const options = {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  };
  return handleRestResponse(await fetch(`${BASE_URL}/student`, options));
}

function handleRestResponse(response: any) {
  if (response.status >= 200 && response.status < 300) {
    return Promise.resolve(response.json());
  } else {
    return response.status;
  }
}

export default App;
