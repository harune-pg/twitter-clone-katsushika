import React, { useEffect } from 'react';
import { getUser } from './api/api';

function App() {
  useEffect(() => {
    // ページがマウントされた時にgetUser関数を呼び出す
    const fetchData = async () => {
      await getUser();
    };
    // 現時点では401エラーが返ってくる
    fetchData();
    });

  return (
    <div>
      <p>App</p>
    </div>
  );
}

export default App;
