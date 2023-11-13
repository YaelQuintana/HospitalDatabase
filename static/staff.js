let staff = []


window.addEventListener('DOMContentLoaded', async() => {
    const response = await fetch('/api/staff');
    const data = await response.json()
    staff = data
    renderStaff(staff)
});

function renderStaff(staff) {
    const staffList = document.querySelector('#staff_list');

    staff.forEach(staff => {
        const staffItem = document.createElement('li');
        staffItem.innerHTML = `
            <h3>${staff}</h3>
        `

        console.log(staff)
        staffList.append(staffItem)
    });
}