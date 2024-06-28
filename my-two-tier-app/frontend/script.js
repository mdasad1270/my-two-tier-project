async function fetchData() {
    const response = await fetch('http://localhost:5000/api/data');
    const data = await response.json();
    const dataList = document.getElementById('data-list');
    dataList.innerHTML = '<h2>Stored Data:</h2>';
    data.forEach(item => {
        dataList.innerHTML += `<p>${item[1]} (Added: ${new Date(item[2]).toLocaleString()})</p>`;
    });
}

async function addData() {
    const input = document.getElementById('data-input');
    const data = input.value;
    if (data) {
        await fetch('http://localhost:5000/api/data', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data: data })
        });
        input.value = '';
        fetchData();
    }
}

fetchData();
