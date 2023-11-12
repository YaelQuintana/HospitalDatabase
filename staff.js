window.addEventListener('DOMContentLoaded', async() => {
    const response = await fetch('/api/staff');
    const data = await response.json();
    console.log(data);
})