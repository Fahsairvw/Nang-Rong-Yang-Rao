document.addEventListener('DOMContentLoaded', () => {
    loadDustData();
    loadSoundData();
  });
  
  function loadDustData() {
    axios.get('http://127.0.0.1:8080/dust-api/v1/dust')
      .then(response => {
        const rows = response.data.map(d => `
          <tr>
            <td>${d.id}</td>
            <td>${d.hour}</td>
            <td>${d.pm25}</td>
            <td>${d.pm10}</td>
            <td>${d.aqi}</td>
            <td>${d.lat}</td>
            <td>${d.lon}</td>
          </tr>
        `).join('');
        document.getElementById('dust-data').innerHTML = rows;
      })
      .catch(err => console.error('Error loading dust data:', err));
  }
  
  function loadSoundData() {
    axios.get('http://127.0.0.1:8080/dust-api/v1/sound')
      .then(response => {
        const rows = response.data.map(s => `
          <tr>
            <td>${s.id}</td>
            <td>${s.adc}</td>
            <td>${s.db}</td>
            <td>${s.voltage}</td>
          </tr>
        `).join('');
        document.getElementById('sound-data').innerHTML = rows;
      })
      .catch(err => console.error('Error loading sound data:', err));
  }
  