import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function InsightsPanel() {
  const [insights, setInsights] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/insights').then(res => setInsights(res.data));
  }, []);

  return insights ? (
    <div className='insight'>
      <h3>Insights</h3>
      <p>{insights.message}</p>
    </div>
  ) : null;
}
