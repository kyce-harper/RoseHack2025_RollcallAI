async function getInsight() {
    const userSchedule = ["Math 101 - 9:00 AM", "CS 202 - 11:00 AM", "History 301 - 1:00 PM"];
    const response = await fetch('http://0.0.0.0:5000/get-insight', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ schedule: userSchedule }),
    });
  
    const data = await response.json();
    if (data.error) {
      console.error("Error:", data.error);
      return;
    }
  
    document.getElementById('insight').innerText = data.insight;
  }
  window.onload = getInsight;